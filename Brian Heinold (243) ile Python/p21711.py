# coding:iso-8859-9 Türkçe

from tkinter import *
from p21601 import Renk
kök = Tk()
kök.title ("Bileşen text değişikliği")

def selamlaşma():
    global sayaç
    etiket.config (fg=Renk.renk(), bg=Renk.renk())
    dizgeDeğişkeni1.set ('Merhaba, sizle karşılaşmak ne güzel bir tesadüf!..\n'\
        if sayaç%2==0 else 'Hoşçakalın, yakın zamanda inşallah tekrar görüşmek dileğiyle!..\n')
    dizgeDeğişkeni2.set ('Selamlaşma' if sayaç%2==0 else 'Vedalaşma')
    sayaç +=1

if __name__ == "__main__":
    sayaç = 0
    dizgeDeğişkeni1 = StringVar()
    dizgeDeğişkeni2 = StringVar()
    dizgeDeğişkeni2.set ("Tıkla")

    etiket = Label (textvariable=dizgeDeğişkeni1, font=("segoe script", 25, "italic bold") )
    etiket.pack()

    Button (textvariable=dizgeDeğişkeni2, font=("serif", 30), bg="black", fg="yellow", command = selamlaşma).pack(fill=X, expand=YES)

mainloop()
