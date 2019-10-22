# coding:iso-8859-9 T�rk�e
# p_40701b.py: �oklu kolonlarla veri giri�i, silme ve g�sterme �rne�i.

from tkinter import *
from p_315 import Renk

k�k=Tk()
k�k.title ("Entry G�sterisi")

def ��kt� (olay): # k�k.bind varsay�l� bir arg�man gerektiriyor...
    etiket.config (text="Say�n, {} {}, do�um y�l�n�z: {:d}'dir."\
        .format (gir1.get(), gir2.get(), (2019 - eval (gir3.get() ))),
        bg=Renk.renk(), fg=Renk.renk())

def sil():
    gir1.delete (0, END)
    gir2.delete (0, END)
    gir3.delete (0, END)
    gir3.insert (0, 0)

�er�eve = Frame (k�k, bg=Renk.renk() )
�er�eve.pack()

Label (�er�eve, text="Ad�n�z: ", width=8, anchor=W, bg="Khaki", fg="Blue").grid (row=0, pady=2, padx=2)
Label (�er�eve, text="Soyad�n�z: ", width=8, anchor=W, bg="Khaki", fg="Blue").grid (row=1, pady=2, padx=2)
Label (�er�eve, text="Ya��n�z: ", width=8, anchor=W, bg="Khaki", fg="Blue").grid (row=2, pady=5, padx=2)

gir1 = Entry (�er�eve, fg="Khaki", bg="DarkGreen")
gir2 = Entry (�er�eve, fg="Khaki", bg="DarkGreen")
gir3 = Entry (�er�eve, fg="Khaki", bg="DarkGreen")
gir1.grid (row=0, column=1)
gir2.grid (row=1, column=1)
gir3.grid (row=2, column=1)
gir3.insert (0, 0)

etiket = Label (�er�eve)

k�k.bind ("<Return>", ��kt�) # Hem [Ent] hem d��me ile...
Button (�er�eve, text="G�ster", command=(lambda x="":��kt�(x)), fg="Yellow", bg="Black").grid (row=3, column=0)
Button (�er�eve, text="Sil", command=sil, fg="Yellow", bg="Black").grid (row=3, column=1)
Button (�er�eve, text="�IK", command=�er�eve.quit, bg="FireBrick", fg="Yellow").grid (row=3, column=2)

etiket.grid (row=4, columnspan=3, pady=5) # etiket tan�m �stte, konumlama d��meler alt�nda...

k�k.mainloop()
