# coding:iso-8859-9 Türkçe

from tkinter import *
from random import randint

kök = Tk()
kök.title ("Lambda ile Artan ve Azalan Sıralama")

def göster (x, y):
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

Button (kök, text="Artan Öğrenci No'lu Liste", bg="BLACK", fg="YELLOW", command=lambda x=0, y=0: göster (x, y) ).pack()
Button (kök, text="Azalan Öğrenci No'lu Liste", command=lambda x=0, y=1: göster (x, y) ).pack()

Button (kök, text="Artan Ödev Not'lu Liste", bg="BLACK", fg="YELLOW", command=lambda x=1, y=0: göster (x, y) ).pack()
Button (kök, text="Azalan Ödev Not'lu Liste", command=lambda x=1, y=1: göster (x, y) ).pack()

Button (kök, text="Artan Ara Sınav Not'lu Liste", bg="BLACK", fg="YELLOW", command=lambda x=2, y=0: göster (x, y) ).pack()
Button (kök, text="Azalan Ara Sınav Not'lu Liste", command=lambda x=2, y=1: göster (x, y) ).pack()

Button (kök, text="Artan Final Sınav Not'lu Liste", bg="BLACK", fg="YELLOW", command=lambda x=3, y=0: göster (x, y) ).pack()
Button (kök, text="Azalan Final Sınav Not'lu Liste", command=lambda x=3, y=1: göster (x, y) ).pack()

etiket = Label (kök, pady=10, bg="CYAN", fg="MAROON")
etiket.pack(side=BOTTOM)

mainloop()