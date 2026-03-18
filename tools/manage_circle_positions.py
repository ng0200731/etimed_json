"""
Tool to manage circle positions in SQLite database
Saves and retrieves red circle positions for price tag field mappings
"""

import sqlite3
import json
import os
from datetime import datetime


class CirclePositionManager:
    def __init__(self, db_path='.tmp/circle_positions.db'):
        """Initialize database connection"""
        self.db_path = db_path

        # Ensure .tmp directory exists
        os.makedirs(os.path.dirname(db_path), exist_ok=True)

        # Initialize database
        self._init_db()

    def _init_db(self):
        """Create tables if they don't exist"""
        schema_path = 'sql/circle_positions.sql'

        with sqlite3.connect(self.db_path) as conn:
            if os.path.exists(schema_path):
                with open(schema_path, 'r') as f:
                    conn.executescript(f.read())
            else:
                # Fallback schema if file doesn't exist
                conn.execute('''
                    CREATE TABLE IF NOT EXISTS circle_positions (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        circle_number INTEGER NOT NULL,
                        label_id TEXT NOT NULL,
                        position_left TEXT NOT NULL,
                        position_top TEXT NOT NULL,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        UNIQUE(circle_number, label_id)
                    )
                ''')
            conn.commit()

    def save_position(self, circle_number, label_id, position_left, position_top):
        """Save or update a circle position"""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute('''
                INSERT INTO circle_positions (circle_number, label_id, position_left, position_top, updated_at)
                VALUES (?, ?, ?, ?, ?)
                ON CONFLICT(circle_number, label_id)
                DO UPDATE SET
                    position_left = excluded.position_left,
                    position_top = excluded.position_top,
                    updated_at = excluded.updated_at
            ''', (circle_number, label_id, position_left, position_top, datetime.now()))
            conn.commit()

        print(f"Saved circle {circle_number} for {label_id} at ({position_left}, {position_top})")

    def save_positions_batch(self, label_id, positions_dict):
        """Save multiple positions at once

        Args:
            label_id: The label identifier (e.g., 'PVP002XG')
            positions_dict: Dict like {2: {'left': '10%', 'top': '20%'}, 3: {...}}
        """
        with sqlite3.connect(self.db_path) as conn:
            for circle_num, pos in positions_dict.items():
                conn.execute('''
                    INSERT INTO circle_positions (circle_number, label_id, position_left, position_top, updated_at)
                    VALUES (?, ?, ?, ?, ?)
                    ON CONFLICT(circle_number, label_id)
                    DO UPDATE SET
                        position_left = excluded.position_left,
                        position_top = excluded.position_top,
                        updated_at = excluded.updated_at
                ''', (int(circle_num), label_id, pos['left'], pos['top'], datetime.now()))
            conn.commit()

        print(f"Saved {len(positions_dict)} circle positions for {label_id}")

    def get_positions(self, label_id):
        """Get all circle positions for a label

        Returns:
            Dict like {2: {'left': '10%', 'top': '20%'}, 3: {...}}
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute('''
                SELECT circle_number, position_left, position_top
                FROM circle_positions
                WHERE label_id = ?
                ORDER BY circle_number
            ''', (label_id,))

            positions = {}
            for row in cursor.fetchall():
                positions[row[0]] = {
                    'left': row[1],
                    'top': row[2]
                }

            return positions

    def get_all_positions(self):
        """Get all circle positions grouped by label_id"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute('''
                SELECT label_id, circle_number, position_left, position_top
                FROM circle_positions
                ORDER BY label_id, circle_number
            ''')

            all_positions = {}
            for row in cursor.fetchall():
                label_id = row[0]
                if label_id not in all_positions:
                    all_positions[label_id] = {}

                all_positions[label_id][row[1]] = {
                    'left': row[2],
                    'top': row[3]
                }

            return all_positions

    def delete_position(self, circle_number, label_id):
        """Delete a specific circle position"""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute('''
                DELETE FROM circle_positions
                WHERE circle_number = ? AND label_id = ?
            ''', (circle_number, label_id))
            conn.commit()

        print(f"Deleted circle {circle_number} for {label_id}")

    def clear_label_positions(self, label_id):
        """Clear all positions for a specific label"""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute('DELETE FROM circle_positions WHERE label_id = ?', (label_id,))
            conn.commit()

        print(f"Cleared all positions for {label_id}")


def main():
    """CLI interface for managing circle positions"""
    import argparse

    parser = argparse.ArgumentParser(description='Manage circle positions in database')
    parser.add_argument('action', choices=['save', 'load', 'list', 'clear'],
                       help='Action to perform')
    parser.add_argument('--label-id', default='PVP002XG',
                       help='Label ID (default: PVP002XG)')
    parser.add_argument('--positions', type=str,
                       help='JSON string of positions to save')
    parser.add_argument('--db', default='.tmp/circle_positions.db',
                       help='Database path')

    args = parser.parse_args()

    manager = CirclePositionManager(args.db)

    if args.action == 'save':
        if not args.positions:
            print("Error: --positions required for save action")
            return

        positions = json.loads(args.positions)
        manager.save_positions_batch(args.label_id, positions)

    elif args.action == 'load':
        positions = manager.get_positions(args.label_id)
        print(json.dumps(positions, indent=2))

    elif args.action == 'list':
        all_positions = manager.get_all_positions()
        print(json.dumps(all_positions, indent=2))

    elif args.action == 'clear':
        manager.clear_label_positions(args.label_id)


if __name__ == '__main__':
    main()
