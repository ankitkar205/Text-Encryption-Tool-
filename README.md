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

1. User enters **plain text**.
2. Selects the encryption algorithm.
3. Enters the **key** (if required).
4. Clicks **Encrypt** or **Decrypt**.
5. Result is shown instantly and can be copied to clipboard.

---

## 🖼️ GUI Screenshot *(optional)*

```bash
# Add this only if you upload screenshot images in a "screenshots/" folder
![App Screenshot](screenshots/gui_light_mode.png)
⚙️ Installation
1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/your-username/text-encryption-tool.git
cd text-encryption-tool
2️⃣ Create & Activate a Virtual Environment (Recommended)
bash
Copy
Edit
python -m venv .venv
.venv\Scripts\activate  # On Windows
source .venv/bin/activate  # On Linux/Mac
3️⃣ Install Required Modules
bash
Copy
Edit
pip install -r requirements.txt
4️⃣ Run the Application
bash
Copy
Edit
python gui.py
📦 Build to Executable (.exe)
💡 Install PyInstaller
bash
Copy
Edit
pip install pyinstaller
🔨 Build .exe (Windows)
bash
Copy
Edit
pyinstaller gui.py --onefile --noconsole --icon=icon.ico
Final .exe will be in the dist/ folder.

💡 Remove --icon=icon.ico if you don’t want to use a custom icon.

📁 Project Structure
bash
Copy
Edit
text-encryption-tool/
├── aes_module.py        # AES encryption/decryption
├── des_module.py        # DES encryption/decryption
├── rsa_module.py        # RSA encryption/decryption
├── gui.py               # Main GUI logic
├── main.py              # Optional CLI version
├── icon.ico             # Optional app icon
├── README.md            # This file
├── requirements.txt     # Python dependencies
└── dist/                # Your .exe will appear here after build
✅ Requirements
Python 3.13.5 or higher

Libraries:

ttkbootstrap

pycryptodome

rsa

📃 License
MIT License © 2025 [Rik]

🤝 Credits
Developed by Rik
Cyber Security Internship – Pinnacle Labs
Made with Python, caffeine ☕, and a love for clean code.

🔗 GitHub Profile

yaml
Copy
Edit

---

## ⚠️ Don’t Forget:
- Replace `your-username` with your **GitHub username**
- Add `requirements.txt`:

```txt
ttkbootstrap
pycryptodome
rsa
