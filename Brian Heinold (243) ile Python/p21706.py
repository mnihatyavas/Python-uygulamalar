# coding:iso-8859-9 Türkçe

from tkinter import *
from time import  time
from p21601 import Renk
kök = Tk()
kök.title ("Zamanı Güncelleme")

def saatıGüncelle():
    global ilk
    zaman = time() - ilk
    saat = int ((zaman % 86400) // 3600)
    dakika = int ((zaman % 3600) // 60)
    saniye = int (zaman % 60)
    etiket.config (text='{:02d}:{:02d}:{:02d}'.format (saat, dakika, saniye) )
    if saniye == 59: etiket.config (bg=Renk.renk(), fg=Renk.renk() ) # Her dakika renk değiştirir...
    if saat >= 86400: ilk = time()
    kök.after (999, saatıGüncelle) # 999 milisaniyede bir zamanı günceller...

if __name__ == "__main__":
    etiket = Label (kök, font=("arial black", 50, "bold"), bg=Renk.renk(), fg=Renk.renk() )
    etiket.grid()

    ilk = time() # 1970'den beri geçen zamanı (tamsayı hanesi) saniye olarak verir...
    saatıGüncelle() # 1 günlük 23:59:59'dan sonra tekrar, saat sayacı 00:00:00'dan başlar...

mainloop()
