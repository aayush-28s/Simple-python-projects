from PIL import Image, ImageDraw

def create_dice_image(value, filename="dice.png"):
    """Create a simple dice image with the given value (1 to 6)."""
    
    # Define image size and colors
    size = 200
    background_color = "white"
    dot_color = "black"
    border_color = None
    border_radius = 100

    # Create a blank image
    img = Image.new("RGB", (size, size), background_color)
    draw = ImageDraw.Draw(img)

    # Define dot positions based on dice number
    dot_positions = {
        1: [(100, 100)],
        2: [(50, 50), (150, 150)],
        3: [(50, 50), (100, 100), (150, 150)],
        4: [(50, 50), (50, 150), (150, 50), (150, 150)],
        5: [(50, 50), (50, 150), (100, 100), (150, 50), (150, 150)],
        6: [(50, 50), (50, 100), (50, 150), (150, 50), (150, 100), (150, 150)],
    }

    # Draw a rounded rectangle for dice 
    draw.rounded_rectangle([10,10,190,190], fill = background_color, outline = border_color, width = 5, radius = border_radius)

    # Draw dots
    for pos in dot_positions.get(value, []):
        draw.ellipse([(pos[0] - 15, pos[1] - 15), (pos[0] + 15, pos[1] + 15)], fill=dot_color)

    # Save image
    img.save(filename)
    print(f"Dice image {filename} created successfully!")

for i in range (1,7):
    create_dice_image(i, f"dice{i}.png")
