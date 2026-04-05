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
 
    