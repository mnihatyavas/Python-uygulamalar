# coding:iso-8859-9 T�rk�e
# p_40501b.py: Radyo d��meleri ve se�ilenin de�erini koyma/alma �rne�i.

from tkinter import *
k�k = Tk()

k�k.title ("Radio D��meleri G�sterisi")
de�er1 = IntVar()

Label (k�k, text="Bir i�ecek se�in:", justify=LEFT).pack()

�er�eve = Frame (k�k, padx=30)
�er�eve.pack() # Radyo butonlar�n� bir grup yapar...

Radiobutton (�er�eve, text="�ay", variable=de�er1, value=1).pack (side=LEFT)
Radiobutton (�er�eve, text="Kahve", variable=de�er1, value=2).pack (side=LEFT)
Radiobutton (�er�eve, text="Kola", variable=de�er1, value=3).pack (side=LEFT)
Radiobutton (�er�eve, text="Ayran", variable=de�er1, value=4).pack (side=LEFT)
Radiobutton (�er�eve, text="Gazoz", variable=de�er1, value=5).pack (side=LEFT)
# �lk a��l��ta varsay�l� se�ilen yok...

Label (k�k, text="-"*66).pack()
#------------------------------------------------------------------------------------------------

de�er2 = IntVar()
de�er2.set (6)  # �lk anda se�ili olan�n de�eri...

diller = [("Python", 1), ("Perl", 2), ("Java", 3), ("C++", 4), ("Java Script", 5), ("MASM", 6)]

def tercihiniz(): print (de�er2.get() ) # DOS pencereye yazacak...

Label (k�k, text="""Tercihiniz olan\nprogramlama dilini se�in:""", justify=CENTER).pack()

for i, dil in enumerate (diller): Radiobutton (k�k, text=dil, padx=2, variable=de�er2, value=(i+1), command=tercihiniz,).pack (anchor=W)
# Radyo d��melerini gruplamay� variable=de�er2 ile sa�lad�...

Label (k�k, text="-"*66).pack()
#------------------------------------------------------------------------------------------------

from p_315 import Renk

de�er3 = IntVar()
de�er3.set (4)

def meyveniz():
    a=de�er3.get()
    etiket.config (text="Buyrun: "+meyveler[a-1]+" ("+str(a)+")", bg=Renk.renk(), fg=Renk.renk() )

Label (k�k, text="Hangi meyveyi isterdiniz?").pack()

meyveler = ["Elma", "Armut", "Muz", "Hurma", "Nar", "Portakal", "Mandalina", "Erik", "�ilek"]
for i, meyve in enumerate (meyveler):
    Radiobutton (k�k, text=meyve, indicatoron=0, width=20, pady=2, variable=de�er3,
            bg="black", fg="orange", command=meyveniz, value=(i+1)).pack ()

etiket = Label (k�k, font=("Segoe Script", 15, "bold") )
etiket.pack (anchor=CENTER)

k�k.mainloop()
