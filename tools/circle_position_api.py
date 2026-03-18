"""
Simple Flask API server to save/load circle positions
Run this server to enable saving circle positions from the HTML interface
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import sys
import os

# Add parent directory to path to import manage_circle_positions
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from tools.manage_circle_positions import CirclePositionManager

app = Flask(__name__)
CORS(app)  # Enable CORS for local HTML files

# Initialize database manager
db_manager = CirclePositionManager('.tmp/circle_positions.db')


@app.route('/')
def index():
    """Root endpoint - API status"""
    return jsonify({
        'status': 'running',
        'message': 'Circle Position API Server',
        'endpoints': {
            'save': 'POST /api/positions/save',
            'load': 'GET /api/positions/load?label_id=XXX',
            'list': 'GET /api/positions/list',
            'clear': 'POST /api/positions/clear'
        }
    })


@app.route('/api/positions/save', methods=['POST'])
def save_positions():
    """Save circle positions"""
    try:
        data = request.json
        label_id = data.get('label_id', 'PVP002XG')
        positions = data.get('positions', {})

        # Convert string keys to integers
        positions_int = {int(k): v for k, v in positions.items()}

        db_manager.save_positions_batch(label_id, positions_int)

        return jsonify({
            'success': True,
            'message': f'Saved {len(positions)} positions for {label_id}'
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/positions/load', methods=['GET'])
def load_positions():
    """Load circle positions for a label"""
    try:
        label_id = request.args.get('label_id', 'PVP002XG')
        positions = db_manager.get_positions(label_id)

        return jsonify({
            'success': True,
            'label_id': label_id,
            'positions': positions
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/positions/list', methods=['GET'])
def list_all_positions():
    """List all positions for all labels"""
    try:
        all_positions = db_manager.get_all_positions()

        return jsonify({
            'success': True,
            'positions': all_positions
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/positions/clear', methods=['POST'])
def clear_positions():
    """Clear positions for a label"""
    try:
        data = request.json
        label_id = data.get('label_id', 'PVP002XG')

        db_manager.clear_label_positions(label_id)

        return jsonify({
            'success': True,
            'message': f'Cleared positions for {label_id}'
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


if __name__ == '__main__':
    print("Starting Circle Position API Server...")
    print("Server running at http://localhost:5000")
    print("\nAvailable endpoints:")
    print("  POST /api/positions/save   - Save circle positions")
    print("  GET  /api/positions/load   - Load circle positions")
    print("  GET  /api/positions/list   - List all positions")
    print("  POST /api/positions/clear  - Clear positions for a label")
    print("\nPress Ctrl+C to stop")

    app.run(debug=True, port=5000)
