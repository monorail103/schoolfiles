import random
from PIL import Image

def generate_random_bmp(width, height, file_path):
    # Create a new image with RGB mode
    image = Image.new('RGB', (width, height))
    
    # Generate random pixels
    pixels = [
        (random.randint(0, 255), random.randint(0, 200), random.randint(0, 255))
        for _ in range(width * height)
    ]
    
    # Put data into image
    image.putdata(pixels)
    
    # Save the image as a BMP file
    image.save(file_path, 'BMP')

if __name__ == "__main__":
    width = 640  # Width of the image
    height = 480  # Height of the image
    file_path = 'random_image.bmp'  # File path to save the image
    
    generate_random_bmp(width, height, file_path)
    print(f"Random BMP image saved as {file_path}")