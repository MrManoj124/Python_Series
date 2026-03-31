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
    