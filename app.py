from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        html_content = """
        <html>
        <head><title>Tollywood App</title></head>
        <body style="font-family: Arial; text-align: center; background-color: #f4f4f4;">
            <h1 style="color: #d9534f;">Jai Balayya! Welcome to Tollywood App!</h1>
            <p style="font-size: 1.2em;">Mana Kubernetes Cluster lo Python App successfully run avthundi!</p>
            <div style="display: inline-block; text-align: left; background: white; padding: 20px; border-radius: 10px; box-shadow: 0px 0px 10px rgba(0,0,0,0.1);">
                <h3>Featured Personalities:</h3>
                <ul>
                    <li><b>Brahmanandam:</b> The Comedy King</li>
                    <li><b>Sivaji:</b> Versatile Actor</li>
                </ul>
            </div>
        </body>
        </html>
        """
        self.wfile.write(html_content.encode('utf-8'))

if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, SimpleHandler)
    print("Server running on port 8000... Jai Balayya!")
    httpd.serve_forever()
EOF


