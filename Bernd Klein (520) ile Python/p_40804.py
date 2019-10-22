# coding:iso-8859-9 T�rk�e
# p_40804.py: Canvas tuvalinde iri noktayla yaz� yazma �rne�i.

from tkinter import *
from p_315 import Renk

renk = Renk.renk()
def �ember�iz (t, x,y, r=3):
    �ember = t.create_oval (x-r,y-r, x+r,y+r, fill=renk)
    return �ember

def yaz (olay):
    x = olay.x
    y = olay.y
    �ember�iz (tuval, x,y)

k�k = Tk()
k�k.title ("TuvaldeYuvarlak Ovalle �izmek-1")

�er�eve = Frame (k�k, bg=Renk.renk() )
�er�eve.pack()

tuvalEni = 500
tuvalBoyu = 200
tuval = Canvas (�er�eve, bg=Renk.renk(), width=tuvalEni, height=tuvalBoyu)
tuval.pack()

tuval.bind ("<B1-Motion>", yaz)

Label (�er�eve, text = "Sabit ebatl� tuvalde, bas�l� fareyi s�r�kleyerek istedi�ini yaz-�iz:", bg="Black", fg="Yellow" ).pack()
Button (�er�eve, text="�IK", font=('Arial', 15, 'bold'), bg="Lime", fg="FireBrick", command=k�k.destroy).pack(side = BOTTOM)

k�k.mainloop()
#-------------------------------------------------------------------------------------------------------

k�k = Tk()
k�k.title ("TuvaldeYuvarlak Ovalle �izmek-2")

tuval = Canvas (k�k, bg=Renk.renk() )
tuval.pack (expand=YES, fill=BOTH)

tuval.bind ("<B1-Motion>", (lambda olay: yaz (olay) ) )

Label (tuval, text = "Pencereyi ara-s�ra geni�leterek, bas�l� fareyle istedi�ini yaz-�iz:", bg="Black", fg="Yellow" ).pack()
Button (tuval, text="�IK", font=('Arial', 15, 'bold'), bg="Lime", fg="FireBrick", command=k�k.destroy).pack (side = BOTTOM)

k�k.mainloop()
