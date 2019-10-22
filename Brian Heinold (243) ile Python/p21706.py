# coding:iso-8859-9 T�rk�e

from tkinter import *
from time import  time
from p21601 import Renk
k�k = Tk()
k�k.title ("Zaman� G�ncelleme")

def saat�G�ncelle():
    global ilk
    zaman = time() - ilk
    saat = int ((zaman % 86400) // 3600)
    dakika = int ((zaman % 3600) // 60)
    saniye = int (zaman % 60)
    etiket.config (text='{:02d}:{:02d}:{:02d}'.format (saat, dakika, saniye) )
    if saniye == 59: etiket.config (bg=Renk.renk(), fg=Renk.renk() ) # Her dakika renk de�i�tirir...
    if saat >= 86400: ilk = time()
    k�k.after (999, saat�G�ncelle) # 999 milisaniyede bir zaman� g�nceller...

if __name__ == "__main__":
    etiket = Label (k�k, font=("arial black", 50, "bold"), bg=Renk.renk(), fg=Renk.renk() )
    etiket.grid()

    ilk = time() # 1970'den beri ge�en zaman� (tamsay� hanesi) saniye olarak verir...
    saat�G�ncelle() # 1 g�nl�k 23:59:59'dan sonra tekrar, saat sayac� 00:00:00'dan ba�lar...

mainloop()
