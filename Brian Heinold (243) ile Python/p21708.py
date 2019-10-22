# coding:iso-8859-9 T�rk�e

from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter.filedialog import *

k�k = Tk()
k�k.title ("Men� Olu�turma")

def dosyaA�():
    global metin
    dosyaAd�=askopenfilename (initialdir='C:/Users/pc/Desktop/MyFiles/4. Dersler/python/')
    k�k.title (dosyaAd�)
    metin = open (dosyaAd�).read()
    metinKutusu.config (width=120, height=20)
    if metinKutusu.get (1.0, END) != "": metinKutusu.delete (1.0, END)
    metinKutusu.insert (1.0, metin)

def yeniAdlaSakla():
    global metin
    dosyaAd� = asksaveasfilename (initialdir='C:/Users/pc/Desktop/MyFiles/4. Dersler/python/')
    if dosyaAd� != '' and metin !="": open (dosyaAd�, "w").write (metin) # Ayn� adl� dosya mevcutsa, �zerine yazacak...

if __name__ == "__main__":
    metin = ""

    metinKutusu = ScrolledText (k�k, width=20, height=5)
    metinKutusu.pack()

    men� = Menu (k�k) # Men� yarat�ld�...
    k�k.config (menu=men�) # k�k men� �ubu�una kuruldu...

    dosyaMen�s� = Menu (men�, tearoff=0) # Men� birimleri kuruluyor...
    dosyaMen�s�.add_command (label='Dosya A�', command=dosyaA�)
    dosyaMen�s�.add_command (label='Yeni Adla Sakla', command=yeniAdlaSakla)
    dosyaMen�s�.add_separator()
    dosyaMen�s�.add_command (label='��k', command=k�k.quit)

    men�.add_cascade (label='Dosya', menu=dosyaMen�s�) # Men� birimleri men�'ye eklendi...

mainloop()
