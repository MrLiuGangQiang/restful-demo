import json
from http.server import BaseHTTPRequestHandler, HTTPServer

HOST = "0.0.0.0"
PORT = 5000
CONFIG_FILE = "config.json"

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/api/config":
            try:
                with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                    config_data = json.load(f)

                response = json.dumps(config_data, ensure_ascii=False)
                self.send_response(200)
                self.send_header("Content-type", "application/json; charset=utf-8")
                self.end_headers()
                self.wfile.write(response.encode("utf-8"))

            except Exception as e:
                self.send_response(500)
                self.end_headers()
                self.wfile.write(str(e).encode("utf-8"))

        else:
            self.send_response(404)
            self.end_headers()

if __name__ == "__main__":
    print(f"Server running at http://{HOST}:{PORT}/api/config")
    HTTPServer((HOST, PORT), RequestHandler).serve_forever()
