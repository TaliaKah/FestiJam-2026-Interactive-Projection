from pythonosc.udp_client import SimpleUDPClient
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

osc_ip = "192.168.1.11"  # or remote IP
osc_port = 5000
osc_client = SimpleUDPClient(osc_ip, osc_port)


click_id = 0.0


class OSCRequestHandler(BaseHTTPRequestHandler):

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_POST(self):
        global click_id
        if self.path == "/click":
            length = int(self.headers["Content-Length"])
            body = self.rfile.read(length)
            data = json.loads(body)
            x = data.get("x", 0)
            y = data.get("y", 0)
            osc_client.send_message("/clickX", x)
            osc_client.send_message("/clickY", y)
            osc_client.send_message("/ID", click_id)
            click_id += 1
            self.send_response(200)
            self.end_headers()


httpd = HTTPServer(("0.0.0.0", 3000), OSCRequestHandler)
print("Serving on port 3000")
httpd.serve_forever()
