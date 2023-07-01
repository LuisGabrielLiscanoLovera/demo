from PIL import Image

img = Image.open('8.jpg') # Open image
img = img.resize((480, 329), Image.ANTIALIAS) # Resize image
img.save('88.jpg', format='JPEG') # Save resized image