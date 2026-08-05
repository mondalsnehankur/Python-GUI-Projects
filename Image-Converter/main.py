# Import the tkinter library for creating the GUI
import tkinter as tk

# Import the file dialog module to open/save files
from tkinter import filedialog

# Import the Image class from the Pillow library for image processing
from PIL import Image

# Create the main application window
root = tk.Tk()

# Create a canvas widget
# width = 300 pixels
# height = 250 pixels
# bg = background color
# relief = border style
canvas1 = tk.Canvas(root, width=300, height=250, bg='azure3', relief='raised')

# Display the canvas inside the main window
canvas1.pack()

# Create a label widget
label1 = tk.Label(root, text="Image Converter", bg='azure3')

# Set the font style and size
label1.config(font=('helvetica', 20))

# Place the label on the canvas at coordinates (150, 60)
canvas1.create_window(150, 60, window=label1)

# Function to browse and select a PNG image
def getPNG():

    # Make im1 a global variable so it can be used in another function
    global im1

    # Open a file selection dialog
    import_file_path = filedialog.askopenfilename()

    # Open the selected image and store it in im1
    im1 = Image.open(import_file_path)

# Create a button to select the PNG file
browse_png = tk.Button(
    text="Select PNG file",
    command=getPNG,
    bg="royalblue",
    fg='white',
    font=('helvetica', 12, 'bold')
)

# Place the button on the canvas
canvas1.create_window(150, 130, window=browse_png)

# Function to convert and save the image as JPG
def convert():

    # Access the global image object
    global im1

    # Ask the user where to save the JPG file
    export_file_path = filedialog.asksaveasfilename(
        defaultextension='.jpg'
    )

    # Save the image in JPG format
    im1.save(export_file_path)

# Create the Convert button
saveasbutton = tk.Button(
    text="Convert PNG to JPG",
    command=convert,
    bg='royalblue',
    fg='white',
    font=('helvetica', 12, 'bold')
)

# Place the button on the canvas
canvas1.create_window(150, 180, window=saveasbutton)

# Start the Tkinter event loop
root.mainloop()
