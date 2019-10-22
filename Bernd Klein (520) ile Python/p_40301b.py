# coding:iso-8859-9 T�rk�e
# p_40301b.py: Butonlarla slogan, saya� ve program sonland�rma �rne�i.

from tkinter import *
from p_315 import Renk

k�k=Tk()
k�k.title ("Sloganl� Saniyeler")

def slogan�Yaz (fi�, a):
    #print (a)
    fi�.config (text=a, bg=Renk.renk(), fg=Renk.renk() )

def sayac�Ba�lat (yafta):
    def say():
        global saya�
        saya� +=1
        yafta.config (text=str (saya�), bg=Renk.renk(), fg=Renk.renk() )
        yafta.after (1000, say)
    say()

�er�eve = Frame (k�k, bg=Renk.renk())
�er�eve.pack()

etiket1 = Label (�er�eve, font=("segoe script",12))
etiket1.pack()

Button (�er�eve,
    text="Programdan\n��kal�m",
    pady=10,
    bg="Yellow",
    fg="red",
    command=quit).pack (side=LEFT)
Button (�er�eve,
    text="Merhaba\nDiyelim",
    bg="Blue",
    fg="Gold",
    command=lambda x="Tkinter, kullan�m� oldukca kolay bir GUI-GrafikselKullan�c�Aray�z�d�r!" : slogan�Yaz (etiket1, x)).pack (side=LEFT)
#-------------------------------------------------------------------------------------------------

saya� = 0

etiket2 = Label (�er�eve, font=("arial black", 100, "bold") )
etiket2.pack()

Button (�er�eve,
    text="Sayac�\nBa�latal�m",
    bg="DarkKhaki",
    fg="Lime",
    command=lambda : sayac�Ba�lat (etiket2)).pack(side=BOTTOM)

mainloop()
