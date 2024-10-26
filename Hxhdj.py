from http.server import BaseHTTPRequestHandler
import json
import urllib.parse

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Parse the query parameters
        query = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
        message = query.get("message", ["Hello, World!"])[0]

        # Set response headers
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        # Send the JSON response
        self.wfile.write(json.dumps({"message": message}).encode())
