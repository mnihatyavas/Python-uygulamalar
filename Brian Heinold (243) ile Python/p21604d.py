# coding:iso-8859-9 T�rk�e
# Gereken resim dosyas�: dikilita�.png

from p21601 import Renk # Listede mevcut...
from tkinter import *
Tk()

def y�ld�zPoligonlar (tuval, x, y, b, e, kal�nl�k=1, dolgu="yellow", s�n�r="black"):
    noktalar = []
    for i in (1, -1):
        noktalar.extend ((x, y + i*b))
        noktalar.extend ((x + i*e, y + i*e))
        noktalar.extend ((x + i*b, y))
        noktalar.extend ((x + i*e, y - i * e))
    #print (noktalar)
    for i in range (len (noktalar)):
        if noktalar[i] < 3: noktalar[i] = 3
    tuval.create_polygon (noktalar, outline=s�n�r, fill=dolgu, width=kal�nl�k)

en = 300
boy = 200

tuval = Canvas (width=1000, height=665, bg="cyan")
tuval.pack()

tuval.create_rectangle (3,3, en+22,boy+31, width=3, outline=Renk.renk(), fill=Renk.renk() )
b = 50
e = 15

y�ld�zSay�s� = 10
xArt�� = int (en / y�ld�zSay�s�)
yArt�� = int (boy / y�ld�zSay�s�)

for i in range(1, y�ld�zSay�s�):
   y�ld�zPoligonlar (tuval, i*xArt��, i*yArt��, b, e, s�n�r=Renk.renk(), dolgu=Renk.renk(), kal�nl�k=3)
   y�ld�zPoligonlar (tuval, i*xArt��, boy - i*yArt��, b, e, s�n�r=Renk.renk(), dolgu=Renk.renk(), kal�nl�k=3)
#------------------------------------------------------------------------------------------------------------
en = 775
boy = 400
tuval.create_rectangle (3,3+229, en+22,boy+31+230, width=3, outline=Renk.renk(), fill=Renk.renk() )
b = 70
e = 15

y�ld�zSay�s� = 10
xArt�� = int (en / y�ld�zSay�s�)
yArt�� = int (boy / y�ld�zSay�s�)

for i in range(1, y�ld�zSay�s�):
   y�ld�zPoligonlar (tuval, i*xArt��, i*yArt��+230, b, e, s�n�r=Renk.renk(), dolgu=Renk.renk(), kal�nl�k=3)
   y�ld�zPoligonlar (tuval, i*xArt��, boy - i*yArt��+230, b, e, s�n�r=Renk.renk(), dolgu=Renk.renk(), kal�nl�k=3)
#----------------------------------------------------------------------------------------------------------
en = 323
boy = 83
tuval.create_rectangle (2+en,3, en+317,boy+3, width=3, outline=Renk.renk(), fill="pink" )

bitmaps = ["error", "gray75", "gray50", "gray25", "gray12", "hourglass", "info", "questhead", "question", "warning"]
�ekilSay�s� = len (bitmaps)
xArt�� = int (en / �ekilSay�s�)

for i in range (0, �ekilSay�s�):
   tuval.create_bitmap ((i+1)*xArt��+en+3 - xArt��/2,50, bitmap=bitmaps[i])
#---------------------------------------------------------------------------------------------------------

resim = PhotoImage (file="resim/dikilita�.png")
tuval.create_image (643, 3, anchor=NW, image=resim)
#-----------------------------------------------------------------------------------------------------------

def �zgara (tuv, aral�k):
    for x in range (aral�k, e, aral�k): tuv.create_line (326+x,83, 323+x,b+80, fill="lightgray") # Dikey �izgiler...
    for y in range (aral�k, b, aral�k): tuv.create_line (326+0,y+83, 323+e,y+80, fill="lightgray") # Yatay �izgiler...

e = 315
b = 150

tuval.create_rectangle (325,83, 640,230, width=3, outline=Renk.renk(), fill=Renk.renk() )
�zgara (tuval,10)
#---------------------------------------------------------------------------------------------------------------
en = 500
boy = 150

def boya (event):
    renk = Renk.renk()
    x1, y1 = (event.x - 5), (event.y - 5)
    x2, y2 = (event.x + 5), (event.y + 5)
    tuval.create_oval (x1,y1, x2,y2, fill=renk)

#tuval.pack (expand = YES, fill = BOTH)
tuval.bind ("<B1-Motion>", boya)

tuval.create_line (800,0, 800,665, width=5, fill=Renk.renk() )
tuval.create_text (880,100, text="��Z�M ALANI", width=1)
mesaj = Label (text = "==>�izmek i�in fareyi bas�l� tutarak tuval �zerinde s�r�kleyin..." )
mesaj.pack (side=RIGHT )

mainloop()
