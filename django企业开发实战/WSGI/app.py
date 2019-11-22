def simple_app(environ, start_response):
    """simple app"""
    status = "200 ok"
    response_headers = [("Content-type", "text/plain")]
    start_response(status, response_headers)
    return [b"hello world"]

class Application(object):
    status = "200 ok"
    response_headers = [("Content-type", "text/plain")]

    def __call__(self, environ, start_response):
        print(environ, start_response)
        start_response(self.status, self.response_headers)
        return [b"hello sim.__call__"]


application = Application()

class AppclassIter(object):
    status = "200 ok"
    response_headers = [("Content-type", "text/plain")]
    
    def __init__(self, environ, start_response):
        self.environ = environ
        self.start_response = start_response

    def __iter__(self):
        self.start_response(self.status, self.response_headers)
        yield b"hello iter"
