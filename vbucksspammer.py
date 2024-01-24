import pyperclip
# import everything from tkinter module 
from tkinter import *
import random
digits = ['1','2','3','4','5','6','7','8','9','0','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

# import messagebox from tkinter module 
import tkinter.messagebox 

# create a tkinter root window 
root = tkinter.Tk() 

# root window title and dimension 
root.title("VBUCKS") 
root.geometry('100x50') 
counter = 0
# Create a messagebox showinfo 
def onClick():
    code = []
    for x in range(0, 19):
        y = random.randint(0, 35)
        if len(code) == 4 or len(code) == 9 or len(code) == 14:
            code.append('-')
        else:
            code.append(digits[y])
    codefull = ''.join(code)
    pyperclip.copy(codefull)
    print(counter)
    counter = counter + 1

    

# Create a Button 
button = Button(root, text="VBUCKS", command=onClick, height=50, width=100) 

# Set the position of button on the top of window. 
button.pack(side='bottom') 
root.mainloop() 

