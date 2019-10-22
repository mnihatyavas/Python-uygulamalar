# coding:iso-8859-9 T�rk�e
# Gereken resim dosyalar�: 0/1/2/3/4.gif

import sys
from tkinter import *
Tk()

def t�kland�():
    global saya�, L
    saya� +=1
    d��me.configure (image=L[saya�%5])

if len (sys.argv) > 1: dosya = sys.argv[1]
else: dosya = "resim/4.gif"

resim = PhotoImage (file=dosya)
etiket = Label (image=resim)
etiket.grid (row=0, column=0)

L=[0]*5
for i in range (5): L[i] = PhotoImage (file="resim/"+str(i)+".gif")

saya�=0
d��me = Button (image=L[0], command=t�kland�)
d��me.grid (row=0, column=1, padx=5)

etiket = Label (text="T�kla", bg="black", fg="yellow")
etiket.grid (row=0, column=1)

mainloop()
