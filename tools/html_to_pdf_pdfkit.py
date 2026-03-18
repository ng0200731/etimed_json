"""
Convert HTML report to PDF using pdfkit (wkhtmltopdf wrapper)
"""

import sys
import os

try:
    import pdfkit
except ImportError:
    print("pdfkit not installed. Install with:")
    print("pip install pdfkit")
    print("\nAlso download wkhtmltopdf from:")
    print("https://wkhtmltopdf.org/downloads.html")
    sys.exit(1)


def html_to_pdf_pdfkit(html_file, pdf_file):
    """Convert HTML file to PDF using pdfkit"""
    try:
        print(f"Converting {html_file} to PDF...")

        # Configure options to maintain layout
        options = {
            'page-size': 'A4',
            'margin-top': '10mm',
            'margin-right': '10mm',
            'margin-bottom': '10mm',
            'margin-left': '10mm',
            'encoding': "UTF-8",
            'enable-local-file-access': None,
            'no-outline': None,
            'print-media-type': None
        }

        # Convert HTML to PDF
        pdfkit.from_file(html_file, pdf_file, options=options)

        print(f"PDF created successfully: {pdf_file}")

        # Get file size
        size_mb = os.path.getsize(pdf_file) / (1024 * 1024)
        print(f"File size: {size_mb:.2f} MB")

    except Exception as e:
        print(f"Error converting to PDF: {e}")
        print("\nMake sure wkhtmltopdf is installed:")
        print("https://wkhtmltopdf.org/downloads.html")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: py html_to_pdf_pdfkit.py <html_file> <output_pdf>")
        sys.exit(1)

    html_file = sys.argv[1]
    pdf_file = sys.argv[2]

    if not os.path.exists(html_file):
        print(f"HTML file not found: {html_file}")
        sys.exit(1)

    html_to_pdf_pdfkit(html_file, pdf_file)
