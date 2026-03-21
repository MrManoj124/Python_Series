#Create a simple Desktop Calculator Application
import tkinter as tk

root = tk.Tk()
root.title("Smart Calculator")
root.geometry("300x400")
root.mainloop()

entry = tk.Entry(root, width=20 , font=("Arial", 18), borderwidth=5, justify="right")
