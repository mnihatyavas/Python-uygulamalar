# coding:iso-8859-9 T�rk�e

from tkinter import *

k�k = Tk()
k�k.title ("De�i�ken arg�manl� bile�enler")

def saya�():
    saya�.kere = saya�.kere + 1
    etiket.config (text="D��meyi <<"+ str(saya�.kere)+">> kez t�klad�n�z")

def s�f�rla():
    saya�.kere = 0
    etiket.config (text="   << Saya� s�f�rland� >>   ")

saya�.kere = 0
arg�manlar = {'fg':'YELLOW', 'bg':'BLACK', 'font':('Verdana', 16, 'bold')}

Button (k�k, text="TIKLAYIN L�TFEN", **arg�manlar, command=saya�).pack()
Button (k�k, text="Sayac� S�f�rlay�n", **arg�manlar, command=s�f�rla).pack()
Button (k�k, text="�IK", **arg�manlar, command=quit).pack()

etiket = Label (k�k, **arg�manlar, pady=20)
etiket.pack()

mainloop()