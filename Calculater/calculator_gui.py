#Create a simple Desktop Calculator Application
import tkinter as tk

root = tk.Tk()
root.title("Smart Calculator")
root.geometry("300x400")
root.mainloop()

#Add Display
entry = tk.Entry(root, width=20 , font=("Arial", 18), borderwidth=5, justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


#Button Click Function
def click_button(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)

    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

buttons = [
    
]
    