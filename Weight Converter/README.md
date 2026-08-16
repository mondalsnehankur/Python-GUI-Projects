# ⚖️ Weight Converter GUI

A simple **Weight Converter GUI application** built using Python's **Tkinter** library. The application takes a weight value in kilograms (KG) and converts it into **grams, pounds, and ounces**.

This project demonstrates the basics of creating a graphical user interface in Python using Tkinter, including labels, input fields, buttons, text boxes, functions, and the `grid()` geometry manager.

---

## 📌 Features

* Convert weight from **Kilograms (KG)** to:

  * Grams
  * Pounds
  * Ounces
* Simple graphical user interface
* Input is taken through an `Entry` widget
* Conversion is triggered using a **Convert** button
* Results are displayed in separate text boxes
* Uses Tkinter's `grid()` layout system

---

## 🛠️ Technologies Used

* **Python 3**
* **Tkinter**

---

## 📂 Project Structure

```text
Weight Converter/
│
├── weight_converter.py
└── README.md
```

> The Python file can be named according to your preference.

---

## 🧮 Conversion Formulas

The application uses the following conversion formulas:

### Kilograms → Grams

```text
1 KG = 1000 Grams
```

```python
gram = kg * 1000
```

### Kilograms → Pounds

```text
1 KG ≈ 2.20462 Pounds
```

```python
pound = kg * 2.20462
```

### Kilograms → Ounces

```text
1 KG ≈ 35.274 Ounces
```

```python
ounce = kg * 35.274
```

---

## 💻 Source Code

```python
from tkinter import *

# Creating a GUI Window
window = Tk()


def from_kg():
    gram = float(e2_value.get()) * 1000
    pound = float(e2_value.get()) * 2.20462
    ounce = float(e2_value.get()) * 35.274

    t1.delete("1.0", END)
    t1.insert(END, gram)

    t2.delete("1.0", END)
    t2.insert(END, pound)

    t3.delete("1.0", END)
    t3.insert(END, ounce)


e1 = Label(window, text="Input the weight in KG")

e2_value = StringVar()
e2 = Entry(window, textvariable=e2_value)

e3 = Label(window, text="Gram")
e4 = Label(window, text="Pound")
e5 = Label(window, text="Ounce")

t1 = Text(window, height=5, width=30)
t2 = Text(window, height=5, width=30)
t3 = Text(window, height=5, width=30)

b1 = Button(window, text="Convert", command=from_kg)


e1.grid(row=0, column=0)
e2.grid(row=0, column=1)

e3.grid(row=1, column=0)
e4.grid(row=1, column=1)
e5.grid(row=1, column=2)

t1.grid(row=2, column=0)
t2.grid(row=2, column=1)
t3.grid(row=2, column=2)

b1.grid(row=0, column=2)


window.mainloop()
```

---

## ▶️ How to Run

### 1. Check Python Installation

Make sure Python 3 is installed:

```bash
python --version
```

### 2. Check Tkinter

Tkinter is normally included with standard Python installations.

You can test it using:

```bash
python -m tkinter
```

If a small Tkinter test window appears, Tkinter is installed correctly.

### 3. Run the Program

Navigate to the project directory:

```bash
cd "Weight Converter"
```

Then run:

```bash
python weight_converter.py
```

---

## 🖥️ How the Application Works

The application follows a simple sequence:

```text
Enter weight in KG
        ↓
Click "Convert"
        ↓
from_kg() function executes
        ↓
Weight is converted
        ↓
Results displayed
        ↓
Grams | Pounds | Ounces
```

---

## 🔍 Code Explanation

### Creating the Window

```python
window = Tk()
```

Creates the main Tkinter window.

---

### Getting User Input

```python
e2_value = StringVar()
e2 = Entry(window, textvariable=e2_value)
```

`StringVar()` stores the value entered by the user.

The value can then be retrieved using:

```python
e2_value.get()
```

---

### Conversion Function

```python
def from_kg():
```

This function performs all the weight conversions.

The input is converted from a string to a floating-point number using:

```python
float(e2_value.get())
```

---

### Displaying the Results

The `Text` widgets are used to display the converted values.

Before displaying a new result, the existing content is removed:

```python
t1.delete("1.0", END)
```

The new result is then inserted:

```python
t1.insert(END, gram)
```

The same process is used for pounds and ounces.

---

### Convert Button

```python
b1 = Button(window, text="Convert", command=from_kg)
```

The button calls the `from_kg()` function whenever it is clicked.

---

### Grid Layout

The `grid()` geometry manager arranges the widgets into rows and columns.

For example:

```python
e1.grid(row=0, column=0)
e2.grid(row=0, column=1)
b1.grid(row=0, column=2)
```

This places the input label, input box, and Convert button in the first row.

---

## 🧪 Example

Suppose the user enters:

```text
5
```

The application calculates:

```text
Grams  = 5000
Pounds = 11.0231
Ounces = 176.37
```

The results are then displayed in the GUI.

---

## 📚 Concepts Practiced

This project provides practice with:

* Python functions
* Variables
* Floating-point numbers
* Type conversion using `float()`
* User input
* String variables
* GUI programming
* Tkinter
* `Tk()`
* `Label`
* `Entry`
* `Button`
* `Text`
* `StringVar`
* `grid()`
* Button callbacks
* `delete()`
* `insert()`
* `mainloop()`

---

## 🚀 Possible Improvements

The application can be improved further by adding:

* Input validation
* Error handling for non-numeric input
* A Clear button
* Better GUI styling
* Decimal-place formatting
* More units such as kilograms, milligrams, stones, and metric tons
* Dropdown menus for selecting input and output units
* A more modern GUI layout

---

## 👨‍💻 Author

**Snehankur Mondal**

This project was created as part of a Python learning journey and focuses on practicing GUI development with Tkinter.

---

## 📄 License

This project is intended for educational and learning purposes.
