# coding:iso-8859-9 T�rk�e
# p_40301a.py: Tkinter Button ile slogan yazd�rma ve saniye sayac� �rne�i.

import tkinter as tk
from p_315 import Renk

def sloganYaz():
    print ("Tkinter kullan�m� �ok kolay bir GUI mod�l�d�r!..")
    tk.Label (�er�eve,
        text="Tkinter kullan�m� �ok kolay bir GUI mod�l�d�r!..",
        bg=Renk.renk(),
        fg=Renk.renk() ).pack()

k�k = tk.Tk()
k�k.title ("Slogan d��mesi")
�er�eve =  tk.Frame (k�k, bg=Renk.renk())
�er�eve.pack()

tk.Button (�er�eve,
    text="�IK",
    bg="FireBrick",
    fg="Yellow",
    command=k�k.destroy).pack (side=tk.LEFT) # quit arada kapatm�yor...
tk.Button (�er�eve,
    text="L�tfen t�klay�n",
    bg="Gold",
    fg="Blue",
    padx=10,
    pady=10,
    command=sloganYaz).pack (side=tk.LEFT)

k�k.mainloop()
#-----------------------------------------------------------------------------------------------------

saya�=0
def saya�Etiketi (fi�):
    def say():
        global saya�
        saya� += 1
        fi�.config (text=str (saya�), bg=Renk.renk(), fg=Renk.renk() )
        fi�.after (1000, say)
    say()
 
k�k = tk.Tk()
k�k.title ("Saniye sayac�")
�er�eve = tk.Frame (k�k, bg=Renk.renk() )
�er�eve.pack()

etiket = tk.Label (�er�eve, font=("Arial", 100, "bold") )
etiket.pack()

tk.Button (�er�eve, text="Sayac� Ba�lat", command=lambda:saya�Etiketi (etiket), bg="#000", fg="MintCream").pack()
# Parametreli fonksiyon komutlar�nda, arada lambda olmazsa, ilk ba�ta t�klamadan i�letir...
tk.Button (�er�eve, text='Program� Sonland�r', width=50, command=k�k.quit, bg="#057fb5", fg="#ff0").pack()

k�k.mainloop()