# coding:iso-8859-9 T�rk�e

from tkinter import *
from tkinter.messagebox import *
k�k = Tk()
k�k.title ("Mesaj Kutular�")

def kapat�lacak():
    cevap = askquestion (title='Kapat�ls�n m�?', message='Program� kapatmak istedi�inden emin misin?')
    if cevap== 'yes': k�k.destroy()

def g�ster (d�nen):
    d�nen = str (d�nen).upper()
    etiket.config (text="Mesajdan d�nen cevap: ["+d�nen+"]'dir.")

etiket = Label (k�k)
etiket.pack()

k�k.protocol ('WM_DELETE_WINDOW', kapat�lacak) # WM: PencereY�netimi, sil pencereyi...

mesaj1 = showinfo (title="Bilgi", message="Bu sadece bir enformasyon mesaj kutusudur!..")
g�ster (mesaj1)
mesaj2 = askquestion (title="SoruEH", message="Sorumuza cevab�n Evet mi, Hay�r m�?")
g�ster (mesaj2)
mesaj3 = showwarning (title="�kaz", message="Dikkat, bu bi�imleme MS Windows taraf�ndan desteklenmemektedir!..")
g�ster (mesaj3)

mesaj4 = askokcancel (title="SoruT�", message="Sorumuza cevab�n Tamam m�, �ptal mi?")
g�ster (mesaj4)
mesaj5 = askretrycancel (title="SoruY�", message="Sorumuza cevab�n Yinele mi, �ptal mi?")
g�ster (mesaj5)
mesaj6 = askyesnocancel (title="SoruEH�", message="Sorumuza cevab�n Evet mi, Hay�r m�, �ptal mi?")
g�ster (mesaj6)
mesaj7 = showerror (title="Hata", message="Dikkat, yapt���n�z i�lem hatal�d�r!..")
g�ster (mesaj7)

mainloop()
