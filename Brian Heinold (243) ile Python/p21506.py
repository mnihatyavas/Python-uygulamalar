# coding:iso-8859-9 T�rk�e

from tkinter import *
Tk()

def t�kland���n�Bildir (x):
    global uz, L2, alfabe
    L2[x] +=1
    a��klama = Label (font=("Verdana", 20, "italic bold"), fg="green",\
        text='"{}" d��mesini <{:d}>.kez t�klad�n�z!' .format (alfabe[x], L2[x]))
    a��klama.grid (row=1, column=0, columnspan=uz, pady=20)

alfabe = 'ABC�DEFG�HI�JKLMNO�PRS�TU�VYZ'

uz = len (alfabe)
L1 = [0]*uz
L2 = [0]*uz
for i in range (uz):
    L1[i] = Button (text=alfabe[i], command=lambda x=i: t�kland���n�Bildir (x) )
    L1[i].grid (row=0, column=i, padx=1)

mainloop()