# coding:iso-8859-9 T�rk�e

from math import *
from tkinter import *
k�k = Tk()

def hesapla (olay):
    de�er = eval (gir.get() )
    print ("Sonu� =", de�er)
    etiket.config (text="Sonu�: "+str (de�er) )

def g�ster (olay): print (olay.keysym, "tu�una bast�n�z")

Label (k�k, text="��lem gir ve [Ent] bas").pack()

gir = Entry (k�k, width=20)
gir.pack() #�rn. [log(123)/sin(76)*1e-7**78] gir, dene...
gir.focus_set()

gir.bind ("<Key>", g�ster)
gir.bind ("<Return>", hesapla)

etiket = Label (k�k, pady=10)
etiket.pack()

mainloop()

"""
1) Baz� ba�lanabilecek olaylar:
<Button-1> Fare sol d��mesi t�kland�
<Double-Button-1> Fare sol d��mesi �ift-t�kland�
Farenin, 1:sol, 2:orta, 3:sa� d��mesi...
<Button-Release-1> Fare sol d��mesi b�rak�ld�
<B1-Motion> Fare sol d��mesiyle t�klan�p s�r�klendi
<MouseWheel> Fare tekeri oynad�
<Motion> Fare oynad�
<Enter> Fare bile�ke �zerinde
<Leave> Fare bile�keden ayr�ld�
<Key> Bir tu�a bas�ld�
<"tu� ad�"> Ad� belirtilen tu�a bas�ld�

2) Event olay nesne �zellikleri:
keysym: tu� sembolleri
x,y: farenin (x,y) kordinat�
delta: fare teker de�eri

3) Baz� bind olay yakalay�c�/ba�lay�c� keysym: key symbol = tu� sembolleri
<Return>, <Tab>, <Space>, <F1>, . . . , <F12> F1, . . . , F12
<Next>, <Prior> Page up, Page down
<Up>, <Down>, <Left>, <Right> Arrow keys
<Home>, <End>, <Insert>, <Delete>, <Caps_Lock>, <Num_Lock>
<Control_L>, <Control_R>, <Alt_L>, <Alt_R>, <Shift_L>, <Shift_R>
"a", "A", "-", <Space>, <Less>, <Greater>,
<Shift-F5>, <Control-Next>, <Alt-2>, <Control-Shift-F1>.
"""