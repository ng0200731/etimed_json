"""
Convert HTML report to PDF using Playwright (browser-based)
"""

import sys
import os
from pathlib import Path

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    print("Playwright not installed. Install with:")
    print("pip install playwright")
    print("playwright install chromium")
    sys.exit(1)


def html_to_pdf_playwright(html_file, pdf_file):
    """Convert HTML file to PDF using Playwright"""
    try:
        print(f"Converting {html_file} to PDF using browser...")

        # Convert to absolute path and file URL
        html_path = Path(html_file).resolve()
        file_url = html_path.as_uri()

        with sync_playwright() as p:
            # Launch browser
            browser = p.chromium.launch()
            page = browser.new_page()

            # Load HTML file
            page.goto(file_url)

            # Wait for page to load
            page.wait_for_load_state('networkidle')

            # Generate PDF
            page.pdf(
                path=pdf_file,
                format='A4',
                margin={
                    'top': '10mm',
                    'right': '10mm',
                    'bottom': '10mm',
                    'left': '10mm'
                },
                print_background=True,
                prefer_css_page_size=False,
                scale=0.8
            )

            browser.close()

        print(f"PDF created successfully: {pdf_file}")

        # Get file size
        size_mb = os.path.getsize(pdf_file) / (1024 * 1024)
        print(f"File size: {size_mb:.2f} MB")

    except Exception as e:
        print(f"Error converting to PDF: {e}")
        print("\nMake sure Playwright is installed:")
        print("pip install playwright")
        print("playwright install chromium")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: py html_to_pdf_playwright.py <html_file> <output_pdf>")
        sys.exit(1)

    html_file = sys.argv[1]
    pdf_file = sys.argv[2]

    if not os.path.exists(html_file):
        print(f"HTML file not found: {html_file}")
        sys.exit(1)

    html_to_pdf_playwright(html_file, pdf_file)
