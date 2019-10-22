# coding:iso-8859-9 Türkçe
# p_40809.py: Canvas tuvalinde toplu şekiller örneği

from tkinter import *
from p_315 import Renk

kök = Tk()
kök.title ("Canvas Tuvali")

tuval = Canvas (kök, width=1000, height=680, bg="cyan")
tuval.pack()
#------------------------------------------------------------------------------------------------------------

en = 322 # 2 yıldızlı flama kutusu...
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

resim = PhotoImage (file="resim/dikilitaş.png")
tuval.create_image (646, 20, anchor=NW, image=resim)
#-----------------------------------------------------------------------------------------------------------

en = 775 # Çaprazlama çoklu yıldızlar kutusu...
boy = 400
tuval.create_rectangle (3,3+229, en+22,boy+31+230, width=3, outline=Renk.renk(), fill=Renk.renk() )

def yıldızPoligonlar (tuval, x, y, b, e, kalınlık=1, dolgu="yellow", sınır="black"):
    noktalar = []
    for i in (1, -1):
        noktalar.extend ((x, y + i*b))
        noktalar.extend ((x + i*e, y + i*e))
        noktalar.extend ((x + i*b, y))
        noktalar.extend ((x + i*e, y - i * e))
    for i in range (len (noktalar)):
        if noktalar[i] < 3: noktalar[i] = 3
    tuval.create_polygon (noktalar, outline=sınır, fill=dolgu, width=kalınlık)

b = 70
e = 10
yıldızSayısı = 10
xArtış = int (en / yıldızSayısı)
yArtış = int (boy / yıldızSayısı)

for i in range(1, yıldızSayısı):
   yıldızPoligonlar (tuval, i*xArtış, i*yArtış+230, b, e, sınır=Renk.renk(), dolgu=Renk.renk(), kalınlık=3)
   yıldızPoligonlar (tuval, i*xArtış, boy - i*yArtış+230, b, e, sınır=Renk.renk(), dolgu=Renk.renk(), kalınlık=3)
#----------------------------------------------------------------------------------------------------------

en = 323 # İkiliharitalama kutusu...
boy = 83
tuval.create_rectangle (2+en,3, en+317,boy+3, width=3, outline=Renk.renk(), fill="pink" )

ikiliharitalamalar = ["error", "gray75", "gray50", "gray25", "gray12", "hourglass", "info", "questhead", "question", "warning"]
şekilSayısı = len (ikiliharitalamalar)
xArtış = int (en / şekilSayısı)

for i in range (0, şekilSayısı): tuval.create_bitmap ((i+1)*xArtış+en+3 - xArtış/2,50, bitmap=ikiliharitalamalar [i])
#---------------------------------------------------------------------------------------------------------

e = 315 # Izgaralama kutusu...
b = 150
tuval.create_rectangle (325,83, 640,230, width=3, outline=Renk.renk(), fill=Renk.renk() )

def ızgara (tuv, aralık):
    for x in range (aralık, e, aralık): tuv.create_line (326+x,83, 323+x,b+80, fill="lightgray") # Dikey çizgiler...
    for y in range (aralık, b, aralık): tuv.create_line (326+0,y+83, 323+e,y+80, fill="lightgray") # Yatay çizgiler...

ızgara (tuval,10)
#---------------------------------------------------------------------------------------------------------------

def boya (olay):
    x1, y1 = (olay.x - 5), (olay.y - 5)
    x2, y2 = (olay.x + 5), (olay.y + 5)
    if x1 < 800: x1 = 800
    if x2 < 800: x2 = 800
    if y1 > 665: y1 = 665
    if y2 > 665: y2 = 665
    tuval.create_oval (x1,y1, x2,y2, fill=Renk.renk() )

tuval.bind ("<B1-Motion>", boya) # İri noktalı serbest çizim...

tuval.create_line (800,0, 800,665, width=5, fill=Renk.renk() )
tuval.create_line (0,665, 1000,665, width=5, fill="black" )
tuval.create_text (880,100, text="ÇİZİM-ALANI", width=1)
tuval.create_text (75,674, text="Copyright: [M.Nihat Yavaş]")
tuval.create_text (830,674, text="==>Çizmek için fareyi basılı tutarak tuval üzerinde sürükleyin...")

kök.mainloop()
