# coding:iso-8859-9 Türkçe
# p_40301b.py: Butonlarla slogan, sayaç ve program sonlandırma örneği.

from tkinter import *
from p_315 import Renk

kök=Tk()
kök.title ("Sloganlı Saniyeler")

def sloganıYaz (fiş, a):
    #print (a)
    fiş.config (text=a, bg=Renk.renk(), fg=Renk.renk() )

def sayacıBaşlat (yafta):
    def say():
        global sayaç
        sayaç +=1
        yafta.config (text=str (sayaç), bg=Renk.renk(), fg=Renk.renk() )
        yafta.after (1000, say)
    say()

çerçeve = Frame (kök, bg=Renk.renk())
çerçeve.pack()

etiket1 = Label (çerçeve, font=("segoe script",12))
etiket1.pack()

Button (çerçeve,
    text="Programdan\nÇıkalım",
    pady=10,
    bg="Yellow",
    fg="red",
    command=quit).pack (side=LEFT)
Button (çerçeve,
    text="Merhaba\nDiyelim",
    bg="Blue",
    fg="Gold",
    command=lambda x="Tkinter, kullanımı oldukca kolay bir GUI-GrafikselKullanıcıArayüzüdür!" : sloganıYaz (etiket1, x)).pack (side=LEFT)
#-------------------------------------------------------------------------------------------------

sayaç = 0

etiket2 = Label (çerçeve, font=("arial black", 100, "bold") )
etiket2.pack()

Button (çerçeve,
    text="Sayacı\nBaşlatalım",
    bg="DarkKhaki",
    fg="Lime",
    command=lambda : sayacıBaşlat (etiket2)).pack(side=BOTTOM)

mainloop()
