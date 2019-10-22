# coding:iso-8859-9 T�rk�e
# p_41301.py: A�a��-a��lan men� ve altse�enekleri �rne�i.

from tkinter import *
from tkinter.filedialog import askopenfilename as aof

def YeniDosya(): mesaj.config (text="Yeni bir dosya yarat�lacak.")
def DosyaA�():
    dosyaAd� = aof()
    mesaj.config (text=dosyaAd�)

def Hakk�nda(): mesaj.config (text="Bu basit bir a�a��-a��lan men� �rne�idir.")

k�k = Tk()
k�k.title ("A�a��ya-a��lan Men�")
k�k.geometry ("250x85")

men� = Menu (k�k)
k�k.config (menu=men�, bg="DarkKhaki")

dosyaMen�s� = Menu (men�, bg="Navy", fg="Coral")
men�.add_cascade (label="Dosya", menu=dosyaMen�s�)
dosyaMen�s�.add_command (label="Yeni", command=YeniDosya)
dosyaMen�s�.add_command (label="A�...", command=DosyaA�)
dosyaMen�s�.add_separator()
dosyaMen�s�.add_command (label="�IK", command=k�k.quit)

yard�mMen�s� = Menu (men�, bg="DarkRed", fg="Yellow")
men�.add_cascade (label="Yard�m", menu=yard�mMen�s�)
yard�mMen�s�.add_command (label="Hakk�m�zda...", command=Hakk�nda)

mesaj = Message (k�k, bg="Purple", fg="Gold")
mesaj.pack (side=BOTTOM)

k�k.mainloop()