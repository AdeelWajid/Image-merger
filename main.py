import tkinter as tk
from tkinter import filedialog
from PIL import Image

def select_image():
    # Open a file dialog to select the image
    file_path = filedialog.askopenfilename()
    return file_path

def merge_images():
    # Select the first image
    image1_path = select_image()
    image1 = Image.open(image1_path)

    # Select the second image
    image2_path = select_image()
    image2 = Image.open(image2_path)

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

# Create the main window
root = tk.Tk()

# Create a button to start the merge process
merge_button = tk.Button(root, text='Merge Images', command=merge_images)
merge_button.pack()

# Run the main loop
root.mainloop()
