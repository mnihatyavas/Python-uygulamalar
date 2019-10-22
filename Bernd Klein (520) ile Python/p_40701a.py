# coding:iso-8859-9 T�rk�e
# p_40701a.py: Tek sat�rl�k entry dizgesel veri giri�i �rne�i.

from tkinter import *
from p_315 import Renk

k�k = Tk()
k�k.title ("Entry Veri Giri�i")

def g�ster():
    etiket.config (text="Merhaba {" + giri�1.get() + " " + giri�2.get() + "}", bg=Renk.renk(), fg=Renk.renk() )
    giri�1.delete (0, END) # Ba�tan son endekse kadar t�m�n� siler...
    giri�2.delete (0, END)

�er�eve = Frame (k�k, bg="Cyan" )
�er�eve.pack()

Label (�er�eve, text="Ad�n�z:", bg="Khaki", fg="Purple").grid (row=0, column=0, pady=2)
giri�1 = Entry (�er�eve, bg="Lime", fg="Coral")
giri�1.grid (row=0, column=1)

Label (�er�eve, text="Soyad�n�z", bg="Khaki", fg="Purple").grid (row=1) # Belirtilmeyen varsay�l� column=0
giri�2 = Entry (�er�eve, bg="Lime", fg="Coral")
giri�2.grid (row=1, column=1)

giri�1.insert (0, "M.Nihat")
giri�2.insert (0, "Yava�")

Button (�er�eve, text="G�ster", command=g�ster, bg="black", fg="Yellow").grid (row=3, column=0, sticky=W, pady=4)
Button (�er�eve, text="�IK", command=�er�eve.quit, bg="black", fg="Red").grid(row=3, column=1, sticky=W, pady=4)

etiket = Label (�er�eve)
etiket.grid (row=4, columnspan=2, stick=W, pady=10, padx=2)

k�k.mainloop( )
