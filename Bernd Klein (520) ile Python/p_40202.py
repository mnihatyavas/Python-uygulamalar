# coding:iso-8859-9 Türkçe
# p_40202.py: Message bileşeni ve parametrelerinin gelişigüzel değiştirilmesi örneği.

from tkinter import *
from p_315 import Renk
from random import randint

kök=Tk()

def değiştir():
    global çerçeve, hizala
    mesaj.config (font=('segoe script', 20, 'normal'),
        bg=Renk.renk(), fg=Renk.renk(),
        width=randint (275,1200),
        justify=hizala [randint (0, 2)],
        bd=randint (1,10), relief=çerçeve [randint (0, 4)])

boşdeyiş = """Yapılagelen şeylerin hiçbir önemi yoktur, önemli olan yapılagiden şeylerle \
    boşu-boşuna ve de hiçi-hiçine etkileşim ve katılım halinde vakit geçirerek kendini \
    süründürebilmendir.\n\n(M.Nihat Yavaş)"""
mesaj = Message (kök, text=boşdeyiş, anchor=CENTER, padx=5, pady=5)
mesaj.pack()

Button (kök, text="DEĞİŞTİR", bg="black", fg="yellow", command=değiştir).pack()

hizala = [LEFT, RIGHT, CENTER]
çerçeve = [FLAT, SUNKEN, RAISED, GROOVE, RIDGE]

mainloop()
