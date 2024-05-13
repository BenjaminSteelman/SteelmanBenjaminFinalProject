# -*- coding: utf-8 -*-
"""
Filename: SteelmanBenjamin_Tkinter.py 
Author: Benjamin Steelman
DLM: May 12th, 2024
This program includes the GUI for the program, as well as the actual binary program itself.
"""

import functions
from functions import Conversion_from_Base_Ten
from functions import Conversion_to_Base_Ten
from functions import Conversion_from_any_Base_to_Another
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk

# Imports essential goods

# define our MainWindow class
class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.resizable(width=False, height=False)
        self.number = tk.StringVar()
        self.root.title("Main")
        self.root.geometry("200x220")
        # Sets up root and main window
        image = Image.open("convert.JPG")
        image = image.resize((200, 220), Image.Resampling.LANCZOS)
        self.photo = ImageTk.PhotoImage(image)
        self.background_label = tk.Label(self.root, image=self.photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        # Gets the background image
        OPTIONS = [
        "Base 2(Binary)","Base 3","Base 4","Base 5","Base 6","Base 7","Base 8(Octal)","Base 9","Base 10(Decimal)","Base 11","Base 12", "Base 14","Base 15", "Base 16(Hexadecimal)"
        ] 
        check = ttk.Frame(self.root)
        check.pack(pady=10, fill='x')
        inputtedNumber = ttk.Label(check, text="Number to be converted:")
        inputtedNumber.pack(fill='x')
        inputtedNumber = ttk.Entry(check, textvariable=self.number)
        inputtedNumber.pack(fill='x')
        inputtedNumber.focus()
        # Gets the input
        self.variableOne = StringVar(self.root)
        self.variableTwo = StringVar(self.root)
        self.variableOne.set(OPTIONS[0]) 
        self.variableTwo.set(OPTIONS[0])
        self.first = OptionMenu(self.root, self.variableOne, *OPTIONS)
        self.first.pack()
        self.second = OptionMenu(self.root, self.variableTwo, *OPTIONS)
        self.second.pack()
        self.convertButton = tk.Button(self.root, text="Convert", command=self.open_second_window)
        self.exitButton = tk.Button(self.root, text="Exit", command=self.Close)
        self.convertButton.pack(pady=10)
        self.exitButton.pack(pady=10)
        self.root.mainloop()
        
    def run(self):
            self.root.mainloop()

    def open_second_window(self):
        firstBase = self.variableOne.get()
        if firstBase == "Base 2(Binary)":
            firstBase = 2
        elif firstBase == "Base 3":
            firstBase= 3
        elif firstBase == "Base 4":
            firstBase= 4
        elif firstBase == "Base 5":
            firstBase= 5
        elif firstBase == "Base 6":
            firstBase= 6
        elif firstBase == "Base 7":
            firstBase= 7
        elif firstBase == "Base 8(Octal)":
            firstBase= 8
        elif firstBase == "Base 9":
            firstBase= 9
        elif firstBase == "Base 10(Decimal)":
            firstBase= 10
        elif firstBase == "Base 11":
            firstBase= 11
        elif firstBase == "Base 12":
            firstBase= 12
        elif firstBase == "Base 13":
            firstBase= 13
        elif firstBase == "Base 14":
            firstBase= 14
        elif firstBase == "Base 15":
            firstBase= 15
        else:
            firstBase = 16
            # Gets the first base and decides what it is
        secondBase = self.variableTwo.get()
        if secondBase == "Base 2(Binary)":
            secondBase = 2
            numberImage = "two.JPG"
        elif secondBase == "Base 3":
            secondBase= 3
            numberImage = "three.JPG"
        elif secondBase == "Base 4":
            secondBase= 4
            numberImage = "four.JPG"
        elif secondBase == "Base 5":
            secondBase= 5
            numberImage = "five.JPG"
        elif secondBase == "Base 6":
            secondBase= 6
            numberImage = "six.JPG"
        elif secondBase == "Base 7":
            secondBase= 7
            numberImage = "seven.JPG"
        elif secondBase == "Base 8(Octal)":
            secondBase= 8
            numberImage = "eight.JPG"
        elif secondBase == "Base 9":
            secondBase= 9
            numberImage = "nine.JPG"
        elif secondBase == "Base 10(Decimal)":
            secondBase= 10
            numberImage = "ten.JPG"
        elif secondBase == "Base 11":
            secondBase= 11
            numberImage = "eleven.JPG"
        elif secondBase == "Base 12":
            secondBase= 12
            numberImage = "twelve.JPG"
        elif secondBase == "Base 13":
            secondBase == 13
            numberImage = "thirteen.JPG"
        elif secondBase == "Base 14":
            secondBase= 14
            numberImage = "fourteen.JPG"
        elif secondBase == "Base 15":
            secondBase= 15
            numberImage = "fifteen.JPG"
        else:
            secondBase = 16
            numberImage = "sixteen.JPG"
            # Gets the second base and decides what it is
        number = str(self.number.get())
        convert = functions.Conversion_from_any_Base_to_Another(Conversion_from_Base_Ten, Conversion_to_Base_Ten, number, firstBase, secondBase, 0)
        if convert == 'Invalid' or firstBase == secondBase:
            self.third_window = ThirdWindow(self.root, self)
        else:
            self.second_window = SecondWindow(self.root, self, numberImage, convert)
            # Opens up the second window, or the error window
        
    def Close(self):
        self.root.destroy()
        # Exit button function
class SecondWindow:
    def __init__(self, master, main_window, numberImage, convert):
        self.master = master
        self.main_window = main_window
        self.top = tk.Toplevel(self.master)
        self.top.title("Second Window")
        self.top.geometry("300x215")
        self.label = tk.Label(self.top, text=convert)
        self.label.pack(pady=10)
        outputImage = Image.open(numberImage)
        outputImage = outputImage.resize((300, 200), Image.Resampling.LANCZOS)
        self.photo = ImageTk.PhotoImage(outputImage)
        self.background_label = tk.Label(self.top, image=self.photo)
        self.background_label.place(x=0, y=30, relwidth=1, relheight=1)
        # Includes the converted number and a background image with the type
class ThirdWindow:
    def __init__(self, master, main_window):
        self.master = master
        self.main_window = main_window
        self.top = tk.Toplevel(self.master)
        self.top.title("Third Window")
        self.top.geometry("400x40")
        self.topLabel = tk.Label(self.top, text="Your input was invalid, or you tried to convert to the same base.") 
        self.bottomLabel = tk.Label(self.top, text="Please try again in accordance with the User Manual.")
        self.topLabel.pack(pady=1)
        self.bottomLabel.pack(pady=1)
        # Error message
        
if __name__ == '__main__':
    main_window = MainWindow()
    main_window.run()
# Main window