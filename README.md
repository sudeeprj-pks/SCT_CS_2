# Simple Image Encryption Tool

## 📘 Project Overview

The **Simple Image Encryption Tool** is a beginner-friendly Python project that demonstrates **image encryption and decryption using pixel manipulation** techniques. Instead of complex cryptographic algorithms, this project applies simple arithmetic operations on pixel values to help learners understand how encryption concepts can be applied to image files.

This project is ideal for students and beginners in **Python, cybersecurity, and cryptography fundamentals**.

---

## 🔐 How It Works (Concept)

* Each pixel in an image is represented by RGB values
* A numeric **key** is used to modify pixel values
* **Encryption:** Pixel values are modified using addition with the key
* **Decryption:** The same key is used to reverse the operation (subtraction)

⚠️ This is a **learning-oriented encryption method**, not suitable for real-world secure image protection.

---

## ✨ Features

* Encrypts and decrypts image files (PNG, JPG, JPEG, etc.)
* Uses simple pixel manipulation (addition / subtraction with a key)
* Easy to understand and beginner-friendly
* Works completely offline
* Lightweight and minimal dependencies

---

## 🛠️ Technologies Used

* **Python 3.x**
* **Pillow (PIL)** – Python Imaging Library

---

## 📦 Requirements

* Python 3.x
* Pillow library

### Install Pillow

```bash
pip install Pillow
```

---

## 📂 Project Structure

```
image_encryption_tool/
│── image_encrypt.py     # Main Python script
│── input_image.png      # Original image (example)
│── encrypted_image.png  # Encrypted output image
│── decrypted_image.png  # Decrypted output image
└── README.md            # Documentation
```

---

## 🚀 How to Run the Project (Kali Linux / Linux)

1️⃣ Open the terminal

2️⃣ Navigate to the project directory

```bash
cd image_encryption_tool
```

3️⃣ Run the program

```bash
python3 image_encrypt.py
```

4️⃣ Provide:

* Image file path
* Encryption key (integer value)
* Choose encrypt or decrypt option

---

## 🧪 Example Workflow

```
Enter image path: input_image.png
Enter key value: 50
Choose option:
1. Encrypt
2. Decrypt
Encrypted image saved successfully!
```

To decrypt, use the **same key** used during encryption.

---

## 🎯 Learning Outcomes

By completing this project, you will learn:

* Basics of image processing in Python
* How pixel values work (RGB manipulation)
* Practical understanding of encryption and decryption
* File handling and user input in Python
* Ethical use of cryptographic concepts

---

## ⚠️ Disclaimer

This project is intended **only for educational purposes**.
It does **not provide strong cryptographic security** and should not be used for protecting sensitive or confidential images.

---

## 📄 License

This project is open-source and free to use for **educational and academic purposes**.

---

**Project Title:** Simple Image Encryption Tool
**Domain:** Encryption & Decryption using Python
**Author:** Sudeep
**Category:** Python • Cryptography Basics
