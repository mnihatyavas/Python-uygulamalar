# coding:iso-8859-9 T�rk�e

from tkinter import *
Tk()

def a��kla1 (k):
    a��kla = Label (text=alfabe[k]+" harfini t�klad�n�z")
    a��kla.grid (row=1, column=1, columnspan=10)

def a��kla2 (k):
    global saya�
    saya� +=1
    a��kla = Label (text=k+" d��mesini " + str (saya�) + ".kere t�klad�n�z")
    a��kla.grid (row=1, column=10, columnspan=10)

alfabe = 'ABC�DEFG�HI�JKLMNO�PRS�TU�VYZ'
uz = len (alfabe)
d��meler = [0]*uz

for i in range (uz):
    d��meler[i] = Button (text=alfabe[i], command=lambda x=i: a��kla1 (x))
    d��meler[i].grid (row=0, column=i)

saya� = 0
tamam = Button (text='Tamam', font=('Verdana', 24), command=lambda: a��kla2 ("Tamam"))
tamam.grid (row=1, column=0)

mainloop()