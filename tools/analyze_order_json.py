"""
Analyze product order JSON structure
"""

import json
import sys


def main(json_file):
    print(f"Analyzing: {json_file}\n")
    print("=" * 80)

    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # This is a list with one order
    if isinstance(data, list) and len(data) > 0:
        order = data[0]

        print("\nORDER INFORMATION\n")
        print("=" * 80)
        print(f"Order ID: {order.get('Id')}")
        print(f"Season: {order.get('Temporada')}")
        print(f"Order Quantity: {order.get('OrderQty')}")
        print(f"Type: {order.get('TypePOdesc')} ({order.get('TypePO')})")
        print(f"Status: {order.get('Status')}")
        print(f"Production Date: {order.get('ProductionDate')}")
        print(f"Version: {order.get('Version')}")

        print("\n" + "=" * 80)
        print("\nSUPPLIER INFORMATION\n")
        print("=" * 80)
        supplier = order.get('Supplier', {})
        print(f"Code: {supplier.get('SupplierCode')}")
        print(f"Name: {supplier.get('SupplierName')}")
        print(f"Address: {supplier.get('Address')}")
        print(f"Phone: {supplier.get('PhoneNumber')}")
        print(f"Email: {supplier.get('MailAddress')}")

        print("\n" + "=" * 80)
        print("\nPRODUCT INFORMATION\n")
        print("=" * 80)

        style_colors = order.get('StyleColor', [])
        print(f"Number of Style/Colors: {len(style_colors)}")

        for i, sc in enumerate(style_colors):
            print(f"\nStyle/Color #{i+1}:")
            print(f"  Reference ID: {sc.get('ReferenceID')}")
            print(f"  Style ID: {sc.get('StyleID')}")
            print(f"  Color: {sc.get('Color')} (Code: {sc.get('MangoColorCode')})")
            print(f"  Product Type: {sc.get('ProductType')}")
            print(f"  Generic: {sc.get('Generic')}")
            print(f"  Line: {sc.get('Line')}")
            print(f"  Gender: {sc.get('Gender')}")
            print(f"  Age: {sc.get('Age')}")

            # Composition
            if 'Composition' in sc:
                print(f"\n  Composition ({len(sc['Composition'])} materials):")
                for comp in sc['Composition']:
                    material = comp.get('Material', 'Unknown')
                    percentage = comp.get('Percentage', 'N/A')
                    print(f"    - {material}: {percentage}%")

            # Size Range
            if 'SizeRange' in sc:
                sizes = [str(s.get('Size', '')) for s in sc['SizeRange'] if s.get('Size')]
                if sizes:
                    print(f"\n  Size Range: {', '.join(sizes)}")

            # PVP (Prices)
            if 'PVP' in sc:
                print(f"\n  Prices ({len(sc['PVP'])} markets):")
                for pvp in sc['PVP'][:5]:  # Show first 5
                    print(f"    - {pvp.get('Country')}: {pvp.get('Price')} {pvp.get('Currency')}")

            # Care Instructions
            if 'CareInstructions' in sc:
                print(f"\n  Care Instructions: {len(sc['CareInstructions'])} items")

            # Label Data
            if 'LabelData' in sc:
                print(f"  Label Data: {len(sc['LabelData'])} labels")

        print("\n" + "=" * 80)
        print("\nJSON TYPE: Product Order Data (NOT vector graphics)")
        print("=" * 80)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: py analyze_order_json.py <json_file>")
        sys.exit(1)

    main(sys.argv[1])
