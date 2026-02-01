"""
Advanced QR Code Generator Examples
Demonstrates various use cases for the ColoredQRCodeGenerator
"""

import os
from qr_generator import ColoredQRCodeGenerator


def example_1_simple_colored():
    """Generate simple colored QR codes"""
    print("\n" + "=" * 60)
    print("Example 1: Simple Colored QR Codes")
    print("=" * 60)
    
    # Create output directory
    os.makedirs('output', exist_ok=True)
    
    colors = [
        {'name': 'Blue', 'fill': '#1f77b4', 'back': 'white'},
        {'name': 'Red', 'fill': '#d62728', 'back': '#ffffcc'},
        {'name': 'Green', 'fill': '#2ca02c', 'back': 'white'},
        {'name': 'Purple', 'fill': '#9467bd', 'back': '#f0f0f0'},
    ]
    
    for color_set in colors:
        generator = ColoredQRCodeGenerator(
            fill_color=color_set['fill'],
            back_color=color_set['back'],
            box_size=10
        )
        
        qr_img = generator.generate_qr(f"https://example.com/{color_set['name'].lower()}")
        output_file = f"output/qrcode_{color_set['name'].lower()}.png"
        generator.save_qr(qr_img, output_file)
        print(f"✓ Generated {color_set['name']} QR code: {output_file}")


def example_2_different_data():
    """Generate QR codes for different types of data"""
    print("\n" + "=" * 60)
    print("Example 2: QR Codes for Different Data Types")
    print("=" * 60)
    
    os.makedirs('output', exist_ok=True)
    
    data_types = [
        {'name': 'URL', 'data': 'https://www.github.com', 'color': '#1f77b4'},
        {'name': 'Email', 'data': 'contact@example.com', 'color': '#d62728'},
        {'name': 'Phone', 'data': 'tel:+1234567890', 'color': '#2ca02c'},
        {'name': 'WiFi', 'data': 'WIFI:T:WPA;S:NetworkName;P:Password;;', 'color': '#ff7f0e'},
        {'name': 'Text', 'data': 'Hello, this is a QR code!', 'color': '#9467bd'},
    ]
    
    for data_type in data_types:
        generator = ColoredQRCodeGenerator(
            fill_color=data_type['color'],
            back_color='white',
            box_size=8
        )
        
        qr_img = generator.generate_qr(data_type['data'])
        output_file = f"output/qr_{data_type['name'].lower()}.png"
        generator.save_qr(qr_img, output_file)
        print(f"✓ Generated {data_type['name']} QR code: {output_file}")


def example_3_custom_sizing():
    """Generate QR codes with different box sizes"""
    print("\n" + "=" * 60)
    print("Example 3: QR Codes with Different Box Sizes")
    print("=" * 60)
    
    os.makedirs('output', exist_ok=True)
    
    box_sizes = [5, 10, 15, 20]
    
    for box_size in box_sizes:
        generator = ColoredQRCodeGenerator(
            fill_color='#1f77b4',
            back_color='white',
            box_size=box_size
        )
        
        qr_img = generator.generate_qr("https://example.com")
        output_file = f"output/qr_boxsize_{box_size}.png"
        generator.save_qr(qr_img, output_file)
        print(f"✓ Generated QR code with box size {box_size}: {output_file}")


def example_4_with_logo():
    """Generate QR code with embedded logo"""
    print("\n" + "=" * 60)
    print("Example 4: QR Code with Embedded Logo")
    print("=" * 60)
    
    os.makedirs('output', exist_ok=True)
    
    # Check if sample logo exists
    logo_path = 'sample_logo.png'
    
    if os.path.exists(logo_path):
        generator = ColoredQRCodeGenerator(
            fill_color='#2ca02c',
            back_color='white',
            box_size=10
        )
        
        try:
            qr_with_logo = generator.generate_and_save(
                data="https://github.com",
                output_path='output/qr_with_logo.png',
                logo_path=logo_path,
                logo_size_ratio=0.25
            )
            print("✓ QR code with embedded logo generated successfully!")
        except Exception as e:
            print(f"✗ Error embedding logo: {e}")
    else:
        print(f"ℹ Logo file '{logo_path}' not found.")
        print("  To use this feature:")
        print(f"  1. Place your PNG logo at: {os.path.abspath(logo_path)}")
        print("  2. Run this example again")
        print("\n  Tip: You can create a sample logo using:")
        print("  - Python: PIL.Image.new('RGBA', (200, 200), color=(0,0,0,0)).save('sample_logo.png')")
        print("  - Or download any PNG image and save it as 'sample_logo.png'")


def example_5_batch_generation():
    """Generate multiple QR codes in batch"""
    print("\n" + "=" * 60)
    print("Example 5: Batch QR Code Generation")
    print("=" * 60)
    
    os.makedirs('output', exist_ok=True)
    
    # List of product URLs to generate QR codes for
    products = [
        {'name': 'Product A', 'url': 'https://example.com/product/a', 'color': '#1f77b4'},
        {'name': 'Product B', 'url': 'https://example.com/product/b', 'color': '#d62728'},
        {'name': 'Product C', 'url': 'https://example.com/product/c', 'color': '#2ca02c'},
        {'name': 'Product D', 'url': 'https://example.com/product/d', 'color': '#ff7f0e'},
    ]
    
    for product in products:
        generator = ColoredQRCodeGenerator(
            fill_color=product['color'],
            back_color='white',
            box_size=10
        )
        
        qr_img = generator.generate_qr(product['url'])
        output_file = f"output/qr_product_{product['name'].split()[1].lower()}.png"
        generator.save_qr(qr_img, output_file)
        print(f"✓ Generated QR for {product['name']}: {output_file}")


def main():
    """Run all examples"""
    print("\n" + "=" * 60)
    print("QR Code Generator - Advanced Examples")
    print("=" * 60)
    
    example_1_simple_colored()
    example_2_different_data()
    example_3_custom_sizing()
    example_4_with_logo()
    example_5_batch_generation()
    
    print("\n" + "=" * 60)
    print("All examples completed! Check the 'output' folder for results.")
    print("=" * 60 + "\n")


if __name__ == '__main__':
    main()
