# coding:iso-8859-9 T�rk�e
# p_40808.py: Canvas tuvalinde e�it aral�kl� yatay-dikey �zgara hatlar� �izimi �rne�i.

from tkinter import *
from p_315 import Renk

def �zgaralama (t, aral�k, en, boy): # Dikey/boy ve yatay/en �izgiler aral�k/px mesafeli olacak...
    renk = Renk.renk()
    for x in range (aral�k, en, aral�k): t.create_line (x,0, x,boy, fill=renk)
    for y in range (aral�k, boy, aral�k): t.create_line (0,y, en,y, fill=renk)

k�k = Tk()
k�k.title ("Izgaralama")

tuvalEni = 300
tuvalBoyu =100
tuval = Canvas (k�k, width=tuvalEni, height=tuvalBoyu, bg=Renk.renk() )
tuval.pack()

�zgaralama (tuval,10, tuvalEni, tuvalBoyu)

k�k.mainloop()