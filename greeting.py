import tkinter as tk

root = tk.Tk()
root.title("Greeting App")
root.geometry("400x300")

instructions_label = tk.Label(root, text="Enter your name below:", font=("Arial", 14))
instructions_label.pack(pady=10)

name_entry = tk.Entry(root, font=("Arial", 14))
name_entry.pack(pady=5)

root.mainloop()