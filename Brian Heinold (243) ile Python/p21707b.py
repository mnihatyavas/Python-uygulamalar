# coding:iso-8859-9 Türkçe

from tkinter import *
from tkinter.filedialog import *
from tkinter.scrolledtext import ScrolledText

kök = Tk()
kök.title ("askopenfilename")

def seç():
    kök1 = Tk()
    metinKutusu = ScrolledText (kök1, width=130)
    metinKutusu.pack()

    dosyaAdı=askopenfilename (
            initialdir='C:/Users/pc/Desktop/MyFiles/4. Dersler/python/',
            filetypes=[('Python dosyaları', '*.py'), ('Tüm dizinler', '*')] )
    kök1.title (dosyaAdı)
    metin = open (dosyaAdı).read()
    metinKutusu.insert (1.0, metin)

if __name__ == "__main__":
    Button (kök, text="Dosya Seç", command=seç ).pack()
    Button (kök, text="Çık", command=kök.quit ).pack()

mainloop()
