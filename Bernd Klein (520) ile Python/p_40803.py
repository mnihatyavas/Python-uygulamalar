# coding:iso-8859-9 T�rk�e
# p_40803.py: Canvas tuvalinde dairemsi ve yumurtams� oval �izimi �rne�i.

from tkinter import *
from p_315 import Renk

def �ember�iz (t, x,y, r): # Tuvalde, merkezi ve yar��ap� verili (kirli beyaz) daire �izimi...
    �ember = t.create_oval (x-r,y-r, x+r,y+r, width=3, fill="#f0f0f0")
    return �ember

k�k = Tk()
k�k.title ("Oval �izmek")

tuvalEni = 800
tuvalBoyu =200
tuval = Canvas (k�k,
    bg=Renk.renk(),
    width=tuvalEni,
    height=tuvalBoyu)
tuval.pack()

tuval.create_oval (50,50, 150,150, width=3, outline=Renk.renk(), fill="Cyan") # �ap�=100, olan �ember...
tuval.create_oval (225,50, 375,150, width=3, outline=Renk.renk(), fill="Khaki") # Yatay oval/yumurta...
tuval.create_oval (450,25, 550,175, width=3, outline=Renk.renk(), fill="Gold") # Dikey oval...

�ember�iz (tuval, 700,100, 95) # Merkez=(700,100) ve yar��ap=95 verili �ember �izimi...

k�k.mainloop()