# coding:iso-8859-9 T�rk�e

from tkinter import *
Tk()

def t�kland���n�Bildir (x):
    a��klama = Label (font=("Verdana", 20, "italic bold"), fg="blue",\
        text='"{}" d��mesini t�klad�n�z!' .format (alfabe[x]))
    a��klama.grid (row=1, column=0, columnspan=29, pady=20)

alfabe = 'ABC�DEFG�HI�JKLMNO�PRS�TU�VYZ'

L = [0]*29 # 29 d��meyi kapsayan bir liste...
for i in range (29):
    L[i] = Button (text=alfabe[i], command=lambda x=i: t�kland���n�Bildir (x) )
    L[i].grid (row=0, column=i, padx=1)

mainloop()