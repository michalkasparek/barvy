import os
import glob
import json
from colorsys import rgb_to_hsv, hsv_to_rgb
from PIL import Image, ImageDraw

def process_colors(hex_colors):
    def hex_to_rgb(hex_color):
        # Remove '#' if present and convert to RGB
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    
    def rgb_to_hex(rgb):
        # Convert RGB tuple back to hex
        return f"#{int(rgb[0]):02x}{int(rgb[1]):02x}{int(rgb[2]):02x}".upper()
    
    def get_brightness(hex_color):
        # Convert to RGB and calculate perceived brightness
        r, g, b = hex_to_rgb(hex_color)
        return (0.299 * r + 0.587 * g + 0.114 * b) / 255
    
    def increase_saturation(hex_color, saturation_increase=0.2):
        # Convert hex to RGB
        rgb = hex_to_rgb(hex_color)
        
        # Convert RGB to HSV
        r, g, b = [x/255.0 for x in rgb]
        h, s, v = rgb_to_hsv(r, g, b)
        
        # Increase saturation while keeping it <= 1.0
        s = min(s + saturation_increase, 1)
        
        # Convert back to RGB
        r, g, b = hsv_to_rgb(h, s, v)
        
        # Convert to 0-255 range and then back to hex
        rgb = (int(r * 255), int(g * 255), int(b * 255))
        return rgb_to_hex(rgb)
    
    # Sort colors by brightness (darkest to brightest)
    sorted_colors = sorted(hex_colors, key=get_brightness)
    
    # Create vivid versions of the sorted colors
    vivid_colors = [increase_saturation(color) for color in sorted_colors]
    
    return sorted_colors, vivid_colors

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

with open('barvy_zdroj.json', 'r', encoding='utf-8') as vstup:
    vstup = json.loads(vstup.read())

os.makedirs('palety', exist_ok=True)

files = glob.glob('palety/*')
for f in files:
    os.remove(f)

vystup = {}

with open("readme_intro.md", "r", encoding="utf-8") as vypis:
    vypis =  vypis.read().replace('xxx',str(len(vstup)))

for paleta, vlastnosti in vstup.items():

    vylepseni = process_colors(vlastnosti['rgb'])
    vystup[paleta] = vlastnosti['rgb']
    vystup[f'{paleta}_sorted'] = vylepseni[0]
    vystup[f'{paleta}_plus'] = vylepseni[1]

    vypis += f"## {paleta}"
    vypis += "\n\n"
    vypis += f"originál: [{vlastnosti['zdroj']}]({vlastnosti['link']})"
    
    try:
        vypis += f", kudos: {vlastnosti['kudos']}"
    except:
        pass

    vypis += "\n\n"
    vypis += "```" + str(vlastnosti['rgb']) + "```"
    vypis += "\n\n"

    create_color_squares(vlastnosti['rgb'], paleta)

    vypis += f'![{paleta}](palety/{paleta}.png)'

    vypis += "\n\n"
    vypis += "```" + str(vylepseni[0]) + "```"
    vypis += "\n\n"

    create_color_squares(vylepseni[0], f'{paleta}_sorted')

    vypis += f'![{f'{paleta}_sorted'}](palety/{paleta}_sorted.png)'

    vypis += "\n\n"


with open('README.md', 'w+', encoding='utf-8') as readme:
    readme.write(vypis.strip())

with open('barvy.json', 'w+', encoding='utf-8') as export:
    export.write(json.dumps(vystup, sort_keys=True))

print("Fertig.")