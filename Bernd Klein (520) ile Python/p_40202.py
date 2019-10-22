# coding:iso-8859-9 T�rk�e
# p_40202.py: Message bile�eni ve parametrelerinin geli�ig�zel de�i�tirilmesi �rne�i.

from tkinter import *
from p_315 import Renk
from random import randint

k�k=Tk()

def de�i�tir():
    global �er�eve, hizala
    mesaj.config (font=('segoe script', 20, 'normal'),
        bg=Renk.renk(), fg=Renk.renk(),
        width=randint (275,1200),
        justify=hizala [randint (0, 2)],
        bd=randint (1,10), relief=�er�eve [randint (0, 4)])

bo�deyi� = """Yap�lagelen �eylerin hi�bir �nemi yoktur, �nemli olan yap�lagiden �eylerle \
    bo�u-bo�una ve de hi�i-hi�ine etkile�im ve kat�l�m halinde vakit ge�irerek kendini \
    s�r�nd�rebilmendir.\n\n(M.Nihat Yava�)"""
mesaj = Message (k�k, text=bo�deyi�, anchor=CENTER, padx=5, pady=5)
mesaj.pack()

Button (k�k, text="DE���T�R", bg="black", fg="yellow", command=de�i�tir).pack()

hizala = [LEFT, RIGHT, CENTER]
�er�eve = [FLAT, SUNKEN, RAISED, GROOVE, RIDGE]

mainloop()
