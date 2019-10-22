# coding:iso-8859-9 T�rk�e
# p_40702.py: Form doldurma ve g�r�nt�leme �rne�i.

from tkinter import *
from p_315 import Renk

alanlar = ('Soyad�n�z', 'Ad�n�z', 'Mesle�iniz', 'Tabiyetiniz')

def getir (veriGiri�leri):
    metin = ""
    for veri in veriGiri�leri:
        alan = veri [0]
        dizge  = veri [1].get()
        metin += "(" + alan + ": " + dizge + ") "
    etiket.config (text= "[ " + metin [:-1] + " ]", bg=Renk.renk(), fg=Renk.renk() ) 

def veriGiri�Formu (k�k, alanlar):
    veriGiri�leri = []
    for alan in alanlar:
      sat�r = Frame (k�k) # sat�r=�er�eve...
      sat�r.pack (side=TOP, fill=X, padx=5, pady=5)
      yafta = Label (sat�r, width=15, text=alan, anchor='w', bg="Lime", fg="Blue", padx=2)
      yafta.pack (side=LEFT, padx=2)
      girilenVeri = Entry (sat�r, bg="Cyan", fg="FireBrick")
      girilenVeri.pack (side=RIGHT, expand=YES, fill=X)
      veriGiri�leri.append ((alan, girilenVeri))
    return veriGiri�leri

if __name__ == '__main__':
    k�k = Tk()
    k�k.title ("Ba�vuru Formu")
    �er�eve = Frame (k�k, bg="DarkKhaki")
    �er�eve.pack()
    veriGiri�leri = veriGiri�Formu (�er�eve, alanlar)
    k�k.bind ('<Return>', (lambda event, x=veriGiri�leri: getir (x) ) ) # [Ent]="G�ster" olay�...
    d��me1 = Button (�er�eve, text='G�ster', bg="DarkSlateGray", fg="Yellow",
        command=(lambda x=veriGiri�leri: getir (x) ) )
    d��me1.pack (side=LEFT, padx=5, pady=5)
    d��me2 = Button (�er�eve, text='�IK', bg="#ddd", fg="Red",command=k�k.quit)
    d��me2.pack (side=LEFT, padx=5, pady=5)
    etiket = Label (�er�eve)
    etiket.pack(pady=7)

k�k.mainloop( )
