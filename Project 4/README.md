# Basic Image Recognition

## 📌 Project Overview

This project is a simple Python application that recognizes an image file by opening it and displaying its basic information. It uses the **Pillow (PIL)** library to load an image and provides details such as the image name, format, size, and color mode.

This project was developed as part of a Python programming assignment to demonstrate basic image processing and file handling.

---

## 🚀 Features

- Accepts an image path from the user
- Checks whether the image file exists
- Opens the image using the Pillow library
- Displays:
  - File Name
  - Image Format
  - Image Size
  - Color Mode
- Handles invalid file paths gracefully

---

## 🛠️ Technologies Used

- Python 3
- Pillow (PIL)
- OS Module

---

## 📂 Project Structure

```
Project 4/
│── project4.py
│── sample image.png
│── README.md
```

---

## 📦 Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/your-repository-name.git
```

2. Navigate to the project folder:

```bash
cd your-repository-name
```

3. Install the required library:

```bash
pip install pillow
```

---

## ▶️ How to Run

Run the Python file:

```bash
python project4.py
```

When prompted, enter the full path of an image.

Example:

```text
Enter the path of your image:
C:\Users\Username\Pictures\sample.png
```

---

## 💻 Sample Output

```
========================================
       BASIC IMAGE RECOGNITION
========================================

Enter the path of your image:
C:\Users\Username\Pictures\sample.png

Image successfully recognized!

File name: sample.png
Image format: PNG
Image size: (800, 600)
Color mode: RGB

Image information displayed successfully.
```

---

## 📚 Learning Outcomes

Through this project, I learned how to:

- Work with image files in Python
- Use the Pillow library
- Handle user input
- Validate file paths
- Implement exception handling
- Display image properties

---

## 👨‍💻 Author

**Ehtisham Malik**

---

## 📄 License

This project is created for educational purposes.