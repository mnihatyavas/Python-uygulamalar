# coding:iso-8859-9 T�rk�e

from p21604 import renk
from random import randint
from tkinter import *
k�k = Tk()

tuval_eni = 400
tuval_boyu = 100

tuval = Canvas (k�k, 
    width=tuval_eni,
    height=tuval_boyu,
    bg=renk[randint(0,1000)] )
tuval.pack() # tuval.grid (row=0, column=0)

y = int (tuval_boyu / 2)
tuval.create_line (0, y, tuval_eni, y, width=3, fill=renk[randint(0,1000)])

k�k.mainloop()
