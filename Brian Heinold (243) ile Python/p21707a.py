# coding:iso-8859-9 Türkçe

from tkinter import *
from tkinter.filedialog import *
from tkinter.scrolledtext import ScrolledText

kök = Tk()
kök.title ("askopenfilename")

metinKutusu = ScrolledText (kök, width=110)
metinKutusu.pack()
metinKutusu.insert (1.0, "M.Nihat Yavaş\n===================\n\n")

dosyaAdı=askopenfilename (
        initialdir='C:/Users/pc/Desktop/MyFiles/4. Dersler/python/',
        filetypes=[('Python dosyaları', '*.py'), ('Tüm dizinler', '*')] )

metin = open (dosyaAdı).read()
metinKutusu.insert (END, metin)

mainloop()

"""Birkaç diyalog örneği:
askopenfilename: Dosya seçici diyaloğu açar, dönen seçilen dosya adıdır.
askopenfilenames: Birönceki gibidir, ancak çoklu dosya seçilebilir; dönen seçilen dosyalar listesidir.
asksaveasfilename: Seçili dosyanın saklanma dizin-dosyaadı diyaloğunu açar.
askdirectory: Dizin seçici diyaloğu açar, dönen seçilen dizin adıdır.
"""