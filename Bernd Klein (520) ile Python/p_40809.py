# coding:iso-8859-9 T�rk�e
# p_40809.py: Canvas tuvalinde toplu �ekiller �rne�i

from tkinter import *
from p_315 import Renk

k�k = Tk()
k�k.title ("Canvas Tuvali")

tuval = Canvas (k�k, width=1000, height=680, bg="cyan")
tuval.pack()
#------------------------------------------------------------------------------------------------------------

en = 322 # 2 y�ld�zl� flama kutusu...
boy = 231
tuval.create_rectangle (3,3, en,boy, width=3, outline=Renk.renk(), fill=Renk.renk() )

noktalar1 = [6,6, en-2,boy/2, 3,boy, 6,6]
noktalar2 = [206,155, 216,125, 246,115, 213,105, 206,78, 196,105, 166,115, 196,125]
noktalar3 = [46,155, 56,125, 86,115, 53,105, 46,75, 36,105, 6,115, 36,125]

tuval.create_polygon (noktalar1, width=3, outline=Renk.renk(), fill=Renk.renk() )
tuval.create_polygon (noktalar2, width=3, outline=Renk.renk(), fill=Renk.renk() )
tuval.create_polygon (noktalar3, width=3, outline=Renk.renk(), fill=Renk.renk() )
#------------------------------------------------------------------------------------------------------------

tuval.create_rectangle (643,3, 796,230, width=3, fill="Black" ) # Resim kutusu...

resim = PhotoImage (file="resim/dikilita�.png")
tuval.create_image (646, 20, anchor=NW, image=resim)
#-----------------------------------------------------------------------------------------------------------

en = 775 # �aprazlama �oklu y�ld�zlar kutusu...
boy = 400
tuval.create_rectangle (3,3+229, en+22,boy+31+230, width=3, outline=Renk.renk(), fill=Renk.renk() )

def y�ld�zPoligonlar (tuval, x, y, b, e, kal�nl�k=1, dolgu="yellow", s�n�r="black"):
    noktalar = []
    for i in (1, -1):
        noktalar.extend ((x, y + i*b))
        noktalar.extend ((x + i*e, y + i*e))
        noktalar.extend ((x + i*b, y))
        noktalar.extend ((x + i*e, y - i * e))
    for i in range (len (noktalar)):
        if noktalar[i] < 3: noktalar[i] = 3
    tuval.create_polygon (noktalar, outline=s�n�r, fill=dolgu, width=kal�nl�k)

b = 70
e = 10
y�ld�zSay�s� = 10
xArt�� = int (en / y�ld�zSay�s�)
yArt�� = int (boy / y�ld�zSay�s�)

for i in range(1, y�ld�zSay�s�):
   y�ld�zPoligonlar (tuval, i*xArt��, i*yArt��+230, b, e, s�n�r=Renk.renk(), dolgu=Renk.renk(), kal�nl�k=3)
   y�ld�zPoligonlar (tuval, i*xArt��, boy - i*yArt��+230, b, e, s�n�r=Renk.renk(), dolgu=Renk.renk(), kal�nl�k=3)
#----------------------------------------------------------------------------------------------------------

en = 323 # �kiliharitalama kutusu...
boy = 83
tuval.create_rectangle (2+en,3, en+317,boy+3, width=3, outline=Renk.renk(), fill="pink" )

ikiliharitalamalar = ["error", "gray75", "gray50", "gray25", "gray12", "hourglass", "info", "questhead", "question", "warning"]
�ekilSay�s� = len (ikiliharitalamalar)
xArt�� = int (en / �ekilSay�s�)

for i in range (0, �ekilSay�s�): tuval.create_bitmap ((i+1)*xArt��+en+3 - xArt��/2,50, bitmap=ikiliharitalamalar [i])
#---------------------------------------------------------------------------------------------------------

e = 315 # Izgaralama kutusu...
b = 150
tuval.create_rectangle (325,83, 640,230, width=3, outline=Renk.renk(), fill=Renk.renk() )

def �zgara (tuv, aral�k):
    for x in range (aral�k, e, aral�k): tuv.create_line (326+x,83, 323+x,b+80, fill="lightgray") # Dikey �izgiler...
    for y in range (aral�k, b, aral�k): tuv.create_line (326+0,y+83, 323+e,y+80, fill="lightgray") # Yatay �izgiler...

�zgara (tuval,10)
#---------------------------------------------------------------------------------------------------------------

def boya (olay):
    x1, y1 = (olay.x - 5), (olay.y - 5)
    x2, y2 = (olay.x + 5), (olay.y + 5)
    if x1 < 800: x1 = 800
    if x2 < 800: x2 = 800
    if y1 > 665: y1 = 665
    if y2 > 665: y2 = 665
    tuval.create_oval (x1,y1, x2,y2, fill=Renk.renk() )

tuval.bind ("<B1-Motion>", boya) # �ri noktal� serbest �izim...

tuval.create_line (800,0, 800,665, width=5, fill=Renk.renk() )
tuval.create_line (0,665, 1000,665, width=5, fill="black" )
tuval.create_text (880,100, text="��Z�M-ALANI", width=1)
tuval.create_text (75,674, text="Copyright: [M.Nihat Yava�]")
tuval.create_text (830,674, text="==>�izmek i�in fareyi bas�l� tutarak tuval �zerinde s�r�kleyin...")

k�k.mainloop()
