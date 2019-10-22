# coding:iso-8859-9 T�rk�e
# p_40901.py: Yatay ve dikey �l�ekli s�rg�ler ve de�erlerinin g�sterimi �rne�i

from tkinter import *
from p_315 import Renk

k�k = Tk()
k�k.title ("�l�ekli S�rg�ler")

def g�ster (olay): etiket.config (text="(" + str (s�rg�2.get()) + ", " + str (s�rg�1.get()) + ")")

�er�eve = Frame (k�k, bg=Renk.renk() )
�er�eve.pack()

s�rg�1 = Scale (�er�eve, from_=-20, to=50, tickinterval=5, length=250, bg="Sienna", fg="Azure") # Varsay�l� orient=VERTICAL...
s�rg�1.pack()
s�rg�1.set (-20) # Belirtilmezse varsay�l� ilk de�er=0'd�r...

s�rg�2 = Scale (�er�eve, from_=0, to=200, orient=HORIZONTAL, tickinterval=10, length=500, bg="Teal", fg="Cyan")
s�rg�2.pack()
s�rg�2.set (100)

s�rg�1.bind ("<B1-Motion>", g�ster)
s�rg�2.bind ("<B1-Motion>", g�ster)

�er�eve2 = Frame (�er�eve)
�er�eve2.pack()
Button (�er�eve2, text='Hassas G�ster', command=(lambda x=0: g�ster (x) ), bg="Navy", fg="Gold").pack(side=LEFT)
Button (�er�eve2, text='�IK', command=�er�eve.quit, bg="Orange", fg="Blue").pack(side=LEFT)

etiket = Label (�er�eve, bg="black", fg="Yellow")
etiket.pack()

k�k.mainloop()