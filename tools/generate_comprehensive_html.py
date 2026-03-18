"""
Generate comprehensive HTML report for label groups with PDF selection logic
"""

import json
import sys
import os


def format_currency(value, currency):
    """Format currency values"""
    if currency == 'EUR':
        return f"€{value}"
    elif currency == 'INR':
        return f"₹{value}"
    else:
        return f"{value} {currency}"


def generate_comprehensive_html(json_file, output_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Extract order data
    if isinstance(data, list) and len(data) > 0:
        order = data[0]
    else:
        order = data

    # Get order info
    order_info = order.get('LabelOrder', order)
    supplier = order.get('Supplier', {})
    style_colors = order.get('StyleColor', [])

    if not style_colors:
        print("No StyleColor data found")
        return

    style_color = style_colors[0]
    label_data = style_color.get('LabelData', [])

    # PDF mappings
    pdf_mappings = {
        'ADHEDIST': 'ADHEDIST-mango.pdf',
        'GI000PRO': 'GI000DPO-SAP_1.pdf',
        'GI001BAW': 'GI001BAW-GI001BAC.pdf',
        'PVP002XG': 'PVPV0102-PVP002XG.pdf'
    }

    purposes = {
        'ADHEDIST': 'Brand Logo',
        'GI000PRO': 'Composition Label Template (sewn-in)',
        'GI001BAW': 'Hang Tag Template (95x40mm)',
        'PVP002XG': 'Price Tag with RFID (90x58mm)'
    }

    # Image data (base64 encoded)
    # Place image1.png, image2.png, image3.png, image4.png in the same folder as the HTML
    image_data = {
        'ADHEDIST': 'image1.png',  # ADHEDIST-mango.pdf preview
        'GI000PRO': 'image2.png',  # GI000DPO-SAP_1.pdf preview
        'GI001BAW': 'image3.png',  # GI001BAW-GI001BAC.pdf preview
        'PVP002XG': 'image4.png'   # PVPV0102-PVP002XG.pdf preview
    }

    # Start HTML
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Label Generation Report</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: #ffffff;
            color: #000000;
            line-height: 1.6;
            padding: 20px;
        }}

        .container {{
            max-width: 1400px;
            margin: 0 auto;
        }}

        header {{
            border-bottom: 3px solid #000000;
            padding-bottom: 20px;
            margin-bottom: 40px;
        }}

        h1 {{
            font-size: 32px;
            font-weight: 700;
            margin-bottom: 10px;
        }}

        .subtitle {{
            font-size: 14px;
            color: #666666;
            margin-bottom: 5px;
        }}

        .order-info {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
            margin-top: 20px;
            padding: 15px;
            background: #f5f5f5;
            border: 1px solid #000000;
        }}

        .order-info-item {{
            display: flex;
            flex-direction: column;
        }}

        .order-info-label {{
            font-size: 11px;
            font-weight: 600;
            color: #666666;
            text-transform: uppercase;
        }}

        .order-info-value {{
            font-size: 14px;
            font-weight: 600;
        }}

        .label-group {{
            border: 2px solid #000000;
            margin-bottom: 40px;
            background: #ffffff;
        }}

        .label-header {{
            background: #000000;
            color: #ffffff;
            padding: 20px;
        }}

        .label-title {{
            font-size: 24px;
            font-weight: 700;
            margin-bottom: 10px;
        }}

        .label-meta {{
            font-size: 14px;
            display: flex;
            gap: 30px;
            flex-wrap: wrap;
        }}

        .label-meta-item {{
            display: flex;
            gap: 8px;
        }}

        .label-meta-label {{
            font-weight: 600;
        }}

        .pdf-link {{
            display: inline-block;
            background: #ffffff;
            color: #000000;
            border: 2px solid #ffffff;
            padding: 8px 16px;
            text-decoration: none;
            font-weight: 700;
            font-size: 16px;
            margin-top: 15px;
        }}

        .purpose-badge {{
            display: inline-block;
            background: #ffffff;
            border: 2px solid #000000;
            padding: 6px 12px;
            font-weight: 600;
            font-size: 13px;
            margin-top: 10px;
        }}

        .label-body {{
            padding: 20px;
        }}

        .section {{
            margin-bottom: 30px;
        }}

        .section-title {{
            font-size: 16px;
            font-weight: 700;
            margin-bottom: 15px;
            padding-bottom: 8px;
            border-bottom: 2px solid #000000;
        }}

        .data-grid {{
            display: grid;
            gap: 20px;
        }}

        .data-card {{
            border: 1px solid #000000;
            padding: 15px;
            background: #ffffff;
        }}

        .data-card-title {{
            font-weight: 700;
            margin-bottom: 10px;
            font-size: 14px;
            padding-bottom: 5px;
            border-bottom: 1px solid #cccccc;
        }}

        .data-table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 13px;
        }}

        .data-table th {{
            background: #000000;
            color: #ffffff;
            padding: 10px 8px;
            text-align: left;
            font-weight: 600;
            font-size: 12px;
        }}

        .data-table td {{
            padding: 8px;
            border: 1px solid #cccccc;
        }}

        .data-table tr:nth-child(even) {{
            background: #f9f9f9;
        }}

        .info-grid {{
            display: grid;
            grid-template-columns: 200px 1fr;
            gap: 10px;
            font-size: 13px;
        }}

        .info-label {{
            font-weight: 700;
        }}

        .info-value {{
            color: #333333;
        }}

        .pdf-selection {{
            background: #f5f5f5;
            border: 2px solid #000000;
            padding: 15px;
            margin-top: 10px;
        }}

        .pdf-selection-title {{
            font-weight: 700;
            font-size: 16px;
            margin-bottom: 10px;
        }}

        .pdf-preview {{
            margin-top: 15px;
            text-align: center;
            border: 1px solid #cccccc;
            padding: 10px;
            background: #ffffff;
        }}

        .pdf-preview img {{
            max-width: 100%;
            height: auto;
            border: 1px solid #000000;
        }}

        .pdf-preview-caption {{
            margin-top: 10px;
            font-size: 12px;
            color: #666666;
            font-style: italic;
        }}

        .rules-section {{
            background: #fffacd;
            border: 2px solid #000000;
            padding: 20px;
            margin-bottom: 30px;
        }}

        .rules-title {{
            font-size: 18px;
            font-weight: 700;
            margin-bottom: 15px;
        }}

        .rule-group {{
            margin-bottom: 20px;
            padding: 15px;
            background: #ffffff;
            border: 1px solid #000000;
        }}

        .rule-group-title {{
            font-weight: 700;
            font-size: 14px;
            margin-bottom: 10px;
        }}

        .rule-logic {{
            font-family: 'Courier New', monospace;
            font-size: 12px;
            background: #f5f5f5;
            padding: 10px;
            margin: 5px 0;
        }}

        .selected {{
            color: #006400;
            font-weight: 700;
        }}

        .not-selected {{
            color: #8b0000;
            font-weight: 700;
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>Label Generation Report</h1>
            <div class="subtitle">Comprehensive analysis of label data and PDF file selection</div>

            <div class="order-info">
                <div class="order-info-item">
                    <span class="order-info-label">Order ID</span>
                    <span class="order-info-value">{order_info.get('Id', 'N/A')}</span>
                </div>
                <div class="order-info-item">
                    <span class="order-info-label">Season</span>
                    <span class="order-info-value">{order_info.get('Temporada', 'N/A')}</span>
                </div>
                <div class="order-info-item">
                    <span class="order-info-label">Supplier</span>
                    <span class="order-info-value">{supplier.get('SupplierName', 'N/A')}</span>
                </div>
                <div class="order-info-item">
                    <span class="order-info-label">Style ID</span>
                    <span class="order-info-value">{style_color.get('StyleID', 'N/A')}</span>
                </div>
                <div class="order-info-item">
                    <span class="order-info-label">Product</span>
                    <span class="order-info-value">{style_color.get('ProductType', 'N/A')}</span>
                </div>
                <div class="order-info-item">
                    <span class="order-info-label">Color</span>
                    <span class="order-info-value">{style_color.get('Color', 'N/A')}</span>
                </div>
            </div>
        </header>

        <div class="rules-section">
            <div class="rules-title">PRODUCT INFORMATION</div>
            <div class="info-grid">
                <div class="info-label">Line:</div>
                <div class="info-value">{style_color.get('Line', 'N/A')}</div>
                <div class="info-label">Packaging:</div>
                <div class="info-value">{style_color.get('Packaging', 'N/A')}</div>
                <div class="info-label">Product Type:</div>
                <div class="info-value">{style_color.get('ProductType', 'N/A')}</div>
                <div class="info-label">Family:</div>
                <div class="info-value">{style_color.get('FAMILY', 'N/A')}</div>
            </div>
            <div style="margin-top: 15px; font-size: 13px; color: #666666;">
                Each label group below shows how these JSON values determine which PDFs are selected from the available pools.
            </div>
        </div>
"""

    # Generate each label group
    for idx, label in enumerate(label_data, 1):
        label_id = label.get('LabelID', 'UNKNOWN')
        vendor = label.get('Vendor', 'N/A')
        variable = label.get('Variable', 'N/A')
        pdf_file = pdf_mappings.get(label_id, f'{label_id}-*.pdf')
        purpose = purposes.get(label_id, 'Unknown')
        image_file = image_data.get(label_id, '')

        html += f"""
        <div class="label-group">
            <div class="label-header">
                <div class="label-title">[{idx}] LabelID: {label_id}</div>
                <div class="label-meta">
                    <div class="label-meta-item">
                        <span class="label-meta-label">Vendor:</span>
                        <span>{vendor}</span>
                    </div>
                    <div class="label-meta-item">
                        <span class="label-meta-label">Variable:</span>
                        <span>{variable}</span>
                    </div>
                </div>
                <div class="purpose-badge">{purpose}</div>
                <div class="pdf-link">→ PDF File: {pdf_file}</div>
            </div>

            <div class="label-body">
                <div class="section">
                    <div class="section-title">PRIMARY PDF FILE (from JSON LabelData)</div>
                    <div class="pdf-selection">
                        <div class="pdf-selection-title">This label uses: {pdf_file}</div>
                        <div style="font-size: 13px; color: #666666; margin-top: 5px;">
                            JSON data (LabelID='{label_id}', Vendor={vendor}, Variable={variable}) → PDF: {pdf_file}
                        </div>
                        <div class="pdf-preview">
                            <img src="{image_file}" alt="{pdf_file} preview" onerror="this.onerror=null; this.src='data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%22400%22 height=%22300%22%3E%3Crect width=%22400%22 height=%22300%22 fill=%22%23f5f5f5%22 stroke=%22%23000%22 stroke-width=%222%22/%3E%3Ctext x=%2250%25%22 y=%2250%25%22 text-anchor=%22middle%22 font-family=%22Arial%22 font-size=%2216%22%3E{pdf_file}%3C/text%3E%3C/svg%3E';">
                            <div class="pdf-preview-caption">Preview of {pdf_file}</div>
                        </div>
                    </div>
                </div>

                <div class="section">
                    <div class="section-title">ADDITIONAL PDF FILES (from TRANSLATIONS&RULES.xlsx)</div>
                    <div style="font-size: 13px; margin-bottom: 15px; color: #666666;">
                        Each label group also uses additional PDFs selected from pools based on JSON data values:
                    </div>

                    <div class="rule-group">
                        <div class="rule-group-title">GROUP 1: Product Code PDFs (Pool: CODE 1-16.pdf)</div>
                        <div class="info-grid" style="margin-bottom: 10px;">
                            <div class="info-label">JSON Value - Line:</div>
                            <div class="info-value">{style_color.get('Line', 'N/A')}</div>
                            <div class="info-label">JSON Value - Packaging:</div>
                            <div class="info-value">{style_color.get('Packaging', 'N/A')}</div>
                        </div>
                        <div class="rule-logic">IF Line='{style_color.get('Line')}' AND Packaging='{style_color.get('Packaging')}' → THEN CODE 15.pdf</div>
                        <div class="selected">✓ SELECTED: CODE 15.pdf</div>
                    </div>

                    <div class="rule-group">
                        <div class="rule-group-title">GROUP 2: Triman Recycling Symbols (Pool: triman 1-3.pdf)</div>
                        <div class="info-grid" style="margin-bottom: 10px;">
                            <div class="info-label">JSON Value - ProductType:</div>
                            <div class="info-value">{style_color.get('ProductType', 'N/A')}</div>
                        </div>
                        <div class="rule-logic">IF ProductType='{style_color.get('ProductType')}' → THEN triman 1.pdf</div>
                        <div class="selected">✓ SELECTED: triman 1.pdf</div>
                    </div>

                    <div class="rule-group">
                        <div class="rule-group-title">GROUP 3: EAC Symbol (Pool: EAC.pdf)</div>
                        <div class="info-grid" style="margin-bottom: 10px;">
                            <div class="info-label">JSON Value - EAC:</div>
                            <div class="info-value">1 (from TRANSLATIONS&RULES lookup)</div>
                        </div>
                        <div class="rule-logic">IF EAC=1 → THEN EAC.pdf</div>
                        <div class="selected">✓ SELECTED: EAC.pdf</div>
                    </div>

                    <div class="rule-group">
                        <div class="rule-group-title">GROUP 4: Korean Symbol (Pool: korean_symbol.pdf)</div>
                        <div class="info-grid" style="margin-bottom: 10px;">
                            <div class="info-label">JSON Value - KOREAN SYMBOL:</div>
                            <div class="info-value">(blank/empty)</div>
                        </div>
                        <div class="rule-logic">IF KOREAN SYMBOL=blank → THEN skip</div>
                        <div class="not-selected">✗ NOT SELECTED</div>
                    </div>

                    <div style="margin-top: 15px; padding: 10px; background: #f0f0f0; border-left: 4px solid #000000;">
                        <strong>Total PDFs for this label group:</strong> 4 files
                        <ul style="margin-top: 5px; margin-left: 20px;">
                            <li>{pdf_file} (primary)</li>
                            <li>CODE 15.pdf (from pool)</li>
                            <li>triman 1.pdf (from pool)</li>
                            <li>EAC.pdf (from pool)</li>
                        </ul>
                    </div>
                </div>
"""

        # Composition data
        if label_id in ['GI000PRO', 'GI001BAW']:
            composition = style_color.get('Composition', [])
            html += f"""
                <div class="section">
                    <div class="section-title">COMPOSITION DATA</div>
                    <div class="data-grid">
"""
            for comp_idx, comp in enumerate(composition, 1):
                fabrics = comp.get('Fabric', [])
                html += f"""
                        <div class="data-card">
                            <div class="data-card-title">{comp.get('TitleName', 'N/A')}</div>
                            <table class="data-table">
                                <thead>
                                    <tr>
                                        <th>Material</th>
                                        <th>Percentage</th>
                                        <th>Type</th>
                                    </tr>
                                </thead>
                                <tbody>
"""
                for fabric in fabrics:
                    html += f"""
                                    <tr>
                                        <td>{fabric.get('FabricName', 'N/A')}</td>
                                        <td>{fabric.get('FabricPercent', 'N/A')}%</td>
                                        <td>{fabric.get('FabricTypeSymbol', 'N/A')}</td>
                                    </tr>
"""
                html += """
                                </tbody>
                            </table>
                        </div>
"""
            html += """
                    </div>
                </div>
"""

        # Care instructions
        if label_id in ['GI000PRO', 'GI001BAW']:
            care = style_color.get('CareInstructions', [])
            html += f"""
                <div class="section">
                    <div class="section-title">CARE INSTRUCTIONS</div>
                    <table class="data-table">
                        <thead>
                            <tr>
                                <th>#</th>
                                <th>Instruction</th>
                                <th>Code</th>
                                <th>Group</th>
                            </tr>
                        </thead>
                        <tbody>
"""
            for care_idx, instruction in enumerate(care, 1):
                html += f"""
                            <tr>
                                <td>{care_idx}</td>
                                <td>{instruction.get('CareName', 'N/A')}</td>
                                <td>{instruction.get('CareCode', 'N/A')}</td>
                                <td>{instruction.get('CareGroup', 'N/A')}</td>
                            </tr>
"""
            html += """
                        </tbody>
                    </table>
                </div>
"""

        # Size/Item data
        item_data = style_color.get('ItemData', [])
        html += f"""
                <div class="section">
                    <div class="section-title">SIZE & ITEM DATA ({len(item_data)} variants)</div>
                    <table class="data-table">
                        <thead>
                            <tr>
                                <th>Size</th>
                                <th>EAN13</th>
                                <th>Material</th>
                                <th>Qty</th>
                                <th>Price (EUR)</th>
                                <th>ES</th>
                                <th>IT</th>
                                <th>UK</th>
                                <th>US</th>
                            </tr>
                        </thead>
                        <tbody>
"""
        for item in item_data:
            price_eur = format_currency(item.get('PVP_EU', item.get('PVP_ES', 'N/A')), 'EUR')
            html += f"""
                            <tr>
                                <td><strong>{item.get('SizeName', 'N/A')}</strong></td>
                                <td>{item.get('EAN13', 'N/A')}</td>
                                <td>{item.get('Material', 'N/A')}</td>
                                <td>{item.get('itemQty', 'N/A')}</td>
                                <td><strong>{price_eur}</strong></td>
                                <td>{item.get('SizeNameES', 'N/A')}</td>
                                <td>{item.get('SizeNameIT', 'N/A')}</td>
                                <td>{item.get('SizeNameUK', 'N/A')}</td>
                                <td>{item.get('SizeNameUS', 'N/A')}</td>
                            </tr>
"""
        html += """
                        </tbody>
                    </table>
                </div>
"""

        # Price data
        if label_id in ['PVP002XG', 'PVPV0102']:
            pvp_data = style_color.get('PVP', [])
            html += f"""
                <div class="section">
                    <div class="section-title">PRICE DATA (Multiple Markets)</div>
                    <table class="data-table">
                        <thead>
                            <tr>
                                <th>Market</th>
                                <th>Price</th>
                                <th>Currency</th>
                            </tr>
                        </thead>
                        <tbody>
"""
            for pvp in pvp_data:
                # Extract price and currency
                for key, value in pvp.items():
                    if key.startswith('PVP_') and key != 'PVP':
                        market = key.replace('PVP_', '')
                        currency = pvp.get('Currency', 'N/A')
                        formatted_price = format_currency(value, currency)
                        html += f"""
                            <tr>
                                <td><strong>{market}</strong></td>
                                <td><strong>{formatted_price}</strong></td>
                                <td>{currency}</td>
                            </tr>
"""
            html += """
                        </tbody>
                    </table>
                </div>
"""

        # Origin/Destination
        origin = style_color.get('Origin', {})
        destination = style_color.get('Destination', {})
        html += f"""
                <div class="section">
                    <div class="section-title">ORIGIN & DESTINATION</div>
                    <div class="data-grid" style="grid-template-columns: 1fr 1fr;">
                        <div class="data-card">
                            <div class="data-card-title">Origin</div>
                            <div class="info-grid">
                                <div class="info-label">Country:</div>
                                <div class="info-value">{origin.get('countryorigin', 'N/A')}</div>
                                <div class="info-label">Code:</div>
                                <div class="info-value">{origin.get('Code_Country', 'N/A')}</div>
                            </div>
                        </div>
                        <div class="data-card">
                            <div class="data-card-title">Destination</div>
                            <div class="info-grid">
                                <div class="info-label">DC:</div>
                                <div class="info-value">{destination.get('dc', 'N/A')}</div>
                                <div class="info-label">Code:</div>
                                <div class="info-value">{destination.get('de_code', 'N/A')}</div>
                                <div class="info-label">Address:</div>
                                <div class="info-value">{destination.get('dc_address', 'N/A')}</div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
"""

    # Summary section
    html += """
        <div class="rules-section">
            <div class="rules-title">SUMMARY: ALL PDF FILES USED</div>
            <table class="data-table">
                <thead>
                    <tr>
                        <th>#</th>
                        <th>PDF File</th>
                        <th>Category</th>
                        <th>Source</th>
                    </tr>
                </thead>
                <tbody>
"""

    file_num = 1
    used_files = []

    for label in label_data:
        label_id = label.get('LabelID', 'UNKNOWN')
        pdf_file = pdf_mappings.get(label_id, f'{label_id}-*.pdf')
        purpose = purposes.get(label_id, 'Unknown')
        used_files.append(pdf_file)
        html += f"""
                    <tr>
                        <td>{file_num}</td>
                        <td><strong>{pdf_file}</strong></td>
                        <td>{purpose}</td>
                        <td>JSON LabelData</td>
                    </tr>
"""
        file_num += 1

    # Add rule-based PDFs
    rule_based_pdfs = [
        ('CODE 15.pdf', 'Product Code', 'TRANSLATIONS&RULES.xlsx'),
        ('triman 1.pdf', 'Recycling Symbol', 'TRANSLATIONS&RULES.xlsx'),
        ('EAC.pdf', 'EAC Symbol', 'TRANSLATIONS&RULES.xlsx')
    ]

    for pdf_file, category, source in rule_based_pdfs:
        used_files.append(pdf_file)
        html += f"""
                    <tr>
                        <td>{file_num}</td>
                        <td><strong>{pdf_file}</strong></td>
                        <td>{category}</td>
                        <td>{source}</td>
                    </tr>
"""
        file_num += 1

    html += """
                </tbody>
            </table>
        </div>

        <div class="rules-section" style="background: #fffacd;">
            <div class="rules-title">AVAILABLE PDFs NOT SELECTED FOR THIS PRODUCT</div>
            <div style="font-size: 13px; margin-bottom: 15px; color: #666666;">
                These PDF files are available in the test folder but were not selected for this specific product based on JSON data values and TRANSLATIONS&RULES.xlsx logic:
            </div>
            <table class="data-table">
                <thead>
                    <tr>
                        <th>#</th>
                        <th>PDF File</th>
                        <th>Category/Pool</th>
                        <th>Why Not Selected</th>
                    </tr>
                </thead>
                <tbody>
"""

    # Define all available PDFs in test folder
    not_selected_pdfs = {
        'CODE 1.pdf': ('Product Code Pool', 'Different Line/Packaging combination'),
        'CODE 2.pdf': ('Product Code Pool', 'Different Line/Packaging combination'),
        'CODE 3.pdf': ('Product Code Pool', 'Different Line/Packaging combination'),
        'CODE 4.pdf': ('Product Code Pool', 'Different Line/Packaging combination'),
        'CODE 5.pdf': ('Product Code Pool', 'Different Line/Packaging combination'),
        'CODE 6.pdf': ('Product Code Pool', 'Different Line/Packaging combination'),
        'CODE 7.pdf': ('Product Code Pool', 'Different Line/Packaging combination'),
        'CODE 8.pdf': ('Product Code Pool', 'Different Line/Packaging combination'),
        'CODE 10.pdf': ('Product Code Pool', 'Different Line/Packaging combination'),
        'CODE 14.pdf': ('Product Code Pool', 'Different Line/Packaging combination'),
        'CODE 16.pdf': ('Product Code Pool', 'Different Line/Packaging combination'),
        'triman 2.pdf': ('Triman Recycling Pool', 'Different product type'),
        'triman 3.pdf': ('Triman Recycling Pool', 'Different product type')
    }

    never_used_pdfs = {
        'ÉLÉMENTS.pdf': ('Additional Elements', 'Not part of any selection pool')
    }

    unused_num = 1
    for pdf_file, (category, reason) in not_selected_pdfs.items():
        if pdf_file not in used_files:
            html += f"""
                    <tr>
                        <td>{unused_num}</td>
                        <td>{pdf_file}</td>
                        <td>{category}</td>
                        <td style="color: #666666; font-size: 12px;">{reason}</td>
                    </tr>
"""
            unused_num += 1

    html += """
                </tbody>
            </table>
            <div style="margin-top: 15px; padding: 10px; background: #ffffff; border-left: 4px solid #d4a017;">
                <strong>Total PDFs in selection pools:</strong> """ + str(len(not_selected_pdfs)) + """<br>
                <strong>Not selected for this product:</strong> """ + str(len(not_selected_pdfs)) + """
            </div>
        </div>

        <div class="rules-section" style="background: #fff0f0;">
            <div class="rules-title">PDFs NEVER USED (Not in Any Selection Pool)</div>
            <div style="font-size: 13px; margin-bottom: 15px; color: #666666;">
                These PDF files exist in the test folder but are not part of any selection logic or rules:
            </div>
            <table class="data-table">
                <thead>
                    <tr>
                        <th>#</th>
                        <th>PDF File</th>
                        <th>Category</th>
                        <th>Status</th>
                    </tr>
                </thead>
                <tbody>
"""

    never_num = 1
    for pdf_file, (category, reason) in never_used_pdfs.items():
        html += f"""
                    <tr>
                        <td>{never_num}</td>
                        <td><strong>{pdf_file}</strong></td>
                        <td>{category}</td>
                        <td style="color: #8b0000; font-size: 12px;">{reason}</td>
                    </tr>
"""
        never_num += 1

    html += """
                </tbody>
            </table>
            <div style="margin-top: 15px; padding: 10px; background: #ffffff; border-left: 4px solid #8b0000;">
                <strong>Total never used:</strong> """ + str(len(never_used_pdfs)) + """<br>
                <em style="font-size: 12px; color: #666666;">These files are not referenced in JSON LabelData or TRANSLATIONS&RULES.xlsx</em>
            </div>
        </div>
    </div>
</body>
</html>
"""

    # Write to file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"HTML report generated: {output_file}")
    print(f"Total PDF files used: {len(used_files)}")
    print(f"Total PDF files not selected: {len(not_selected_pdfs)}")
    print(f"Total PDF files never used: {len(never_used_pdfs)}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: py generate_comprehensive_html.py <json_file> <output_html>")
        sys.exit(1)

    generate_comprehensive_html(sys.argv[1], sys.argv[2])
