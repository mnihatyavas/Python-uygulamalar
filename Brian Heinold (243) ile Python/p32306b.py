# coding:iso-8859-9 Türkçe

from tkinter import *

kök = Tk()
kök.title ("Değişken argümanlı bileşenler")

def sayaç():
    sayaç.kere = sayaç.kere + 1
    etiket.config (text="Düğmeyi <<"+ str(sayaç.kere)+">> kez tıkladınız")

def sıfırla():
    sayaç.kere = 0
    etiket.config (text="   << Sayaç sıfırlandı >>   ")

sayaç.kere = 0
argümanlar = {'fg':'YELLOW', 'bg':'BLACK', 'font':('Verdana', 16, 'bold')}

Button (kök, text="TIKLAYIN LÜTFEN", **argümanlar, command=sayaç).pack()
Button (kök, text="Sayacı Sıfırlayın", **argümanlar, command=sıfırla).pack()
Button (kök, text="ÇIK", **argümanlar, command=quit).pack()

etiket = Label (kök, **argümanlar, pady=20)
etiket.pack()

mainloop()