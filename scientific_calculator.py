import math

from tkinter import *

root = Tk()

root.title("Scientific Calculator")
root.geometry("330x550")
root.resizable(False, False)
root.configure(bg="#f0f0f0")
root.configure(bg="#1e1e1e")
display = Entry(root, font=("Arial", 30), justify="right", bg="#2d2d2d", fg="white", insertbackground="white", bd=10)
display.pack(fill="both", padx=10, pady=10)
def click(number):
    current = display.get()
    display.delete(0, END)
    display.insert(0, str(current) + str(number))
def clear():
    display.delete(0, END)
def calculate():
    try:
        result = eval(display.get())
        display.delete(0, END)
        display.insert(0, result)

    except:
        display.delete(0, END)
        display.insert(0, "Error")
def backspace():
    current = display.get()
    display.delete(0, END)
    display.insert(0, current[:-1])
def square():
    try:
        number = float(display.get())
        result = number ** 2
        display.delete(0, END)
        display.insert(0, result)
    except:
        display.delete(0, END)
        display.insert(0, "Error")

    display.delete(0, END)
    display.insert(0, result)
def square_root():
    try:
        number = float(display.get())
        result = math.sqrt(number)
        display.delete(0, END)
        display.insert(0, result)
    except:
        display.delete(0, END)
        display.insert(0, "Error")
    
def sin_function():
    try:
        number = float(display.get())
        result = math.sin(math.radians(number))

        display.delete(0, END)
        display.insert(0, result)

    except:
        display.delete(0, END)
        display.insert(0, "Error")

def cos_function():
    try:
        number = float(display.get())
        result = math.cos(math.radians(number))

        display.delete(0, END)
        display.insert(0, result)

    except:
        display.delete(0, END)
        display.insert(0, "Error")

def tan_function():
    try:
        number = float(display.get())
        result = math.tan(math.radians(number))

        display.delete(0, END)
        display.insert(0, result)

    except:
        display.delete(0, END)
        display.insert(0, "Error")
    display.delete(0, END)
    display.insert(0, result)

def tan_function():
    try:
        number = float(display.get())
        result = math.tan(math.radians(number))

        display.delete(0, END)
        display.insert(0, result)

    except:
        display.delete(0, END)
        display.insert(0, "Error")
def pi_value():
    display.delete(0, END)
    display.insert(0, math.pi)
def log_function():
    try:
        number = float(display.get())
        result = math.log10(number)

        display.delete(0, END)
        display.insert(0, result)

    except:
        display.delete(0, END)
        display.insert(0, "Error")
def factorial_function():
    try:
        number = int(display.get())
        result = math.factorial(number)

        display.delete(0, END)
        display.insert(0, result)

    except:
        display.delete(0, END)
        display.insert(0, "Error")
def e_value():
    click(str(math.e))
def key_press(event):
    key = event.keysym

    if key in "0123456789":
        click(key)

    elif key in ["plus"]:
        click("+")

    elif key in ["minus"]:
        click("-")

    elif key in ["asterisk"]:
        click("*")

    elif key in ["slash"]:
        click("/")

    elif key == "period":
        click(".")

    elif key == "Return":
        calculate()

    elif key == "BackSpace":
        backspace()

    elif key == "Escape":
        clear()
root.bind("<Key>", key_press)
frame = Frame(root, bg="#1e1e1e")
frame.pack(pady=15)
Button(frame, text="7", width=8, height=3,
       command=lambda: click(7)).grid(row=3, column=0, padx=2, pady=2)

Button(frame, text="8", width=8, height=3,
       command=lambda: click(8)).grid(row=3, column=1, padx=2, pady=2)

Button(frame, text="9", width=8, height=3,
       command=lambda: click(9)).grid(row=3, column=2, padx=2, pady=2)
Button(frame, text="4", width=8, height=3,
       command=lambda: click(4)).grid(row=4, column=0, padx=2, pady=2)

Button(frame, text="5", width=8, height=3,
       command=lambda: click(5)).grid(row=4, column=1, padx=2, pady=2)

Button(frame, text="6", width=8, height=3,
       command=lambda: click(6)).grid(row=4, column=2, padx=2, pady=2)

Button(frame, text="1", width=8, height=3,
       command=lambda: click(1)).grid(row=5, column=0, padx=2, pady=2)

Button(frame, text="2", width=8, height=3,
       command=lambda: click(2)).grid(row=5, column=1, padx=2, pady=2)

Button(frame, text="3", width=8, height=3,
       command=lambda: click(3)).grid(row=5, column=2, padx=2, pady=2)

Button(frame, text="0", width=8, height=3,
       command=lambda: click(0)).grid(row=6, column=1, padx=2, pady=2)

Button(frame, text="AC", bg="#e74c3c", fg="white", width=8, height=3,
       command=clear).grid(row=2, column=0, padx=2, pady=2)

Button(frame, text="+", bg="#ff9500", fg="white", width=8, height=3,
       command=lambda: click("+")).grid(row=5, column=3, padx=2, pady=2)

Button(frame, text="-", bg="#ff9500", fg="white", width=8, height=3,
       command=lambda: click("-")).grid(row=4, column=3, padx=2, pady=2)

Button(frame, text="*", bg="#ff9500", fg="white", width=8, height=3,
       command=lambda: click("*")).grid(row=3, column=3, padx=2, pady=2)

Button(frame, text="/", bg="#ff9500", fg="white", width=8, height=3,
       command=lambda: click("/")).grid(row=2, column=3, padx=2, pady=2)

Button(frame, text="=", bg="#2ecc71", fg="white", width=8, height=3,
       command=calculate).grid(row=6, column=3, padx=2, pady=2)

Button(frame, text="⌫", bg="#bdc3c7", fg="black", width=8, height=3,
       command=backspace).grid(row=2, column=1)

Button(frame, text="%", bg="#3498db", fg="white", width=8, height=3,
       command=lambda: click("%")).grid(row=2, column=2)

Button(frame, text="x²", bg="#3498db", fg="white", width=8, height=3,
       command=square).grid(row=1, column=0)

Button(frame, text="√", bg="#3498db", fg="white", width=8, height=3,
       command=square_root).grid(row=1, column=3)

Button(frame, text="Sin", bg="#3498db", fg="white", width=8, height=3,
       command=sin_function).grid(row=0, column=0)

Button(frame, text="Cos", bg="#3498db", fg="white", width=8, height=3,
       command=cos_function).grid(row=0, column=1)

Button(frame, text="Tan", bg="#3498db", fg="white", width=8, height=3,
       command=tan_function).grid(row=0, column=2)

Button(frame, text="π", bg="#3498db", fg="white", width=8, height=3,
       command=pi_value).grid(row=0, column=3)

Button(frame, text="Log", bg="#3498db", fg="white", width=8, height=3,
       command=log_function).grid(row=1, column=1)

Button(frame, text="!", bg="#3498db", fg="white", width=8, height=3,
       command=factorial_function).grid(row=1, column=2)

Button(frame, text="e", width=8, height=3,
       command=e_value).grid(row=6, column=0)

Button(frame, text=".", width=8, height=3,
       command=lambda: click(".")).grid(row=6, column=2)

root.mainloop()