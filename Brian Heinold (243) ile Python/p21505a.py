# coding:iso-8859-9 Türkçe

from tkinter import *
from random import randint
Tk()

def yaşıHesapla ():
    sonuç = Label (fg="green", font=("arial", 20, "italic"))
    sonuç.grid (row=3, column=0, pady=15)
    içerik11 = içerik1.get()
    try: içerik22 = eval (içerik2.get() )
    except Exception: içerik22 = randint (1900, 2017)
    sonuç.configure (text="Sayın: {}, yaşınız: {}'dir.".format (içerik11, (2018- içerik22)) )
    içerik1.delete (0, END)
    içerik2.delete (0, END)

giriş1 = Label (text="Ad ve soyadınızı girin:", font=(15))
giriş1.grid (row=0, column=0)
içerik1 = Entry (width=25)
içerik1.insert (0, "M.Nihat Yavaş")
içerik1.grid (row=0, column=1)

giriş2 = Label (text="Doğum yılınızı girin:", font=(15))
giriş2.grid (row=1, column=0)
içerik2 = Entry (width=10)
içerik2.insert (0, 1957)
içerik2.grid (row=1, column=1)

düğme = Button (text='Tıkla Beni', command = yaşıHesapla, bg="red", fg="yellow")
düğme.grid (row=2, column=0, columnspan=2, pady=10)

mainloop()
