# coding:iso-8859-9 Türkçe
# p_40804.py: Canvas tuvalinde iri noktayla yazı yazma örneği.

from tkinter import *
from p_315 import Renk

renk = Renk.renk()
def çemberÇiz (t, x,y, r=3):
    çember = t.create_oval (x-r,y-r, x+r,y+r, fill=renk)
    return çember

def yaz (olay):
    x = olay.x
    y = olay.y
    çemberÇiz (tuval, x,y)

kök = Tk()
kök.title ("TuvaldeYuvarlak Ovalle Çizmek-1")

çerçeve = Frame (kök, bg=Renk.renk() )
çerçeve.pack()

tuvalEni = 500
tuvalBoyu = 200
tuval = Canvas (çerçeve, bg=Renk.renk(), width=tuvalEni, height=tuvalBoyu)
tuval.pack()

tuval.bind ("<B1-Motion>", yaz)

Label (çerçeve, text = "Sabit ebatlı tuvalde, basılı fareyi sürükleyerek istediğini yaz-çiz:", bg="Black", fg="Yellow" ).pack()
Button (çerçeve, text="ÇIK", font=('Arial', 15, 'bold'), bg="Lime", fg="FireBrick", command=kök.destroy).pack(side = BOTTOM)

kök.mainloop()
#-------------------------------------------------------------------------------------------------------

kök = Tk()
kök.title ("TuvaldeYuvarlak Ovalle Çizmek-2")

tuval = Canvas (kök, bg=Renk.renk() )
tuval.pack (expand=YES, fill=BOTH)

tuval.bind ("<B1-Motion>", (lambda olay: yaz (olay) ) )

Label (tuval, text = "Pencereyi ara-sıra genişleterek, basılı fareyle istediğini yaz-çiz:", bg="Black", fg="Yellow" ).pack()
Button (tuval, text="ÇIK", font=('Arial', 15, 'bold'), bg="Lime", fg="FireBrick", command=kök.destroy).pack (side = BOTTOM)

kök.mainloop()
