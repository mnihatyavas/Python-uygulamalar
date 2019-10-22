# coding:iso-8859-9 T�rk�e

# Graphical User Interface: GUI (Grafiksel Kullan�c� Aray�z�: GKA)

from tkinter import *
from random import randint

def fahrenhayta�evir():
    try: �s� = eval (i�erik.get() )
    except Exception: �s� = randint (-273, 1000)
    if �s� < -273.15: �s� = -273.15
    f = 9 / 5 * �s� + 32
    ��kt�Etiketi.configure (text = '{:.2f} santigrad derece = {:.2f} fahrenhayt derecedir.' .format (�s�, f) )
    i�erik.delete (0, END)

Tk()

mesajEtiketi = Label (text = 'Santigrad derecesi girin', font = ('Verdana', 16) )
��kt�Etiketi = Label (font = ('Verdana', 16) )
i�erik = Entry (font = ('Verdana', 16), width = 7)
tamamD��mesi = Button (text = 'Tamam', font = ('Verdana', 16), command = fahrenhayta�evir)

mesajEtiketi.grid (row = 0, column = 0)
i�erik.grid (row = 0, column = 1)
tamamD��mesi.grid (row = 0, column = 2)
��kt�Etiketi.grid (row = 1, column = 0, columnspan=3)

mainloop() # Program� ba�latan d�ng�...
