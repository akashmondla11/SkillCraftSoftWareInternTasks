# Task 1 : create a program that convert temperature's between celsius,fahrenhite & Kelvin
# (code written by Akash Mondal)
import tkinter as tk
from tkinter import messagebox, StringVar
class ConvertTemperature:
    def __init__(self, root):
        self.root = root
        self.root.title("Convert Temperature projrct[By Akash Mondal] ")
        self.root.geometry("500x270")
        self.root.configure(bg='#4d7c44')  
 # A frame for makng the program easy to build 
        frame = tk.Frame(root, bg='#4d7c44')
        frame.pack(pady=17)
 # Input from the user to convert the data 
        tk.Label(frame, text="Enter Temperature:", font=("Leelawadee UI Semilight", 14), bg='#4d7c44').grid(row=0, column=0, padx=10, pady=10)
        self.tempentry = tk.Entry(frame, font=("Leelawadee UI Semilight", 14), width=10, bg='#a7e6a3')
        self.tempentry.grid(row=0, column=1, padx=10, pady=10)
# i had Changed the cursor to text selection when it enterd the input box
        self.tempentry.config(cursor="xterm")
        self.tempentry.bind("<Return>", lambda event: self.convertedValue())
# i add a select menu auction for convert input data 
        self.ver = StringVar(value="Celsius")  
#  i Set Celsius to default
        self.menu = tk.OptionMenu(frame, self.ver, "Celsius", "Fahrenheit", "Kelvin")
# remove border of the select box
        self.menu.config(font=("Leelawadee UI Semilight", 14), width=10, bg='#006400', fg='white', cursor='hand2', 
                         highlightthickness=0)  
        self.menu.grid(row=0, column=2, padx=10, pady=10)
# i create a Convert button to convert the data
        convert_button = tk.Button(frame, text="Convert", command=self.convertedValue, font=("Leelawadee UI Semilight", 12), width=20, bg='green', fg='white', cursor='hand2')
        convert_button.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
 # Result displays next line of the convert button
        self.result_box1 = tk.Label(frame, text="", font=("Leelawadee UI Semilight", 14), width=20, bg='#4d7c44', fg='white')
        self.result_box2 = tk.Label(frame, text="", font=("Leelawadee UI Semilight", 14), width=20, bg='#4d7c44', fg='white')
# make result_boxes into the center
        self.result_box1.grid(row=2, column=0, columnspan=3, padx=10, pady=10)
        self.result_box2.grid(row=3, column=0, columnspan=3, padx=10, pady=10)
    def convertedValue(self):
        try:
 # i get temperature input from the user 
            temp = float(self.tempentry.get())
            scale = self.ver.get()
# reset both result (box 1 and box 2)
            self.result_box1.config(text="")
            self.result_box2.config(text="")
            if scale == "Celsius":
                fahrenheit = (temp * 9/5) + 32
                kelvin = temp + 273.15
                self.result_box1.config(text=f"{fahrenheit:.2f} °F")
                self.result_box2.config(text=f"{kelvin:.2f} K")  
            elif scale == "Fahrenheit":
                celsius = (temp - 32) * 5/9
                kelvin = (temp + 459.67) * 5/9
                self.result_box1.config(text=f"{celsius:.2f} °C")
                self.result_box2.config(text=f"{kelvin:.2f} K") 
            elif scale == "Kelvin":
                celsius = temp - 273.15
                fahrenheit = (temp - 273.15) * 9/5 + 32
                self.result_box1.config(text=f"{celsius:.2f} °C")
                self.result_box2.config(text=f"{fahrenheit:.2f} °F")
        except ValueError:
            messagebox.showerror("Error", "Invalid input Pliz try again")
if __name__ == "__main__":
    root = tk.Tk()
    converter = ConvertTemperature(root)
    root.mainloop()
