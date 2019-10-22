# coding:iso-8859-9 T�rk�e
# p_41101.py: Python messagebox ile t�m mesaj kutular� �rne�i.

# >python -m pip install --upgrade pip

from tkinter import *
from tkinter.messagebox import *

k�k = Tk()
k�k.title ("Mesaj Kutular�")

def cevapMesaj�(): showerror ("Cevap", "Pardon, ama cevap bulunamad�")

def ��k��Mesajlar�():
    if askyesno ('Onay', '��kay�m m�?'):
        showwarning ('Evet', 'T�klay�nca ��k�yorum')
        k�k.quit()
    else: showinfo ('�ptal', '��k�� iptal edildi')

def t�mMesajlar():
    askokcancel ("�ptal", "Tamam m�, �ptal mi?")
    askquestion ("Soru Sor", "Sordun mu?")
    askretrycancel ("Tekrar veya �ptal", "Tekrar m�, �ptal mi?")
    askyesno ("Evet veya Hay�r", "Evet mi, Hay�r m�?")
    askyesnocancel ("Evet, Hay�r, �ptal", "Evet mi, Hay�r m�, �ptal mi?")
    showerror ("Hatay� g�ster", "Hata budur")
    showinfo ("Bilgilendirme", "Bu mesaj bilgilendirme maksatl�d�r")
    showwarning ("�kaz", "Bu bir ikaz mesaj�d�r")

Button (k�k, text='T�m varsay�l� mesaj kutular�', command=t�mMesajlar).pack (fill=X)
Button (k�k, text='Cevap ver', command=cevapMesaj�).pack (fill=X)
Button (k�k, text='��k�� mesajlar�', command=��k��Mesajlar�).pack (fill=X)
Button (k�k, text='�IK', command=k�k.quit).pack (fill=X)

k�k.mainloop()