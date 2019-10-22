# coding:iso-8859-9 T�rk�e

from tkinter import *
from random import randint

k�k = Tk()
k�k.title ("Lambda ile Artan ve Azalan S�ralama")

def g�ster (x, y):
    if x == 0 and y == 0:
        L.sort()
        etiket.config (text=str(L))
    elif x == 0 and y == 1:
        L.sort()
        L.reverse()
        etiket.config (text=str(L))
    elif x == 1 and y == 0:
        L.sort(key=lambda x:x[1])
        etiket.config (text=str(L))
    elif x == 1 and y == 1:
        L.sort(key=lambda x:-x[1])
        etiket.config (text=str(L))
    elif x == 2 and y == 0:
        L.sort(key=lambda x:x[2])
        etiket.config (text=str(L))
    elif x == 2 and y == 1:
        L.sort(key=lambda x:-x[2])
        etiket.config (text=str(L))
    elif x == 3 and y == 0:
        L.sort(key=lambda x:x[3])
        etiket.config (text=str(L))
    elif x == 3 and y == 1:
        L.sort(key=lambda x:-x[3])
        etiket.config (text=str(L))

L = [(randint(1000,9999),randint(30,100),randint(30,100),randint(30,100),) for i in range (13)]

Button (k�k, text="Artan ��renci No'lu Liste", bg="BLACK", fg="YELLOW", command=lambda x=0, y=0: g�ster (x, y) ).pack()
Button (k�k, text="Azalan ��renci No'lu Liste", command=lambda x=0, y=1: g�ster (x, y) ).pack()

Button (k�k, text="Artan �dev Not'lu Liste", bg="BLACK", fg="YELLOW", command=lambda x=1, y=0: g�ster (x, y) ).pack()
Button (k�k, text="Azalan �dev Not'lu Liste", command=lambda x=1, y=1: g�ster (x, y) ).pack()

Button (k�k, text="Artan Ara S�nav Not'lu Liste", bg="BLACK", fg="YELLOW", command=lambda x=2, y=0: g�ster (x, y) ).pack()
Button (k�k, text="Azalan Ara S�nav Not'lu Liste", command=lambda x=2, y=1: g�ster (x, y) ).pack()

Button (k�k, text="Artan Final S�nav Not'lu Liste", bg="BLACK", fg="YELLOW", command=lambda x=3, y=0: g�ster (x, y) ).pack()
Button (k�k, text="Azalan Final S�nav Not'lu Liste", command=lambda x=3, y=1: g�ster (x, y) ).pack()

etiket = Label (k�k, pady=10, bg="CYAN", fg="MAROON")
etiket.pack(side=BOTTOM)

mainloop()