# coding:iso-8859-9 T�rk�e
# p_40807.py: Canvas tuvalinde resmin ortalanmas� �rne�i.

from tkinter import *
from p_315 import Renk

k�k = Tk()
k�k.title ("Dikilita� Resmi")

tuvalEni = 300
tuvalBoyu =350
tuval = Canvas (k�k, width=tuvalEni, height=tuvalBoyu, bg=Renk.renk() )
tuval.pack()

resim = PhotoImage (file="resim/dikilita�.png")
print (resim.width(), resim.height())
tuval.create_image ((tuvalEni-resim.width())/2, (tuvalBoyu-resim.height())/2, anchor=NW, image=resim)

k�k.mainloop()