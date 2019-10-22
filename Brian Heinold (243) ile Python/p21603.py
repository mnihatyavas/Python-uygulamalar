# coding:iso-8859-9 Türkçe
# Gereken resim dosyaları: 0/1/2/3/4.gif

import sys
from tkinter import *
Tk()

def tıklandı():
    global sayaç, L
    sayaç +=1
    düğme.configure (image=L[sayaç%5])

if len (sys.argv) > 1: dosya = sys.argv[1]
else: dosya = "resim/4.gif"

resim = PhotoImage (file=dosya)
etiket = Label (image=resim)
etiket.grid (row=0, column=0)

L=[0]*5
for i in range (5): L[i] = PhotoImage (file="resim/"+str(i)+".gif")

sayaç=0
düğme = Button (image=L[0], command=tıklandı)
düğme.grid (row=0, column=1, padx=5)

etiket = Label (text="Tıkla", bg="black", fg="yellow")
etiket.grid (row=0, column=1)

mainloop()
