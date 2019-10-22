# coding:iso-8859-9 Türkçe
# Gereken resim dosyası: dikilitaş.png

from p21601 import Renk # Listede mevcut...
from tkinter import *
Tk()

def yıldızPoligonlar (tuval, x, y, b, e, kalınlık=1, dolgu="yellow", sınır="black"):
    noktalar = []
    for i in (1, -1):
        noktalar.extend ((x, y + i*b))
        noktalar.extend ((x + i*e, y + i*e))
        noktalar.extend ((x + i*b, y))
        noktalar.extend ((x + i*e, y - i * e))
    #print (noktalar)
    for i in range (len (noktalar)):
        if noktalar[i] < 3: noktalar[i] = 3
    tuval.create_polygon (noktalar, outline=sınır, fill=dolgu, width=kalınlık)

en = 300
boy = 200

tuval = Canvas (width=1000, height=665, bg="cyan")
tuval.pack()

tuval.create_rectangle (3,3, en+22,boy+31, width=3, outline=Renk.renk(), fill=Renk.renk() )
b = 50
e = 15

yıldızSayısı = 10
xArtış = int (en / yıldızSayısı)
yArtış = int (boy / yıldızSayısı)

for i in range(1, yıldızSayısı):
   yıldızPoligonlar (tuval, i*xArtış, i*yArtış, b, e, sınır=Renk.renk(), dolgu=Renk.renk(), kalınlık=3)
   yıldızPoligonlar (tuval, i*xArtış, boy - i*yArtış, b, e, sınır=Renk.renk(), dolgu=Renk.renk(), kalınlık=3)
#------------------------------------------------------------------------------------------------------------
en = 775
boy = 400
tuval.create_rectangle (3,3+229, en+22,boy+31+230, width=3, outline=Renk.renk(), fill=Renk.renk() )
b = 70
e = 15

yıldızSayısı = 10
xArtış = int (en / yıldızSayısı)
yArtış = int (boy / yıldızSayısı)

for i in range(1, yıldızSayısı):
   yıldızPoligonlar (tuval, i*xArtış, i*yArtış+230, b, e, sınır=Renk.renk(), dolgu=Renk.renk(), kalınlık=3)
   yıldızPoligonlar (tuval, i*xArtış, boy - i*yArtış+230, b, e, sınır=Renk.renk(), dolgu=Renk.renk(), kalınlık=3)
#----------------------------------------------------------------------------------------------------------
en = 323
boy = 83
tuval.create_rectangle (2+en,3, en+317,boy+3, width=3, outline=Renk.renk(), fill="pink" )

bitmaps = ["error", "gray75", "gray50", "gray25", "gray12", "hourglass", "info", "questhead", "question", "warning"]
şekilSayısı = len (bitmaps)
xArtış = int (en / şekilSayısı)

for i in range (0, şekilSayısı):
   tuval.create_bitmap ((i+1)*xArtış+en+3 - xArtış/2,50, bitmap=bitmaps[i])
#---------------------------------------------------------------------------------------------------------

resim = PhotoImage (file="resim/dikilitaş.png")
tuval.create_image (643, 3, anchor=NW, image=resim)
#-----------------------------------------------------------------------------------------------------------

def ızgara (tuv, aralık):
    for x in range (aralık, e, aralık): tuv.create_line (326+x,83, 323+x,b+80, fill="lightgray") # Dikey çizgiler...
    for y in range (aralık, b, aralık): tuv.create_line (326+0,y+83, 323+e,y+80, fill="lightgray") # Yatay çizgiler...

e = 315
b = 150

tuval.create_rectangle (325,83, 640,230, width=3, outline=Renk.renk(), fill=Renk.renk() )
ızgara (tuval,10)
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
tuval.create_text (880,100, text="ÇİZİM ALANI", width=1)
mesaj = Label (text = "==>Çizmek için fareyi basılı tutarak tuval üzerinde sürükleyin..." )
mesaj.pack (side=RIGHT )

mainloop()
