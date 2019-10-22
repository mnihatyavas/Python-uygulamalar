# coding:iso-8859-9 Türkçe
# python3 -m pip install Pillow
# easy_install Pillow

from tkinter import *
from PIL import  Image, ImageTk, ImageDraw
from p21601 import Renk
from random import randint
kök = Tk()
kök.title ("Rasgele RENKLİ mozaik")

def rengiÇevir (k, y, m): return "#{0:02x}{1:02x}{2:02x}" .format (randint (0, 255), randint (0, 255), randint (0, 255) )

azamiTekrar=75
xtrans=-.5
ytrans=0
xzoom=150
yzoom=-150

tuval = Canvas (kök, width=400, height=400, bg=Renk.renk())
tuval.grid()
resim=Image.new (mode='RGB', size=(350, 350) )
resimÇiz = ImageDraw.Draw (resim)

for x in range (50, 300):
    c_x = (x-150)/float(xzoom)+xtrans
    for y in range (50, 300):
        c = complex (c_x, (y-150)/float(yzoom)+ytrans)
        sayaç=0
        z=0j
        while abs (z) < 2 and sayaç < azamiTekrar:
            z = z*z+c
            sayaç +=1
        resimÇiz.point ((x,y), fill=rengiÇevir (sayaç+25, sayaç+25, sayaç+25))
    tuval.delete (ALL)
    fotoğraf = ImageTk.PhotoImage (resim)
    tuval.create_image (0,0, image=fotoğraf, anchor=NW)
    tuval.update()

mainloop()
