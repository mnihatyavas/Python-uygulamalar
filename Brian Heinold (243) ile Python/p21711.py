# coding:iso-8859-9 T�rk�e

from tkinter import *
from p21601 import Renk
k�k = Tk()
k�k.title ("Bile�en text de�i�ikli�i")

def selamla�ma():
    global saya�
    etiket.config (fg=Renk.renk(), bg=Renk.renk())
    dizgeDe�i�keni1.set ('Merhaba, sizle kar��la�mak ne g�zel bir tesad�f!..\n'\
        if saya�%2==0 else 'Ho��akal�n, yak�n zamanda in�allah tekrar g�r��mek dile�iyle!..\n')
    dizgeDe�i�keni2.set ('Selamla�ma' if saya�%2==0 else 'Vedala�ma')
    saya� +=1

if __name__ == "__main__":
    saya� = 0
    dizgeDe�i�keni1 = StringVar()
    dizgeDe�i�keni2 = StringVar()
    dizgeDe�i�keni2.set ("T�kla")

    etiket = Label (textvariable=dizgeDe�i�keni1, font=("segoe script", 25, "italic bold") )
    etiket.pack()

    Button (textvariable=dizgeDe�i�keni2, font=("serif", 30), bg="black", fg="yellow", command = selamla�ma).pack(fill=X, expand=YES)

mainloop()
