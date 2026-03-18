"""
Show detailed label groups with full JSON data and file links
"""

import json
import sys


def main(json_file):
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

    # Get LabelData from first StyleColor
    label_data = style_colors[0].get('LabelData', [])

    if not label_data:
        print("No LabelData found")
        return

    print("=" * 100)
    print("LABEL GROUPS - DETAILED VIEW")
    print("=" * 100)
    print()

    # Group labels by LabelID
    for idx, label in enumerate(label_data, 1):
        label_id = label.get('LabelID', 'UNKNOWN')
        vendor = label.get('Vendor', 'N/A')
        variable = label.get('Variable', 'N/A')

        print(f"[{idx}] LABEL GROUP: {label_id}")
        print("-" * 100)
        print()

        # Show full JSON data for this label
        print("FULL JSON DATA:")
        print(json.dumps(label, indent=2, ensure_ascii=False))
        print()

        # Show file link information
        print("FILE LINK:")
        print(f"  → Vendor Code: {vendor}")
        print(f"  → Variable: {variable}")
        print(f"  → Expected PDF Pattern: {label_id}-*.pdf")
        print()

        # Show purpose/description based on LabelID
        purposes = {
            'ADHEDIST': 'Brand Logo / Adhesive Distribution Label',
            'GI000PRO': 'Composition Label Template (sewn-in)',
            'GI001BAW': 'Hang Tag Template',
            'PVP002XG': 'Price Tag with RFID',
            'GI000DPO': 'Composition Label (alternative)',
            'PVPV0102': 'Price Tag (alternative)'
        }

        purpose = purposes.get(label_id, 'Unknown Purpose')
        print(f"PURPOSE: {purpose}")
        print()

        # Show how this label relates to the order
        print("RELATIONSHIP TO ORDER:")
        print(f"  → Order ID: {order.get('Id')}")
        print(f"  → Season: {order.get('Temporada')}")
        print(f"  → Style ID: {style_colors[0].get('StyleID')}")
        print(f"  → Product: {style_colors[0].get('ProductType')}")
        print(f"  → Color: {style_colors[0].get('Color')} ({style_colors[0].get('MangoColorCode')})")
        print()

        print("=" * 100)
        print()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: py show_label_groups.py <json_file>")
        sys.exit(1)

    main(sys.argv[1])
