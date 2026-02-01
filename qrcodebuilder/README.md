# QR Code Generator with Color and Logo Support

A Python QR code generator that supports:
- ✅ Custom colors for QR code and background
- ✅ Embedded PNG images/logos at the center
- ✅ Adjustable error correction levels
- ✅ Customizable box sizes and versions

## Installation

1. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Colored QR Code
```python
from qr_generator import ColoredQRCodeGenerator

# Create generator with custom colors
generator = ColoredQRCodeGenerator(
    fill_color='#1f77b4',  # Blue
    back_color='white',
    box_size=10
)

# Generate QR code
qr_img = generator.generate_qr("https://www.example.com")
generator.save_qr(qr_img, 'my_qrcode.png')
```

### QR Code with Embedded Logo
```python
# Generate QR code with embedded PNG logo
generator.generate_and_save(
    data="https://www.example.com",
    output_path='qrcode_with_logo.png',
    logo_path='path/to/your/logo.png',
    logo_size_ratio=0.25  # Logo takes up 25% of QR code width
)
```

## Color Options

You can use:
- Color names: `'black'`, `'white'`, `'red'`, `'blue'`, `'green'`, etc.
- Hex codes: `'#FF5733'`, `'#1f77b4'`, etc.
- RGB tuples: `(255, 87, 51)`, `(31, 119, 180)`, etc.

## Examples

Run the examples:
```bash
python qr_generator.py
```

This will generate:
- `output/colored_qrcode.png` - Blue QR code
- `output/red_qrcode.png` - Red QR code on light yellow background
- `output/qrcode_with_logo.png` - QR code with embedded logo (if logo.png exists)

## API Reference

### ColoredQRCodeGenerator

#### `__init__(fill_color, back_color, box_size)`
Initialize the generator with custom colors.

#### `generate_qr(data, version, error_correction)`
Generate a QR code image.

#### `embed_image(qr_img, logo_path, logo_size_ratio)`
Embed a PNG image at the center of QR code.

#### `generate_and_save(data, output_path, logo_path, logo_size_ratio, version)`
Complete workflow: generate, embed, and save.

## Features

- 🎨 Full color customization (foreground and background)
- 🖼️ PNG logo embedding with automatic sizing
- 📊 Adjustable error correction levels
- 🔧 Customizable QR code version and box size
- 💾 Save to PNG format

## Notes

- Higher error correction levels allow better logo placement without affecting scannability
- Logo size ratio should be between 0.2-0.4 for optimal scannability
- Ensure your logo has a transparent background (RGBA) for best results
