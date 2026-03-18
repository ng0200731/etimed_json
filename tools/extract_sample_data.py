"""
Extract one complete sample of each element type
"""

import json
import sys


def main(json_file):
    print(f"Extracting sample data from: {json_file}\n")
    print("=" * 80)

    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Navigate to main group
    main_layer = data['layers'][0]
    main_group = main_layer['children'][0]

    # Find one sample of each type
    samples = {}

    for i, child in enumerate(main_group['children']):
        child_type = child.get('type', 'unknown')

        if child_type not in samples:
            samples[child_type] = {
                'index': i + 1,
                'data': child
            }

    # Output samples
    print(f"\nFOUND {len(samples)} TYPES\n")
    print("=" * 80 + "\n")

    for obj_type, info in sorted(samples.items()):
        print(f"TYPE: {obj_type}")
        print(f"Sample from Sub-Group #{info['index']}")
        print(f"\nComplete JSON data:\n")
        print(json.dumps(info['data'], indent=2, ensure_ascii=False))
        print("\n" + "=" * 80 + "\n")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: py extract_sample_data.py <json_file>")
        sys.exit(1)

    main(sys.argv[1])
