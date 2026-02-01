import qrcode
from qrcode.image.pure import PyPNGImage
from PIL import Image
import os


class ColoredQRCodeGenerator:
    """Generate colored QR codes with embedded PNG images"""
    
    def __init__(self, fill_color='black', back_color='white', box_size=10):
        """
        Initialize the QR code generator
        
        Args:
            fill_color: QR code foreground color (RGB tuple or color name)
            back_color: QR code background color (RGB tuple or color name)
            box_size: Size of each box in pixels
        """
        self.fill_color = fill_color
        self.back_color = back_color
        self.box_size = box_size
    
    def generate_qr(self, data, version=1, error_correction=qrcode.constants.ERROR_CORRECT_H):
        """
        Generate a basic QR code
        
        Args:
            data: Data to encode in the QR code
            version: QR code version (1-40)
            error_correction: Error correction level
            
        Returns:
            PIL Image object
        """
        qr = qrcode.QRCode(
            version=version,
            error_correction=error_correction,
            box_size=self.box_size,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        
        img = qr.make_image(fill_color=self.fill_color, back_color=self.back_color)
        return img
    
    def embed_image(self, qr_img, logo_path, logo_size_ratio=0.3):
        """
        Embed a PNG image at the center of the QR code
        
        Args:
            qr_img: PIL Image object of the QR code
            logo_path: Path to the PNG logo/image
            logo_size_ratio: Size of logo relative to QR code (0.0-0.5)
            
        Returns:
            PIL Image object with embedded logo
        """
        if not os.path.exists(logo_path):
            raise FileNotFoundError(f"Logo file not found: {logo_path}")
        
        # Open and prepare the logo
        logo = Image.open(logo_path)
        
        # Convert to RGBA if necessary
        if logo.mode != 'RGBA':
            logo = logo.convert('RGBA')
        
        # Calculate logo size
        qr_width, qr_height = qr_img.size
        logo_size = int(min(qr_width, qr_height) * logo_size_ratio)
        logo = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)
        
        # Create a white background for the logo area (improves visibility)
        logo_bg = Image.new('RGB', (logo_size + 20, logo_size + 20), self.back_color)
        logo_bg_pos = ((logo_size + 20 - logo_size) // 2, (logo_size + 20 - logo_size) // 2)
        logo_bg.paste(logo, logo_bg_pos, logo)
        
        # Paste logo at center
        qr_copy = qr_img.convert('RGB')
        pos = ((qr_width - logo_bg.size[0]) // 2, (qr_height - logo_bg.size[1]) // 2)
        qr_copy.paste(logo_bg, pos)
        
        return qr_copy
    
    def save_qr(self, img, filename='qrcode.png'):
        """
        Save the QR code image
        
        Args:
            img: PIL Image object
            filename: Output filename
        """
        img.save(filename)
        print(f"QR code saved as: {filename}")
    
    def generate_and_save(self, data, output_path='qrcode.png', logo_path=None, 
                         logo_size_ratio=0.3, version=1):
        """
        Complete workflow: generate QR code, optionally embed logo, and save
        
        Args:
            data: Data to encode
            output_path: Output file path
            logo_path: Optional path to PNG logo to embed
            logo_size_ratio: Logo size relative to QR code
            version: QR code version
        """
        print(f"Generating QR code for: {data}")
        
        # Generate colored QR code
        qr_img = self.generate_qr(data, version=version)
        
        # Embed logo if provided
        if logo_path:
            print(f"Embedding logo from: {logo_path}")
            qr_img = self.embed_image(qr_img, logo_path, logo_size_ratio)
        
        # Save the result
        self.save_qr(qr_img, output_path)
        return qr_img


def main():
    """Example usage"""
    # Example 1: Simple colored QR code
    print("=" * 50)
    print("Example 1: Colored QR Code")
    print("=" * 50)
    
    generator = ColoredQRCodeGenerator(
        fill_color='#1f77b4',  # Blue
        back_color='white',
        box_size=10
    )
    
    qr_img = generator.generate_qr("https://www.figma.com/make/a1Zd6jA3UiWRj6H7sHkxa7/Wireframe-for-LokSathi-AI?p=f&t=nb8hQGUCjA9Wwn6r-0&fullscreen=1")
    generator.save_qr(qr_img, 'output/colored_qrcode.png')
    
    # Example 2: QR code with different colors
    print("\n" + "=" * 50)
    print("Example 2: Red QR Code")
    print("=" * 50)
    
    generator_red = ColoredQRCodeGenerator(
        fill_color='#d62728',  # Red
        back_color='#ffffcc',  # Light yellow
        box_size=10
    )
    
    qr_img_red = generator_red.generate_qr("Hello World")
    generator_red.save_qr(qr_img_red, 'output/red_qrcode.png')
    
    # Example 3: QR code with embedded logo (uncomment if you have a logo)
    print("\n" + "=" * 50)
    print("Example 3: QR Code with Embedded Logo")
    print("=" * 50)
    
    try:
        generator_logo = ColoredQRCodeGenerator(
            fill_color='#2ca02c',  # Green
            back_color='white',
            box_size=10
        )
        
        # Using a sample logo - replace with your actual PNG file
        logo_path = 'sample_logo.png'
        if os.path.exists(logo_path):
            generator_logo.generate_and_save(
                data="https://www.figma.com/make/a1Zd6jA3UiWRj6H7sHkxa7/Wireframe-for-LokSathi-AI?p=f&t=nb8hQGUCjA9Wwn6r-0&fullscreen=1",
                output_path='output/qrcode_with_logo.png',
                logo_path=logo_path,
                logo_size_ratio=0.25
            )
        else:
            print(f"Logo file '{logo_path}' not found. Skipping logo example.")
            print("To use this feature, place your PNG logo at:", os.path.abspath(logo_path))
    except Exception as e:
        print(f"Error in logo example: {e}")


if __name__ == '__main__':
    main()
