"""
Count distinct data sets in JSON structure
Identifies top-level groups and their contents
"""

import json
import sys


def count_groups_recursive(obj, depth=0, max_depth=20):
    """Count groups at each level."""
    counts = {'groups': 0, 'paths': 0, 'text': 0, 'images': 0, 'compoundPaths': 0, 'total_elements': 0}

    if depth > max_depth:
        return counts

    if isinstance(obj, dict):
        obj_type = obj.get('type', '')

        if obj_type == 'group':
            counts['groups'] += 1
        elif obj_type == 'path':
            counts['paths'] += 1
        elif obj_type == 'text':
            counts['text'] += 1
        elif obj_type == 'image':
            counts['images'] += 1
        elif obj_type == 'compoundPath':
            counts['compoundPaths'] += 1

        if obj_type:
            counts['total_elements'] += 1

        # Recurse into children
        if 'children' in obj and isinstance(obj['children'], list):
            for child in obj['children']:
                child_counts = count_groups_recursive(child, depth + 1, max_depth)
                for key in counts:
                    counts[key] += child_counts[key]

    elif isinstance(obj, list):
        for item in obj:
            child_counts = count_groups_recursive(item, depth, max_depth)
            for key in counts:
                counts[key] += child_counts[key]

    return counts


def analyze_top_level_groups(layer):
    """Analyze the immediate children of the main layer."""
    if 'children' not in layer:
        return []

    groups_info = []
    for i, child in enumerate(layer['children']):
        if child.get('type') == 'group':
            group_data = {
                'index': i,
                'name': child.get('name', 'Unnamed'),
                'visible': child.get('visible', True),
                'opacity': child.get('opacity', 100),
                'clipped': child.get('clipped', False),
            }

            # Count contents
            counts = count_groups_recursive(child)
            group_data['contents'] = counts

            groups_info.append(group_data)

    return groups_info


def main(json_file):
    print(f"Analyzing data sets in: {json_file}\n")
    print("=" * 70)

    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Get the main layer
    if 'layers' not in data or len(data['layers']) == 0:
        print("No layers found in JSON")
        return

    main_layer = data['layers'][0]
    print(f"Main Layer: {main_layer.get('name', 'Unnamed')}")
    print(f"Direct children: {len(main_layer.get('children', []))}")
    print("=" * 70 + "\n")

    # Analyze top-level groups (these are likely your "data sets")
    top_groups = analyze_top_level_groups(main_layer)

    if not top_groups:
        print("No top-level groups found")
        return

    print(f"TOP-LEVEL DATA SETS: {len(top_groups)}\n")
    print("=" * 70)

    for group in top_groups:
        print(f"\nData Set #{group['index'] + 1}")
        print(f"  Name: {group['name']}")
        print(f"  Visible: {group['visible']}")
        print(f"  Opacity: {group['opacity']}%")
        print(f"  Clipped: {group['clipped']}")
        print(f"  Contents:")
        print(f"    - Groups: {group['contents']['groups']}")
        print(f"    - Paths: {group['contents']['paths']}")
        print(f"    - Text: {group['contents']['text']}")
        print(f"    - Images: {group['contents']['images']}")
        print(f"    - Compound Paths: {group['contents']['compoundPaths']}")
        print(f"    - Total Elements: {group['contents']['total_elements']}")

    print("\n" + "=" * 70)
    print(f"\nSUMMARY: {len(top_groups)} distinct data set(s) found")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: py count_data_sets.py <json_file>")
        sys.exit(1)

    main(sys.argv[1])
