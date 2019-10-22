# coding:iso-8859-9 Türkçe
# p_41401.py: Bileşene (düğme) bağlı olay gerçekleştiğinde fonksiyon yürütme örneği.

from tkinter import *
from tkinter.messagebox import *
from p_315 import Renk

def selam (olay): etiket.config (text="Merhaba, düğmeyi tek tıkladınız!..", bg=Renk.renk(), fg=Renk.renk() )
def çık (olay):
    etiket.config (text="Düğme çıkış için çift tıklandı!..", bg=Renk.renk(), fg=Renk.renk() )
    if askyesno ('Onay', 'Çıkayım mı?'):
        showwarning ('Evet', 'Onayladınız; tıklayınca çıkıyorum...')
        import sys; sys.exit (0)
    else: showinfo ('İptal', 'Çıkış iptal edildi; kalıyorum...')

düğmeBileşeni = Button (None, text="Tek tıkla [selam]\nÇift tıkla [çık]", bg="Blue", fg="Lime")
düğmeBileşeni.pack()

düğmeBileşeni.bind ('<Button-1>', selam)
düğmeBileşeni.bind ('<Double-1>', çık) 

etiket = Label (None, font=("Segoe Script", 18, "italic") )
etiket.pack()

düğmeBileşeni.mainloop()