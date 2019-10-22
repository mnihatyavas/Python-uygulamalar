# coding:iso-8859-9 Türkçe
# python3 -m pip install Pillow
# easy_install Pillow

from tkinter import *
from PIL import  Image, ImageTk, ImageDraw
from p21601 import Renk

kök = Tk()
kök.title ("Mite parazitinin GRİ büyütülmüş resmi")

def rengiÇevir (k, y, m): return "#{0:02x}{1:02x}{2:02x}" .format (int (k*2.55), int (y*2.55), int (m*2.55))

azamiDöngüTekrarı = 75
yatayKaydır = -1 # Şekli yatay sağa kaydırır...
dikeyKaydır = 0.35 # Şekli dikey aşağı kaydırır...
yatayBüyütme = 100
dikeyBüyütme = -100

tuval = Canvas (kök, width=450, height=425, bg=Renk.renk())
tuval.grid()
resim=Image.new (mode='RGB', size=(400, 375))
resimÇiz = ImageDraw.Draw (resim)

for x in range (25, 375):
    c_x = (x-150)/float(yatayBüyütme)+yatayKaydır
    for y in range (25, 350):
        c = complex (c_x, (y-150)/float(dikeyBüyütme)+dikeyKaydır)
        sayaç=0
        z=0j
        while abs(z)<2 and sayaç<azamiDöngüTekrarı:
            z = z*z+c
            sayaç +=1
        resimÇiz.point ((x,y), fill=rengiÇevir (sayaç+25, sayaç+25, sayaç+25))
    tuval.delete (ALL)
    fotoğraf = ImageTk.PhotoImage (resim)
    tuval.create_image (0,0, image=fotoğraf, anchor=NW)
    tuval.update()

mainloop()
