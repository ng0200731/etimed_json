"""
Simple HTTP server to save/load circle positions to SQLite
Uses Python's built-in http.server - no Flask needed
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import sys
import os
from urllib.parse import urlparse, parse_qs

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from tools.manage_circle_positions import CirclePositionManager

# Initialize database manager
db_manager = CirclePositionManager('.tmp/circle_positions.db')


class CirclePositionHandler(BaseHTTPRequestHandler):

    def _set_headers(self, status=200):
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_OPTIONS(self):
        self._set_headers()

    def do_GET(self):
        parsed = urlparse(self.path)

        if parsed.path == '/':
            self._set_headers()
            response = {
                'status': 'running',
                'message': 'Circle Position Server',
                'endpoints': {
                    'save': 'POST /save',
                    'load': 'GET /load?label_id=XXX',
                    'list': 'GET /list'
                }
            }
            self.wfile.write(json.dumps(response).encode())

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

        elif parsed.path == '/list':
            all_positions = db_manager.get_all_positions()

            self._set_headers()
            response = {
                'success': True,
                'positions': all_positions
            }
            self.wfile.write(json.dumps(response).encode())

        else:
            self._set_headers(404)
            response = {'error': 'Not found'}
            self.wfile.write(json.dumps(response).encode())

    def do_POST(self):
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
        # Custom logging
        print(f"[{self.log_date_time_string()}] {format % args}")


def run_server(port=5000):
    server_address = ('', port)
    httpd = HTTPServer(server_address, CirclePositionHandler)

    print("=" * 60)
    print("Circle Position Server Started")
    print("=" * 60)
    print(f"Server running at: http://localhost:{port}")
    print()
    print("Endpoints:")
    print(f"  GET  http://localhost:{port}/          - Server status")
    print(f"  POST http://localhost:{port}/save      - Save positions")
    print(f"  GET  http://localhost:{port}/load      - Load positions")
    print(f"  GET  http://localhost:{port}/list      - List all positions")
    print(f"  POST http://localhost:{port}/clear     - Clear positions")
    print()
    print("Database: .tmp/circle_positions.db")
    print()
    print("Press Ctrl+C to stop")
    print("=" * 60)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n\nServer stopped.")
        httpd.server_close()


if __name__ == '__main__':
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 5000
    run_server(port)
