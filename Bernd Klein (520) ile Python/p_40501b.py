# coding:iso-8859-9 Türkçe
# p_40501b.py: Radyo düğmeleri ve seçilenin değerini koyma/alma örneği.

from tkinter import *
kök = Tk()

kök.title ("Radio Düğmeleri Gösterisi")
değer1 = IntVar()

Label (kök, text="Bir içecek seçin:", justify=LEFT).pack()

çerçeve = Frame (kök, padx=30)
çerçeve.pack() # Radyo butonlarını bir grup yapar...

Radiobutton (çerçeve, text="Çay", variable=değer1, value=1).pack (side=LEFT)
Radiobutton (çerçeve, text="Kahve", variable=değer1, value=2).pack (side=LEFT)
Radiobutton (çerçeve, text="Kola", variable=değer1, value=3).pack (side=LEFT)
Radiobutton (çerçeve, text="Ayran", variable=değer1, value=4).pack (side=LEFT)
Radiobutton (çerçeve, text="Gazoz", variable=değer1, value=5).pack (side=LEFT)
# İlk açılışta varsayılı seçilen yok...

Label (kök, text="-"*66).pack()
#------------------------------------------------------------------------------------------------

değer2 = IntVar()
değer2.set (6)  # İlk anda seçili olanın değeri...

diller = [("Python", 1), ("Perl", 2), ("Java", 3), ("C++", 4), ("Java Script", 5), ("MASM", 6)]

def tercihiniz(): print (değer2.get() ) # DOS pencereye yazacak...

Label (kök, text="""Tercihiniz olan\nprogramlama dilini seçin:""", justify=CENTER).pack()

for i, dil in enumerate (diller): Radiobutton (kök, text=dil, padx=2, variable=değer2, value=(i+1), command=tercihiniz,).pack (anchor=W)
# Radyo düğmelerini gruplamayı variable=değer2 ile sağladı...

Label (kök, text="-"*66).pack()
#------------------------------------------------------------------------------------------------

from p_315 import Renk

değer3 = IntVar()
değer3.set (4)

def meyveniz():
    a=değer3.get()
    etiket.config (text="Buyrun: "+meyveler[a-1]+" ("+str(a)+")", bg=Renk.renk(), fg=Renk.renk() )

Label (kök, text="Hangi meyveyi isterdiniz?").pack()

meyveler = ["Elma", "Armut", "Muz", "Hurma", "Nar", "Portakal", "Mandalina", "Erik", "Çilek"]
for i, meyve in enumerate (meyveler):
    Radiobutton (kök, text=meyve, indicatoron=0, width=20, pady=2, variable=değer3,
            bg="black", fg="orange", command=meyveniz, value=(i+1)).pack ()

etiket = Label (kök, font=("Segoe Script", 15, "bold") )
etiket.pack (anchor=CENTER)

kök.mainloop()
