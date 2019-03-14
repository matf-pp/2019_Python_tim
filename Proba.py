from tkinter import *

def click():
    entered_text=textentry.get()

## main

window=Tk()
window.title("Nov gui")

Label(window, text="Unesite neki tekst:").grid(row=0, column=1)
textentry=Entry(window, width=20, bg="white")
textentry.grid(row=0, column=2, sticky=W)
Button(window, text="SUBMIT", width=6, command=click).grid(column=3, row=0, sticky=W)




window.mainloop()