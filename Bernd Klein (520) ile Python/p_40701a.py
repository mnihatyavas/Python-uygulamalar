# coding:iso-8859-9 Türkçe
# p_40701a.py: Tek satırlık entry dizgesel veri girişi örneği.

from tkinter import *
from p_315 import Renk

kök = Tk()
kök.title ("Entry Veri Girişi")

def göster():
    etiket.config (text="Merhaba {" + giriş1.get() + " " + giriş2.get() + "}", bg=Renk.renk(), fg=Renk.renk() )
    giriş1.delete (0, END) # Baştan son endekse kadar tümünü siler...
    giriş2.delete (0, END)

çerçeve = Frame (kök, bg="Cyan" )
çerçeve.pack()

Label (çerçeve, text="Adınız:", bg="Khaki", fg="Purple").grid (row=0, column=0, pady=2)
giriş1 = Entry (çerçeve, bg="Lime", fg="Coral")
giriş1.grid (row=0, column=1)

Label (çerçeve, text="Soyadınız", bg="Khaki", fg="Purple").grid (row=1) # Belirtilmeyen varsayılı column=0
giriş2 = Entry (çerçeve, bg="Lime", fg="Coral")
giriş2.grid (row=1, column=1)

giriş1.insert (0, "M.Nihat")
giriş2.insert (0, "Yavaş")

Button (çerçeve, text="Göster", command=göster, bg="black", fg="Yellow").grid (row=3, column=0, sticky=W, pady=4)
Button (çerçeve, text="ÇIK", command=çerçeve.quit, bg="black", fg="Red").grid(row=3, column=1, sticky=W, pady=4)

etiket = Label (çerçeve)
etiket.grid (row=4, columnspan=2, stick=W, pady=10, padx=2)

kök.mainloop( )
