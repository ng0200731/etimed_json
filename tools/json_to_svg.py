"""
Convert JSON vector graphics to SVG format
Renders paths, text, and images from the JSON structure
"""

import json
import sys
import html


def rgb_to_hex(r, g, b):
    """Convert RGB to hex color."""
    return f"#{int(r):02x}{int(g):02x}{int(b):02x}"


def get_fill_color(fill):
    """Extract fill color from fill object."""
    if not fill or fill.get('type') == 'none':
        return 'none'

    if fill.get('type') == 'rgb':
        return rgb_to_hex(fill['r'], fill['g'], fill['b'])

    if fill.get('type') == 'spot' and 'fallback' in fill:
        fallback = fill['fallback']
        if fallback.get('type') == 'rgb':
            return rgb_to_hex(fallback['r'], fallback['g'], fallback['b'])

    return 'none'


def get_stroke_color(stroke):
    """Extract stroke color from stroke object."""
    if not stroke or stroke.get('type') == 'none':
        return 'none'

    if stroke.get('type') == 'rgb':
        return rgb_to_hex(stroke['r'], stroke['g'], stroke['b'])

    return 'none'


def path_data_to_svg(path_data):
    """Convert pathData array to SVG path d attribute."""
    if not path_data or len(path_data) == 0:
        return ""

    d_parts = []

    # Move to first point
    first = path_data[0]
    d_parts.append(f"M {first['x']:.2f} {first['y']:.2f}")

    # Draw subsequent points
    for i in range(1, len(path_data)):
        point = path_data[i]
        prev_point = path_data[i - 1]

        # Check if we need bezier curve
        has_curve = (
            prev_point.get('handleOut', {}) != prev_point or
            point.get('handleIn', {}) != point
        )

        if has_curve:
            # Cubic bezier curve
            handle_out = prev_point.get('handleOut', prev_point)
            handle_in = point.get('handleIn', point)
            d_parts.append(
                f"C {handle_out['x']:.2f} {handle_out['y']:.2f}, "
                f"{handle_in['x']:.2f} {handle_in['y']:.2f}, "
                f"{point['x']:.2f} {point['y']:.2f}"
            )
        else:
            # Straight line
            d_parts.append(f"L {point['x']:.2f} {point['y']:.2f}")

    return " ".join(d_parts)


def render_path(path_obj, svg_elements):
    """Render a path element to SVG."""
    if 'pathData' not in path_obj:
        return

    d = path_data_to_svg(path_obj['pathData'])
    if not d:
        return

    fill = get_fill_color(path_obj.get('fill', {}))
    stroke = get_stroke_color(path_obj.get('stroke', {}))
    stroke_width = path_obj.get('strokeWidth', 1)
    opacity = path_obj.get('opacity', 100) / 100.0
    closed = path_obj.get('closed', False)

    if closed:
        d += " Z"

    # Build SVG path element
    path_attrs = [
        f'd="{d}"',
        f'fill="{fill}"',
        f'stroke="{stroke}"',
        f'stroke-width="{stroke_width}"',
        f'opacity="{opacity}"'
    ]

    if stroke != 'none':
        stroke_cap = path_obj.get('strokeCap', 'round')
        stroke_join = path_obj.get('strokeJoin', 'round')
        path_attrs.append(f'stroke-linecap="{stroke_cap}"')
        path_attrs.append(f'stroke-linejoin="{stroke_join}"')

        if 'strokeDashes' in path_obj and path_obj['strokeDashes']:
            dashes = ','.join(str(d) for d in path_obj['strokeDashes'])
            path_attrs.append(f'stroke-dasharray="{dashes}"')

    svg_elements.append(f'  <path {" ".join(path_attrs)} />')


def render_text(text_obj, svg_elements):
    """Render a text element to SVG."""
    if 'content' not in text_obj or 'bounds' not in text_obj:
        return

    content = html.escape(text_obj['content'])
    bounds = text_obj['bounds']
    x = bounds['x']
    y = bounds['y'] + bounds.get('height', 10)  # Baseline adjustment
    opacity = text_obj.get('opacity', 100) / 100.0

    # Get text styling from paragraphs
    font_family = "Arial"
    font_size = 12
    fill = "#000000"

    if 'paragraphs' in text_obj and len(text_obj['paragraphs']) > 0:
        para = text_obj['paragraphs'][0]
        if 'runs' in para and len(para['runs']) > 0:
            run = para['runs'][0]
            font_family = run.get('fontFamily', font_family)
            font_size = run.get('fontSize', font_size)

            if 'color' in run and run['color'].get('type') == 'rgb':
                color = run['color']
                fill = rgb_to_hex(color['r'], color['g'], color['b'])

    text_attrs = [
        f'x="{x:.2f}"',
        f'y="{y:.2f}"',
        f'font-family="{font_family}"',
        f'font-size="{font_size}"',
        f'fill="{fill}"',
        f'opacity="{opacity}"'
    ]

    svg_elements.append(f'  <text {" ".join(text_attrs)}>{content}</text>')


def render_element(element, svg_elements):
    """Render any element type."""
    elem_type = element.get('type')

    if elem_type == 'path':
        render_path(element, svg_elements)
    elif elem_type == 'text':
        render_text(element, svg_elements)
    elif elem_type == 'group':
        # Render group children
        if 'children' in element:
            for child in element['children']:
                render_element(child, svg_elements)
    elif elem_type == 'compoundPath':
        # Render compound path children
        if 'children' in element:
            for child in element['children']:
                render_element(child, svg_elements)


def json_to_svg(json_file, output_file):
    """Convert JSON to SVG file."""
    print(f"Converting {json_file} to SVG...")

    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Get canvas dimensions
    metadata = data.get('metadata', {})
    width = metadata.get('width', 1190.55)
    height = metadata.get('height', 841.89)

    # Start SVG
    svg_lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        f'<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" '
        'xmlns="http://www.w3.org/2000/svg">',
        f'  <title>{metadata.get("name", "Design")}</title>',
        '  <rect width="100%" height="100%" fill="white"/>'  # White background
    ]

    # Render all layers
    svg_elements = []
    if 'layers' in data:
        for layer in data['layers']:
            if layer.get('visible', True) and 'children' in layer:
                for child in layer['children']:
                    render_element(child, svg_elements)

    svg_lines.extend(svg_elements)
    svg_lines.append('</svg>')

    # Write to file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(svg_lines))

    print(f"SVG created: {output_file}")
    print(f"  Dimensions: {width} x {height}")
    print(f"  Elements rendered: {len(svg_elements)}")


def main():
    if len(sys.argv) != 3:
        print("Usage: py json_to_svg.py <input.json> <output.svg>")
        sys.exit(1)

    json_file = sys.argv[1]
    output_file = sys.argv[2]

    json_to_svg(json_file, output_file)


if __name__ == "__main__":
    main()
