import tkinter
from tkinter import *

window = Tk()
window.title("Raspored")
window.geometry("1100x200")

###  OKVIR ###

for i in range(6):
    for j in range(15):
        l = Label(text=" ", relief=RIDGE)
        l.grid(row=i, column=j, sticky=NSEW)

### DANI ###

dv = Label(window, text="Dan \ Vreme")
dv.grid(column=0, row=0)

pon = Label(window, text="Ponedeljak ", bg="silver",
            heigh=1, width=10, relief=RIDGE)
pon.grid(column=0, row=1)

ut = Label(window, text="Utorak ", bg="silver",
           heigh=1, width=10, relief=RIDGE)
ut.grid(column=0, row=2)

sreda = Label(window, text="Sreda ", bg="silver",
              heigh=1, width=10, relief=RIDGE)
sreda.grid(column=0, row=3)

cet = Label(window, text="Cetvrtak ", bg="silver",
            heigh=1, width=10, relief=RIDGE)
cet.grid(column=0, row=4)

petak = Label(window, text="Petak ", bg="silver",
              heigh=1, width=10, relief=RIDGE)
petak.grid(column=0, row=5)

### SATI ###

label1 = Label(window, text="08:00 - 09:00", relief=RIDGE)
label1.grid(column=1, row=0)

label2 = Label(window, text="09:00 - 10:00", relief=RIDGE)
label2.grid(column=2, row=0)

label3 = Label(window, text="10:00 - 11:00", relief=RIDGE)
label3.grid(column=3, row=0)

label4 = Label(window, text="11:00 - 12:00", relief=RIDGE)
label4.grid(column=4, row=0)

label5 = Label(window, text="12:00 - 13:00", relief=RIDGE)
label5.grid(column=5, row=0)

label6 = Label(window, text="13:00 - 14:00", relief=RIDGE)
label6.grid(column=6, row=0)

label7 = Label(window, text="14:00 - 15:00", relief=RIDGE)
label7.grid(column=7, row=0)

label8 = Label(window, text="15:00 - 16:00", relief=RIDGE)
label8.grid(column=8, row=0)

label9 = Label(window, text="16:00 - 17:00", relief=RIDGE)
label9.grid(column=9, row=0)

label10 = Label(window, text="17:00 - 18:00", relief=RIDGE)
label10.grid(column=10, row=0)

label11 = Label(window, text="18:00 - 19:00", relief=RIDGE)
label11.grid(column=11, row=0)

label12 = Label(window, text="19:00 - 20:00", relief=RIDGE)
label12.grid(column=12, row=0)

label13 = Label(window, text="20:00 - 21:00", relief=RIDGE)
label13.grid(column=13, row=0)

label14 = Label(window, text="21:00 - 22:00", relief=RIDGE)
label14.grid(column=14, row=0)

dugme = Button(window, text="Dodaj")
dugme.grid(column=4, row=6)

###             ###


window.mainloop()

# https://www.youtube.com/watch?v=JrWHyqonGj8
# https://www.youtube.com/watch?v=B9BRuhqEb2Q
# https://www.youtube.com/watch?v=RJB1Ek2Ko_Y
# https://www.youtube.com/watch?v=KEnDTjBMLhU
