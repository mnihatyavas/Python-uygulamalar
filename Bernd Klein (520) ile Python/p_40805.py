# coding:iso-8859-9 T�rk�e
# p_40805.py: Canvas tuvalinde ��gen ve y�ld�zlar poligonu �izme �rne�i.

from tkinter import *
from p_315 import Renk

k�k = Tk()
k�k.title ("Poligon �izimi")

tuvalEni = 400
tuvalBoyu = 400
tuval = Canvas (k�k,
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
y�ld�zSay�s� = 8
y�ld�zSay�s�X = int (tuvalEni / y�ld�zSay�s�)
y�ld�zSay�s�Y = int (tuvalBoyu / y�ld�zSay�s�)

def y�ld�zPoligonu�iz (t, x,y,u,d, d��hatEni=1, d��hatRengi="#476042", dolguRengi='yellow'):
    noktalar = []
    for i in (1, -1):
        noktalar.append ( (x, y + i*u) ) # extend=append
        noktalar.extend ( (x + i*d, y + i*d) )
        noktalar.extend ( (x + i*u, y) )
        noktalar.append ( (x + i*d, y - i * d) )
    t.create_polygon (noktalar, width=d��hatEni, outline=d��hatRengi, fill=dolguRengi)

def poligon�iz():
    tuval.create_polygon (noktalar1, width=3, outline=Renk.renk(), fill=Renk.renk() )
    tuval.create_polygon (noktalar2, width=3, outline=Renk.renk(), fill=Renk.renk() )
    tuval.create_polygon (noktalar3, width=3, outline=Renk.renk(), fill=Renk.renk() )
    for i in range (1, y�ld�zSay�s�):
        y�ld�zPoligonu�iz (tuval, i*y�ld�zSay�s�X,i*y�ld�zSay�s�Y,u,d, d��hatEni=3, d��hatRengi=renk1, dolguRengi=renk2)
        y�ld�zPoligonu�iz (tuval, i*y�ld�zSay�s�X,tuvalBoyu-i*y�ld�zSay�s�Y,u,d, d��hatEni=3, d��hatRengi=renk1, dolguRengi=renk2)

Button (tuval, text="�IK", bg="Black", fg="Tomato", command=k�k.quit).pack (side=BOTTOM)
Button (tuval, text="Tuvali A� ve Tekrar-tekrar T�kla", bg="Black", fg="Yellow", command=poligon�iz).pack (side=BOTTOM)

k�k.mainloop()