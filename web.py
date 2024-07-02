import http.server
import socketserver
import socket

PORT = 8000
DIRECTORY = "public_html"

# Get the local IP address
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at http://{local_ip}:{PORT}")
    httpd.serve_forever()
