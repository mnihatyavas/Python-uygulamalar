# coding:iso-8859-9 T�rk�e
# p_40703.py: Normal ve kompleks say�lar�n hesap makinesi �rne�i.

from tkinter import *
from p_315 import Renk
from math import *
from cmath import *

def hesapla (olay): netice.configure (text = "Sonu�: " + str (eval (girilen.get() ) ) )

k = Tk()
k.title ("Kompleks Hesap Makinesi")

� = Frame (k, bg=Renk.renk() )
�.pack()

Label (�, text="��leminizi girin:", bg="Black", fg="Cyan").pack()

girilen = Entry (�, width=50, bg="Lime", fg="FireBrick")
girilen.pack()

girilen.bind ("<Return>", hesapla)

netice = Label (�, bg="Black", fg="Yellow")
netice.pack()

k.mainloop()
