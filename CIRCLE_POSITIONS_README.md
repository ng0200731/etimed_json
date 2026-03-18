# Circle Position Management System

This system allows you to save and load red circle positions on price tag images to a SQLite database.

## Setup

1. Install required dependencies:
```bash
pip install -r requirements_api.txt
```

2. The database will be automatically created at `.tmp/circle_positions.db` when you first run the API server.

## Usage

### 1. Start the API Server

```bash
py tools/circle_position_api.py
```

The server will start at `http://localhost:5000`

### 2. Open the HTML Report

Open `LABEL_GENERATION_REPORT.html` in your browser. The page will automatically:
- Load any previously saved circle positions from the database
- Display them on the price tag image

### 3. Place and Save Circles

- **Double-click** a row in the "PRICE TAG FIELD MAPPING" table to activate placement mode
- **Click** on the price tag image to place the red circle
- **Drag** the circle to adjust its position
- Positions are **automatically saved** to the database after placing or dragging

### 4. View Saved Positions

- **Hover** over any table row to see where its circle is positioned (if already placed)
- Saved circles are displayed with semi-transparent red circles and numbers

## Command Line Tools

### Save positions manually:
```bash
py tools/manage_circle_positions.py save --label-id PVP002XG --positions "{\"2\": {\"left\": \"10%\", \"top\": \"20%\"}}"
```

### Load positions:
```bash
py tools/manage_circle_positions.py load --label-id PVP002XG
```

### List all positions:
```bash
py tools/manage_circle_positions.py list
```

### Clear positions for a label:
```bash
py tools/manage_circle_positions.py clear --label-id PVP002XG
```

## API Endpoints

- `POST /api/positions/save` - Save circle positions
- `GET /api/positions/load?label_id=PVP002XG` - Load positions for a label
- `GET /api/positions/list` - List all positions
- `POST /api/positions/clear` - Clear positions for a label

## Database Schema

The SQLite database stores:
- `circle_number` - The field number (2, 3, 4, etc.)
- `label_id` - The label identifier (e.g., 'PVP002XG')
- `position_left` - Horizontal position (e.g., '45.5%')
- `position_top` - Vertical position (e.g., '23.2%')
- `created_at` - When the position was first saved
- `updated_at` - When the position was last updated

## Browser Console Commands

Open the browser console (F12) and use:

```javascript
// Get current positions
getCirclePositions()

// Manually save positions
savePositions()

// Reload positions from database
loadPositions()
```

## Troubleshooting

**"Error saving to database"** - Make sure the API server is running:
```bash
py tools/circle_position_api.py
```

**CORS errors** - The API server has CORS enabled for local development. If you still see errors, check that the API_BASE_URL in the HTML matches your server address.

**Positions not loading** - Check the browser console for error messages. Ensure the database file exists at `.tmp/circle_positions.db`.
