# coding:iso-8859-9 Türkçe
# p_40704.py: Alınan faizli borcun aylık eşit geri ödeme hesabı örneği.

from tkinter import *
from p_315 import Renk

"""Hesaplama formülleri:
==>r aylık ondalık faizle k ay süresince aylık sabit Ö tutarını ödeme sonrası A ana borç'dan geriye ödenmemiş kalan bakiye:
   B =(1+r)**k*A-((1+r)**k-1)*Ö/r
==>Şayet tüm A borcu ödenecek ve B=0 kalacaksa, n sayıdaki aylık eşit ödeme tutarı:
Ö=r*(1+2)**n*A/((1+r)**n-1)
"""

alanlar = ('Yıllık Faiz', 'Ödeme Adedi', 'Alınan Ana Borç', 'Aylık Geri Ödeme', 'Kalan Bakiye')

def aylıkÖdeme (girilenler):
    if girilenler ["Alınan Ana Borç"].get() == "0": return
    r = (float (girilenler ['Yıllık Faiz'].get() ) / 100) / 12 #Aylık ondalık faiz...
    borç = float (girilenler ['Alınan Ana Borç'].get() )
    n =  float (girilenler ['Ödeme Adedi'].get() )
    kalan = float (girilenler ['Kalan Bakiye'].get() )
    b = (1 + r)** n # Birikimli bileşik faiz...
    aylıkÖdeme = r * ( (b * borç - kalan) / ( b - 1 ) )
    girilenler ['Aylık Geri Ödeme'].delete (0, END)
    girilenler ['Aylık Geri Ödeme'].insert (0, ("%8.2f" % (aylıkÖdeme) ).strip() )
    print ("\nAylık ondalık faiz:", r)
    print ("Aylık Geri Ödeme: %8.2f" % (aylıkÖdeme) )

def kalanBakiye (girilenler):
    if girilenler ["Alınan Ana Borç"].get() == "0": return
    r = (float (girilenler ['Yıllık Faiz'].get() ) / 100) / 12 # Aylık ondalık faiz...
    borç = float (girilenler ['Alınan Ana Borç'].get() )
    n =  float (girilenler ['Ödeme Adedi'].get() )
    b = (1 + r)**n # Birikimli bileşik faiz...
    aylıkÖdeme = float (girilenler ['Aylık Geri Ödeme'].get() )
    kalan = b * borç  - ( (b - 1) / r) * aylıkÖdeme
    girilenler ['Kalan Bakiye'].delete (0, END)
    girilenler ['Kalan Bakiye'].insert (0, ("%8.2f" % (kalan) ).strip() )
    print ("\nAylık ondalık faiz:", r)
    print ("Kalan Bakiye: %8.2f" % (kalan) )

def getir (veriGirişleri):
    print()
    for _ in range (len (veriGirişleri) ): print ('%s: %s' % (alanlar [_], veriGirişleri [ alanlar [_] ].get() ))

def formYarat (kök, alanlar):
    girilenler = {}
    for alan in alanlar:
        satır = Frame (kök)
        satır.pack (side=TOP, fill=X, padx=5, pady=5)
        etiket = Label (satır, width=22, text=alan+": ", anchor='w', bg="Navy", fg="Yellow")
        etiket.pack (side=LEFT, padx=1)
        veri = Entry (satır, bg="DarkGreen", fg="Pink")
        veri.pack (side=RIGHT, expand=YES, fill=X)
        veri.insert (0,"0")
        girilenler [alan] = veri
    return girilenler

if __name__ == '__main__':
    kök = Tk()
    kök.title ("Aylık Eşit Borç Ödeme")
    çerçeve = Frame (kök, bg=Renk.renk() )
    çerçeve.pack()
    veriler = formYarat (çerçeve, alanlar)
    kök.bind ('<Return>', (lambda event, x=veriler: getir (x)) )
    düğme1 = Button (çerçeve, text='Kalan Bakiye', bg="Black", fg="Cyan",
          command=(lambda x=veriler: kalanBakiye (x)) )
    düğme1.pack (side=LEFT, padx=5, pady=5)
    düğme2 = Button (çerçeve, text='Aylık Geri Ödeme', bg="Black", fg="Cyan",
          command=(lambda x=veriler: aylıkÖdeme (x)) )
    düğme2.pack (side=LEFT, padx=5, pady=5)
    düğme3 = Button (çerçeve, text='ÇIK',  bg="Brown", fg="Yellow",command=kök.quit)
    düğme3.pack (side=LEFT, padx=5, pady=5)
    kök.mainloop()



"""Çıktı:
>python p_40704.py

Aylık ondalık faiz: 0.020833333333333332
Aylık Geri Ödeme:  1619.16

Aylık ondalık faiz: 0.020833333333333332
Kalan Bakiye:     0.12

Yıllık Faiz: 25
Ödeme Adedi: 50
Alınan Ana Borç: 50000
Aylık Geri Ödeme: 1619.16
Kalan Bakiye: 0.12
"""