# coding:iso-8859-9 T�rk�e
# p_40802.py: Canvas tuvalinde �izgi, dikd�rtgen ve metin �rne�i.

from tkinter import *
from p_315 import Renk

k�k = Tk()
k�k.title ("Tuval'de Dikd�rtgen")

tuval = Canvas (k�k, width=400, height=200, bg=Renk.renk() )
tuval.pack()

tuval.create_rectangle (50,20, 350,180, fill="#476042")
tuval.create_rectangle (80,50, 320,150, fill="yellow")
tuval.create_line (0,0, 50,20, fill="#476042", width=5)
tuval.create_line (0,200, 50,180, fill="#476042", width=5)
tuval.create_line (350,20, 400,0, fill="#476042", width=5)
tuval.create_line (350,180, 400,200, fill="#476042", width=5)

k�k.mainloop()
#----------------------------------------------------------------------------------------------------------

k�k = Tk()
k�k.title ("Tuval'de Metin")

tuvalEni = 400
tuvalBoyu = 200

renkler = ("#476042", "Gold")
dikd�rtgen=[]

# Heriki dikd�rtgenin de (x1,y1, x2,y2) koordinatlar�n� sapta...
for oran in (0.10, 0.20): # En ve boy'un %15, %30
    dikd�rtgen.append ( (
        tuvalEni * oran, tuvalBoyu * oran,
        tuvalEni * (1 - oran), tuvalBoyu * (1 - oran) ) )

tuval = Canvas (k�k,
    bg=Renk.renk(),
    width=tuvalEni,
    height=tuvalBoyu)
tuval.pack()

for i in range(2): # 2 adet i�-i�e renkli dikd�rtgen yarat...
    tuval.create_rectangle (dikd�rtgen [i] [0],dikd�rtgen [i] [1], dikd�rtgen [i] [2],dikd�rtgen [i] [3], fill=renkler [i] )

# �st sol-sa� ve alt sol-sa� k��e �izgilerini �iz...
tuval.create_line (0,0, dikd�rtgen [0] [0],dikd�rtgen [0] [1], fill=renkler [0], width=5)
tuval.create_line (0,tuvalBoyu, dikd�rtgen [0] [0],dikd�rtgen [0] [3], fill=renkler [0], width=5)
tuval.create_line (dikd�rtgen [0] [2],dikd�rtgen [0] [1], tuvalEni,0, fill=renkler [0], width=5)
tuval.create_line (dikd�rtgen [0] [2],dikd�rtgen [0] [3], tuvalEni,tuvalBoyu, fill=renkler [0], width=5)

# Ortaya yatay-dikey metni yaz...
tuval.create_text (tuvalEni / 2, tuvalBoyu / 2, text="Python 3.9", fill="Red", font=("Vermont", 25, "italic"))
tuval.create_text (tuvalEni / 2, tuvalBoyu / 2, text="Python 3.9", fill="Blue", font=("Arial", 6), width=1)

k�k.mainloop()