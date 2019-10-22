# coding:iso-8859-9 Türkçe

from p21604 import renk # Listede mevcut...
from random import randint
from tkinter import *
Tk()

tuval = Canvas (width=470, height=245, bg="cyan")
tuval.pack()

tuval.create_rectangle (10,10, 210,110, fill=renk[6], width=10, outline=renk[9])
tuval.create_rectangle (60,30, 150,90, fill=renk[0])
tuval.create_rectangle (75,45, 135,75, fill=renk[1])
tuval.create_line (10,10, 60,30, fill=renk[2], width=3)
tuval.create_line (10,110, 60,90, fill=renk[3], width=3)
tuval.create_line (150,30, 210,10, fill=renk[4], width=3)
tuval.create_line (150,90, 210,110, fill=renk[5], width=3)
tuval.create_text (105,60, text="Python", font=("comic sans ms",10,"italic"), fill=renk[6] )
#--------------------------------------------------------------------------------------------

en = 200
boy = 100
ikiRenk = ("#476042", "yellow")
kutu = []

for oran in ( 0.2, 0.35 ):
   kutu.append ( (en * oran,
            boy * oran,
            en * (1 - oran),
            boy * (1 - oran) ) )

tuval.create_rectangle (10,130, 210,230, fill=renk[7], width=10, outline=renk[10])
for i in range (2):
   tuval.create_rectangle (10+kutu[i][0],130+kutu[i][1], 10+kutu[i][2],130+kutu[i][3], fill=ikiRenk[i])

tuval.create_line (10,130, 10+kutu[0][0],130+kutu[0][1], fill=ikiRenk[0], width=3)
tuval.create_line (10,130+boy, 10+kutu[0][0],130+kutu[0][3], fill=ikiRenk[0], width=3)
tuval.create_line (10+kutu[0][2], 130+kutu[0][1],10+en, 130, fill=ikiRenk[0], width=3)
tuval.create_line (10+kutu[0][2],130+kutu[0][3], 10+en,130+boy, fill=ikiRenk[0], width=3)

tuval.create_text (10+en/2, 130+boy/2, text="Python", font=("verdana",20,"bold"), fill=renk[8] )
#------------------------------------------------------------------------------------------------

tuval.create_oval (250,10,450,80, width=10, outline=renk[11])
tuval.create_text (340,45, text="oval", font=("arial",20), fill=renk[12] )
#------------------------------------------------------------------------------------------------

noktalar = [250,130, 250+en,130+boy/2, 250,130+boy]
tuval.create_polygon (noktalar, outline=renk[8], fill='yellow', width=10)
tuval.create_text (310,180, text="poligon", font=("cordial",20, "bold"), fill=renk[13] )
#-------------------------------------------------------------------------------------------------
nokta = [410,160,   420,130,   450,120,  420,110,   410,80,   400,110,   370,120,   400,130]
tuval.create_polygon (nokta, outline=renk[14], fill=renk[15], width=3)

mainloop()
