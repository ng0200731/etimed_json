# Circle Position Management System

This system allows you to save and load red circle positions for price tag field mappings.

## Components

### 1. Database Schema
- **File**: `sql/circle_positions.sql`
- **Table**: `circle_positions`
- Stores circle number, label ID, and position (left/top percentages)

### 2. Python Manager
- **File**: `tools/manage_circle_positions.py`
- **Class**: `CirclePositionManager`
- Handles database operations (save, load, delete, clear)

### 3. Flask API Server
- **File**: `tools/circle_position_api.py`
- **Port**: 5000
- **Endpoints**:
  - `POST /api/positions/save` - Save circle positions
  - `GET /api/positions/load` - Load circle positions
  - `GET /api/positions/list` - List all positions
  - `POST /api/positions/clear` - Clear positions for a label

### 4. HTML Interface
- **File**: `LABEL_GENERATION_REPORT.html`
- Auto-saves positions when placing or dragging circles
- Auto-loads positions on page load
- Shows hover preview when hovering over table rows

## Usage

### Step 1: Start the API Server

```bash
py tools/circle_position_api.py
```

The server will start at `http://localhost:5000`

### Step 2: Open the HTML Report

Open `LABEL_GENERATION_REPORT.html` in your browser. The page will automatically:
- Load any previously saved circle positions from the database
- Display saved circles with reduced opacity
- Save positions automatically when you place or drag circles

### Step 3: Place Circles

1. Double-click on a field mapping row (e.g., "2 Code of supplier")
2. The circle size will reduce to half
3. Click on the price tag image to place the circle
4. The position is automatically saved to the database

### Step 4: Hover to Preview

Hover over any field mapping row to see where its circle is positioned on the price tag image.

## Command Line Interface

You can also manage positions via command line:

### Save positions
```bash
py tools/manage_circle_positions.py save --label-id PVP002XG --positions '{"2": {"left": "10%", "top": "20%"}}'
```

### Load positions
```bash
py tools/manage_circle_positions.py load --label-id PVP002XG
```

### List all positions
```bash
py tools/manage_circle_positions.py list
```

### Clear positions for a label
```bash
py tools/manage_circle_positions.py clear --label-id PVP002XG
```

## Browser Console Functions

Open the browser console (F12) to access these functions:

- `getCirclePositions()` - View current positions in memory
- `savePositions()` - Manually trigger save to database
- `loadPositions()` - Manually reload from database

## Database Location

The SQLite database is stored at: `.tmp/circle_positions.db`

This file is automatically created when you first save positions.

## Troubleshooting

### "Failed to save positions" error
- Make sure the API server is running (`py tools/circle_position_api.py`)
- Check that port 5000 is not blocked by firewall
- Look for error messages in the server console

### Positions not loading
- Check browser console for error messages
- Verify the API server is running
- Try manually loading: `loadPositions()` in browser console

### CORS errors
- The API server has CORS enabled for local development
- If you still see CORS errors, make sure you're accessing the HTML file via `file://` protocol or a local web server
