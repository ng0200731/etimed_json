"""
Show detailed label groups with full JSON data and all related datasets
"""

import json
import sys
import io

# Set UTF-8 encoding for stdout
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


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

    # Get first StyleColor (assuming all share same labels)
    style_color = style_colors[0]
    label_data = style_color.get('LabelData', [])

    if not label_data:
        print("No LabelData found")
        return

    print("=" * 120)
    print("DETAILED LABEL GROUPS WITH ALL RELATED DATA")
    print("=" * 120)
    print()

    # Define PDF mappings
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

    # Process each label group
    for idx, label in enumerate(label_data, 1):
        label_id = label.get('LabelID', 'UNKNOWN')
        vendor = label.get('Vendor', 'N/A')
        variable = label.get('Variable', 'N/A')

        print(f"[{idx}] JSON: LabelID = '{label_id}'")
        print(f"Vendor: {vendor} | Variable: {variable}")
        print(f"→ PDF File: {pdf_mappings.get(label_id, f'{label_id}-*.pdf')}")
        print(f"→ Purpose: {purposes.get(label_id, 'Unknown')}")
        print()
        print("-" * 120)
        print()

        # Show full original JSON for this label
        print("FULL ORIGINAL JSON DATA FOR THIS LABEL:")
        print(json.dumps(label, indent=2, ensure_ascii=False))
        print()

        # Show all related datasets under this group
        print("RELATED DATA SETS UNDER THIS GROUP:")
        print()

        # 1. Composition Data (if this is a composition label)
        if label_id in ['GI000PRO', 'GI001BAW']:
            composition = style_color.get('Composition', [])
            print(f"  [A] COMPOSITION DATA ({len(composition)} material groups):")
            for comp_idx, comp in enumerate(composition, 1):
                print(f"      Group {comp_idx}: {comp.get('TitleName', 'N/A')}")
                print(f"      {json.dumps(comp, indent=8, ensure_ascii=False)}")
            print()

        # 2. Care Instructions (if this is a care label)
        if label_id in ['GI000PRO', 'GI001BAW']:
            care = style_color.get('CareInstructions', [])
            print(f"  [B] CARE INSTRUCTIONS ({len(care)} instructions):")
            for care_idx, instruction in enumerate(care, 1):
                print(f"      Instruction {care_idx}:")
                print(f"      {json.dumps(instruction, indent=8, ensure_ascii=False)}")
            print()

        # 3. Size Data (for all labels)
        item_data = style_color.get('ItemData', [])
        print(f"  [C] SIZE/ITEM DATA ({len(item_data)} size variants):")
        for item_idx, item in enumerate(item_data, 1):
            print(f"      Size Variant {item_idx}: {item.get('SizeName', 'N/A')}")
            print(f"      {json.dumps(item, indent=8, ensure_ascii=False)}")
        print()

        # 4. Price Data (if this is a price tag)
        if label_id in ['PVP002XG', 'PVPV0102']:
            pvp_data = style_color.get('PVP', [])
            print(f"  [D] PRICE DATA ({len(pvp_data)} markets):")
            for pvp_idx, pvp in enumerate(pvp_data, 1):
                print(f"      Market {pvp_idx}:")
                print(f"      {json.dumps(pvp, indent=8, ensure_ascii=False)}")
            print()

        # 5. Origin/Destination Data
        print(f"  [E] ORIGIN/DESTINATION DATA:")
        origin = style_color.get('Origin', {})
        destination = style_color.get('Destination', {})
        print(f"      Origin: {json.dumps(origin, indent=8, ensure_ascii=False)}")
        print(f"      Destination: {json.dumps(destination, indent=8, ensure_ascii=False)}")
        print()

        print("=" * 120)
        print()
        print()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: py show_detailed_label_groups.py <json_file>")
        sys.exit(1)

    main(sys.argv[1])
