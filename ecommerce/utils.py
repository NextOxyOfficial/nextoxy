# for compression
from io import BytesIO
import os
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile


def ShopSetup(newShop, Banner, Blog, Section, Category, Menu, Order_status, Product, ProductImage, Tag):
    # create default menu
    Menu.objects.create(name="Main Menu", shop=newShop)
    Menu.objects.create(name="Footer Menu", shop=newShop)
    # create default order status
    # Order_status.objects.create(name="Pending", shop=newShop)
    # Order_status.objects.create(name="Processing", shop=newShop)
    # Order_status.objects.create(name="Completed", shop=newShop)
    # Order_status.objects.create(name="Cancelled", shop=newShop)
    # create default section and category
    el = Section.objects.create(name="Electronics", shop=newShop)
    Category.objects.create(name="Mobile", section=el)
    Category.objects.create(name="Laptop", section=el)
    Category.objects.create(name="Camera", section=el)
    cl = Section.objects.create(name="Clothing", shop=newShop)
    Category.objects.create(name="T-Shirt", section=cl)
    Category.objects.create(name="Jacket", section=cl)
    Category.objects.create(name="Shoes", section=cl)
    hk = Section.objects.create(name="Home & Kitchen", shop=newShop)
    Category.objects.create(name="Furniture", section=hk)
    Category.objects.create(name="Kitchen", section=hk)
    Category.objects.create(name="Decor", section=hk)
    # create default tag
    Tag.objects.create(name="New year Sale", shop=newShop)
    Tag.objects.create(name="Christmas Sale", shop=newShop)
    Tag.objects.create(name="Summer Sale", shop=newShop)
    # create default banner
    # Banner.objects.create(title="Banner 1", shop=newShop)
    # Banner.objects.create(title="Banner 2", shop=newShop)
    # Banner.objects.create(title="Banner 3", shop=newShop)
    # create default blog
    Blog.objects.create(title="Blog 1", shop=newShop)
    Blog.objects.create(title="Blog 2", shop=newShop)
    Blog.objects.create(title="Blog 3", shop=newShop)
    # create default product
    # product = Product.objects.create(name="Product 1", sale_price=100, buy_price=90, shop=newShop)
    # Product.objects.create(name="Product 2", sale_price=100, buy_price=90, shop=newShop)
    # Product.objects.create(name="Product 3", sale_price=100, buy_price=90, shop=newShop)
    # create default product image
    # ProductImage.objects.create(product=product, image="product_images/product_1.jpg")
    # ProductImage.objects.create(product=product, image="product_images/product_2.jpg")

# def compressImage(uploadedImage, width, height):
#     if uploadedImage.width == width or uploadedImage.height == height:
#         return uploadedImage
#     try:
#         imageTemproary = Image.open(uploadedImage).convert('RGB')
#         outputIoStream = BytesIO()


#         target_width = width
#         target_height = height
#         target_ratio = target_height / target_width
#         im_ratio = uploadedImage.height / uploadedImage.width
#         if target_ratio > im_ratio:
#             # It must be fixed by width
#             resize_width = target_width
#             resize_height = round(resize_width * im_ratio)
#         else:
#             # Fixed by height
#             resize_height = target_height
#             resize_width = round(resize_height / im_ratio)


#         imageTemproaryResized = imageTemproary.resize( (resize_width,resize_height) )
#         imageTemproaryResized.save(outputIoStream , format='JPEG', quality=70)
#         outputIoStream.seek(0)
#         name = uploadedImage.name.split('.')[0][0:10] +"_"+str(width) + 'x' + str(height) + '.jpg'
#         uploadedImage = InMemoryUploadedFile(outputIoStream,'ImageField', name, 'image/jpeg', sys.getsizeof(outputIoStream), None)
#     except:
#         print('error compressing')
#     return uploadedImage


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