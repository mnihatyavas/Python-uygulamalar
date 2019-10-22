# coding:iso-8859-9 Türkçe

# Graphical User Interface: GUI (Grafiksel Kullanıcı Arayüzü: GKA)

from tkinter import *
from random import randint

def fahrenhaytaÇevir():
    try: ısı = eval (içerik.get() )
    except Exception: ısı = randint (-273, 1000)
    if ısı < -273.15: ısı = -273.15
    f = 9 / 5 * ısı + 32
    çıktıEtiketi.configure (text = '{:.2f} santigrad derece = {:.2f} fahrenhayt derecedir.' .format (ısı, f) )
    içerik.delete (0, END)

Tk()

mesajEtiketi = Label (text = 'Santigrad derecesi girin', font = ('Verdana', 16) )
çıktıEtiketi = Label (font = ('Verdana', 16) )
içerik = Entry (font = ('Verdana', 16), width = 7)
tamamDüğmesi = Button (text = 'Tamam', font = ('Verdana', 16), command = fahrenhaytaÇevir)

mesajEtiketi.grid (row = 0, column = 0)
içerik.grid (row = 0, column = 1)
tamamDüğmesi.grid (row = 0, column = 2)
çıktıEtiketi.grid (row = 1, column = 0, columnspan=3)

mainloop() # Programı başlatan döngü...
