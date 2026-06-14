import math
import tkinter as tk

calculation = ""

def add_to_calculation(value):
    global calculation
    calculation += str(value)
    text_result.delete(1.0, tk.END)
    text_result.insert(1.0, calculation)

def calculate_normal():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, tk.END)
        text_result.insert(1.0, calculation)
    except Exception as e:
        clear_calculation()
        text_result.insert(1.0, "Error")

def calculate_and_print_2dec():
    global calculation
    try:
        calculation = "{:.2f}".format(eval(calculation))
        text_result.delete(1.0, tk.END)
        text_result.insert(1.0, calculation)
    except Exception as e:
        clear_calculation()
        text_result.insert(1.0, "Error")

def calculate_and_print_floor():
    global calculation
    try:
        calculation = str(math.floor(float(eval(calculation))))
        text_result.delete(1.0, tk.END)
        text_result.insert(1.0, calculation)
    except Exception as e:
        clear_calculation()
        text_result.insert(1.0, "Error")

def calculate_and_print_ceil():
    global calculation
    try:
        calculation = str(math.ceil(float(eval(calculation))))
        text_result.delete(1.0, tk.END)
        text_result.insert(1.0, calculation)
    except Exception as e:
        clear_calculation()
        text_result.insert(1.0, "Error")

def clear_calculation():
    global calculation
    calculation = ""
    text_result.delete(1.0, tk.END)

def log_with_base(base, number):
    return math.log(number) / math.log(base)

root = tk.Tk()
root.geometry("360x420")
root.title("Calculator")

text_result = tk.Text(root, height=2, width=22, font=("Arial", 20))
text_result.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

equation_label = tk.StringVar()
label = tk.Label(root, textvariable=equation_label, font=("Arial", 14), bg="white", width=30, height=1)
label.grid(row=1, column=0, columnspan=4, pady=5)

button_1 = tk.Button(root, text="1", font=("Arial", 14), width=6, height=2, command=lambda: add_to_calculation(1))
button_1.grid(row=2, column=0)

button_2 = tk.Button(root, text="2", font=("Arial", 14), width=6, height=2, command=lambda: add_to_calculation(2))
button_2.grid(row=2, column=1)

button_3 = tk.Button(root, text="3", font=("Arial", 14), width=6, height=2, command=lambda: add_to_calculation(3))
button_3.grid(row=2, column=2)

button_plus = tk.Button(root, text="+", font=("Arial", 14), width=6, height=2, command=lambda: add_to_calculation("+"))
button_plus.grid(row=2, column=3)

button_4 = tk.Button(root, text="4", font=("Arial", 14), width=6, height=2, command=lambda: add_to_calculation(4))
button_4.grid(row=3, column=0)

button_5 = tk.Button(root, text="5", font=("Arial", 14), width=6, height=2, command=lambda: add_to_calculation(5))
button_5.grid(row=3, column=1)

button_6 = tk.Button(root, text="6", font=("Arial", 14), width=6, height=2, command=lambda: add_to_calculation(6))
button_6.grid(row=3, column=2)

button_minus = tk.Button(root, text="-", font=("Arial", 14), width=6, height=2, command=lambda: add_to_calculation("-"))
button_minus.grid(row=3, column=3)

button_7 = tk.Button(root, text="7", font=("Arial", 14), width=6, height=2, command=lambda: add_to_calculation(7))
button_7.grid(row=4, column=0)

button_8 = tk.Button(root, text="8", font=("Arial", 14), width=6, height=2, command=lambda: add_to_calculation(8))
button_8.grid(row=4, column=1)

button_9 = tk.Button(root, text="9", font=("Arial", 14), width=6, height=2, command=lambda: add_to_calculation(9))
button_9.grid(row=4, column=2)

button_multiply = tk.Button(root, text="*", font=("Arial", 14), width=6, height=2, command=lambda: add_to_calculation("*"))
button_multiply.grid(row=4, column=3)

button_clear = tk.Button(root, text="C", font=("Arial", 14), width=6, height=2, command=clear_calculation)
button_clear.grid(row=5, column=0)

button_0 = tk.Button(root, text="0", font=("Arial", 14), width=6, height=2, command=lambda: add_to_calculation(0))
button_0.grid(row=5, column=1)

button_equal = tk.Button(root, text="=", font=("Arial", 14), width=6, height=2, command=calculate_normal)
button_equal.grid(row=5, column=2)

button_divide = tk.Button(root, text="/", font=("Arial", 14), width=6, height=2, command=lambda: add_to_calculation("/"))
button_divide.grid(row=5, column=3)

button_2dec = tk.Button(root, text="2dec", font=("Arial", 14), width=6, height=2, command=calculate_and_print_2dec)
button_2dec.grid(row=6, column=0)

button_floor = tk.Button(root, text="floor", font=("Arial", 14), width=6, height=2, command=calculate_and_print_floor)
button_floor.grid(row=6, column=1)

button_ceil = tk.Button(root, text="ceil", font=("Arial", 14), width=6, height=2, command=calculate_and_print_ceil)
button_ceil.grid(row=6, column=2)

root.mainloop()