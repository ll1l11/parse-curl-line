# -*- coding: utf-8 -*-
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('command')
parser.add_argument('url')
parser.add_argument('-#', '--progress-bar')
parser.add_argument('-:', '--next')
parser.add_argument('-0', '--http1.0')
parser.add_argument('--http1.1')
parser.add_argument('--http2')
parser.add_argument('--no-npn')
parser.add_argument('--no-alpn')
parser.add_argument('-1', '--tlsv1')
parser.add_argument('-2', '--sslv2')
parser.add_argument('-3', '--sslv3')
parser.add_argument('-4', '--ipv4')
parser.add_argument('-6', '--ipv6')
parser.add_argument('-a', '--append')
parser.add_argument('-A', '--user-agent')
parser.add_argument('--anyauth')
parser.add_argument('-b', '--cookie')
parser.add_argument('-B', '--use-ascii')
parser.add_argument('--basic')
parser.add_argument('-c', '--cookie-jar')
parser.add_argument('-C', '--continue-at')
parser.add_argument('--ciphers')
parser.add_argument('--compressed')
parser.add_argument('--connect-timeout')
parser.add_argument('--create-dirs')
parser.add_argument('--crlf')
parser.add_argument('--crlfile')
parser.add_argument('-d', '--data')
parser.add_argument('-D', '--dump-header')
parser.add_argument('--data-ascii')
parser.add_argument('--data-binary')
parser.add_argument('--data-raw')
parser.add_argument('--data-urlencode')
parser.add_argument('--delegation')
parser.add_argument('--digest')
parser.add_argument('--disable-eprt')
parser.add_argument('--disable-epsv')
parser.add_argument('--dns-interface')
parser.add_argument('--dns-ipv4-addr')
parser.add_argument('--dns-ipv6-addr')
parser.add_argument('--dns-servers')
parser.add_argument('-e', '--referer')
parser.add_argument('-E', '--cert')
parser.add_argument('--engine')
parser.add_argument('--environment')
parser.add_argument('--egd-file')
parser.add_argument('--expect100-timeout')
parser.add_argument('--cert-type')
parser.add_argument('--cacert')
parser.add_argument('--capath')
parser.add_argument('--pinnedpubkey')
parser.add_argument('--cert-status')
parser.add_argument('--false-start')
parser.add_argument('-f', '--fail')
parser.add_argument('-F', '--form')
parser.add_argument('--ftp-account')
parser.add_argument('--ftp-alternative-to-user')
parser.add_argument('--ftp-create-dirs')
parser.add_argument('--ftp-method')
parser.add_argument('--ftp-pasv')
parser.add_argument('--ftp-skip-pasv-ip')
parser.add_argument('--ftp-pret')
parser.add_argument('--ftp-ssl-ccc')
parser.add_argument('--ftp-ssl-ccc-mode')
parser.add_argument('--ftp-ssl-control')
parser.add_argument('--form-string')
parser.add_argument('-g', '--globoff')
parser.add_argument('-G', '--get')
parser.add_argument('-H', '--header')
parser.add_argument('--hostpubmd5')
parser.add_argument('--ignore-content-length')
parser.add_argument('-i', '--include')
parser.add_argument('-I', '--head')
parser.add_argument('--interface')
parser.add_argument('-j', '--junk-session-cookies')
parser.add_argument('-J', '--remote-header-name')
parser.add_argument('-k', '--insecure')
parser.add_argument('-K', '--config')
parser.add_argument('--keepalive-time')
parser.add_argument('--key')
parser.add_argument('--key-type')
parser.add_argument('--krb')
parser.add_argument('-l', '--list-only')
parser.add_argument('-L', '--location')
parser.add_argument('--libcurl')
parser.add_argument('--limit-rate')
parser.add_argument('--local-port')
parser.add_argument('--location-trusted')
parser.add_argument('-m', '--max-time')
parser.add_argument('--login-options')
parser.add_argument('--mail-auth')
parser.add_argument('--mail-from')
parser.add_argument('--max-filesize')
parser.add_argument('--mail-rcpt')
parser.add_argument('--max-redirs')
parser.add_argument('--metalink')
parser.add_argument('-n', '--netrc')
parser.add_argument('-N', '--no-buffer')
parser.add_argument('--netrc-file')
parser.add_argument('--netrc-optional')
parser.add_argument('--negotiate')
parser.add_argument('--no-keepalive')
parser.add_argument('--no-sessionid')
parser.add_argument('--noproxy')
parser.add_argument('--ntlm')
parser.add_argument('-o', '--output')
parser.add_argument('-O', '--remote-name')
parser.add_argument('--oauth2-bearer')
parser.add_argument('--proxy-header')
parser.add_argument('-p', '--proxytunnel')
parser.add_argument('-P', '--ftp-port')
parser.add_argument('--pass')
parser.add_argument('--path-as-is')
parser.add_argument('--post301')
parser.add_argument('--post302')
parser.add_argument('--post303')
parser.add_argument('--proto')
parser.add_argument('--proto-default')
parser.add_argument('--proto-redir')
parser.add_argument('--proxy-anyauth')
parser.add_argument('--proxy-basic')
parser.add_argument('--proxy-digest')
parser.add_argument('--proxy-negotiate')
parser.add_argument('--proxy-ntlm')
parser.add_argument('--proxy-service-name')
parser.add_argument('--proxy1.0')
parser.add_argument('--pubkey')
parser.add_argument('-Q', '--quote')
parser.add_argument('-r', '--range')
parser.add_argument('-R', '--remote-time')
parser.add_argument('--random-file')
parser.add_argument('--raw')
parser.add_argument('--remote-name-all')
parser.add_argument('--resolve')
parser.add_argument('--retry')
parser.add_argument('--retry-delay')
parser.add_argument('--retry-max-time')
parser.add_argument('-s', '--silent')
parser.add_argument('--sasl-ir')
parser.add_argument('--service-name')
parser.add_argument('-S', '--show-error')
parser.add_argument('--ssl')
parser.add_argument('--ssl-reqd')
parser.add_argument('--ssl-allow-beast')
parser.add_argument('--ssl-no-revoke')
parser.add_argument('--socks4')
parser.add_argument('--socks4a')
parser.add_argument('--socks5-hostname')
parser.add_argument('--socks5')
parser.add_argument('--socks5-gssapi-service')
parser.add_argument('--socks5-gssapi-nec')
parser.add_argument('--stderr')
parser.add_argument('-t', '--telnet-option')
parser.add_argument('-T', '--upload-file')
parser.add_argument('--tcp-nodelay')
parser.add_argument('--tftp-blksize')
parser.add_argument('--tlsauthtype')
parser.add_argument('--tlspassword')
parser.add_argument('--tlsuser')
parser.add_argument('--tlsv1.0')
parser.add_argument('--tlsv1.1')
parser.add_argument('--tlsv1.2')
parser.add_argument('--tr-encoding')
parser.add_argument('--trace')
parser.add_argument('--trace-ascii')
parser.add_argument('--trace-time')
parser.add_argument('--unix-socket')
parser.add_argument('-u', '--user')
parser.add_argument('-U', '--proxy-user')
parser.add_argument('--url')
parser.add_argument('-v', '--verbose')
parser.add_argument('-w', '--write-out')
parser.add_argument('-x', '--proxy')
parser.add_argument('-X', '--request')
parser.add_argument('--xattr')
parser.add_argument('-y', '--speed-time')
parser.add_argument('-Y', '--speed-limit')
parser.add_argument('-z', '--time-cond')
parser.add_argument('-M', '--manual')
parser.add_argument('-V', '--version')
