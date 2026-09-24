from PIL import Image, ImageDraw

def make_circle(img_path, out_path):
    # Open the image
    img = Image.open(img_path).convert('RGBA')
    
    # Get dimensions
    width, height = img.size
    
    # Create a mask
    mask = Image.new('L', (width, height), 0)
    draw = ImageDraw.Draw(mask)
    
    # Draw a white circle on the mask
    # The logo in the uploaded image has a blue border. 
    # Let's crop it tightly to that border. The image is a square, 
    # so we just draw an ellipse (circle) covering the whole image area.
    draw.ellipse((0, 0, width, height), fill=255)
    
    # Create the output image with the mask
    out = Image.new('RGBA', (width, height))
    out.paste(img, (0, 0), mask=mask)
    
    # Save it
    out.save(out_path, format='PNG')
    
    # Also resize to a small icon and save as favicon.ico
    icon = out.resize((256, 256), Image.Resampling.LANCZOS)
    icon.save('public/favicon.ico', format='ICO')

make_circle(r'C:\Users\vinay\.gemini\antigravity\brain\2f1b1452-cd76-47c7-b176-6e2e735469ef\.user_uploaded\media_1789224993319.jpg', r'src\assets\logo.png')
print("Successfully cropped and saved as PNG and ICO.")
