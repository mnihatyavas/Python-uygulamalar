# coding:iso-8859-9 Türkçe

from tkinter import *
Tk()

def kontrol1(a):
    mesaj ("-"*30, 2)
    if a.get() == 1: mesaj ("Çentikli kutu ÇENTİKLENDİ", 3)
    else: mesaj ("Çentikli kutu ÇENTİKSİZLENDİ", 3)

def kontrol2 (a):
    mesaj ("-"*30, 4)
    if a.get() == 1: mesaj ("KIRMIZI radyo butonu seçildi", 5)
    elif a.get() == 2: mesaj ("YEŞİL radyo butonu seçildi", 5)
    elif a.get() == 3: mesaj ("MAVİ radyo butonu seçildi", 5)
    else: mesaj ("Seçili radyo butonu YOK", 5)

def mesaj (mesaj, satır):
    etiket = Label (text=mesaj)
    etiket.grid (row=satır, column=0, columnspan=3)

toplamlarınıGöster = IntVar()
çentikliKutu = Checkbutton (text='Toplamlarını göster', var=toplamlarınıGöster,
    command=lambda x=toplamlarınıGöster: kontrol1(x) )
çentikliKutu.grid (row=0, column=0, columnspan=3)

toplamlarınıGöster.set (1)

hangiRenk = IntVar()
kırmızıDüğme = Radiobutton (text='Kırmızı', var=hangiRenk, value=1,
    command=lambda x=hangiRenk: kontrol2 (x))
yeşilDüğme = Radiobutton (text='Yeşil', var=hangiRenk, value=2,
    command=lambda x=hangiRenk: kontrol2 (x))
maviDüğme = Radiobutton (text='Mavi', var=hangiRenk, value=3,
    command=lambda x=hangiRenk: kontrol2 (x))
kırmızıDüğme.grid (row=1, column=0)
yeşilDüğme.grid (row=1, column=1)
maviDüğme.grid (row=1, column=2)
hangiRenk.set (2)

mainloop()
