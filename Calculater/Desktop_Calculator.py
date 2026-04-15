import tkinter as tk
from tkinter import messagebox
import speech_recognition as sr

# ------------------ CORE LOGIC ------------------

history = []

def evaluate_expression(expr):
    try:
        result = eval(expr)
        history.append(f"{expr} = {result}")
        update_history()
        return result
    except:
        return "Error"

# ------------------ GUI FUNCTIONS ------------------

def click(value):
    entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)

def calculate():
    expr = entry.get()
    result = evaluate_expression(expr)
    entry.delete(0, tk.END)
    entry.insert(0, result)

# ------------------ HISTORY PANEL ------------------

def update_history():
    history_box.delete(0, tk.END)
    for item in history:
        history_box.insert(tk.END, item)

# ------------------ KEYBOARD SUPPORT ------------------

def key_input(event):
    key = event.char

    if key in "0123456789+-*/%":
        entry.insert(tk.END, key)

    elif key == "\r":  # Enter key
        calculate()

    elif key == "\x08":  # Backspace
        current = entry.get()
        entry.delete(0, tk.END)
        entry.insert(0, current[:-1])

# ------------------ AI COMMAND ------------------

def ai_calculate():
    text = entry.get().lower()

    try:
        text = text.replace("plus", "+") \
                   .replace("minus", "-") \
                   .replace("multiply", "*") \
                   .replace("times", "*") \
                   .replace("divide", "/")

        result = evaluate_expression(text)
        entry.delete(0, tk.END)
        entry.insert(0, result)

    except:
        entry.insert(0, "AI Error")

# ------------------ VOICE INPUT ------------------
def voice_input():
    recognizer = sr.Recognizer()

    try :
        #Get Available Microphones


# ------------------ GUI SETUP ------------------

root = tk.Tk()
root.title("🔥 Smart Calculator AI Pro")
root.geometry("500x500")
root.configure(bg="#1e1e1e")

entry = tk.Entry(root, font=("Arial", 20), bg="#2d2d2d", fg="white", insertbackground="white")
entry.pack(fill="both", padx=10, pady=10)

# Buttons Frame
frame = tk.Frame(root, bg="#1e1e1e")
frame.pack()

buttons = [
    '7','8','9','/',
    '4','5','6','*',
    '1','2','3','-',
    '0','%','=','+'
]

row = 0
col = 0

for btn in buttons:
    action = lambda x=btn: click(x) if x != "=" else calculate()
    tk.Button(frame, text=btn, width=5, height=2,
              bg="#3a3a3a", fg="white",
              command=action).grid(row=row, column=col, padx=5, pady=5)

    col += 1
    if col > 3:
        col = 0
        row += 1

# Special Buttons
tk.Button(root, text="Clear", bg="red", fg="white", command=clear).pack(fill="x")
tk.Button(root, text="AI Calculate", bg="blue", fg="white", command=ai_calculate).pack(fill="x")
tk.Button(root, text="🎤 Voice Input", bg="green", fg="white", command=voice_input).pack(fill="x")

# History Panel
history_box = tk.Listbox(root, bg="#2d2d2d", fg="white")
history_box.pack(fill="both", expand=True, padx=10, pady=10)

# Keyboard Binding
root.bind("<Key>", key_input)

root.mainloop()