# for compression
from io import BytesIO
import os
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile

def compressImage(uploadedImage, width, height):
    # Check if image is already compressed or has the same size
    # if uploadedImage.size <= 50000 or uploadedImage.width == width and uploadedImage.height == height:
    #     return uploadedImage

    # Open the image and resize it
    img = Image.open(uploadedImage)
    print(img.width, img.height, width, height)
    if img.width == width or img.height == height:
        return uploadedImage
    img_format = img.format or 'JPEG'
    img_ratio = img.width / img.height
    new_width, new_height = width, height
    if img_ratio > width/height:
        new_height = int(width / img_ratio)
    else:
        new_width = int(height * img_ratio)
    img = img.resize((new_width, new_height), Image.ANTIALIAS)

    # Create the new filename with dimensions and original extension
    filename, ext = os.path.splitext(uploadedImage.name)
    max_length = 50
    suffix = f'_{new_width}x{new_height}_{os.urandom(4).hex()}'
    new_filename = f'{filename[:max_length-len(suffix)-len(ext)]}{suffix}{ext}'

    # Compress and save the new image
    img_quality = 70
    output_io = BytesIO()
    img.save(output_io, format=img_format, quality=img_quality)
    output_io.seek(0)
    inmemory_uploaded_file = InMemoryUploadedFile(output_io, None, new_filename, f'image/{img_format}', output_io.tell(), None)
    return inmemory_uploaded_file