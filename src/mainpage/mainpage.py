from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.request

class Controller(BaseHTTPRequestHandler):

    def do_GET(self):
        self.do_POST()

    def do_POST(self):
        self.process()

    def process(self):
        if '/info' == self.path:
            # res = urllib.request.urlopen("http://127.0.0.1:8082/detail")
            try:
                res = urllib.request.urlopen("http://detail:8082/detail")
                detail = res.read().decode("utf-8")
            except BaseException:
                detail = 'error'

            self.writeResponse('''
            <html>
                <meta charset="UTF-8">
                <title>Book Info</title>
            </head>
            <body>
                <p>Title: A Great Book</p>
                <p>Detail: %s</p>
            </body>
            </html>
            ''' % detail, content_type='html')
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


HTTPServer(("", 8081), Controller).serve_forever()
