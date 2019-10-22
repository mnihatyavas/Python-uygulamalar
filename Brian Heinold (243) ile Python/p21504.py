# coding:iso-8859-9 Türkçe

from tkinter import *
Tk()

giriş1 = Label (text="Ad ve soyadınızı girin:")
giriş1.grid (row=0, column=0)
içerik1 = Entry (width=20)
içerik1.insert (0, "M.Nihat Yavaş")
içerik1.grid (row=0, column=1)
içerik11 = içerik1.get()

giriş2 = Label (text="Doğum yılınızı girin:" )
giriş2.grid (row=1, column=0)
içerik2 = Entry (width=10)
içerik2.insert (0, 1957)
içerik2.grid (row=1, column=1)
try: içerik22 = eval (içerik2.get() )
except Exception: içerik22 = 0

sonuç = Label()
sonuç.grid (row=5, column=0)
sonuç.configure (text="Sayın: {}, yaşınız: {}'dir.".format (içerik11, (2018- içerik22)) )

mainloop()
