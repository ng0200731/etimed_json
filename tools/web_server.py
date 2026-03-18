"""
Web server that serves the HTML report and handles circle position API
Other users on the network can access via http://YOUR_IP:5000
"""

from http.server import HTTPServer, SimpleHTTPRequestHandler
import json
import sys
import os
import socket
from urllib.parse import urlparse, parse_qs

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from tools.manage_circle_positions import CirclePositionManager

# Initialize database manager
db_manager = CirclePositionManager('.tmp/circle_positions.db')

# Path to the HTML file
HTML_FILE_PATH = r'd:\temp\IT-customer\etimed\further_sharing\test\test\LABEL_GENERATION_REPORT.html'


class WebServerHandler(SimpleHTTPRequestHandler):

    def _set_headers(self, status=200, content_type='application/json'):
        self.send_response(status)
        self.send_header('Content-Type', content_type)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_OPTIONS(self):
        self._set_headers()

    def do_GET(self):
        parsed = urlparse(self.path)

        # Serve the main HTML page
        if parsed.path == '/' or parsed.path == '/index.html':
            try:
                with open(HTML_FILE_PATH, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Replace localhost with current server address for network access
                content = content.replace(
                    "const API_BASE_URL = 'http://localhost:5000'",
                    f"const API_BASE_URL = window.location.origin"
                )

                self._set_headers(content_type='text/html; charset=utf-8')
                self.wfile.write(content.encode('utf-8'))
            except Exception as e:
                self._set_headers(500, 'text/plain')
                self.wfile.write(f'Error loading HTML: {str(e)}'.encode())

        # API: Load positions
        elif parsed.path == '/load':
            query = parse_qs(parsed.query)
            label_id = query.get('label_id', ['PVP002XG'])[0]

            positions = db_manager.get_positions(label_id)

            self._set_headers()
            response = {
                'success': True,
                'label_id': label_id,
                'positions': positions
            }
            self.wfile.write(json.dumps(response).encode())

        # API: List all positions
        elif parsed.path == '/list':
            all_positions = db_manager.get_all_positions()

            self._set_headers()
            response = {
                'success': True,
                'positions': all_positions
            }
            self.wfile.write(json.dumps(response).encode())

        # API: Status
        elif parsed.path == '/status':
            self._set_headers()
            response = {
                'status': 'running',
                'message': 'Circle Position Web Server',
                'endpoints': {
                    'home': 'GET /',
                    'save': 'POST /save',
                    'load': 'GET /load?label_id=XXX',
                    'list': 'GET /list'
                }
            }
            self.wfile.write(json.dumps(response).encode())

        else:
            self._set_headers(404, 'text/plain')
            self.wfile.write(b'Not found')

    def do_POST(self):
        # API: Save positions
        if self.path == '/save':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode())

            label_id = data.get('label_id', 'PVP002XG')
            positions = data.get('positions', {})

            # Convert string keys to integers
            positions_int = {int(k): v for k, v in positions.items()}

            db_manager.save_positions_batch(label_id, positions_int)

            self._set_headers()
            response = {
                'success': True,
                'message': f'Saved {len(positions_int)} positions for {label_id}'
            }
            self.wfile.write(json.dumps(response).encode())

        # API: Clear positions
        elif self.path == '/clear':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode())

            label_id = data.get('label_id', 'PVP002XG')
            db_manager.clear_label_positions(label_id)

            self._set_headers()
            response = {
                'success': True,
                'message': f'Cleared positions for {label_id}'
            }
            self.wfile.write(json.dumps(response).encode())

        else:
            self._set_headers(404)
            response = {'error': 'Not found'}
            self.wfile.write(json.dumps(response).encode())

    def log_message(self, format, *args):
        print(f"[{self.log_date_time_string()}] {format % args}")


def get_local_ip():
    """Get the local IP address"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "localhost"


def run_server(port=5000):
    server_address = ('0.0.0.0', port)  # Listen on all network interfaces
    httpd = HTTPServer(server_address, WebServerHandler)

    local_ip = get_local_ip()

    print("=" * 70)
    print("Circle Position Web Server Started")
    print("=" * 70)
    print()
    print("Access the application:")
    print(f"  Local:   http://localhost:{port}")
    print(f"  Network: http://{local_ip}:{port}")
    print()
    print("Share this URL with other users on your network:")
    print(f"  → http://{local_ip}:{port}")
    print()
    print("Database: .tmp/circle_positions.db")
    print()
    print("Press Ctrl+C to stop")
    print("=" * 70)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n\nServer stopped.")
        httpd.server_close()


if __name__ == '__main__':
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 5000
    run_server(port)
