"""
Create placeholder images for PDF previews
"""

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    print("PIL not installed. Install with: pip install pillow")
    import sys
    sys.exit(1)


def create_placeholder(text, filename, width=400, height=300):
    """Create a placeholder image with text"""
    # Create image
    img = Image.new('RGB', (width, height), color='#f5f5f5')
    draw = ImageDraw.Draw(img)

    # Draw border
    draw.rectangle([0, 0, width-1, height-1], outline='#000000', width=2)

    # Add text
    try:
        font = ImageFont.truetype("arial.ttf", 20)
        font_small = ImageFont.truetype("arial.ttf", 14)
    except:
        font = ImageFont.load_default()
        font_small = ImageFont.load_default()

    # Center text
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]

    x = (width - text_width) // 2
    y = (height - text_height) // 2 - 20

    draw.text((x, y), text, fill='#000000', font=font)

    # Add instruction
    instruction = "Place actual PDF preview here"
    inst_bbox = draw.textbbox((0, 0), instruction, font=font_small)
    inst_width = inst_bbox[2] - inst_bbox[0]
    inst_x = (width - inst_width) // 2
    inst_y = y + 40

    draw.text((inst_x, inst_y), instruction, fill='#666666', font=font_small)

    # Save
    img.save(filename)
    print(f"Created: {filename}")


if __name__ == "__main__":
    import os

    output_dir = "D:/temp/IT-customer/etimed/further_sharing/test/test/"

    # Create 4 placeholder images
    create_placeholder("ADHEDIST-mango.pdf", os.path.join(output_dir, "image1.png"))
    create_placeholder("GI000DPO-SAP_1.pdf", os.path.join(output_dir, "image2.png"))
    create_placeholder("GI001BAW-GI001BAC.pdf", os.path.join(output_dir, "image3.png"))
    create_placeholder("PVPV0102-PVP002XG.pdf", os.path.join(output_dir, "image4.png"))

    print("\nPlaceholder images created successfully!")
