# coding:iso-8859-9 T�rk�e
# p_40101b.py: Python tkinter'le etiket, resim, buton, �er�eve ve saya� tek-ekran �rne�i.

from tkinter import *
k�k=Tk()
k�k.title ("Karma �rnekler")

Label (text="  MERHABA TK�NTER  ", pady=5, bg="Navy", fg="Lime").pack()
#-----------------------------------------------------------------------------

logo = PhotoImage (file="resim/pythonLogosu.gif")

a��klama = """
�nceleri sadece GIF ve PPM/PGM resim bi�emleri
destekleniyordu, ancak g�ncel python 3.8 s�r�m�nde
di�er resim dosya bi�emlerine de g�r�nt� imkan�
sa�layan GUI grafiksel kullan�c� aray�z geli�tirilmi�tir."""

Label (compound = CENTER, # Metin ve resim bile�ik ve resim ortada olacak. BOTTOM/TOP/LEFT/RIGHT/CENTER olabilir...
    text=a��klama, # justify hizalama varsay�l� center/ortala'd�r...
    image=logo).pack()
#-----------------------------------------------------------------------------
�er�eve = Frame() # a��klamay� ve logoyu bir arada tutar...
Label (�er�eve,
    justify=LEFT,
    padx = 10,
    text=a��klama).pack (side="left")
Label (�er�eve, image=logo).pack (side="right")
�er�eve.pack()
#-----------------------------------------------------------------------------

Label (justify=RIGHT,
    compound = BOTTOM,
    padx = 10, pady=10,
    text=a��klama, 
    image=logo).pack()
#-----------------------------------------------------------------------------

Label (text="Koyu haki zeminli k�rm�z� metin 'Times' yaz� fonuyla",
    fg="red",
    bg="DarkKhaki",
    font="Times").pack()
Label (text="Ye�il metin 'Helvetica 10 koyu yat�k' yaz� fonuyla",
    fg="light green",
    bg="dark green",
    font="Helvetica 10 bold italic").pack()
Label (text="Mavi metin 'Verdana 10 koyu' yaz� fonuyla",
    fg="blue",
    bg="yellow",
    font="Verdana 10 bold").pack()
Label (text="Siyah zeminde alt�n yaz�l� metin 'Segoe Script 10 koyu' fonuyla",
    fg="Gold",
    bg="Black",
    font=("Segoe Script", 10, "bold") ).pack()
Label (pady=5, width=80, bg="Navy").pack()
#-----------------------------------------------------------------------------
from p_315 import Renk

saya� = 0 
def sayac�Ba�lat (fi�):
    def say():
        global saya�
        saya� +=1
        fi�.config (text=str (saya�), fg=Renk.renk(), bg=Renk.renk() )
        fi�.after (1000, say)
    say()
  
�er�eve = Frame (k�k, bg=Renk.renk())
�er�eve.pack()
etiket = Label (�er�eve, font=("arial", 80, "bold") )
etiket.pack()
sayac�Ba�lat (etiket)
Button (�er�eve, text="Program� Sonland�r", width=50, bg=Renk.renk(), fg=Renk.renk(), command=k�k.destroy).pack()
#-----------------------------------------------------------------------------

mainloop()
