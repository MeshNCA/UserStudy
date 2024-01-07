import numpy as np
from PIL import Image, ImageDraw, ImageFont
from tqdm import tqdm
import random

# Function to concatenate images horizontally with margins and add text below each image

base_path = "images"
h, w = 256, 256
gray_level = 255


def concatenate_images(images, margin=10):
    # Load images
    pil_images = [Image.open(f"{base_path}/{img_name}").resize((h, w)) for img_name in images]

    # Calculate total width and height for the concatenated image
    total_width = sum(img.width for img in pil_images) + (len(images) - 1) * margin
    max_height = max(img.height for img in pil_images)

    # Create a blank image with the calculated dimensions
    concatenated_image = Image.new("RGB", (total_width, max_height + 50), (gray_level, gray_level, gray_level))

    # Paste each image onto the blank image
    current_x = 0
    draw = ImageDraw.Draw(concatenated_image)
    # font = ImageFont.load_default()

    font_path = "C:\Windows\Fonts\\times.ttf"  # Replace with the actual path to Times New Roman font file
    font_size = 24  # Adjust the font size as needed
    font = ImageFont.truetype(font_path, font_size)

    i = 1
    for img, name in zip(pil_images, images):
        concatenated_image.paste(img, (current_x, 5))
        draw.text((current_x + 84, max_height + 10), f"Option ({i})", font=font, fill=(0, 0, 0))
        current_x += img.width + margin
        i += 1

    # Save the result

    return concatenated_image


def create_question(target_texture, target_mesh, methods):
    image_paths = [f"{method}_{target_texture}_{target_mesh}.png" for method in methods]

    option_images = concatenate_images(image_paths, margin=2)
    target_mesh = Image.open(f"{base_path}/{target_mesh}.png").resize((h, w))

    total_width = option_images.width
    total_height = target_mesh.height + option_images.height + 10

    final_image = Image.new("RGB", (total_width, total_height), (gray_level, gray_level, gray_level))
    final_image.paste(option_images, (0, target_mesh.height + 10))

    final_image.paste(target_mesh, (70, 10))

    draw = ImageDraw.Draw(final_image)
    # font = ImageFont.load_default()

    font_path = "C:\Windows\Fonts\\timesbd.ttf"  # Replace with the actual path to Times New Roman font file
    font_size = 24  # Adjust the font size as needed
    font = ImageFont.truetype(font_path, font_size)

    draw.text((10, target_mesh.height // 2), "Object:", font=font, fill=(0, 0, 0))

    draw.text((345, target_mesh.height // 2), f"Reference Material:", font=font, fill=(0, 0, 0))
    draw.text((555, target_mesh.height // 2), f"\"{target_texture}\"", font=font, fill=(200, 0, 15))

    return final_image


methods = ["meshnca", "text2mesh", "xmesh"]

texture_names = [
    "bark", "cactus", "colorful crochet", "feathers", "jelly beans",
    "marble", "moss", "patchwork leather", "sandstone", "stained glass"
]

mesh_names = ["bunny", "alien", "chair", "mug", "vase"]

with open("questions.txt", "w") as f:
    for target_texture in tqdm(texture_names):
        for target_mesh in mesh_names:

            random.shuffle(methods)

            img_name = f"{target_texture}_{target_mesh}"

            img = create_question(target_texture, target_mesh, methods)
            # img.show()
            img.save(f"questions/{img_name}.png")
            f.write(img_name + " " + " ".join(methods) + "\n")
