"""
Convert HTML report to PDF
"""

import sys
import os

try:
    from weasyprint import HTML
except ImportError:
    print("WeasyPrint not installed. Install with:")
    print("pip install weasyprint")
    sys.exit(1)


def html_to_pdf(html_file, pdf_file):
    """Convert HTML file to PDF"""
    try:
        print(f"Converting {html_file} to PDF...")

        # Convert HTML to PDF
        HTML(filename=html_file).write_pdf(pdf_file)

        print(f"PDF created successfully: {pdf_file}")

        # Get file size
        size_mb = os.path.getsize(pdf_file) / (1024 * 1024)
        print(f"File size: {size_mb:.2f} MB")

    except Exception as e:
        print(f"Error converting to PDF: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: py html_to_pdf.py <html_file> <output_pdf>")
        sys.exit(1)

    html_file = sys.argv[1]
    pdf_file = sys.argv[2]

    if not os.path.exists(html_file):
        print(f"HTML file not found: {html_file}")
        sys.exit(1)

    html_to_pdf(html_file, pdf_file)
