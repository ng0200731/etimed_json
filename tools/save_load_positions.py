"""
Simple Python script to save/load circle positions from HTML via file-based communication
No server needed - uses JSON file as intermediate storage
"""

import json
import os
import sys
from manage_circle_positions import CirclePositionManager

# Paths
TEMP_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.tmp')
POSITIONS_FILE = os.path.join(TEMP_DIR, 'circle_positions_temp.json')
DB_PATH = os.path.join(TEMP_DIR, 'circle_positions.db')

# Ensure temp directory exists
os.makedirs(TEMP_DIR, exist_ok=True)

# Initialize database manager
db_manager = CirclePositionManager(DB_PATH)


def save_from_file(label_id='PVP002XG'):
    """Read positions from temp JSON file and save to database"""
    if not os.path.exists(POSITIONS_FILE):
        print(f"No positions file found at {POSITIONS_FILE}")
        return

    with open(POSITIONS_FILE, 'r') as f:
        data = json.load(f)

    positions = data.get('positions', {})
    if not positions:
        print("No positions to save")
        return

    # Convert string keys to integers
    positions_int = {int(k): v for k, v in positions.items()}

    db_manager.save_positions_batch(label_id, positions_int)
    print(f"✓ Saved {len(positions_int)} positions to database")

    # Clean up temp file
    os.remove(POSITIONS_FILE)


def load_to_file(label_id='PVP002XG'):
    """Load positions from database and write to temp JSON file"""
    positions = db_manager.get_positions(label_id)

    data = {
        'label_id': label_id,
        'positions': positions
    }

    with open(POSITIONS_FILE, 'w') as f:
        json.dump(data, f, indent=2)

    print(f"✓ Loaded {len(positions)} positions from database")
    print(f"Written to: {POSITIONS_FILE}")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage:")
        print("  py save_load_positions.py save [label_id]")
        print("  py save_load_positions.py load [label_id]")
        sys.exit(1)

    action = sys.argv[1]
    label_id = sys.argv[2] if len(sys.argv) > 2 else 'PVP002XG'

    if action == 'save':
        save_from_file(label_id)
    elif action == 'load':
        load_to_file(label_id)
    else:
        print(f"Unknown action: {action}")
        sys.exit(1)
