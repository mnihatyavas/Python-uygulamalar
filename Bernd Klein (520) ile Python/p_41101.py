# coding:iso-8859-9 Türkçe
# p_41101.py: Python messagebox ile tüm mesaj kutuları örneği.

# >python -m pip install --upgrade pip

from tkinter import *
from tkinter.messagebox import *

kök = Tk()
kök.title ("Mesaj Kutuları")

def cevapMesajı(): showerror ("Cevap", "Pardon, ama cevap bulunamadı")

def çıkışMesajları():
    if askyesno ('Onay', 'Çıkayım mı?'):
        showwarning ('Evet', 'Tıklayınca çıkıyorum')
        kök.quit()
    else: showinfo ('İptal', 'Çıkış iptal edildi')

def tümMesajlar():
    askokcancel ("İptal", "Tamam mı, İptal mi?")
    askquestion ("Soru Sor", "Sordun mu?")
    askretrycancel ("Tekrar veya İptal", "Tekrar mı, İptal mi?")
    askyesno ("Evet veya Hayır", "Evet mi, Hayır mı?")
    askyesnocancel ("Evet, Hayır, İptal", "Evet mi, Hayır mı, İptal mi?")
    showerror ("Hatayı göster", "Hata budur")
    showinfo ("Bilgilendirme", "Bu mesaj bilgilendirme maksatlıdır")
    showwarning ("İkaz", "Bu bir ikaz mesajıdır")

Button (kök, text='Tüm varsayılı mesaj kutuları', command=tümMesajlar).pack (fill=X)
Button (kök, text='Cevap ver', command=cevapMesajı).pack (fill=X)
Button (kök, text='Çıkış mesajları', command=çıkışMesajları).pack (fill=X)
Button (kök, text='ÇIK', command=kök.quit).pack (fill=X)

kök.mainloop()