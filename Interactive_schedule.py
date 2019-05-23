import tkinter
from tkinter import *
import random
from datetime import datetime
import tkinter.messagebox
import xlwt
from xlwt import Workbook


colors = ["PaleTurquoise4", "CadetBlue1", "medium spring green", "green yellow", "lime green",
          "violet", "silver", "lightblue", "snow", "pale violet red", "maroon"]
dani = ["Ponedeljak", "Utorak", "Sreda", "Cetvrtak", "Petak", "Subota", "Nedelja"]


def exportuj():
    ime = ime_excel.get()
    sheet1 = wb.add_sheet('Sheet 1')

    sheet1.write(0, 0, "Dan\ vreme")
    sheet1.write(0, 1, "08:00 - 09:00")
    sheet1.write(0, 2, "09:00 - 10:00")
    sheet1.write(0, 3, "10:00 - 11:00")
    sheet1.write(0, 4, "11:00 - 12:00")
    sheet1.write(0, 5, "12:00 - 13:00")
    sheet1.write(0, 6, "13:00 - 14:00")
    sheet1.write(0, 7, "14:00 - 15:00")
    sheet1.write(0, 8, "15:00 - 16:00")
    sheet1.write(0, 9, "16:00 - 17:00")
    sheet1.write(0, 10, "17:00 - 18:00")
    sheet1.write(0, 11, "18:00 - 19:00")
    sheet1.write(0, 12, "19:00 - 20:00")
    sheet1.write(0, 13, "20:00 - 21:00")

    sheet1.write(1, 0, "Ponedeljak")
    sheet1.write(2, 0, "Utorak")
    sheet1.write(3, 0, "Sreda")
    sheet1.write(4, 0, "Cetvrtak")
    sheet1.write(5, 0, "Petak")
    sheet1.write(6, 0, "Subota")
    sheet1.write(7, 0, "Nedelja")

    for i in range(0, 7):
        for j in range(0, 14):
            sheet1.write(i + 1, j + 1, matrica[i][j])

    wb.save(ime + ".xls")


def dodaj_vikend():
    for i in range(11, 13):
        for j in range(1, 14):
            l = Label(text=" ", relief=RIDGE).grid(row=i, column=j, sticky=NSEW)

    subota.grid(column=0, row=11)
    nedelja.grid(column=0, row=12)


def ukloni_vikend():
    # for i in range(11, 13):
    #    l[i]=[" "]


    subota.grid_remove()
    nedelja.grid_remove()

def upisipredmet():
    dodaj.configure(bg=random.choice(colors))
    obrisi.configure(bg="gray95")
    predmet = predmet1.get()
    predmet1.delete(0, 30)
    danunedelji = pom.get()

    if danunedelji == 'Ponedeljak':
        i = 6
    elif danunedelji == 'Utorak':
        i = 7
    elif danunedelji == 'Sreda':
        i = 8
    elif danunedelji == 'Cetvrtak':
        i = 9
    elif danunedelji == 'Petak':
        i = 10
    elif danunedelji == 'Subota':
        i = 11
    else:
        i =12

    vremepocetkacasa = int(vrp1.get())
    vrp1.delete(0, 10)
    duzinatrajanjacasa = int(vrt1.get())
    vrt1.delete(0, 10)

    j = vremepocetkacasa - 7

    if vremepocetkacasa >= 8 and vremepocetkacasa <= 21 and vremepocetkacasa + duzinatrajanjacasa <= 21:
        while duzinatrajanjacasa > 0:
            if j <= 13:
                matrica[i - 6][j - 1] = predmet
                l = Label(text=predmet, relief=RIDGE, bg="lightblue").grid(row=i, column=j, sticky=NSEW)
                duzinatrajanjacasa = duzinatrajanjacasa - 1
                j = j + 1

    else:
        tkinter.messagebox.showinfo("Upozorenje", "Greska!\nMolimo Vas da unesete tacno vreme i duzinu trajanja casa."
                                                  "\nCasovi pocinju u 8:00, a zavrsavaju se u 21:00.")

    # for i in range(0, 7):
    # for j in range(0, 14):
    # print(matrica[i][j])
    # print("\n")

def obrisipredmet():
    obrisi.configure(bg=random.choice(colors))
    dodaj.configure(bg="gray95")
    predmet = predmet1.get()
    predmet1.delete(0, 30)
    danunedelji = pom.get()


    if danunedelji == 'Ponedeljak':
        i = 6
    elif danunedelji == 'Utorak':
        i = 7
    elif danunedelji == 'Sreda':
        i = 8
    elif danunedelji == 'Cetvrtak':
        i = 9
    elif danunedelji == 'Petak':
        i = 10
    elif danunedelji == 'Subota':
        i = 11
    else:
        i = 12

    vremepocetkacasa = int(vrp1.get())
    vrp1.delete(0, 10)
    duzinatrajanjacasa = int(vrt1.get())
    vrt1.delete(0, 10)

    j = vremepocetkacasa - 7

    if vremepocetkacasa >= 8 and vremepocetkacasa <= 21 and vremepocetkacasa + duzinatrajanjacasa <= 21:
        while duzinatrajanjacasa > 0:
            if j <= 13:
                l = Label(text=" ", relief=RIDGE, bg="gray95").grid(row=i, column=j, sticky=NSEW)
                matrica[i - 6][j - 1]=" "
                duzinatrajanjacasa = duzinatrajanjacasa - 1
                j = j + 1

    else:
        tkinter.messagebox.showinfo("Upozorenje", "Greska!\nMolimo Vas da unesete tacno vreme i duzinu trajanja casa."
                                                  "\nCasovi pocinju u 8:00, a zavrsavaju se u 21:00.")


window = Tk()
window.title("Interactive schedule")
window.geometry("1100x300")

###  OKVIR ### ### DANI ###

predmet = Label(window, text= "Ime predmeta")
predmet.grid(column=0, row=0)

predmet1 = Entry(window, width=11)
predmet1.grid(column=1, row=0)


vrp = Label(window, text= "Vreme pocetka casa")
vrp.grid(column=0, row=2)

vrp1 = Entry(window, width=11)
vrp1.grid(column=1, row=2)

vrt = Label(window, text="Duzina trajanja casa")
vrt.grid(column=0, row=3)

vrt1 = Entry(window, width=11)
vrt1.grid(column=1, row=3)

matrica = [[" "] * 14 for x in range(0, 7)]


l = [[] * 14] * 7
for i in range(6,11):
    for j in range(1,14):
        l = Label(text=" ", relief=RIDGE, bg="gray95").grid(row=i, column=j, sticky=NSEW)

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
obrisi.grid(column=9, row=2, sticky=NSEW)

vreme = datetime.now().strftime('%H:%M:%S')
labela_vreme = Label(text=vreme, width=9, relief=RIDGE)
labela_vreme.grid(column=12, row=0)

datum = datetime.now().strftime('%d-%m-%Y')
labela_datum = Label(text=datum, width=9, relief=RIDGE)
labela_datum.grid(column=11, row=0)

pom = StringVar(window)
pom.set(dani[0])

om = OptionMenu(window, pom, *dani)
om.grid(column=0, row=1)

subota = Label(text="Subota", bg="silver", heigh=1, width=10, relief=RIDGE)
nedelja = Label(text="Nedelja", bg="silver", heigh=1, width=10, relief=RIDGE)

vikendp = Button(window, text="Vikend +", command=dodaj_vikend)
vikendp.grid(column=6, row=2, sticky=NSEW)

vikendm = Button(window, text="Vikend -", command=ukloni_vikend)
vikendm.grid(column=7, row=2, sticky=NSEW)

wb = xlwt.Workbook()

excel = Button(window, text="Save", command=exportuj)
excel.grid(column=6, row=14, sticky=NSEW)

ime_excel = Entry(window, width=11)
ime_excel.grid(column=7, row=14)

window.mainloop()