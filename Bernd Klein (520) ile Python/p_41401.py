# coding:iso-8859-9 T�rk�e
# p_41401.py: Bile�ene (d��me) ba�l� olay ger�ekle�ti�inde fonksiyon y�r�tme �rne�i.

from tkinter import *
from tkinter.messagebox import *
from p_315 import Renk

def selam (olay): etiket.config (text="Merhaba, d��meyi tek t�klad�n�z!..", bg=Renk.renk(), fg=Renk.renk() )
def ��k (olay):
    etiket.config (text="D��me ��k�� i�in �ift t�kland�!..", bg=Renk.renk(), fg=Renk.renk() )
    if askyesno ('Onay', '��kay�m m�?'):
        showwarning ('Evet', 'Onaylad�n�z; t�klay�nca ��k�yorum...')
        import sys; sys.exit (0)
    else: showinfo ('�ptal', '��k�� iptal edildi; kal�yorum...')

d��meBile�eni = Button (None, text="Tek t�kla [selam]\n�ift t�kla [��k]", bg="Blue", fg="Lime")
d��meBile�eni.pack()

d��meBile�eni.bind ('<Button-1>', selam)
d��meBile�eni.bind ('<Double-1>', ��k) 

etiket = Label (None, font=("Segoe Script", 18, "italic") )
etiket.pack()

d��meBile�eni.mainloop()