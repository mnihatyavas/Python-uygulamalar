# coding:iso-8859-9 T�rk�e
# p_40601.py: �entik kutusuyla cinsiyet, ya� ve medeni durum �oklu se�enek �rne�i.

from tkinter import *
from p_315 import Renk

k�k = Tk()
k�k.title ("�okse�enekli �entik Kutular�")

def g�ster():
    metin = ""
    if de�i�ken1.get() == 1: metin += "Kad�n, " # 0=false/�entiksiz, 1=true/�entikli
    if de�i�ken2.get() == 1: metin += "Erkek, "
    if de�i�ken3.get() == 1: metin += "�ocuk, "
    if de�i�ken4.get() == 1: metin += "Gen�, "
    if de�i�ken5.get() == 1: metin += "Kamil, "
    if de�i�ken6.get() == 1: metin += "Ya�l�, "
    if de�i�ken7.get() == 1: metin += "Bekar, "
    if de�i�ken8.get() == 1: metin += "Evli, "
    if de�i�ken9.get() == 1: metin += "Dul, "
    etiket.config (text=metin, bg=Renk.renk(), fg=Renk.renk() )

�er�eve = Frame (k�k, bg=Renk.renk() )
�er�eve.grid()

Label (�er�eve, text="L�tfen a�a��dakilerden\nenaz birini i�aretleyin:", bg=Renk.renk(), fg=Renk.renk(), font=("Arial", 15, "bold") ).grid (row=0, stick=W, pady=10)

de�i�ken1 = IntVar()
Checkbutton (�er�eve, text="Kad�n", variable=de�i�ken1, fg="Coral", bg="Black" ).grid (row=1, sticky=W)

de�i�ken2 = IntVar()
Checkbutton (�er�eve, text="Erkek", variable=de�i�ken2, fg="Coral", bg="Black" ).grid (row=2, sticky=W)

Label (�er�eve, text="-"*20, bg="Brown", fg="Yellow").grid (row=3, stick=W)

de�i�ken3 = IntVar()
Checkbutton (�er�eve, text="�ocuk", variable=de�i�ken3, fg="Coral", bg="Black" ).grid (row=4, sticky=W)

de�i�ken4 = IntVar()
Checkbutton (�er�eve, text="Gen�", variable=de�i�ken4, fg="Coral", bg="Black" ).grid (row=5, sticky=W)

de�i�ken5 = IntVar()
Checkbutton (�er�eve, text="Kamil", variable=de�i�ken5, fg="Coral", bg="Black" ).grid (row=6, sticky=W)

de�i�ken6 = IntVar()
Checkbutton (�er�eve, text="Ya�l�", variable=de�i�ken6, fg="Coral", bg="Black" ).grid (row=7, sticky=W)

Label (�er�eve, text="-"*20, bg="Brown", fg="Yellow").grid (row=8, stick=W)

de�i�ken7 = IntVar()
Checkbutton (�er�eve, text="Bekar", variable=de�i�ken7, fg="Coral", bg="Black" ).grid (row=9, sticky=W)

de�i�ken8 = IntVar()
Checkbutton (�er�eve, text="Evli", variable=de�i�ken8, fg="Coral", bg="Black" ).grid (row=10, sticky=W)

de�i�ken9 = IntVar()
Checkbutton (�er�eve, text="Dul", variable=de�i�ken9, fg="Coral", bg="Black" ).grid (row=11, sticky=W)

Button (�er�eve, text="Se�ilenleri G�ster", command=g�ster, bg=Renk.renk(), fg=Renk.renk() ).grid (row=12, column=0, sticky=W, pady=5)
Button (�er�eve, text="��k", command=k�k.quit, bg=Renk.renk(), fg=Renk.renk() ).grid (row=12, column=0, pady=5)

etiket = Label (�er�eve, font=("Verdana", 15, "bold") )
etiket.grid (row=13, stick=W)

k�k.mainloop()