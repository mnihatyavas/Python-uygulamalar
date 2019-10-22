# coding:iso-8859-9 Türkçe
# p_40802.py: Canvas tuvalinde çizgi, dikdörtgen ve metin örneği.

from tkinter import *
from p_315 import Renk

kök = Tk()
kök.title ("Tuval'de Dikdörtgen")

tuval = Canvas (kök, width=400, height=200, bg=Renk.renk() )
tuval.pack()

tuval.create_rectangle (50,20, 350,180, fill="#476042")
tuval.create_rectangle (80,50, 320,150, fill="yellow")
tuval.create_line (0,0, 50,20, fill="#476042", width=5)
tuval.create_line (0,200, 50,180, fill="#476042", width=5)
tuval.create_line (350,20, 400,0, fill="#476042", width=5)
tuval.create_line (350,180, 400,200, fill="#476042", width=5)

kök.mainloop()
#----------------------------------------------------------------------------------------------------------

kök = Tk()
kök.title ("Tuval'de Metin")

tuvalEni = 400
tuvalBoyu = 200

renkler = ("#476042", "Gold")
dikdörtgen=[]

# Heriki dikdörtgenin de (x1,y1, x2,y2) koordinatlarını sapta...
for oran in (0.10, 0.20): # En ve boy'un %15, %30
    dikdörtgen.append ( (
        tuvalEni * oran, tuvalBoyu * oran,
        tuvalEni * (1 - oran), tuvalBoyu * (1 - oran) ) )

tuval = Canvas (kök,
    bg=Renk.renk(),
    width=tuvalEni,
    height=tuvalBoyu)
tuval.pack()

for i in range(2): # 2 adet iç-içe renkli dikdörtgen yarat...
    tuval.create_rectangle (dikdörtgen [i] [0],dikdörtgen [i] [1], dikdörtgen [i] [2],dikdörtgen [i] [3], fill=renkler [i] )

# Üst sol-sağ ve alt sol-sağ köşe çizgilerini çiz...
tuval.create_line (0,0, dikdörtgen [0] [0],dikdörtgen [0] [1], fill=renkler [0], width=5)
tuval.create_line (0,tuvalBoyu, dikdörtgen [0] [0],dikdörtgen [0] [3], fill=renkler [0], width=5)
tuval.create_line (dikdörtgen [0] [2],dikdörtgen [0] [1], tuvalEni,0, fill=renkler [0], width=5)
tuval.create_line (dikdörtgen [0] [2],dikdörtgen [0] [3], tuvalEni,tuvalBoyu, fill=renkler [0], width=5)

# Ortaya yatay-dikey metni yaz...
tuval.create_text (tuvalEni / 2, tuvalBoyu / 2, text="Python 3.9", fill="Red", font=("Vermont", 25, "italic"))
tuval.create_text (tuvalEni / 2, tuvalBoyu / 2, text="Python 3.9", fill="Blue", font=("Arial", 6), width=1)

kök.mainloop()