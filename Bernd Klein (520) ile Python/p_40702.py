# coding:iso-8859-9 Türkçe
# p_40702.py: Form doldurma ve görüntüleme örneği.

from tkinter import *
from p_315 import Renk

alanlar = ('Soyadınız', 'Adınız', 'Mesleğiniz', 'Tabiyetiniz')

def getir (veriGirişleri):
    metin = ""
    for veri in veriGirişleri:
        alan = veri [0]
        dizge  = veri [1].get()
        metin += "(" + alan + ": " + dizge + ") "
    etiket.config (text= "[ " + metin [:-1] + " ]", bg=Renk.renk(), fg=Renk.renk() ) 

def veriGirişFormu (kök, alanlar):
    veriGirişleri = []
    for alan in alanlar:
      satır = Frame (kök) # satır=çerçeve...
      satır.pack (side=TOP, fill=X, padx=5, pady=5)
      yafta = Label (satır, width=15, text=alan, anchor='w', bg="Lime", fg="Blue", padx=2)
      yafta.pack (side=LEFT, padx=2)
      girilenVeri = Entry (satır, bg="Cyan", fg="FireBrick")
      girilenVeri.pack (side=RIGHT, expand=YES, fill=X)
      veriGirişleri.append ((alan, girilenVeri))
    return veriGirişleri

if __name__ == '__main__':
    kök = Tk()
    kök.title ("Başvuru Formu")
    çerçeve = Frame (kök, bg="DarkKhaki")
    çerçeve.pack()
    veriGirişleri = veriGirişFormu (çerçeve, alanlar)
    kök.bind ('<Return>', (lambda event, x=veriGirişleri: getir (x) ) ) # [Ent]="Göster" olayı...
    düğme1 = Button (çerçeve, text='Göster', bg="DarkSlateGray", fg="Yellow",
        command=(lambda x=veriGirişleri: getir (x) ) )
    düğme1.pack (side=LEFT, padx=5, pady=5)
    düğme2 = Button (çerçeve, text='ÇIK', bg="#ddd", fg="Red",command=kök.quit)
    düğme2.pack (side=LEFT, padx=5, pady=5)
    etiket = Label (çerçeve)
    etiket.pack(pady=7)

kök.mainloop( )
