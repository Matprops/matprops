# from PIL import Image
#
#
# def images_are_equal(image1_path, image2_path):
#     try:
#         # Open images
#         image1 = Image.open(image1_path)
#         image2 = Image.open(image2_path)
#
#         # Check if images have the same size
#         if image1.size != image2.size:
#             return False
#
#         # Iterate over each pixel and compare them
#         for x in range(image1.width):
#             for y in range(image1.height):
#                 if image1.getpixel((x, y)) != image2.getpixel((x, y)):
#                     return False
#
#         return True
#
#     except Exception as e:
#         print(f"Error: {e}")
#         return False
#
#
# # Example usage
# image1_path = "image1.png"
# image2_path = "image2.png"
#
# if images_are_equal(image1_path, image2_path):
#     print("The images are equal.")
# else:
#     print("The images are not equal.")
