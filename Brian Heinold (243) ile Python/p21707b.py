# coding:iso-8859-9 T�rk�e

from tkinter import *
from tkinter.filedialog import *
from tkinter.scrolledtext import ScrolledText

k�k = Tk()
k�k.title ("askopenfilename")

def se�():
    k�k1 = Tk()
    metinKutusu = ScrolledText (k�k1, width=130)
    metinKutusu.pack()

    dosyaAd�=askopenfilename (
            initialdir='C:/Users/pc/Desktop/MyFiles/4. Dersler/python/',
            filetypes=[('Python dosyalar�', '*.py'), ('T�m dizinler', '*')] )
    k�k1.title (dosyaAd�)
    metin = open (dosyaAd�).read()
    metinKutusu.insert (1.0, metin)

if __name__ == "__main__":
    Button (k�k, text="Dosya Se�", command=se� ).pack()
    Button (k�k, text="��k", command=k�k.quit ).pack()

mainloop()
