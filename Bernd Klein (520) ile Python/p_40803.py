# coding:iso-8859-9 Türkçe
# p_40803.py: Canvas tuvalinde dairemsi ve yumurtamsı oval çizimi örneği.

from tkinter import *
from p_315 import Renk

def çemberÇiz (t, x,y, r): # Tuvalde, merkezi ve yarıçapı verili (kirli beyaz) daire çizimi...
    çember = t.create_oval (x-r,y-r, x+r,y+r, width=3, fill="#f0f0f0")
    return çember

kök = Tk()
kök.title ("Oval Çizmek")

tuvalEni = 800
tuvalBoyu =200
tuval = Canvas (kök,
    bg=Renk.renk(),
    width=tuvalEni,
    height=tuvalBoyu)
tuval.pack()

tuval.create_oval (50,50, 150,150, width=3, outline=Renk.renk(), fill="Cyan") # çapı=100, olan çember...
tuval.create_oval (225,50, 375,150, width=3, outline=Renk.renk(), fill="Khaki") # Yatay oval/yumurta...
tuval.create_oval (450,25, 550,175, width=3, outline=Renk.renk(), fill="Gold") # Dikey oval...

çemberÇiz (tuval, 700,100, 95) # Merkez=(700,100) ve yarıçap=95 verili çember çizimi...

kök.mainloop()