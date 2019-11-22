import os
import sys
from app import simple_app

def wsgi_with_bytes(s):
    return s.encode()

def run_with_cgi(application):
    environ = dict(os.environ.items())
    environ["wsgi.input"] = sys.stdin.buffer
    environ["wsgi.errors"] = sys.stderr
    environ["wsgi.version"] = (1, 0)
    environ["wsgi.multithread"] = False
    environ["wsgi.multiprocess"] = True
    environ["wsgi.run_once"] = True

    # 设置请求模式
    if environ.get("HTTPS", "off") in ("on", "1"):
        environ["wsgi.url_scheme"] = "https"
    else:
        environ["wsgi.url_scheme"] = "http"

    headers_set = []
    headers_sent = []
    
    def write(data):
        out = sys.stdout.buffer
        if not headers_set:
            raise AssertionError("write() before start_response")
        elif not headers_sent:
            status, response_headers = headers_sent[:] = headers_set
            out.write(wsgi_with_bytes("Status: %s\r\n" %status))
            for header in response_headers:
                out.write(wsgi_with_bytes("%s: %s\r\n" % header))
            out.write(wsgi_with_bytes("\r\n"))
        out.write(data)
        out.flush()

    def start_response(status, response_headers, exc_info = None):
        if exc_info:
            try:
                if headers_sent:
                    raise (exc_info[0], exc_info[1], exc_info[2])

            finally:
                exc_info = None
        elif headers_set:
            raise AssertionError("headers already set")
        headers_set[:] = [status, response_headers]
        return write
    
    result = application(environ, start_response)
    try:
        for data in result:
            if data:
                write(data)
        if not headers_sent:
            write("")
    finally:
        if hasattr(result, "close"):
            result.close()

if __name__ == "__main__":
    run_with_cgi(simple_app)