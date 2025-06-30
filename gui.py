import tkinter as tk  # for native Text widget
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
import aes_module, des_module, rsa_module

def process_text():
    text = input_text.get("1.0", "end").strip()
    key = key_entry.get()
    mode = algorithm_var.get()
    action = action_var.get()

    if not text:
        messagebox.showwarning("Missing Text", "Please enter some text.")
        return
    if mode in ["AES", "DES"] and not key:
        messagebox.showwarning("Missing Key", "Please enter a key for AES or DES.")
        return

    try:
        if action == "Encrypt":
            if mode == "AES":
                result = aes_module.encrypt_aes(text, key)
            elif mode == "DES":
                result = des_module.encrypt_des(text, key)
            else:
                result = rsa_module.encrypt_rsa(text)
        else:
            if mode == "AES":
                result = aes_module.decrypt_aes(text, key)
            elif mode == "DES":
                result = des_module.decrypt_des(text, key)
            else:
                result = rsa_module.decrypt_rsa(text)

        output_text.delete("1.0", "end")
        output_text.insert("end", result)
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{str(e)}")

def copy_result():
    app.clipboard_clear()
    app.clipboard_append(output_text.get("1.0", "end").strip())
    messagebox.showinfo("Copied", "Result copied to clipboard.")

def update_key_field(*args):
    if algorithm_var.get() == "RSA":
        key_entry.configure(state="disabled")
        key_entry_var.set("Not needed for RSA")
    else:
        key_entry.configure(state="normal")
        key_entry_var.set("")

# Initialize GUI window
app = ttk.Window(themename="cosmo")  # Try 'darkly', 'cyborg', 'flatly' for dark modes
app.title("🔐 Text Encryption Tool")
app.geometry("620x640")
app.resizable(False, False)

# Fonts
title_font = ("Segoe UI", 13, "bold")
text_font = ("Consolas", 11)

# Text input
ttk.Label(app, text="Enter Text:", font=title_font).pack(anchor="w", padx=10, pady=(10, 0))
input_text = tk.Text(app, height=4, font=text_font, wrap="word", relief="groove", bd=2)
input_text.pack(fill="x", padx=10, pady=5)

# Key entry
ttk.Label(app, text="Enter Key (AES=16, DES=8):", font=title_font).pack(anchor="w", padx=10)
key_entry_var = ttk.StringVar()
key_entry = ttk.Entry(app, textvariable=key_entry_var, font=text_font, width=50, bootstyle="info")
key_entry.pack(fill="x", padx=10, pady=5)

# Algorithm selection
ttk.Label(app, text="Select Algorithm:", font=title_font).pack(anchor="w", padx=10)
algorithm_var = ttk.StringVar(value="AES")
algo_menu = ttk.Combobox(app, textvariable=algorithm_var, values=["AES", "DES", "RSA"], bootstyle="primary")
algo_menu.pack(fill="x", padx=10, pady=5)
algorithm_var.trace_add('write', update_key_field)

# Action selection
ttk.Label(app, text="Action:", font=title_font).pack(anchor="w", padx=10)
action_var = ttk.StringVar(value="Encrypt")
action_frame = ttk.Frame(app)
action_frame.pack(pady=5)
ttk.Radiobutton(action_frame, text="Encrypt", variable=action_var, value="Encrypt", bootstyle="success").pack(side="left", padx=10)
ttk.Radiobutton(action_frame, text="Decrypt", variable=action_var, value="Decrypt", bootstyle="danger").pack(side="left", padx=10)

# Process button
ttk.Button(app, text="🔄 Process", command=process_text, bootstyle="primary-outline").pack(pady=10)

# Copy to clipboard
ttk.Button(app, text="📋 Copy to Clipboard", command=copy_result, bootstyle="secondary").pack()

# Output text
ttk.Label(app, text="Result:", font=title_font).pack(anchor="w", padx=10, pady=(15, 0))
output_text = tk.Text(app, height=5, font=text_font, wrap="word", relief="groove", bd=2)
output_text.pack(fill="x", padx=10, pady=5)

# Start GUI
app.mainloop()
