# coding:iso-8859-9 Türkçe
# p_41202.py: Tkinter serilim yönetiminde place kullanımı örneği.

from tkinter import *
from p_315 import Renk
    
kök = Tk()
kök.title ("place()'le Serilim")

# en x boy + xKenarlık + yKenarlık:
kök.geometry ("200x245+30+30")

kabartı = [SUNKEN, RAISED, GROOVE, RIDGE, FLAT, SUNKEN, RAISED]
liste = ['Python', 'JavaScript', 'MASM', 'HTML', 'CSS', "Java", "C++"]
d = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "a":10, "b":11, "c":12, "d":13, "e":14, "f":15}
uz = len (liste)
for i in range (uz):
    renk = Renk.renk()
    parlaklık = int (round ( (d[renk[1:3][0]] *16 + d[renk[1:3][0]]) * 0.299 + (d[renk[3:5][0]] *16 + d[renk[3:5][0]]) * 0.587 + (d[renk[5:][0]] *16 + d[renk[5:][0]]) * 0.114))
    # parlaklık = kırmızı*%29.9 + yeşil*%58.7 + mavi*%11.4
    etiket = Label (kök,
        text=liste [i] + "  (" + str (renk) + "), " + str (parlaklık),
        fg="White" if parlaklık < 150 else "Black",
        bg=renk, bd=5, relief=kabartı [i])
    etiket.place (x=20, y=20+i*30, width=160, height=25)
          
kök.mainloop()