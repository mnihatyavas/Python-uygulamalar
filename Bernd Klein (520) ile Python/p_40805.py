# coding:iso-8859-9 Türkçe
# p_40805.py: Canvas tuvalinde üçgen ve yıldızlar poligonu çizme örneği.

from tkinter import *
from p_315 import Renk

kök = Tk()
kök.title ("Poligon Çizimi")

tuvalEni = 400
tuvalBoyu = 400
tuval = Canvas (kök,
    bg=Renk.renk(),
    width=tuvalEni,
    height=tuvalBoyu)
tuval.pack (expand=YES, fill=BOTH)

noktalar1 = [3,3, tuvalEni,tuvalBoyu/2, 3,tuvalBoyu, 3,3]
noktalar2 = [50,240, 60,210, 90,200, 60,190, 50,160, 40,190, 10,200, 40,210]
noktalar3 = [300,240, 310,210, 340,200, 310,190, 300,160, 290,190, 260,200, 290,210]
renk1 = Renk.renk()
renk2 = Renk.renk()
u = 50
d = 8
yıldızSayısı = 8
yıldızSayısıX = int (tuvalEni / yıldızSayısı)
yıldızSayısıY = int (tuvalBoyu / yıldızSayısı)

def yıldızPoligonuÇiz (t, x,y,u,d, dışhatEni=1, dışhatRengi="#476042", dolguRengi='yellow'):
    noktalar = []
    for i in (1, -1):
        noktalar.append ( (x, y + i*u) ) # extend=append
        noktalar.extend ( (x + i*d, y + i*d) )
        noktalar.extend ( (x + i*u, y) )
        noktalar.append ( (x + i*d, y - i * d) )
    t.create_polygon (noktalar, width=dışhatEni, outline=dışhatRengi, fill=dolguRengi)

def poligonÇiz():
    tuval.create_polygon (noktalar1, width=3, outline=Renk.renk(), fill=Renk.renk() )
    tuval.create_polygon (noktalar2, width=3, outline=Renk.renk(), fill=Renk.renk() )
    tuval.create_polygon (noktalar3, width=3, outline=Renk.renk(), fill=Renk.renk() )
    for i in range (1, yıldızSayısı):
        yıldızPoligonuÇiz (tuval, i*yıldızSayısıX,i*yıldızSayısıY,u,d, dışhatEni=3, dışhatRengi=renk1, dolguRengi=renk2)
        yıldızPoligonuÇiz (tuval, i*yıldızSayısıX,tuvalBoyu-i*yıldızSayısıY,u,d, dışhatEni=3, dışhatRengi=renk1, dolguRengi=renk2)

Button (tuval, text="ÇIK", bg="Black", fg="Tomato", command=kök.quit).pack (side=BOTTOM)
Button (tuval, text="Tuvali Aç ve Tekrar-tekrar Tıkla", bg="Black", fg="Yellow", command=poligonÇiz).pack (side=BOTTOM)

kök.mainloop()