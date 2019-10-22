#coding:iso-8859-9 T�rk�e
# p_40101a.py: Python tkinter'le etiket, resim, buton, �er�eve ve saya� �rne�i.

import tkinter as tk

k�k = tk.Tk() # tk mod�l�n�n Tk() aletkutulu k�k widget/bile�en'i...
k�k.mainloop() # ��i bo� k�k penceresi...
#----------------------------------------------------------------------------------------------------------

k�k = tk.Tk()
bile�en = tk.Label (k�k, text="Merhaba Renkli Tkinter Pencereli D�nyas�!..") # k�k ebeveynin Label yavrusu...
bile�en.pack() # Label metni ebat�nda paketle...
k�k.mainloop() # ��i etiket beyanl� pencere...
#----------------------------------------------------------------------------------------------------------

k�k = tk.Tk()
logo = tk.PhotoImage (file="resim/pythonLogosu.gif")
etiketBile�eni1 = tk.Label (k�k, image=logo).pack (side="right")
a��klama = """
�nceleri sadece GIF ve PPM/PGM resim bi�emleri
destekleniyordu, ancak g�ncel python 3.8 s�r�m�nde
di�er resim dosya bi�emlerine de g�r�nt� imkan�
sa�layan GUI grafiksel kullan�c� aray�z geli�tirilmi�tir."""

etiketBile�eni2 = tk.Label (
    k�k,
    justify=tk.LEFT, # Metni LEFT, RIGHT veya CENTER (varsay�l�) hizalar...
    padx = 10, # metnin sol ve sa��na 10px bo�luk b�rak�r; pady ise �st ve alt�na...
    text=a��klama).pack (side="left")
k�k.mainloop()
#----------------------------------------------------------------------------------------------------------

k�k = tk.Tk()
logo = tk.PhotoImage (file="resim/pythonLogosu.gif")
etiket = tk.Label (
    k�k,
    text=a��klama,
    justify=tk.CENTER, # varsay�l�...
    padx = 50, # Sol-sa� bo�luk...
    pady = 50, # Alt-�st bo�luk...
    image=logo,
    compound = tk.CENTER # etiket bile�enindeki resmin metinle bili�imi ortas�nda...
    ).pack (side="right")
k�k.mainloop()
#----------------------------------------------------------------------------------------------------------

k�k = tk.Tk()
logo = tk.PhotoImage (file="resim/pythonLogosu.gif")
etiket = tk.Label (
    k�k,
    text=a��klama,
    #justify=tk.CENTER, # varsay�l�...
    padx = 50, # Sol-sa� bo�luk...
    pady = 10, # Alt-�st bo�luk...
    image=logo,
    compound = tk.TOP # LEFT, RIGHT, TOP ve BOTTOM...
    ).pack (side="right")
k�k.mainloop()
#----------------------------------------------------------------------------------------------------------

k�k = tk.Tk()
tk.Label (k�k,
    text="Times yaz� fonlu k�rm�z� metin",
    fg = "red",
    font = "Times").pack()
tk.Label (k�k,
    text="Helvetica 16 koyu yat�k fonlu ye�il zeminde a��k-ye�il metin",
    fg = "LightGreen",
    bg = "dark green",
    font = "Helvetica 16 bold italic").pack()
tk.Label (k�k,
    text="Verdana 10 koyu fonlu sar� zeminde mavi metin",
    fg = "blue",
    bg = "yellow",
    font = "Verdana 10 bold").pack()
tk.Label (k�k,
    text="Segoe Script 20 normal fonlu ate�-tu�las� zeminde alt�n renkli metin",
    fg = "Gold",
    bg = "FireBrick",
    font = ("Segoe Script", 20, 'normal') ).pack()
k�k.mainloop()
#----------------------------------------------------------------------------------------------------------

from tkinter import Tk, Frame
from p_315 import Renk

saya� = 0
def sayac�Ba�lat (yafta):
    def say():
        global saya�
        saya� += 1
        yafta.config (text=str (saya�), fg=Renk.renk(), bg=Renk.renk() )
        yafta.after (1000, say) # Her 1000mS=1sn'de tekrar i�let...
    say()

k�k = Tk()
k�k.title ("Saniye Sayac�")
�er�eve = Frame (k�k, bg="MidnightBlue")
etiket = tk.Label (�er�eve, font=("arial", 100, "bold") )
etiket.pack()
sayac�Ba�lat (etiket)
d��me = tk.Button (�er�eve, text='Program� Sonland�r', width=50, height=2, bg="black", fg="yellow", command=k�k.destroy).pack()
�er�eve.pack()
k�k.mainloop()
