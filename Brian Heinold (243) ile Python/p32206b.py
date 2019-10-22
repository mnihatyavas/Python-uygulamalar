# coding:iso-8859-9 T�rk�e
# python3 -m pip install Pillow
# easy_install Pillow

from tkinter import *
from PIL import  Image, ImageTk, ImageDraw
from p21601 import Renk
from random import randint
k�k = Tk()
k�k.title ("Rasgele RENKL� mozaik")

def rengi�evir (k, y, m): return "#{0:02x}{1:02x}{2:02x}" .format (randint (0, 255), randint (0, 255), randint (0, 255) )

azamiTekrar=75
xtrans=-.5
ytrans=0
xzoom=150
yzoom=-150

tuval = Canvas (k�k, width=400, height=400, bg=Renk.renk())
tuval.grid()
resim=Image.new (mode='RGB', size=(350, 350) )
resim�iz = ImageDraw.Draw (resim)

for x in range (50, 300):
    c_x = (x-150)/float(xzoom)+xtrans
    for y in range (50, 300):
        c = complex (c_x, (y-150)/float(yzoom)+ytrans)
        saya�=0
        z=0j
        while abs (z) < 2 and saya� < azamiTekrar:
            z = z*z+c
            saya� +=1
        resim�iz.point ((x,y), fill=rengi�evir (saya�+25, saya�+25, saya�+25))
    tuval.delete (ALL)
    foto�raf = ImageTk.PhotoImage (resim)
    tuval.create_image (0,0, image=foto�raf, anchor=NW)
    tuval.update()

mainloop()
