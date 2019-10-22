# coding:iso-8859-9 T�rk�e

from random import randint
from tkinter import *
Tk()

def �evir1():
    try: renk1 = abs (int (eval (veri1.get() )))
    except Exception: renk1 = randint (0, 10)
    if renk1 > 10: renk1 = 10
    try: renk2 = abs (int (eval (veri2.get() )))
    except Exception: renk2 = randint (0, 10)
    if renk2 > 10: renk2 = 10
    try: renk3 = abs (int (eval (veri3.get() )))
    except Exception: renk3 = randint (0, 10)
    if renk3 > 10: renk3 = 10
    renk = "#{:02x}{:02x}{:02x}".format (int (renk1 * 25.5), int (renk2 * 25.5), int (renk3 * 25.5))
    mesaj = Label (font=("arial", 30, "bold"), text="Merhaba ("+str(renk1)+","+str(renk2)+","+str(renk3)+")", fg=renk, bg="white")
    mesaj.grid (row=3, column=0, columnspan=4, pady=10)
    veri1.delete (0, END); veri2.delete (0, END); veri3.delete (0, END)

def �evir2():
    try: renk1 = abs (int (eval (veri1.get() )))
    except Exception: renk1 = randint (0, 15)
    if renk1 > 15: renk1 = 15
    try: renk2 = abs (int (eval (veri2.get() )))
    except Exception: renk2 = randint (0, 15)
    if renk2 > 15: renk2 = 15
    try: renk3 = abs (int (eval (veri3.get() )))
    except Exception: renk3 = randint (0, 15)
    if renk3 > 15: renk3 = 15
    renk = "#{:02x}{:02x}{:02x}".format (int (renk1 * 17), int (renk2 * 17), int (renk3 * 17))
    mesaj = Label (font=("arial", 30, "bold"), text="Merhaba ("+str(renk1)+","+str(renk2)+","+str(renk3)+")", fg=renk, bg="white")
    mesaj.grid (row=3, column=0, columnspan=4, pady=10)
    veri1.delete (0, END); veri2.delete (0, END); veri3.delete (0, END)

def �evir3():
    try: renk1 = abs (int (eval (veri1.get() )))
    except Exception: renk1 = randint (0, 100)
    if renk1 > 100: renk1 = 100
    try: renk2 = abs (int (eval (veri2.get() )))
    except Exception: renk2 = randint (0, 100)
    if renk2 > 100: renk2 = 100
    try: renk3 = abs (int (eval (veri3.get() )))
    except Exception: renk3 = randint (0, 100)
    if renk3 > 100: renk3 = 100
    renk = "#{:02x}{:02x}{:02x}".format (int (renk1 * 2.55), int (renk2 * 2.55), int (renk3 * 2.55))
    mesaj = Label (font=("arial", 30, "bold"), text="Merhaba ("+str(renk1)+","+str(renk2)+","+str(renk3)+")", fg=renk, bg="white")
    mesaj.grid (row=3, column=0, columnspan=4, pady=10)
    veri1.delete (0, END); veri2.delete (0, END); veri3.delete (0, END)

def �evir4():
    try: renk1 = abs (int (eval (veri1.get() )))
    except Exception: renk1 = randint (0, 255)
    if renk1 > 255: renk1 = 255
    try: renk2 = abs (int (eval (veri2.get() )))
    except Exception: renk2 = randint (0, 255)
    if renk2 > 255: renk2 = 255
    try: renk3 = abs (int (eval (veri3.get() )))
    except Exception: renk3 = randint (0, 255)
    if renk3 > 255: renk3 = 255
    renk = "#{:02x}{:02x}{:02x}".format (renk1, renk2, renk3)
    mesaj = Label (font=("arial", 30, "bold"), text="Merhaba ("+str(renk1)+","+str(renk2)+","+str(renk3)+")", fg=renk, bg="white")
    mesaj.grid (row=3, column=0, columnspan=4, pady=10)
    veri1.delete (0, END); veri2.delete (0, END); veri3.delete (0, END)

def temizle():
    mesaj = Label (font=("arial", 30, "bold"), text="abc�defg�h�ijklmno�prs�t", fg="white", bg="white")
    mesaj.grid (row=3, column=0, columnspan=4, pady=10)
#-----------------------------------------------------------------------------------------------

etiket = Label (font=("verdana", 24, "bold"), text="Genel Renk �evrim Panosu")
d��me1 = Button (text="0->10", command=�evir1)
d��me2 = Button (text="0->15", command=�evir2)
d��me3 = Button (text="0->100", command=�evir3)
d��me4 = Button (text="0->255", command=�evir4)
d��me5 = Button (text="Temizle", command=temizle)
veri1 = Entry (width=5)
veri2 = Entry (width=5)
veri3 = Entry (width=5)

etiket.grid (row=0, column=0, columnspan=3)
d��me1.grid (row=1, column=0)
d��me2.grid (row=1, column=1)
d��me3.grid (row=1, column=2)
d��me4.grid (row=1, column=3)
d��me5.grid (row=4, column=0, columnspan=4, pady=10)
veri1.grid (row=2, column=0, pady=5)
veri2.grid (row=2, column=1, pady=5)
veri3.grid (row=2, column=2, pady=5)

mainloop()