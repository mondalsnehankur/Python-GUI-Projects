# Code Explanation

This document explains how the calculator program works.

---

# 1. Importing Modules

```python
from kivy.app import App
```

Imports the main application class from Kivy.

```python
from kivy.uix.gridlayout import GridLayout
```

Imports GridLayout, which arranges widgets in rows and columns.

```python
from kivy.uix.button import Button
```

Used to create clickable buttons.

```python
from kivy.uix.textinput import TextInput
```

Creates the calculator display.

---

# 2. Creating the Layout

```python
class Calculator(GridLayout):
```

Defines a custom layout for the calculator.

The calculator inherits from GridLayout.

---

# 3. Constructor

```python
def __init__(self, **kwargs):
```

Initializes the calculator.

Inside this method:

- Number of columns is set.
- Display is created.
- Buttons are added.

---

# 4. Display

```python
self.display = TextInput(...)
```

The TextInput widget acts as the calculator screen.

Important properties:

- readonly=False
- multiline=False
- font_size=40

---

# 5. Buttons

A list stores every calculator button.

Example:

```python
buttons = [
'7','8','9','/',
'4','5','6','*',
'1','2','3','-',
'.','0','=','+',
'C'
]
```

Each string represents one button.

---

# 6. Creating Buttons

A loop creates every button.

```python
for button in buttons:
```

Each iteration:

- Creates a Button widget
- Assigns its text
- Connects it to a function

---

# 7. Event Binding

```python
btn.bind(on_press=...)
```

Event binding tells Kivy:

"When this button is pressed, execute this function."

---

# 8. Processing Input

If the button is:

### Number

Append it to the display.

Example:

```
Display:
12

Press:
3

Result:
123
```

---

### Operator

Append the operator.

Example:

```
12

+

8
```

becomes

```
12+8
```

---

### Clear Button

```
C
```

Removes everything from the display.

---

### Equal Button

```
=
```

Evaluates the expression.

```python
eval(expression)
```

Example:

```
25+75
```

returns

```
100
```

---

# 9. Error Handling

If the expression is invalid:

```python
5++
```

or

```python
9/0
```

Python raises an exception.

The calculator catches this and displays:

```
Error
```

instead of crashing.

---

# 10. Running the Application

```python
class CalculatorApp(App):
```

Represents the application itself.

Its job is to return the Calculator layout.

```python
def build(self):
    return Calculator()
```

---

# 11. Entry Point

```python
if __name__ == "__main__":
```

Runs the application.

```python
CalculatorApp().run()
```

starts the GUI event loop.

---

# Overall Flow

```
Program Starts
      │
      ▼
Create Calculator Window
      │
      ▼
Display Appears
      │
      ▼
User Presses Button
      │
      ▼
Update Display
      │
      ▼
If "="
      │
      ▼
Evaluate Expression
      │
      ▼
Show Result
      │
      ▼
Wait for Next Input
```

---

# Concepts Demonstrated

- Python Classes
- Inheritance
- Constructors
- GUI Programming
- GridLayout
- Widgets
- Event Handling
- Lambda Functions
- String Concatenation
- Exception Handling
- Object-Oriented Programming
