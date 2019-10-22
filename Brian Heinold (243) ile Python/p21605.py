# coding:iso-8859-9 T�rk�e

from tkinter import *
Tk()

def kontrol1(a):
    mesaj ("-"*30, 2)
    if a.get() == 1: mesaj ("�entikli kutu �ENT�KLEND�", 3)
    else: mesaj ("�entikli kutu �ENT�KS�ZLEND�", 3)

def kontrol2 (a):
    mesaj ("-"*30, 4)
    if a.get() == 1: mesaj ("KIRMIZI radyo butonu se�ildi", 5)
    elif a.get() == 2: mesaj ("YE��L radyo butonu se�ildi", 5)
    elif a.get() == 3: mesaj ("MAV� radyo butonu se�ildi", 5)
    else: mesaj ("Se�ili radyo butonu YOK", 5)

def mesaj (mesaj, sat�r):
    etiket = Label (text=mesaj)
    etiket.grid (row=sat�r, column=0, columnspan=3)

toplamlar�n�G�ster = IntVar()
�entikliKutu = Checkbutton (text='Toplamlar�n� g�ster', var=toplamlar�n�G�ster,
    command=lambda x=toplamlar�n�G�ster: kontrol1(x) )
�entikliKutu.grid (row=0, column=0, columnspan=3)

toplamlar�n�G�ster.set (1)

hangiRenk = IntVar()
k�rm�z�D��me = Radiobutton (text='K�rm�z�', var=hangiRenk, value=1,
    command=lambda x=hangiRenk: kontrol2 (x))
ye�ilD��me = Radiobutton (text='Ye�il', var=hangiRenk, value=2,
    command=lambda x=hangiRenk: kontrol2 (x))
maviD��me = Radiobutton (text='Mavi', var=hangiRenk, value=3,
    command=lambda x=hangiRenk: kontrol2 (x))
k�rm�z�D��me.grid (row=1, column=0)
ye�ilD��me.grid (row=1, column=1)
maviD��me.grid (row=1, column=2)
hangiRenk.set (2)

mainloop()
