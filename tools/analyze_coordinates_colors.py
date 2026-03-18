"""
Analyze coordinates and colors in the JSON
Show which elements have drawable paths and colors
"""

import json
import sys


def analyze_colors(obj, path="", results=None):
    """Recursively find all color definitions."""
    if results is None:
        results = []

    if isinstance(obj, dict):
        # Check for color in fill
        if 'fill' in obj and isinstance(obj['fill'], dict):
            fill_type = obj['fill'].get('type')
            if fill_type == 'rgb':
                color = f"RGB({obj['fill']['r']}, {obj['fill']['g']}, {obj['fill']['b']})"
                results.append({
                    'location': path,
                    'property': 'fill',
                    'type': 'rgb',
                    'color': color,
                    'element_type': obj.get('type', 'unknown')
                })
            elif fill_type == 'spot':
                spot_name = obj['fill'].get('name', 'unnamed')
                fallback = obj['fill'].get('fallback', {})
                if fallback.get('type') == 'rgb':
                    color = f"Spot '{spot_name}' (RGB fallback: {fallback['r']}, {fallback['g']}, {fallback['b']})"
                else:
                    color = f"Spot '{spot_name}'"
                results.append({
                    'location': path,
                    'property': 'fill',
                    'type': 'spot',
                    'color': color,
                    'element_type': obj.get('type', 'unknown')
                })

        # Check for color in stroke
        if 'stroke' in obj and isinstance(obj['stroke'], dict):
            stroke_type = obj['stroke'].get('type')
            if stroke_type == 'rgb':
                color = f"RGB({obj['stroke']['r']}, {obj['stroke']['g']}, {obj['stroke']['b']})"
                results.append({
                    'location': path,
                    'property': 'stroke',
                    'type': 'rgb',
                    'color': color,
                    'element_type': obj.get('type', 'unknown')
                })

        # Check for color in text
        if 'paragraphs' in obj:
            for para in obj['paragraphs']:
                if 'runs' in para:
                    for run in para['runs']:
                        if 'color' in run and run['color'].get('type') == 'rgb':
                            color = f"RGB({run['color']['r']}, {run['color']['g']}, {run['color']['b']})"
                            results.append({
                                'location': path,
                                'property': 'text color',
                                'type': 'rgb',
                                'color': color,
                                'element_type': 'text',
                                'text_content': run.get('text', '')[:30]
                            })

        # Recurse
        for key, value in obj.items():
            analyze_colors(value, f"{path}/{key}", results)

    elif isinstance(obj, list):
        for i, item in enumerate(obj):
            analyze_colors(item, f"{path}[{i}]", results)

    return results


def analyze_paths(obj, results=None):
    """Find all path elements with coordinates."""
    if results is None:
        results = []

    if isinstance(obj, dict):
        if obj.get('type') == 'path' and 'pathData' in obj:
            path_info = {
                'type': 'path',
                'closed': obj.get('closed', False),
                'points': len(obj['pathData']),
                'bounds': obj.get('bounds', {}),
                'has_fill': obj.get('fill', {}).get('type') != 'none',
                'has_stroke': obj.get('stroke', {}).get('type') != 'none',
                'fill_type': obj.get('fill', {}).get('type', 'none'),
                'stroke_type': obj.get('stroke', {}).get('type', 'none')
            }
            results.append(path_info)

        # Recurse
        for value in obj.values():
            if isinstance(value, (dict, list)):
                analyze_paths(value, results)

    elif isinstance(obj, list):
        for item in obj:
            analyze_paths(item, results)

    return results


def main(json_file):
    print(f"Analyzing coordinates and colors in: {json_file}\n")
    print("=" * 80)

    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Analyze paths
    print("\nPATH ANALYSIS (Drawable Shapes)\n")
    print("=" * 80)

    paths = analyze_paths(data)
    print(f"\nTotal paths found: {len(paths)}")

    # Group by fill/stroke status
    filled_paths = [p for p in paths if p['has_fill']]
    stroked_paths = [p for p in paths if p['has_stroke']]
    both = [p for p in paths if p['has_fill'] and p['has_stroke']]
    neither = [p for p in paths if not p['has_fill'] and not p['has_stroke']]

    print(f"  - With fill: {len(filled_paths)}")
    print(f"  - With stroke: {len(stroked_paths)}")
    print(f"  - With both: {len(both)}")
    print(f"  - With neither (invisible): {len(neither)}")

    # Show sample paths
    print(f"\nSample drawable paths (first 5):")
    for i, path in enumerate(paths[:5]):
        print(f"\n  Path #{i+1}:")
        print(f"    Points: {path['points']}")
        print(f"    Closed: {path['closed']}")
        print(f"    Fill: {path['fill_type']}")
        print(f"    Stroke: {path['stroke_type']}")
        print(f"    Bounds: x={path['bounds'].get('x', 0):.2f}, y={path['bounds'].get('y', 0):.2f}, "
              f"w={path['bounds'].get('width', 0):.2f}, h={path['bounds'].get('height', 0):.2f}")

    # Analyze colors
    print("\n" + "=" * 80)
    print("\nCOLOR ANALYSIS\n")
    print("=" * 80)

    colors = analyze_colors(data)
    print(f"\nTotal color instances found: {len(colors)}")

    # Unique colors
    unique_colors = {}
    for c in colors:
        color_key = c['color']
        if color_key not in unique_colors:
            unique_colors[color_key] = {'count': 0, 'usage': []}
        unique_colors[color_key]['count'] += 1
        unique_colors[color_key]['usage'].append(c['property'])

    print(f"Unique colors: {len(unique_colors)}")
    print(f"\nColor palette (sorted by frequency):\n")

    for color, info in sorted(unique_colors.items(), key=lambda x: x[1]['count'], reverse=True):
        print(f"  {color}")
        print(f"    Used {info['count']} times in: {', '.join(set(info['usage']))}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: py analyze_coordinates_colors.py <json_file>")
        sys.exit(1)

    main(sys.argv[1])
