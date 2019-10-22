# coding:iso-8859-9 Türkçe
# p_40703.py: Normal ve kompleks sayıların hesap makinesi örneği.

from tkinter import *
from p_315 import Renk
from math import *
from cmath import *

def hesapla (olay): netice.configure (text = "Sonuç: " + str (eval (girilen.get() ) ) )

k = Tk()
k.title ("Kompleks Hesap Makinesi")

ç = Frame (k, bg=Renk.renk() )
ç.pack()

Label (ç, text="İşleminizi girin:", bg="Black", fg="Cyan").pack()

girilen = Entry (ç, width=50, bg="Lime", fg="FireBrick")
girilen.pack()

girilen.bind ("<Return>", hesapla)

netice = Label (ç, bg="Black", fg="Yellow")
netice.pack()

k.mainloop()
