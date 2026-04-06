import tkinter as tk
from tkinter import messagebox
import speech_recognition as sr


# ------------------ CORE LOGIC ------------------#

history = []

def evaluate_expression(expr):
    try:
        result = eval(expr)
        history.append(F"{expr} = {result}")
        update_history()
        return result
    except:
        return "Error"
    

#---------GUI Functions-------------#
def click(value):
    entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)

def calculate():
    expr = entry.get()
    result = evaluate_expression(expr)
    entry.delete(0, tk.END)
    entry.insert(0, str(result))


#-------------- History Panel -------------#
def update_history():
    history_box.delete(0, tk.END)
    for item in history:
        history_box.insert(tk.END, item)


#--------------- Keyboard Support ------------#
def key_input(event):
     key = event.char

     #check if key is a digit or operator
     if key in "0123456789+-*/().":
         entry.insert(tk.END, key)

    elif key == "\r": # Enter key
        calculate()

    elif key == "x08": #Backspace
        current = entry.get()
        entry.delete(0, tk.END)
        entry.insert(0, current[:-1])


#-------------AI Command----------#
def ai_calculate():
    text = entry.get().lower()

    try
        text = text.replace("plus", "+") \
        .replace("minus", "-") \
        .replace("multiply","*") \
        .replace("times","*") \
        .replace("devide","/") \
        .replace("over","/") \
        .replace("open paranthesis") \
        .replace("close paranthesis")

        result = evaluate_expression(text)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))

    except:
        entry.insert(0, "Ai Error")


#--------------Voice Input-----------------#
def voice_input():
    recognizer = sr.Recognizer()

    # Use the default microphone as the audio source
    with sr.Microphone() as source:
          messagebox.showinfo("Voice", "Speak now...")
          audio = recognizer.listen(source)
          
    try:
        text = recognizer.recognize_google(audio)
        entry.delete(0, tk.END)
        entry.insert(0, text)

    except:
         messagebox.showerror("Error","Could not understand audio")


#----------------GUI Setup--------------------#
root=tk.Tk()
root.title("Desktop Calculator Ai Pro")
root.geometry("400x500")
root.configure(bg="#1e1e1e")

entry = tk.Entry(root, font=("Arial", 20), bg="#333", fg="#fff", )
entry.pack(fill="both", padx=10, pady=10)

#Buttons Frame
frame = tk.Frame(root, bg="1e1e1e")
frame.pack()

buttons = [
    '7', '8', '9', '/',
    '4','5','6','*',
    '1','2','3','-',
    '0','%','=','+'
]

row = 0
col = 0

for btn in buttons:
     action = lambda x=btn: click(x) if x != "=" else calculate()
     tk.button(frame, text=btn, width=5, height=2,
               
               )