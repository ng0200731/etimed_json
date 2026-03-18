"""
Show the exact key structure for each sub-group type
"""

import json
import sys


def get_keys_structure(obj, depth=0, max_depth=3):
    """Get the keys structure of an object."""
    if depth > max_depth or not isinstance(obj, dict):
        return None

    structure = {}
    for key, value in obj.items():
        if isinstance(value, dict):
            structure[key] = get_keys_structure(value, depth + 1, max_depth)
        elif isinstance(value, list):
            if len(value) > 0 and isinstance(value[0], dict):
                structure[key] = f"[list of {len(value)} items, first item keys: {list(value[0].keys())}]"
            else:
                structure[key] = f"[list of {len(value)} items]"
        else:
            structure[key] = type(value).__name__

    return structure


def main(json_file):
    print(f"Analyzing key structures in: {json_file}\n")
    print("=" * 80)

    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Navigate to main group
    main_layer = data['layers'][0]
    main_group = main_layer['children'][0]

    # Group by type and collect key structures
    type_samples = {}

    for i, child in enumerate(main_group['children']):
        child_type = child.get('type', 'unknown')

        if child_type not in type_samples:
            type_samples[child_type] = {
                'count': 0,
                'sample_index': i + 1,
                'keys': list(child.keys()),
                'structure': child
            }

        type_samples[child_type]['count'] += 1

    # Display results
    print(f"FOUND {len(type_samples)} DIFFERENT TYPES\n")
    print("=" * 80 + "\n")

    for obj_type, info in sorted(type_samples.items()):
        print(f"TYPE: {obj_type}")
        print(f"  Count: {info['count']} sub-groups")
        print(f"  Sample: Sub-Group #{info['sample_index']}")
        print(f"  Keys present: {info['keys']}")
        print(f"\n  Detailed structure:")

        sample = info['structure']
        for key in info['keys']:
            value = sample[key]
            if isinstance(value, dict):
                print(f"    {key}: dict with keys {list(value.keys())}")
            elif isinstance(value, list):
                if len(value) > 0:
                    print(f"    {key}: list[{len(value)}] (first item type: {type(value[0]).__name__})")
                else:
                    print(f"    {key}: list[0] (empty)")
            elif isinstance(value, str):
                display_val = value[:30] + "..." if len(value) > 30 else value
                print(f"    {key}: str = \"{display_val}\"")
            else:
                print(f"    {key}: {type(value).__name__} = {value}")

        print("\n" + "-" * 80 + "\n")

    # Show the distinguishing key
    print("=" * 80)
    print("\nKEY IDENTIFIER:\n")
    print("  The 'type' field is the key that distinguishes different groups:")
    for obj_type, info in sorted(type_samples.items()):
        print(f"    type = \"{obj_type}\" → {info['count']} occurrences")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: py show_key_structure.py <json_file>")
        sys.exit(1)

    main(sys.argv[1])
