# coding:iso-8859-9 Türkçe
# p_40301a.py: Tkinter Button ile slogan yazdırma ve saniye sayacı örneği.

import tkinter as tk
from p_315 import Renk

def sloganYaz():
    print ("Tkinter kullanımı çok kolay bir GUI modülüdür!..")
    tk.Label (çerçeve,
        text="Tkinter kullanımı çok kolay bir GUI modülüdür!..",
        bg=Renk.renk(),
        fg=Renk.renk() ).pack()

kök = tk.Tk()
kök.title ("Slogan düğmesi")
çerçeve =  tk.Frame (kök, bg=Renk.renk())
çerçeve.pack()

tk.Button (çerçeve,
    text="ÇIK",
    bg="FireBrick",
    fg="Yellow",
    command=kök.destroy).pack (side=tk.LEFT) # quit arada kapatmıyor...
tk.Button (çerçeve,
    text="Lütfen tıklayın",
    bg="Gold",
    fg="Blue",
    padx=10,
    pady=10,
    command=sloganYaz).pack (side=tk.LEFT)

kök.mainloop()
#-----------------------------------------------------------------------------------------------------

sayaç=0
def sayaçEtiketi (fiş):
    def say():
        global sayaç
        sayaç += 1
        fiş.config (text=str (sayaç), bg=Renk.renk(), fg=Renk.renk() )
        fiş.after (1000, say)
    say()
 
kök = tk.Tk()
kök.title ("Saniye sayacı")
çerçeve = tk.Frame (kök, bg=Renk.renk() )
çerçeve.pack()

etiket = tk.Label (çerçeve, font=("Arial", 100, "bold") )
etiket.pack()

tk.Button (çerçeve, text="Sayacı Başlat", command=lambda:sayaçEtiketi (etiket), bg="#000", fg="MintCream").pack()
# Parametreli fonksiyon komutlarında, arada lambda olmazsa, ilk başta tıklamadan işletir...
tk.Button (çerçeve, text='Programı Sonlandır', width=50, command=kök.quit, bg="#057fb5", fg="#ff0").pack()

kök.mainloop()