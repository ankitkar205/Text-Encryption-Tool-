# 🔐 Text Encryption Tool

A powerful, beginner-friendly cybersecurity application built in **Python** for encrypting and decrypting text using modern algorithms like **AES**, **DES**, and **RSA**.

This tool includes a sleek GUI built with `ttkbootstrap`, designed to run seamlessly on **Windows** and **Kali Linux**, featuring a minimalist, rounded, and dynamic theme.

---

## 🧠 Features

- 🔐 Encrypt & decrypt text using:
  - **AES (Advanced Encryption Standard)**
  - **DES (Data Encryption Standard)**
  - **RSA (Rivest–Shamir–Adleman)**
- 🖥️ Modern and minimal **GUI** with theme support
- 🧠 Smart key detection (RSA disables key entry)
- 📋 Copy encrypted/decrypted output to clipboard
- ⚙️ Built with **Python 3.13.5**
- 🪟 Converts easily into `.exe` (ready for production use)
- 💼 Internship-ready cybersecurity project

---

## 🔒 Algorithms Used

| Algorithm | Type         | Key Required? | Key Size         |
|-----------|--------------|---------------|------------------|
| AES       | Symmetric    | ✅ Yes         | 16 characters     |
| DES       | Symmetric    | ✅ Yes         | 8 characters      |
| RSA       | Asymmetric   | ❌ No (Auto)   | Public/Private Key Pair |

---

## 🚀 How It Works

1. Enter **plain text** into the input field.
2. Select an **encryption algorithm**.
3. Enter the **key** (if required).
4. Choose between **Encrypt** or **Decrypt**.
5. Get the result instantly and **copy** it if needed.

---

## 🖼️ GUI Screenshots

<img src="a.png" width="100%" >
<img src="b.png" width="100%" >
<img src="c.png" width="100%" >

---

## ⚙️ Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/text-encryption-tool.git
cd text-encryption-tool

```bash
python -m venv .venv
.venv\Scripts\activate        # On Windows
source .venv/bin/activate    # On Linux/Mac

pip install -r requirements.txt
python gui.py

pip install pyinstaller


📁 Project Structure
bash
Copy
Edit
text-encryption-tool/
├── aes_module.py        # AES encryption/decryption logic
├── des_module.py        # DES encryption/decryption logic
├── rsa_module.py        # RSA encryption/decryption logic
├── gui.py               # Main GUI script
├── main.py              # Optional CLI version
├── icon.ico             # Optional app icon
├── README.md            # This file
├── requirements.txt     # Python dependencies
└── dist/                # Output folder for .exe

✅ Requirements
Python 3.13.5 or higher

Required Libraries:
txt
Copy
Edit
ttkbootstrap
pycryptodome
rsa

📃 License
MIT License © 2025 [Rik]

🤝 Credits
Developed by Ankit
Cyber Security Internship – Pinnacle Labs
Made with Python, caffeine ☕, and a love for clean code 💻❤️



