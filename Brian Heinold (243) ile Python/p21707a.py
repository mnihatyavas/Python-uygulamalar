# coding:iso-8859-9 T�rk�e

from tkinter import *
from tkinter.filedialog import *
from tkinter.scrolledtext import ScrolledText

k�k = Tk()
k�k.title ("askopenfilename")

metinKutusu = ScrolledText (k�k, width=110)
metinKutusu.pack()
metinKutusu.insert (1.0, "M.Nihat Yava�\n===================\n\n")

dosyaAd�=askopenfilename (
        initialdir='C:/Users/pc/Desktop/MyFiles/4. Dersler/python/',
        filetypes=[('Python dosyalar�', '*.py'), ('T�m dizinler', '*')] )

metin = open (dosyaAd�).read()
metinKutusu.insert (END, metin)

mainloop()

"""Birka� diyalog �rne�i:
askopenfilename: Dosya se�ici diyalo�u a�ar, d�nen se�ilen dosya ad�d�r.
askopenfilenames: Bir�nceki gibidir, ancak �oklu dosya se�ilebilir; d�nen se�ilen dosyalar listesidir.
asksaveasfilename: Se�ili dosyan�n saklanma dizin-dosyaad� diyalo�unu a�ar.
askdirectory: Dizin se�ici diyalo�u a�ar, d�nen se�ilen dizin ad�d�r.
"""