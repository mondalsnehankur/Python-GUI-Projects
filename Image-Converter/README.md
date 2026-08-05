# PNG to JPG Image Converter

A simple desktop application built with **Python**, **Tkinter**, and **Pillow (PIL)** that allows users to convert PNG images into JPG format through an easy-to-use graphical interface.

## 📌 Overview

This project provides a lightweight GUI for image conversion. Users can browse for a PNG image, select a destination, and save the image as a JPG file with just a few clicks.

It is an excellent beginner project for learning:

* Python GUI development
* File handling
* Image processing with Pillow
* Tkinter widgets and event handling

---

## ✨ Features

* Simple and intuitive graphical interface
* Browse and select PNG images
* Convert PNG images to JPG format
* Choose a custom save location
* Built using Python's Tkinter library
* Image processing powered by Pillow

---

## 🖼 Application Workflow

1. Launch the application.
2. Click **Select PNG File**.
3. Choose the PNG image you want to convert.
4. Click **Convert PNG to JPG**.
5. Select the destination folder and filename.
6. Save the converted JPG image.

---

## 📂 Project Structure

```text
PNG-to-JPG-Converter/
│
├── image_converter.py
├── README.md
└── requirements.txt
```

---

## 🛠 Technologies Used

* Python 3
* Tkinter
* Pillow (PIL)

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/png-to-jpg-converter.git
```

### 2. Navigate to the project directory

```bash
cd png-to-jpg-converter
```

### 3. Install the required dependency

```bash
pip install pillow
```

> **Note:** Tkinter is included with most standard Python installations. If it is missing, install it using your operating system's package manager or Python distribution.

---

## ▶️ Running the Application

Run the following command:

```bash
python image_converter.py
```

The application window will open, allowing you to select and convert images.

---

## 🧩 GUI Components

| Component                 | Purpose                                |
| ------------------------- | -------------------------------------- |
| Label                     | Displays the application title         |
| Select PNG File Button    | Opens a file picker to select an image |
| Convert PNG to JPG Button | Saves the selected image in JPG format |
| Canvas                    | Organizes and displays GUI elements    |

---

## 📚 Concepts Demonstrated

This project demonstrates:

* Creating a Tkinter application window
* Using the `Canvas` widget
* Creating labels and buttons
* Handling button click events
* Opening file dialogs
* Saving files with custom extensions
* Working with images using Pillow
* Using functions and global variables

---

## ⚠️ Current Limitation

If the selected PNG image contains transparency (an alpha channel), saving it directly as a JPG may raise an error because the JPG format does not support transparency.

A common solution is to convert the image before saving:

```python
if im1.mode == "RGBA":
    im1 = im1.convert("RGB")
```

Adding this step improves compatibility with transparent PNG files.

---

## 🚀 Future Improvements

* Drag-and-drop image support
* Batch image conversion
* Preview selected image
* Support for additional image formats
* Adjustable JPG quality
* Progress and success notifications
* Error handling for invalid files
* Dark mode interface

---

## 🎯 Suitable For

* Python beginners
* Students learning Tkinter
* GUI programming practice
* Image processing projects
* Academic mini projects

---

## 📄 License

This project is open-source and intended for educational and learning purposes.
