# 🔐 Password Manager App (Tkinter + Python)
A simple yet secure **Password Manager** built using **Python** and **Tkinter**, allowing you to generate strong passwords, store them securely in a local JSON file, and search for saved credentials.

<img width="1536" height="1024" alt="9d7e0817-9de1-4f4c-a80a-e376ab5621c3" src="https://github.com/user-attachments/assets/d00e2cec-55ed-44c3-9901-1a258650656f" />

---

## 🧰 Features
- ✅ Save website credentials (email & password) locally in a `.json` file
- 🔒 Auto-generates strong, random passwords
- 📋 Automatically copies the password to clipboard
- 🔎 Search functionality to retrieve stored credentials
- 💾 Secure storage using JSON and `os.environ` (no hardcoded secrets)
- 🧠 Clean and intuitive GUI built with Tkinter
---

## 🖼️ GUI Preview

> A clean and minimal desktop app built using the Tkinter library.
> <img width="492" height="411" alt="Capture" src="https://github.com/user-attachments/assets/c6474725-09e2-4355-89bb-b15b362f6f6a" />

---

## 🧠 Built With
- Python 3.7+  
- `tkinter` for GUI  
- `random` for password generation  
- `json` for storing credentials  
- `pyperclip` for clipboard copy  
- `os` for basic file handling  

---

## 💻 How It Works
1. You enter the website name, your email/username, and click "Generate Password" or enter your own.
2. Clicking "Add" saves the credentials in a `data.json` file.
3. Use the "Search" button to retrieve saved credentials instantly.
4. Passwords are automatically copied to your clipboard for quick use.

---

## 🔧 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/password-manager-app.git
cd password-manager-app
```

### 2. Install Dependencies
```bash
pip install pyperclip
```
---

## ▶️ Running the Script
After setting the environment variables, run the script:

```bash
python main.py
```
---

## 🌐 File Structure

| API                | Purpose                              |
|--------------------|--------------------------------------|
| main.py            | Main script handling the UI and logic|
| data.json          | Local storage for saved credentials  |
| logo.png           | App icon used in the UI              |


---

## 🧠 What You’ll Learn
- How to build desktop apps with Python and Tkinter
- Managing local data using JSON
- Safe handling of passwords (no plain-text exposure in UI)
- GUI interaction patterns (forms, search, notifications)
- Integration of clipboard support for better UX

---

## 🙌 Credits
- 👨‍💻 **Built by: Mussa Tariq
- LinkedIn: https://www.linkedin.com/in/mussa-tariq-0652712a0/
-  💡 Inspired by Angela Yu's 100 Days of Code Project 

---

## 📬 Final Note
Keep your credentials safe, generate unbreakable passwords, and make "forgot password?" a thing of the past.

#Python #Tkinter #PasswordManager #Clipboard #GUIApp #Automation #JSON #OpenSource
