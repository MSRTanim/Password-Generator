import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate password
def generate_password():
    try:
        length = int(length_entry.get())
        if length < 6:
            messagebox.showerror("Error", "Password length should be at least 6.")
            return
        password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))
        result_label.config(text=password)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

# Function to copy password to clipboard
def copy_to_clipboard():
    app.clipboard_clear()
    app.clipboard_append(result_label.cget("text"))
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# Application setup
app = tk.Tk()
app.title("Premium Password Generator")
app.geometry("400x300")
app.config(bg="#2C3E50")

# Styling options
title_font = ("Helvetica", 18, "bold")
label_font = ("Helvetica", 12)
result_font = ("Helvetica", 14, "bold")

# UI Design
title_label = tk.Label(app, text="Premium Password Generator", font=title_font, bg="#2C3E50", fg="#ECF0F1")
title_label.pack(pady=10)

length_label = tk.Label(app, text="Enter Password Length:", font=label_font, bg="#2C3E50", fg="#ECF0F1")
length_label.pack()

length_entry = tk.Entry(app, font=label_font, justify="center", width=10)
length_entry.pack(pady=5)

generate_button = tk.Button(app, text="Generate Password", font=label_font, command=generate_password, bg="#3498DB", fg="white", activebackground="#2980B9", cursor="hand2")
generate_button.pack(pady=10)

result_label = tk.Label(app, text="", font=result_font, bg="#2C3E50", fg="#E74C3C")
result_label.pack(pady=10)

copy_button = tk.Button(app, text="Copy to Clipboard", font=label_font, command=copy_to_clipboard, bg="#27AE60", fg="white", activebackground="#229954", cursor="hand2")
copy_button.pack(pady=10)

# Run the application
app.mainloop()
