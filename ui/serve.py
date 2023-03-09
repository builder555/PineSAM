import http.server
import socketserver
import os

class Server:

    def __init__(self, port=8080):
        self.dir = os.path.dirname(os.path.abspath(__file__))
        if os.path.exists(os.path.join(self.dir,'ui')):
            self.dir = os.path.join(self.dir,'ui')
        self.port = port

    @property
    def handler(self):
        directory = self.dir
        class Handler(http.server.SimpleHTTPRequestHandler):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, directory=directory, **kwargs)
        return Handler

    def start(self):
        os.chdir(self.dir)
        with socketserver.TCPServer(("", self.port), self.handler) as httpd:
            try:
                httpd.serve_forever()
            except KeyboardInterrupt:
                return


if __name__ == "__main__":
    Server().start()
