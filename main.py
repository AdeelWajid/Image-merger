from PIL import Image

# Open the images
image1 = Image.open('image1.jpg')
image2 = Image.open('image2.jpg')

# Resize the images to the same size
image1 = image1.resize((426, 240))
image2 = image2.resize((426, 240))

# Create a new image with the same size as the input images
merged_image = Image.new('RGB', (426, 240))

# Paste the input images into the merged image
merged_image.paste(image1, (0, 0))
merged_image.paste(image2, (213, 0))

# Save the merged image
merged_image.save('merged_image.jpg')