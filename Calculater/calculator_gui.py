#Create a simple Desktop Calculator Application
import tkinter as tk

root = tk.Tk()
root.title("Smart Calculator")
root.geometry("300x400")
root.mainloop()

entry = tk.Entry(root, width=20 , font=("Arial", 18), borderwidth=5, justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)