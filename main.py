import os
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

PORT = 8000

os.chdir(os.path.dirname(__file__))

with TCPServer(("", PORT), SimpleHTTPRequestHandler) as httpd:
    print("تشغيل الذكرى على http://localhost:8000 ...")
    httpd.serve_forever()