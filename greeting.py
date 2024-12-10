import tkinter as tk

def greet_user():
    name = name_entry.get()
    if name.strip():
        greeting_label.config(text=f"Hello, {name}!")
    else:
        greeting_label.config(text="Please enter your name.")

root = tk.Tk()
root.title("Greeting App")
root.geometry("400x300")

instructions_label = tk.Label(root, text="Enter your name below:", font=("Arial", 14))
instructions_label.pack(pady=10)

name_entry = tk.Entry(root, font=("Arial", 14))
name_entry.pack(pady=5)

greet_button = tk.Button(root, text="Greet Me", command=greet_user, font=("Arial", 12))
greet_button.pack(pady=5)

reset_button = tk.Button(root, text="Reset", command=reset, font=("Arial", 12), bg="gray")
reset_button.pack(padx=5)

greeting_label = tk.Label(root, text="", font=("Arial", 14), fg="blue")
greeting_label.pack(pady=10)

root.mainloop()