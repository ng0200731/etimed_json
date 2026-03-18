"""
Detailed analysis of sub-groups
Shows the structure and content of each sub-group
"""

import json
import sys


def count_elements(obj, depth=0, max_depth=20):
    """Count elements in a structure."""
    counts = {
        'groups': 0,
        'paths': 0,
        'text': 0,
        'images': 0,
        'compoundPaths': 0,
        'total': 0
    }

    if depth > max_depth:
        return counts

    if isinstance(obj, dict):
        obj_type = obj.get('type', '')

        if obj_type == 'group':
            counts['groups'] += 1
            counts['total'] += 1
        elif obj_type == 'path':
            counts['paths'] += 1
            counts['total'] += 1
        elif obj_type == 'text':
            counts['text'] += 1
            counts['total'] += 1
        elif obj_type == 'image':
            counts['images'] += 1
            counts['total'] += 1
        elif obj_type == 'compoundPath':
            counts['compoundPaths'] += 1
            counts['total'] += 1

        # Recurse into children
        if 'children' in obj and isinstance(obj['children'], list):
            for child in obj['children']:
                child_counts = count_elements(child, depth + 1, max_depth)
                for key in counts:
                    counts[key] += child_counts[key]

    elif isinstance(obj, list):
        for item in obj:
            child_counts = count_elements(item, depth, max_depth)
            for key in counts:
                counts[key] += child_counts[key]

    return counts


def get_text_sample(obj, max_samples=3):
    """Extract sample text content from structure."""
    texts = []

    if isinstance(obj, dict):
        if obj.get('type') == 'text' and 'content' in obj:
            texts.append(obj['content'][:50])  # First 50 chars

        if 'children' in obj and isinstance(obj['children'], list):
            for child in obj['children']:
                child_texts = get_text_sample(child, max_samples)
                texts.extend(child_texts)
                if len(texts) >= max_samples:
                    break

    elif isinstance(obj, list):
        for item in obj:
            item_texts = get_text_sample(item, max_samples)
            texts.extend(item_texts)
            if len(texts) >= max_samples:
                break

    return texts[:max_samples]


def analyze_subgroups(main_group):
    """Analyze all sub-groups within the main group."""
    if 'children' not in main_group:
        return []

    subgroups = []

    for i, child in enumerate(main_group['children']):
        group_info = {
            'index': i + 1,
            'type': child.get('type', 'unknown'),
            'name': child.get('name', 'Unnamed'),
            'visible': child.get('visible', True),
            'opacity': child.get('opacity', 100),
            'clipped': child.get('clipped', False),
            'locked': child.get('locked', False),
        }

        # Count contents
        counts = count_elements(child)
        group_info['counts'] = counts

        # Get text samples if any
        if counts['text'] > 0:
            group_info['text_samples'] = get_text_sample(child, 3)

        # Get direct children count
        if 'children' in child:
            group_info['direct_children'] = len(child['children'])
        else:
            group_info['direct_children'] = 0

        subgroups.append(group_info)

    return subgroups


def main(json_file):
    print(f"Analyzing sub-groups in: {json_file}\n")
    print("=" * 80)

    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Navigate to main group
    if 'layers' not in data or len(data['layers']) == 0:
        print("No layers found")
        return

    main_layer = data['layers'][0]
    if 'children' not in main_layer or len(main_layer['children']) == 0:
        print("No children in main layer")
        return

    main_group = main_layer['children'][0]

    # Analyze sub-groups
    subgroups = analyze_subgroups(main_group)

    print(f"FOUND {len(subgroups)} SUB-GROUPS\n")
    print("=" * 80 + "\n")

    for sg in subgroups:
        print(f"Sub-Group #{sg['index']}")
        print(f"  Type: {sg['type']}")
        print(f"  Name: {sg['name']}")
        print(f"  Visible: {sg['visible']} | Opacity: {sg['opacity']}% | Clipped: {sg['clipped']} | Locked: {sg['locked']}")
        print(f"  Direct Children: {sg['direct_children']}")
        print(f"  Total Contents:")
        print(f"    - Groups: {sg['counts']['groups']}")
        print(f"    - Paths: {sg['counts']['paths']}")
        print(f"    - Text: {sg['counts']['text']}")
        print(f"    - Images: {sg['counts']['images']}")
        print(f"    - Compound Paths: {sg['counts']['compoundPaths']}")
        print(f"    - Total Elements: {sg['counts']['total']}")

        if 'text_samples' in sg and sg['text_samples']:
            print(f"  Text Samples:")
            for text in sg['text_samples']:
                try:
                    print(f"    - \"{text}\"")
                except UnicodeEncodeError:
                    print(f"    - [Unicode text: {len(text)} chars]")

        print()

    # Summary by type
    print("=" * 80)
    print("\nSUMMARY BY TYPE:\n")

    type_counts = {}
    for sg in subgroups:
        sg_type = sg['type']
        type_counts[sg_type] = type_counts.get(sg_type, 0) + 1

    for sg_type, count in sorted(type_counts.items()):
        print(f"  {sg_type}: {count}")

    print(f"\nTotal: {len(subgroups)} sub-groups")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: py analyze_subgroups.py <json_file>")
        sys.exit(1)

    main(sys.argv[1])
