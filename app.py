from http.server import Flask, BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"<h1>Hello from CI/CD on EC2!</h1>")

if __name__ == "__main__":
    print("Server starting on port 8080...")
    server = HTTPServer(('0.0.0.0', 8080), Handler)
    server.serve_forever()
