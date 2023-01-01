# simple converter, using a tkinter interface

import tkinter as tk
from tkinter import messagebox

def convertTemperature():
    celsius = temp_celsius.get()
    clear_text()
    print(type(celsius))
    while True:
        if celsius.isdigit():
            celsius = int(celsius)
            Fahrenheit = celsius * 1.80 + 32.00 
            Kelvin = celsius + 273.15
            temp_fahrenheit.insert(0, Fahrenheit)
            temp_kelvin.insert(0, Kelvin)
            break
        elif celsius.isalpha() or celsius.isspace() or celsius == "":
            messagebox.showerror(title=None, message="Please insert a numeric value")
            break
        else:
            celsius = float(celsius.replace(",","."))
            Fahrenheit = celsius * 1.80 + 32.00 
            Kelvin = celsius + 273.15
            temp_fahrenheit.insert(0, Fahrenheit)
            temp_kelvin.insert(0, Kelvin)
            break


def clear_text():
    temp_fahrenheit.delete(0, "end")
    temp_kelvin.delete(0, "end")


master = tk.Tk()

master.title("temperature converter")
master.maxsize(400, 100)
master.eval("tk::PlaceWindow . center")

tk.Label(master, text="Type the desired temperature in the 'Celsius' field").grid(row=0, column=0, columnspan="3")
tk.Label(master, text="Celsius", fg="red").grid(row=1, column=0)
tk.Label(master, text="Fahrenheit").grid(row=1, column=1)
tk.Label(master, text="Kelvin").grid(row=1, column=2)
tk.Button(master, text="Calcular", command=convertTemperature).grid(row=3, column=1, pady="10")

temp_celsius = tk.Entry(master)
temp_fahrenheit = tk.Entry(master)
temp_kelvin = tk.Entry(master)

temp_celsius.grid(row=2, column=0, padx=5)
temp_fahrenheit.grid(row=2, column=1, padx=5)
temp_kelvin.grid(row=2, column=2, padx=5)  

master.mainloop()
