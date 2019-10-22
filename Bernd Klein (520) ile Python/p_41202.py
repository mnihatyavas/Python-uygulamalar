# coding:iso-8859-9 T�rk�e
# p_41202.py: Tkinter serilim y�netiminde place kullan�m� �rne�i.

from tkinter import *
from p_315 import Renk
    
k�k = Tk()
k�k.title ("place()'le Serilim")

# en x boy + xKenarl�k + yKenarl�k:
k�k.geometry ("200x245+30+30")

kabart� = [SUNKEN, RAISED, GROOVE, RIDGE, FLAT, SUNKEN, RAISED]
liste = ['Python', 'JavaScript', 'MASM', 'HTML', 'CSS', "Java", "C++"]
d = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "a":10, "b":11, "c":12, "d":13, "e":14, "f":15}
uz = len (liste)
for i in range (uz):
    renk = Renk.renk()
    parlakl�k = int (round ( (d[renk[1:3][0]] *16 + d[renk[1:3][0]]) * 0.299 + (d[renk[3:5][0]] *16 + d[renk[3:5][0]]) * 0.587 + (d[renk[5:][0]] *16 + d[renk[5:][0]]) * 0.114))
    # parlakl�k = k�rm�z�*%29.9 + ye�il*%58.7 + mavi*%11.4
    etiket = Label (k�k,
        text=liste [i] + "  (" + str (renk) + "), " + str (parlakl�k),
        fg="White" if parlakl�k < 150 else "Black",
        bg=renk, bd=5, relief=kabart� [i])
    etiket.place (x=20, y=20+i*30, width=160, height=25)
          
k�k.mainloop()