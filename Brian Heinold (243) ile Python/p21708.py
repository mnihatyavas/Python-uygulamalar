# coding:iso-8859-9 Türkçe

from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter.filedialog import *

kök = Tk()
kök.title ("Menü Oluşturma")

def dosyaAç():
    global metin
    dosyaAdı=askopenfilename (initialdir='C:/Users/pc/Desktop/MyFiles/4. Dersler/python/')
    kök.title (dosyaAdı)
    metin = open (dosyaAdı).read()
    metinKutusu.config (width=120, height=20)
    if metinKutusu.get (1.0, END) != "": metinKutusu.delete (1.0, END)
    metinKutusu.insert (1.0, metin)

def yeniAdlaSakla():
    global metin
    dosyaAdı = asksaveasfilename (initialdir='C:/Users/pc/Desktop/MyFiles/4. Dersler/python/')
    if dosyaAdı != '' and metin !="": open (dosyaAdı, "w").write (metin) # Aynı adlı dosya mevcutsa, üzerine yazacak...

if __name__ == "__main__":
    metin = ""

    metinKutusu = ScrolledText (kök, width=20, height=5)
    metinKutusu.pack()

    menü = Menu (kök) # Menü yaratıldı...
    kök.config (menu=menü) # kök menü çubuğuna kuruldu...

    dosyaMenüsü = Menu (menü, tearoff=0) # Menü birimleri kuruluyor...
    dosyaMenüsü.add_command (label='Dosya Aç', command=dosyaAç)
    dosyaMenüsü.add_command (label='Yeni Adla Sakla', command=yeniAdlaSakla)
    dosyaMenüsü.add_separator()
    dosyaMenüsü.add_command (label='Çık', command=kök.quit)

    menü.add_cascade (label='Dosya', menu=dosyaMenüsü) # Menü birimleri menü'ye eklendi...

mainloop()
