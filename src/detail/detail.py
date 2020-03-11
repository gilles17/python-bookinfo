from http.server import HTTPServer, BaseHTTPRequestHandler


class Controller(BaseHTTPRequestHandler):

    def do_GET(self):
        self.do_POST()

    def do_POST(self):
        self.process()

    def process(self):
        if '/detail' == self.path:
            self.writeResponse('Very good book!')
        else:
            self.writeResponse('ERROR')

    def writeResponse(self, message, content_type='plain'):
        self.send_response(200)
        if content_type == 'json':
            self.send_header("Content-type", "application/json")
        elif content_type == 'html':
            self.send_header("Content-type", "text/html")
        else:
            self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(message.encode())


HTTPServer(("", 8082), Controller).serve_forever()
