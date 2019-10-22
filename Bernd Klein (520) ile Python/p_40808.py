# coding:iso-8859-9 Türkçe
# p_40808.py: Canvas tuvalinde eşit aralıklı yatay-dikey ızgara hatları çizimi örneği.

from tkinter import *
from p_315 import Renk

def ızgaralama (t, aralık, en, boy): # Dikey/boy ve yatay/en çizgiler aralık/px mesafeli olacak...
    renk = Renk.renk()
    for x in range (aralık, en, aralık): t.create_line (x,0, x,boy, fill=renk)
    for y in range (aralık, boy, aralık): t.create_line (0,y, en,y, fill=renk)

kök = Tk()
kök.title ("Izgaralama")

tuvalEni = 300
tuvalBoyu =100
tuval = Canvas (kök, width=tuvalEni, height=tuvalBoyu, bg=Renk.renk() )
tuval.pack()

ızgaralama (tuval,10, tuvalEni, tuvalBoyu)

kök.mainloop()