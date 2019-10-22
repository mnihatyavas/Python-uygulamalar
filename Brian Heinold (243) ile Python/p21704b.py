# coding:iso-8859-9 T�rk�e

from tkinter import *
from tkinter.messagebox import *
k�k = Tk()
k�k.title ("Mesaj Kutular�")

def kapat�lacak():
    cevap = askquestion (title='Kapat�ls�n m�?', message='Program� kapatmak istedi�inden emin misin?')
    if cevap== 'yes': k�k.quit() # veya "k�k.destroy()"
    else: g�ster (cevap)

def g�ster (d�nen):
    d�nen = str (d�nen).upper()
    etiket.config (text="\n\nMesajdan d�nen cevap: ["+d�nen+"]'dir.")

def bilgi(): g�ster (showinfo (title="Bilgi", message="Bu sadece bir enformasyon mesaj kutusudur!..") )
def ikaz(): g�ster (showwarning (title="�kaz", message="Dikkat, bu bi�imleme MS Windows taraf�ndan desteklenmemektedir!..") )
def hata(): g�ster (showerror (title="Hata", message="Dikkat, yapt���n�z i�lem hatal�d�r!..") )
def sorEH(): g�ster (askquestion (title="SoruEH", message="Sorumuza cevab�n Evet mi, Hay�r m�?") )
def sorEH�(): g�ster (askyesnocancel (title="SoruEH�", message="Sorumuza cevab�n Evet mi, Hay�r m�, �ptal mi?") )
def sorT�(): g�ster (askokcancel (title="SoruT�", message="Sorumuza cevab�n Tamam m�, �ptal mi?") )
def sorY�(): g�ster (askretrycancel (title="SoruY�", message="Sorumuza cevab�n Yinele mi, �ptal mi?") )


if __name__ == "__main__":
    �er�eve = Frame (k�k)
    �er�eve.pack()
    Button (�er�eve, text="Bilgi", command=bilgi ).pack (side=LEFT)
    Button (�er�eve, text="�kaz", command=ikaz ).pack (side=LEFT)
    Button (�er�eve, text="Hata", command=hata ).pack (side=LEFT)
    Button (�er�eve, text="Sor EH", command=sorEH ).pack (side=LEFT)
    Button (�er�eve, text="Sor EH�", command=sorEH� ).pack (side=LEFT)
    Button (�er�eve, text="Sor T�", command=sorT� ).pack (side=LEFT)
    Button (�er�eve, text="Sor Y�", command=sorY� ).pack (side=LEFT)

    etiket = Label (k�k)
    etiket.pack()

    k�k.protocol ('WM_DELETE_WINDOW', kapat�lacak) # WM: PencereY�netimi, sil pencereyi...

mainloop()
