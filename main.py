from PIL import Image
import os

input_folder = "static/images"
output_folder = "static/resized_images"
os.makedirs(output_folder, exist_ok=True)

target_size = (1920, 1080)  # Desired dimensions (width, height)

for image_name in os.listdir(input_folder):
    if image_name.endswith(('png', 'jpg', 'jpeg', 'gif')):
        image_path = os.path.join(input_folder, image_name)
        img = Image.open(image_path)
        img_resized = img.resize(target_size, Image.LANCZOS)
        img_resized.save(os.path.join(output_folder, image_name))

print("Images resized successfully!")