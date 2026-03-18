import json
import sys

with open('PVPV0102-PVP02MXG.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print("=== JSON Analysis ===\n")
print(f"Top-level keys: {list(data.keys())}\n")

if 'version' in data:
    print(f"Version: {data['version']}")

if 'metadata' in data:
    print(f"\nMetadata:")
    for key, value in data['metadata'].items():
        if key != 'artboards' and key != 'panels':
            print(f"  {key}: {value}")
    if 'artboards' in data['metadata']:
        print(f"  Number of artboards: {len(data['metadata']['artboards'])}")

if 'layers' in data:
    print(f"\nLayers: {len(data['layers'])} layer(s)")
    for i, layer in enumerate(data['layers']):
        print(f"\n  Layer {i+1}:")
        print(f"    Name: {layer.get('name', 'N/A')}")
        print(f"    Visible: {layer.get('visible', 'N/A')}")
        print(f"    Locked: {layer.get('locked', 'N/A')}")
        print(f"    Opacity: {layer.get('opacity', 'N/A')}")
        if 'children' in layer:
            print(f"    Children: {len(layer['children'])} element(s)")

            # Count element types
            types = {}
            def count_types(children):
                for child in children:
                    child_type = child.get('type', 'unknown')
                    types[child_type] = types.get(child_type, 0) + 1
                    if 'children' in child:
                        count_types(child['children'])

            count_types(layer['children'])
            print(f"    Element types breakdown:")
            for elem_type, count in sorted(types.items()):
                print(f"      {elem_type}: {count}")
