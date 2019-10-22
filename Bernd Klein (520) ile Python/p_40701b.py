# coding:iso-8859-9 Türkçe
# p_40701b.py: Çoklu kolonlarla veri girişi, silme ve gösterme örneği.

from tkinter import *
from p_315 import Renk

kök=Tk()
kök.title ("Entry Gösterisi")

def çıktı (olay): # kök.bind varsayılı bir argüman gerektiriyor...
    etiket.config (text="Sayın, {} {}, doğum yılınız: {:d}'dir."\
        .format (gir1.get(), gir2.get(), (2019 - eval (gir3.get() ))),
        bg=Renk.renk(), fg=Renk.renk())

def sil():
    gir1.delete (0, END)
    gir2.delete (0, END)
    gir3.delete (0, END)
    gir3.insert (0, 0)

çerçeve = Frame (kök, bg=Renk.renk() )
çerçeve.pack()

Label (çerçeve, text="Adınız: ", width=8, anchor=W, bg="Khaki", fg="Blue").grid (row=0, pady=2, padx=2)
Label (çerçeve, text="Soyadınız: ", width=8, anchor=W, bg="Khaki", fg="Blue").grid (row=1, pady=2, padx=2)
Label (çerçeve, text="Yaşınız: ", width=8, anchor=W, bg="Khaki", fg="Blue").grid (row=2, pady=5, padx=2)

gir1 = Entry (çerçeve, fg="Khaki", bg="DarkGreen")
gir2 = Entry (çerçeve, fg="Khaki", bg="DarkGreen")
gir3 = Entry (çerçeve, fg="Khaki", bg="DarkGreen")
gir1.grid (row=0, column=1)
gir2.grid (row=1, column=1)
gir3.grid (row=2, column=1)
gir3.insert (0, 0)

etiket = Label (çerçeve)

kök.bind ("<Return>", çıktı) # Hem [Ent] hem düğme ile...
Button (çerçeve, text="Göster", command=(lambda x="":çıktı(x)), fg="Yellow", bg="Black").grid (row=3, column=0)
Button (çerçeve, text="Sil", command=sil, fg="Yellow", bg="Black").grid (row=3, column=1)
Button (çerçeve, text="ÇIK", command=çerçeve.quit, bg="FireBrick", fg="Yellow").grid (row=3, column=2)

etiket.grid (row=4, columnspan=3, pady=5) # etiket tanım üstte, konumlama düğmeler altında...

kök.mainloop()
