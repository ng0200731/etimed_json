"""
Convert PDF first page to base64 encoded image for HTML embedding
"""

import sys
import base64
import os

try:
    from pdf2image import convert_from_path
    from PIL import Image
    import io
except ImportError:
    print("Required libraries not installed. Install with:")
    print("pip install pdf2image pillow")
    sys.exit(1)


def pdf_to_base64(pdf_path, max_width=400):
    """Convert first page of PDF to base64 encoded PNG"""
    try:
        # Convert first page of PDF to image
        images = convert_from_path(pdf_path, first_page=1, last_page=1, dpi=150)

        if not images:
            return None

        img = images[0]

        # Resize if too large
        if img.width > max_width:
            ratio = max_width / img.width
            new_height = int(img.height * ratio)
            img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)

        # Convert to PNG bytes
        buffer = io.BytesIO()
        img.save(buffer, format='PNG')
        buffer.seek(0)

        # Encode to base64
        img_base64 = base64.b64encode(buffer.read()).decode('utf-8')

        return f"data:image/png;base64,{img_base64}"

    except Exception as e:
        print(f"Error converting {pdf_path}: {e}")
        return None


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: py pdf_to_base64.py <pdf_file>")
        sys.exit(1)

    pdf_path = sys.argv[1]

    if not os.path.exists(pdf_path):
        print(f"File not found: {pdf_path}")
        sys.exit(1)

    base64_data = pdf_to_base64(pdf_path)

    if base64_data:
        print(base64_data[:100] + "...")
        print(f"\nTotal length: {len(base64_data)} characters")
    else:
        print("Failed to convert PDF")
