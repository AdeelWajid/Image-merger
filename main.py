import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def select_image(image_label):
    # Open a file dialog to select the image
    file_path = filedialog.askopenfilename()
    # Set the image_path attribute for the label object
    image_label.image_path = file_path
    # Open the image and resize it to fit the label
    image = Image.open(file_path)
    image.thumbnail((200, 200))
    # Create a PhotoImage object from the image
    photo = ImageTk.PhotoImage(image)
    # Update the label with the new image
    image_label.configure(image=photo)
    image_label.image = photo
    return file_path

def merge_images(image1_label, image2_label, merged_image_label):
    # Get the file paths of the selected images
    image1_path = image1_label.image_path
    image2_path = image2_label.image_path

    # Open the images
    image1 = Image.open(image1_path)
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

    # Resize the merged image to fit the label
    merged_image.thumbnail((400, 400))

    # Create a PhotoImage object from the merged image
    photo = ImageTk.PhotoImage(merged_image)

    # Update the label with the new image
    merged_image_label.configure(image=photo)
    merged_image_label.image = photo

# Create the main window
root = tk.Tk()

# Create a label to display the first selected image
image1_label = tk.Label(root)
image1_label.pack()

# Create a button to select the first image
select_image1_button = tk.Button(root, text='Select Image 1', command=lambda: select_image(image1_label))
select_image1_button.pack()

# Create a label to display the second selected image
image2_label = tk.Label(root)
image2_label.pack()

# Create a button to select the second image
select_image2_button = tk.Button(root, text='Select Image 2', command=lambda: select_image(image2_label))
select_image2_button.pack()

# Create a button to start the merge process
merge_button = tk.Button(root, text='Merge Images', command=lambda: merge_images(image1_label, image2_label, merged_image_label))
merge_button.pack()

# Create a label to display the merged image
merged_image_label = tk.Label(root)
merged_image_label.pack()

# Run the main loop
root.mainloop()
