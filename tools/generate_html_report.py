"""
Generate HTML report for label groups
"""

import json
import sys
import os


def generate_html_report(json_file, output_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Extract order data
    if isinstance(data, list) and len(data) > 0:
        order = data[0]
    else:
        order = data

    # Get StyleColor array
    style_colors = order.get('StyleColor', [])
    if not style_colors:
        print("No StyleColor data found")
        return

    style_color = style_colors[0]
    label_data = style_color.get('LabelData', [])

    if not label_data:
        print("No LabelData found")
        return

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
            border-bottom: 1px solid #000000;
        }}

        .json-block {{
            background: #f5f5f5;
            border: 1px solid #000000;
            padding: 15px;
            font-family: 'Courier New', monospace;
            font-size: 12px;
            overflow-x: auto;
            white-space: pre-wrap;
            word-wrap: break-word;
        }}

        .data-grid {{
            display: grid;
            gap: 20px;
        }}

        .data-card {{
            border: 1px solid #000000;
            padding: 15px;
        }}

        .data-card-title {{
            font-weight: 700;
            margin-bottom: 10px;
            font-size: 14px;
        }}

        .data-table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 13px;
        }}

        .data-table th {{
            background: #000000;
            color: #ffffff;
            padding: 8px;
            text-align: left;
            font-weight: 600;
        }}

        .data-table td {{
            padding: 8px;
            border: 1px solid #cccccc;
        }}

        .data-table tr:nth-child(even) {{
            background: #f9f9f9;
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
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>Label Generation Report</h1>
            <div class="subtitle">Order ID: {order.get('Id')} | Season: {order.get('Temporada')} | Style: {style_color.get('StyleID')} | Product: {style_color.get('ProductType')} {style_color.get('Color')}</div>
        </header>
"""

    # Generate each label group
    for idx, label in enumerate(label_data, 1):
        label_id = label.get('LabelID', 'UNKNOWN')
        vendor = label.get('Vendor', 'N/A')
        variable = label.get('Variable', 'N/A')
        pdf_file = pdf_mappings.get(label_id, f'{label_id}-*.pdf')
        purpose = purposes.get(label_id, 'Unknown')

        html += f"""
        <div class="label-group">
            <div class="label-header">
                <div class="label-title">[{idx}] JSON: LabelID = '{label_id}'</div>
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
                <div class="purpose-badge">Purpose: {purpose}</div>
                <div class="pdf-link">→ PDF File: {pdf_file}</div>
            </div>

            <div class="label-body">
                <div class="section">
                    <div class="section-title">PDF FILE LINK</div>
                    <div class="data-card">
                        <div style="font-size: 18px; font-weight: 700; margin-bottom: 10px;">
                            This label uses: <span style="background: #000000; color: #ffffff; padding: 4px 12px;">{pdf_file}</span>
                        </div>
                        <div style="font-size: 13px; color: #666666;">
                            The JSON data below (LabelID='{label_id}', Vendor={vendor}, Variable={variable}) links to the PDF file: {pdf_file}
                        </div>
                    </div>
                </div>

                <div class="section">
                    <div class="section-title">FULL ORIGINAL JSON DATA</div>
                    <div class="json-block">{json.dumps(label, indent=2, ensure_ascii=False)}</div>
                </div>
"""

        # Composition data
        if label_id in ['GI000PRO', 'GI001BAW']:
            composition = style_color.get('Composition', [])
            html += f"""
                <div class="section">
                    <div class="section-title">COMPOSITION DATA ({len(composition)} material groups)</div>
                    <div class="data-grid">
"""
            for comp_idx, comp in enumerate(composition, 1):
                html += f"""
                        <div class="data-card">
                            <div class="data-card-title">Group {comp_idx}: {comp.get('TitleName', 'N/A')}</div>
                            <div class="json-block">{json.dumps(comp, indent=2, ensure_ascii=False)}</div>
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
                    <div class="section-title">CARE INSTRUCTIONS ({len(care)} instructions)</div>
                    <table class="data-table">
                        <thead>
                            <tr>
                                <th>#</th>
                                <th>Care Name</th>
                                <th>Code</th>
                                <th>SAP Code</th>
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
                                <td>{instruction.get('CareSAPCode', 'N/A')}</td>
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
                    <div class="section-title">SIZE/ITEM DATA ({len(item_data)} size variants)</div>
                    <table class="data-table">
                        <thead>
                            <tr>
                                <th>#</th>
                                <th>Size</th>
                                <th>EAN13</th>
                                <th>Material</th>
                                <th>Qty</th>
                                <th>ES</th>
                                <th>IT</th>
                                <th>UK</th>
                                <th>US</th>
                            </tr>
                        </thead>
                        <tbody>
"""
        for item_idx, item in enumerate(item_data, 1):
            html += f"""
                            <tr>
                                <td>{item_idx}</td>
                                <td>{item.get('SizeName', 'N/A')}</td>
                                <td>{item.get('EAN13', 'N/A')}</td>
                                <td>{item.get('Material', 'N/A')}</td>
                                <td>{item.get('itemQty', 'N/A')}</td>
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
                    <div class="section-title">PRICE DATA ({len(pvp_data)} markets)</div>
                    <div class="data-grid">
"""
            for pvp_idx, pvp in enumerate(pvp_data, 1):
                html += f"""
                        <div class="data-card">
                            <div class="data-card-title">Market {pvp_idx}</div>
                            <div class="json-block">{json.dumps(pvp, indent=2, ensure_ascii=False)}</div>
                        </div>
"""
            html += """
                    </div>
                </div>
"""

        # Origin/Destination
        origin = style_color.get('Origin', {})
        destination = style_color.get('Destination', {})
        html += f"""
                <div class="section">
                    <div class="section-title">ORIGIN/DESTINATION DATA</div>
                    <div class="data-grid" style="grid-template-columns: 1fr 1fr;">
                        <div class="data-card">
                            <div class="data-card-title">Origin</div>
                            <div class="json-block">{json.dumps(origin, indent=2, ensure_ascii=False)}</div>
                        </div>
                        <div class="data-card">
                            <div class="data-card-title">Destination</div>
                            <div class="json-block">{json.dumps(destination, indent=2, ensure_ascii=False)}</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
"""

    # Close HTML
    html += """
    </div>
</body>
</html>
"""

    # Write to file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"HTML report generated: {output_file}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: py generate_html_report.py <json_file> <output_html>")
        sys.exit(1)

    generate_html_report(sys.argv[1], sys.argv[2])
