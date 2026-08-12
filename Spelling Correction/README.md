# Text Correction using TextBlob

A simple Python program that uses the **TextBlob** library to automatically identify and correct misspelled words.

## 📌 Overview

This project demonstrates basic **spell correction** in Python using TextBlob.

The program takes a list of intentionally misspelled words, creates `TextBlob` objects for each word, and uses the `.correct()` method to generate corrected versions.

### Example

Input:

```text
Machne
Learnin
Comptgn
```

Output:

```text
Machine Learning Computing
```

---

## ✨ Features

* Detects misspelled words
* Uses TextBlob for spelling correction
* Processes multiple words using a loop
* Displays the original misspelled words
* Prints the corrected words

---

## 🛠 Technologies Used

* **Python 3**
* **TextBlob**

---

## 📦 Installation

First, make sure Python is installed.

Install TextBlob using `pip`:

```bash
pip install textblob
```

If required, download the TextBlob corpora:

```bash
python -m textblob.download_corpora
```

---

## 📂 How the Code Works

### 1. Import TextBlob

```python
from textblob import TextBlob
```

The `TextBlob` class provides natural language processing functionality, including spelling correction.

---

### 2. Define Misspelled Words

```python
words = ["Machne", "Learnin", "Comptgn"]
```

The list contains intentionally misspelled words.

---

### 3. Create an Empty List

```python
corrected_words = []
```

This list stores the `TextBlob` objects corresponding to the input words.

---

### 4. Convert Words into TextBlob Objects

```python
for i in words:
    corrected_words.append(TextBlob(i))
```

Each word is converted into a `TextBlob` object and added to `corrected_words`.

---

### 5. Display the Original Words

```python
print("Wrong words :", words)
```

This prints the original misspelled words.

---

### 6. Correct the Words

```python
for i in corrected_words:
    print(i.correct(), end=" ")
```

The `.correct()` method attempts to identify the most likely spelling correction for each word.

---

## ▶️ Example Output

```text
Wrong words : ['Machne', 'Learnin', 'Comptgn']
Corrected Words are :
Machine Learning Computing
```

> **Note:** TextBlob's spelling correction is probabilistic, so the exact correction may vary depending on the input word and TextBlob's underlying spelling corpus. For unusual or heavily misspelled words, the result may not always be what you expect.

---

## 📂 Project Structure

```text
TextBlob-Spell-Correction/
│
├── spell_correction.py
└── README.md
```

---

## ▶️ How to Run

Clone the repository:

```bash
git clone https://github.com/your-username/textblob-spell-correction.git
```

Navigate to the project:

```bash
cd textblob-spell-correction
```

Install the dependency:

```bash
pip install textblob
```

Download the required corpora:

```bash
python -m textblob.download_corpora
```

Run the program:

```bash
python spell_correction.py
```

---

## 🧠 Concepts Demonstrated

* Python lists
* `for` loops
* List manipulation
* External Python libraries
* TextBlob objects
* Spell correction
* String output formatting
* Natural Language Processing (NLP) basics

---

## 🚀 Possible Improvements

This basic implementation can be extended to:

* Accept words from user input
* Correct complete sentences
* Read text from a file
* Create a GUI spell checker
* Highlight misspelled words
* Provide multiple correction suggestions
* Build a real-time spell-checking application

---

## 🎯 Learning Outcome

This project provides a basic introduction to using a third-party **Natural Language Processing (NLP)** library in Python and demonstrates how pre-trained linguistic resources can be used for automated spelling correction.

---

## 📄 License

This project is intended for educational and learning purposes.
