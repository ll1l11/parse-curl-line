# -*- coding: utf-8 -*-
import json
import shlex
import urllib.parse
from six.moves import http_cookies as Cookie
from io import BytesIO
from collections import OrderedDict

from requests.structures import CaseInsensitiveDict

import werkzeug.urls
import werkzeug.http
import werkzeug.formparser


from curl_parser import parser

command = ''

with open('test_curl2.txt') as f:
    command = f.read()


def parse(curl_command):
    method, url, kwargs = _parse(curl_command)
    return format_requests_code(method, url, **kwargs)


def _parse(curl_command):
    tokens = shlex.split(curl_command)
    parsed_args = parser.parse_args(tokens)

    kwargs = {}

    body = parsed_args.data or parsed_args.data_binary

    # method
    method = parsed_args.request
    if not method:
        if body:
            method = 'POST'
        else:
            method = 'GET'

    url, params = parse_url_and_params(parsed_args.url)
    if params:
        kwargs['params'] = params

    cookies, headers = parse_cookies_and_headers(parsed_args.header)
    kwargs['cookies'], kwargs['headers'] = cookies, headers

    content_type = headers.get('Content-Type')
    if not content_type and parsed_args.data:
        content_type = 'application/x-www-form-urlencoded'
    _, kwargs['data'], kwargs['files'] = parse_formdata(body, content_type)

    return method, url, kwargs


def format_requests_code(method, url, **kwargs):
    keys = [
        'params', 'data', 'headers', 'cookies', 'files', 'auth', 'timeout',
        'allow_redirects', 'proxies', 'hooks', 'stream', 'verify', 'cert',
        'json'
    ]
    kw = []
    variables = []
    for k in keys:
        v = kwargs.get(k)
        if not v:
            continue
        if isinstance(v, dict):
            v = dict_to_pretty_string(v)
            variables.append('\n{0} = {1}\n'.format(k, v))
        else:
            variables.append('\n{0} = "{1}"\n'.format(k, v))
        kw.append(', {0}={0}'.format(k))

    result = """import requests

url = "{url}"
{variables}
r = requests.{method}(url{kwargs})

print(r.text)""".format(
        method=method.lower(),
        url=url,
        variables=''.join(variables),
        kwargs=''.join(kw)
    )
    return result


def dict_to_pretty_string(the_dict):
    if not the_dict:
        return "{}"

    return ('\n').join(
        json.dumps(the_dict, indent=4, separators=(',', ': ')).splitlines()
    )


def parse_url_and_params(origin_url):
    """:return: tuple. type is (str, MultiDict)"""
    if not (origin_url.startswith('//') or origin_url.startswith('http')):
        origin_url = 'http://' + origin_url
    url_parse_result = urllib.parse.urlparse(origin_url)
    url = '{0}://{1}{2}'.format(url_parse_result.scheme or 'http',
                                url_parse_result.netloc,
                                url_parse_result.path)

    query = url_parse_result.query
    params = None
    if query:
        params = werkzeug.urls.url_decode(query)
    return url, params


def parse_cookies_and_headers(header):
    """:return: tuple. type is (OrderedDict(), OrderedDict())"""
    cookies = OrderedDict()
    headers = CaseInsensitiveDict()
    for curl_header in header:
        header_key, header_value = curl_header.split(':', 1)

        if header_key.lower() == 'cookie':
            cookie = Cookie.SimpleCookie(header_value)
            for key in cookie:
                cookies[key] = cookie[key].value
        else:
            headers[header_key] = header_value.strip()
    return cookies, headers


def parse_formdata(body, content_type):
    data = body.encode('utf-8')

    content_length = None
    mimetype, options = werkzeug.http.parse_options_header(content_type)

    stream = BytesIO(data)
    parser = werkzeug.formparser.FormDataParser()

    data, form, files = parser.parse(stream, mimetype, content_length, options)
    return data.getvalue(), form, files


if __name__ == '__main__':
    print(parse(command))
