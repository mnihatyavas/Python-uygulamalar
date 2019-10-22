# coding:iso-8859-9 T�rk�e
# python3 -m pip install Pillow
# easy_install Pillow

from tkinter import *
from PIL import  Image, ImageTk, ImageDraw
from p21601 import Renk

k�k = Tk()
k�k.title ("Mite parazitinin GR� b�y�t�lm�� resmi")

def rengi�evir (k, y, m): return "#{0:02x}{1:02x}{2:02x}" .format (int (k*2.55), int (y*2.55), int (m*2.55))

azamiD�ng�Tekrar� = 75
yatayKayd�r = -1 # �ekli yatay sa�a kayd�r�r...
dikeyKayd�r = 0.35 # �ekli dikey a�a�� kayd�r�r...
yatayB�y�tme = 100
dikeyB�y�tme = -100

tuval = Canvas (k�k, width=450, height=425, bg=Renk.renk())
tuval.grid()
resim=Image.new (mode='RGB', size=(400, 375))
resim�iz = ImageDraw.Draw (resim)

for x in range (25, 375):
    c_x = (x-150)/float(yatayB�y�tme)+yatayKayd�r
    for y in range (25, 350):
        c = complex (c_x, (y-150)/float(dikeyB�y�tme)+dikeyKayd�r)
        saya�=0
        z=0j
        while abs(z)<2 and saya�<azamiD�ng�Tekrar�:
            z = z*z+c
            saya� +=1
        resim�iz.point ((x,y), fill=rengi�evir (saya�+25, saya�+25, saya�+25))
    tuval.delete (ALL)
    foto�raf = ImageTk.PhotoImage (resim)
    tuval.create_image (0,0, image=foto�raf, anchor=NW)
    tuval.update()

mainloop()
