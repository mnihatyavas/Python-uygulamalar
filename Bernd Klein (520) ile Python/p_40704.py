# coding:iso-8859-9 T�rk�e
# p_40704.py: Al�nan faizli borcun ayl�k e�it geri �deme hesab� �rne�i.

from tkinter import *
from p_315 import Renk

"""Hesaplama form�lleri:
==>r ayl�k ondal�k faizle k ay s�resince ayl�k sabit � tutar�n� �deme sonras� A ana bor�'dan geriye �denmemi� kalan bakiye:
   B =(1+r)**k*A-((1+r)**k-1)*�/r
==>�ayet t�m A borcu �denecek ve B=0 kalacaksa, n say�daki ayl�k e�it �deme tutar�:
�=r*(1+2)**n*A/((1+r)**n-1)
"""

alanlar = ('Y�ll�k Faiz', '�deme Adedi', 'Al�nan Ana Bor�', 'Ayl�k Geri �deme', 'Kalan Bakiye')

def ayl�k�deme (girilenler):
    if girilenler ["Al�nan Ana Bor�"].get() == "0": return
    r = (float (girilenler ['Y�ll�k Faiz'].get() ) / 100) / 12 #Ayl�k ondal�k faiz...
    bor� = float (girilenler ['Al�nan Ana Bor�'].get() )
    n =  float (girilenler ['�deme Adedi'].get() )
    kalan = float (girilenler ['Kalan Bakiye'].get() )
    b = (1 + r)** n # Birikimli bile�ik faiz...
    ayl�k�deme = r * ( (b * bor� - kalan) / ( b - 1 ) )
    girilenler ['Ayl�k Geri �deme'].delete (0, END)
    girilenler ['Ayl�k Geri �deme'].insert (0, ("%8.2f" % (ayl�k�deme) ).strip() )
    print ("\nAyl�k ondal�k faiz:", r)
    print ("Ayl�k Geri �deme: %8.2f" % (ayl�k�deme) )

def kalanBakiye (girilenler):
    if girilenler ["Al�nan Ana Bor�"].get() == "0": return
    r = (float (girilenler ['Y�ll�k Faiz'].get() ) / 100) / 12 # Ayl�k ondal�k faiz...
    bor� = float (girilenler ['Al�nan Ana Bor�'].get() )
    n =  float (girilenler ['�deme Adedi'].get() )
    b = (1 + r)**n # Birikimli bile�ik faiz...
    ayl�k�deme = float (girilenler ['Ayl�k Geri �deme'].get() )
    kalan = b * bor�  - ( (b - 1) / r) * ayl�k�deme
    girilenler ['Kalan Bakiye'].delete (0, END)
    girilenler ['Kalan Bakiye'].insert (0, ("%8.2f" % (kalan) ).strip() )
    print ("\nAyl�k ondal�k faiz:", r)
    print ("Kalan Bakiye: %8.2f" % (kalan) )

def getir (veriGiri�leri):
    print()
    for _ in range (len (veriGiri�leri) ): print ('%s: %s' % (alanlar [_], veriGiri�leri [ alanlar [_] ].get() ))

def formYarat (k�k, alanlar):
    girilenler = {}
    for alan in alanlar:
        sat�r = Frame (k�k)
        sat�r.pack (side=TOP, fill=X, padx=5, pady=5)
        etiket = Label (sat�r, width=22, text=alan+": ", anchor='w', bg="Navy", fg="Yellow")
        etiket.pack (side=LEFT, padx=1)
        veri = Entry (sat�r, bg="DarkGreen", fg="Pink")
        veri.pack (side=RIGHT, expand=YES, fill=X)
        veri.insert (0,"0")
        girilenler [alan] = veri
    return girilenler

if __name__ == '__main__':
    k�k = Tk()
    k�k.title ("Ayl�k E�it Bor� �deme")
    �er�eve = Frame (k�k, bg=Renk.renk() )
    �er�eve.pack()
    veriler = formYarat (�er�eve, alanlar)
    k�k.bind ('<Return>', (lambda event, x=veriler: getir (x)) )
    d��me1 = Button (�er�eve, text='Kalan Bakiye', bg="Black", fg="Cyan",
          command=(lambda x=veriler: kalanBakiye (x)) )
    d��me1.pack (side=LEFT, padx=5, pady=5)
    d��me2 = Button (�er�eve, text='Ayl�k Geri �deme', bg="Black", fg="Cyan",
          command=(lambda x=veriler: ayl�k�deme (x)) )
    d��me2.pack (side=LEFT, padx=5, pady=5)
    d��me3 = Button (�er�eve, text='�IK',  bg="Brown", fg="Yellow",command=k�k.quit)
    d��me3.pack (side=LEFT, padx=5, pady=5)
    k�k.mainloop()



"""��kt�:
>python p_40704.py

Ayl�k ondal�k faiz: 0.020833333333333332
Ayl�k Geri �deme:  1619.16

Ayl�k ondal�k faiz: 0.020833333333333332
Kalan Bakiye:     0.12

Y�ll�k Faiz: 25
�deme Adedi: 50
Al�nan Ana Bor�: 50000
Ayl�k Geri �deme: 1619.16
Kalan Bakiye: 0.12
"""