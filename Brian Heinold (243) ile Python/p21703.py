# coding:iso-8859-9 T�rk�e

from tkinter import *
k�k = Tk()

def selam(): etiket.config (text="Merhaba Pythoncular")
def g�ster(): etiket.config (text=str (d��me1.cget ("state") ) )

def de�i�tir():
    if d��me1.cget ("state") == DISABLED: d��me1.config (state=NORMAL)
    else: d��me1.config (state=DISABLED)

def ba�l�k():
    etiket.config (text="�imdi 'Tkinter GUI' ba�l���n� pencere �st�nde g�rebilirsiniz")
    k�k.title ("Tkinter GUI Ba�l���")

if __name__ == "__main__":
    d��me1 = Button (k�k, text="Selam Ver", state=DISABLED, command=selam)
    d��me1.pack()
    d��me2 = Button (k�k, text="Durum De�i�tir", command=de�i�tir).pack()
    d��me3 = Button (k�k, text="Durum G�ster", command=g�ster).pack()
    d��me4 = Button (k�k, text="Ba�l�k At", command=ba�l�k).pack()
    d��me5 = Button (k�k, text="��k", command=k�k.quit).pack()

    etiket = Label (k�k)
    etiket.pack()

mainloop()
