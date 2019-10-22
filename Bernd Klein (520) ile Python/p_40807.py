# coding:iso-8859-9 Türkçe
# p_40807.py: Canvas tuvalinde resmin ortalanması örneği.

from tkinter import *
from p_315 import Renk

kök = Tk()
kök.title ("Dikilitaş Resmi")

tuvalEni = 300
tuvalBoyu =350
tuval = Canvas (kök, width=tuvalEni, height=tuvalBoyu, bg=Renk.renk() )
tuval.pack()

resim = PhotoImage (file="resim/dikilitaş.png")
print (resim.width(), resim.height())
tuval.create_image ((tuvalEni-resim.width())/2, (tuvalBoyu-resim.height())/2, anchor=NW, image=resim)

kök.mainloop()