# coding:iso-8859-9 T�rk�e

from tkinter import *
Tk()

def a��kla1 (k):
    global d��meler2
    d��meler2[k] +=1
    a��kla = Label (text=alfabe[k]+" harfini " + str (d��meler2[k]) + ".kere t�klad�n�z")
    a��kla.grid (row=2, column=0, pady=10)

def a��kla2 (k):
    global saya�
    saya� +=1
    a��kla = Label (text=k+" d��mesini " + str (saya�) + ".kere t�klad�n�z")
    a��kla.grid (row=3, column=0, pady=10)
#----------------------------------------------------------------------------------------
alfabe = 'ABC�DEFG�HI�JKLMNO�PRS�TU�VYZ'
uz = len (alfabe)
d��meler1 = [0]*uz
d��meler2 = [0]*uz

�er�eve = Frame()
for i in range (uz):
    d��meler1[i] = Button (�er�eve, text=alfabe[i], command=lambda x=i: a��kla1 (x))
    d��meler1[i].grid (row=0, column=i)
�er�eve.grid (row=0, column=0)

saya� = 0
tamam = Button (text='Tamam', font=('Verdana', 24), command=lambda: a��kla2 ("Tamam"))
tamam.grid (row=1, column=0)

mainloop()