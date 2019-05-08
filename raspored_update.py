import tkinter
from tkinter import *
import random
from datetime import datetime


colors = ["PaleTurquoise4", "CadetBlue1", "medium spring green", "green yellow", "lime green",
          "violet", "silver", "lightblue", "snow", "pale violet red", "maroon"]
dani = ["Ponedeljak", "Utorak", "Sreda", "Cetvrtak", "Petak"]

def upisipredmet():
    dodaj.configure(bg=random.choice(colors))
    obrisi.configure(bg="gray95")
    predmet = predmet1.get()
    predmet1.delete(0, 30)
    #  danunedelji = dan1.get()
    # dan1.delete(0, 30)

    #  danunedelji= ovde mora da se napise koji je dan izaran iz skupa
    if danunedelji == 'Ponedeljak':
        i = 6
    elif danunedelji == 'Utorak':
        i = 7
    elif danunedelji == 'Sreda':
        i = 8
    elif danunedelji == 'Cetvrtak':
        i = 9
    else:
        i = 10

    vremepocetkacasa = int(vrp1.get())
    vrp1.delete(0, 10)
    vremetrajanjacasa = int(vrt1.get())
    vrt1.delete(0, 10)

    j = vremepocetkacasa - 7

    while vremetrajanjacasa > 0:
        if j <= 13:
            l = Label(text=predmet, relief=RIDGE, bg="lightblue")
            l.grid(row=i, column=j, sticky=NSEW)

        vremetrajanjacasa = vremetrajanjacasa - 1
        j = j + 1

def obrisipredmet():
    obrisi.configure(bg=random.choice(colors))
    dodaj.configure(bg="gray95")
    predmet = predmet1.get()
    predmet1.delete(0, 30)
    # danunedelji = dan1.get()
    # dan1.delete(0, 30)

    # danunedelji= ovde mora da se napise koji je dan izaran iz skupa
    if danunedelji == 'Ponedeljak':
        i = 6
    elif danunedelji == 'Utorak':
        i = 7
    elif danunedelji == 'Sreda':
        i = 8
    elif danunedelji == 'Cetvrtak':
        i = 9
    else:
        i = 10

    vremepocetkacasa = int(vrp1.get())
    vrp1.delete(0, 10)
    vremetrajanjacasa = int(vrt1.get())
    vrt1.delete(0, 10)

    j = vremepocetkacasa - 7

    while vremetrajanjacasa > 0:
        l = Label(text=" ", relief=RIDGE,  bg="gray95")
        l.grid(row=i, column=j, sticky=NSEW)

        vremetrajanjacasa = vremetrajanjacasa - 1
        j = j + 1

window = Tk()
window.title("Interactive schedule")
window.geometry("1100x300")


###  OKVIR ###

### DANI ###

predmet = Label(window, text= "Ime predmeta")
predmet.grid(column=0, row=0)

predmet1 = Entry(window, width=11)
predmet1.grid(column=1, row=0)


#dan = Label(window, text= "Dan u nedelji")
#dan.grid(column=0, row=1)

#dan1 = Entry(window, width=11)
#dan1.grid(column=1, row=1)


vrp = Label(window, text= "Vreme pocetka casa")
vrp.grid(column=0, row=2)

vrp1 = Entry(window, width=11)
vrp1.grid(column=1, row=2)

vrt = Label(window, text="Vreme trajanja casa")
vrt.grid(column=0, row=3)

vrt1 = Entry(window, width=11)
vrt1.grid(column=1, row=3)

for i in range(6,11):
    for j in range(1,14):
        l = Label(text=" ", relief=RIDGE)
        l.grid(row=i, column=j, sticky=NSEW)

dv = Label(text="Dan \ Vreme", heigh=1, width=10, relief=RIDGE )
dv.grid(column=0, row=5)

pon = Label(text="Ponedeljak ", bg="silver", heigh=1, width=10, relief=RIDGE)
pon.grid(column=0, row=6)

ut = Label(text="Utorak ", bg="silver", heigh=1, width=10, relief=RIDGE)
ut.grid(column=0, row=7)

sreda = Label(text="Sreda ", bg="silver", heigh=1, width=10, relief=RIDGE)
sreda.grid(column=0, row=8)

cet = Label(text="Cetvrtak ", bg="silver",
                heigh=1, width=10, relief=RIDGE)
cet.grid(column=0, row=9)

petak = Label(text="Petak ", bg="silver",
                  heigh=1, width=10, relief=RIDGE)
petak.grid(column=0, row=10)

label1 = Label(text="08:00 - 09:00", bg="lightgreen", relief=RIDGE)
label1.grid(column=1, row=5)

label2 = Label(text="09:00 - 10:00", bg="lightgreen", relief=RIDGE)
label2.grid(column=2, row=5)

label3 = Label(text="10:00 - 11:00", bg="lightgreen", relief=RIDGE)
label3.grid(column=3, row=5)

label4 = Label(text="11:00 - 12:00", bg="lightgreen", relief=RIDGE)
label4.grid(column=4, row=5)

label5 = Label(text="12:00 - 13:00", bg="lightgreen", relief=RIDGE)
label5.grid(column=5, row=5)

label6 = Label(text="13:00 - 14:00", bg="lightgreen", relief=RIDGE)
label6.grid(column=6, row=5)

label7 = Label(text="14:00 - 15:00", bg="lightgreen", relief=RIDGE)
label7.grid(column=7, row=5)

label8 = Label(text="15:00 - 16:00", bg="lightgreen", relief=RIDGE)
label8.grid(column=8, row=5)

label9 = Label(text="16:00 - 17:00", bg="lightgreen", relief=RIDGE)
label9.grid(column=9, row=5)

label10 = Label(text="17:00 - 18:00", bg="lightgreen", relief=RIDGE)
label10.grid(column=10, row=5)

label11 = Label(text="18:00 - 19:00", bg="lightgreen", relief=RIDGE)
label11.grid(column=11, row=5)

label12 = Label(text="19:00 - 20:00", bg="lightgreen", relief=RIDGE)
label12.grid(column=12, row=5)

label13 = Label(text="20:00 - 21:00", bg="lightgreen", relief=RIDGE)
label13.grid(column=13, row=5)


dodaj = Button(window, text="Upisi", command=upisipredmet)
dodaj.grid(column=4, row = 2, sticky = NSEW)

obrisi = Button(window, text="Obrisi", command=obrisipredmet)
obrisi.grid(column=5,row=2, sticky = NSEW)

vreme = datetime.now().strftime('%H:%M:%S')
labela_vreme = Label(text=vreme, width=9, relief=RIDGE)
labela_vreme.grid(column=12, row=0)

datum = datetime.now().strftime('%d-%m-%Y')
labela_datum = Label(text=datum, width=9, relief=RIDGE)
labela_datum.grid(column=11, row=0)

pom = StringVar(window)
pom.set(dani[0]) # default value

om = OptionMenu(window, pom, *dani)
om.grid(column=0, row=1)





window.mainloop()
