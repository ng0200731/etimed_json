-- Schema for storing red circle positions on price tag images
-- Each circle represents a field mapping location on the PDF template

CREATE TABLE IF NOT EXISTS circle_positions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    circle_number INTEGER NOT NULL,
    label_id TEXT NOT NULL,
    position_left TEXT NOT NULL,
    position_top TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(circle_number, label_id)
);

-- Index for faster lookups by label_id
CREATE INDEX IF NOT EXISTS idx_label_id ON circle_positions(label_id);

-- Index for faster lookups by circle_number
CREATE INDEX IF NOT EXISTS idx_circle_number ON circle_positions(circle_number);
