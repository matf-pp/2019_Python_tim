import tkinter
from tkinter import *

window = Tk()
window.title("Raspored")
window.geometry("600x200")


###  OKVIR ###

### DANI ###

predmet = Label(window, text= "Ime predmeta")
predmet.grid(column=0, row=0)

predmet1 = Entry(window)
predmet1.grid(column=1, row=0)


dan = Label(window, text= "Dan u nedelji")
dan.grid(column=0, row=1)

dan1 = Entry(window)
dan1.grid(column=1, row=1)


vrp = Label(window, text= "Vreme pocetka casa")
vrp.grid(column=0, row=2)

vrp1 = Entry(window)
vrp1.grid(column=1, row=2)


vrk = Label(window, text= "Vreme kraja casa")
vrk.grid(column=0, row=3)

vrk1 = Entry(window)
vrk1.grid(column=1, row=3)

dodaj = Button(window, text="Dodaj")
dodaj.grid(column=1, row = 4)


window.mainloop()
