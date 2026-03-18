"""
JSON Structure Analyzer
Analyzes large JSON files and outputs structure, statistics, and element breakdowns.
"""

import json
import sys
from collections import Counter
from pathlib import Path


def analyze_structure(data, path="root", max_depth=10, current_depth=0):
    """Recursively analyze JSON structure."""
    results = {
        'path': path,
        'type': type(data).__name__,
        'children': []
    }

    if current_depth >= max_depth:
        results['note'] = 'Max depth reached'
        return results

    if isinstance(data, dict):
        results['keys'] = list(data.keys())
        results['key_count'] = len(data.keys())
        for key, value in data.items():
            child_result = analyze_structure(value, f"{path}.{key}", max_depth, current_depth + 1)
            results['children'].append(child_result)

    elif isinstance(data, list):
        results['length'] = len(data)
        if len(data) > 0:
            # Analyze first item as sample
            results['children'].append(analyze_structure(data[0], f"{path}[0]", max_depth, current_depth + 1))
            if len(data) > 1:
                results['note'] = f'Array with {len(data)} items (showing first item only)'

    elif isinstance(data, (str, int, float, bool, type(None))):
        results['value'] = str(data)[:100]  # Truncate long strings

    return results


def count_element_types(obj, counter=None):
    """Recursively count element types in nested structure."""
    if counter is None:
        counter = Counter()

    if isinstance(obj, dict):
        if 'type' in obj:
            counter[obj['type']] += 1
        for value in obj.values():
            count_element_types(value, counter)
    elif isinstance(obj, list):
        for item in obj:
            count_element_types(item, counter)

    return counter


def print_structure(results, indent=0):
    """Pretty print structure analysis."""
    prefix = "  " * indent
    print(f"{prefix}{results['path']} ({results['type']})")

    if 'keys' in results:
        print(f"{prefix}  Keys: {', '.join(results['keys'])}")
    if 'length' in results:
        print(f"{prefix}  Length: {results['length']}")
    if 'value' in results:
        print(f"{prefix}  Value: {results['value']}")
    if 'note' in results:
        print(f"{prefix}  Note: {results['note']}")

    for child in results.get('children', []):
        print_structure(child, indent + 1)


def main(json_file):
    """Main analysis function."""
    print(f"Analyzing: {json_file}\n")
    print("=" * 60)

    # Load JSON
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # File size
    file_size = Path(json_file).stat().st_size
    print(f"File size: {file_size:,} bytes ({file_size / 1024:.1f} KB)")

    # Structure analysis
    print("\n" + "=" * 60)
    print("STRUCTURE ANALYSIS")
    print("=" * 60 + "\n")

    structure = analyze_structure(data, max_depth=4)
    print_structure(structure)

    # Element type counting
    print("\n" + "=" * 60)
    print("ELEMENT TYPE BREAKDOWN")
    print("=" * 60 + "\n")

    type_counts = count_element_types(data)
    if type_counts:
        for elem_type, count in sorted(type_counts.items(), key=lambda x: x[1], reverse=True):
            print(f"  {elem_type}: {count}")
    else:
        print("  No 'type' fields found in structure")

    # Top-level summary
    print("\n" + "=" * 60)
    print("TOP-LEVEL SUMMARY")
    print("=" * 60 + "\n")

    if isinstance(data, dict):
        for key, value in data.items():
            value_type = type(value).__name__
            if isinstance(value, (list, dict)):
                size = len(value)
                print(f"  {key}: {value_type} (size: {size})")
            else:
                print(f"  {key}: {value_type} = {str(value)[:50]}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: py analyze_json_structure.py <json_file>")
        sys.exit(1)

    main(sys.argv[1])
