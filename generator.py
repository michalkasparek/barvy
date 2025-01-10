import os
import glob
import json
from PIL import Image, ImageDraw

with open('barvy.json', 'r', encoding='utf-8') as seznam:
    seznam = json.loads(seznam.read())

os.makedirs('palety', exist_ok=True)

files = glob.glob('palety/*')
for f in files:
    os.remove(f)

def create_color_squares(colors, name, square_size=100, padding=10, height=60):
    """
    Create an image with a line of colored squares
    
    Args:
        colors (list): List of hex color codes
        square_size (int): Size of each square in pixels
        padding (int): Padding between squares in pixels
        height (int): Height of the image in pixels
    """
    # Calculate total width needed
    total_width = (square_size * len(colors)) + (padding * (len(colors) + 1))
    
    # Create new image with white background
    img = Image.new('RGB', (total_width, height), 'white')
    draw = ImageDraw.Draw(img)
    
    # Calculate vertical position to center squares
    y_position = (height - square_size) // 2
    
    # Draw each colored square
    for i, color in enumerate(colors):
        x_position = padding + (i * (square_size + padding))
        
        # Draw rectangle with specified color
        draw.rectangle(
            [(x_position, y_position), 
             (x_position + square_size, y_position + square_size)],
            fill=color
        )
    
    # Save the image
    img.save(os.path.join('palety',f'{name}.png'))

export = "Barevné palety vytahané z knih a dalších zdrojů.\n\n"

for paleta, vlastnosti in seznam.items():

    export += f"## {paleta}"
    export += "\n\n"
    export += f"Zdroj: [{vlastnosti['zdroj']}]({vlastnosti['online_zdroj']})"
    export += "\n\n"
    export += str(vlastnosti['rgb'])
    export += "\n\n"

    create_color_squares(vlastnosti['rgb'], paleta)

    export += f'![{paleta}](palety/{paleta}.png)'

    export += "\n\n"

print("README.md přegenerován.")

with open('README.md', 'w+', encoding='utf-8') as readme:
    readme.write(export.strip())