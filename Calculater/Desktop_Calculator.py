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
    