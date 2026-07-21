from PIL import Image
import os

print("=" * 40)
print("       BASIC IMAGE RECOGNITION")
print("=" * 40)

image_path = input("Enter the path of your image: ").strip().strip('"')

if os.path.exists(image_path):
    try:
        image = Image.open(image_path)

        print("\nImage successfully recognized!")
        print(f"File name: {os.path.basename(image_path)}")
        print(f"Image format: {image.format}")
        print(f"Image size: {image.size}")
        print(f"Color mode: {image.mode}")

        print("\nImage information displayed successfully.")

    except Exception as error:
        print("Error opening image:", error)

else:
    print("\nImage file not found.")
    