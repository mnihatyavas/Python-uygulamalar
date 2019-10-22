#coding:iso-8859-9 Türkçe
# p_40101a.py: Python tkinter'le etiket, resim, buton, çerçeve ve sayaç örneği.

import tkinter as tk

kök = tk.Tk() # tk modülünün Tk() aletkutulu kök widget/bileşen'i...
kök.mainloop() # İçi boş kök penceresi...
#----------------------------------------------------------------------------------------------------------

kök = tk.Tk()
bileşen = tk.Label (kök, text="Merhaba Renkli Tkinter Pencereli Dünyası!..") # kök ebeveynin Label yavrusu...
bileşen.pack() # Label metni ebatında paketle...
kök.mainloop() # İçi etiket beyanlı pencere...
#----------------------------------------------------------------------------------------------------------

kök = tk.Tk()
logo = tk.PhotoImage (file="resim/pythonLogosu.gif")
etiketBileşeni1 = tk.Label (kök, image=logo).pack (side="right")
açıklama = """
Önceleri sadece GIF ve PPM/PGM resim biçemleri
destekleniyordu, ancak güncel python 3.8 sürümünde
diğer resim dosya biçemlerine de görüntü imkanı
sağlayan GUI grafiksel kullanıcı arayüz geliştirilmiştir."""

etiketBileşeni2 = tk.Label (
    kök,
    justify=tk.LEFT, # Metni LEFT, RIGHT veya CENTER (varsayılı) hizalar...
    padx = 10, # metnin sol ve sağına 10px boşluk bırakır; pady ise üst ve altına...
    text=açıklama).pack (side="left")
kök.mainloop()
#----------------------------------------------------------------------------------------------------------

kök = tk.Tk()
logo = tk.PhotoImage (file="resim/pythonLogosu.gif")
etiket = tk.Label (
    kök,
    text=açıklama,
    justify=tk.CENTER, # varsayılı...
    padx = 50, # Sol-sağ boşluk...
    pady = 50, # Alt-üst boşluk...
    image=logo,
    compound = tk.CENTER # etiket bileşenindeki resmin metinle bilişimi ortasında...
    ).pack (side="right")
kök.mainloop()
#----------------------------------------------------------------------------------------------------------

kök = tk.Tk()
logo = tk.PhotoImage (file="resim/pythonLogosu.gif")
etiket = tk.Label (
    kök,
    text=açıklama,
    #justify=tk.CENTER, # varsayılı...
    padx = 50, # Sol-sağ boşluk...
    pady = 10, # Alt-üst boşluk...
    image=logo,
    compound = tk.TOP # LEFT, RIGHT, TOP ve BOTTOM...
    ).pack (side="right")
kök.mainloop()
#----------------------------------------------------------------------------------------------------------

kök = tk.Tk()
tk.Label (kök,
    text="Times yazı fonlu kırmızı metin",
    fg = "red",
    font = "Times").pack()
tk.Label (kök,
    text="Helvetica 16 koyu yatık fonlu yeşil zeminde açık-yeşil metin",
    fg = "LightGreen",
    bg = "dark green",
    font = "Helvetica 16 bold italic").pack()
tk.Label (kök,
    text="Verdana 10 koyu fonlu sarı zeminde mavi metin",
    fg = "blue",
    bg = "yellow",
    font = "Verdana 10 bold").pack()
tk.Label (kök,
    text="Segoe Script 20 normal fonlu ateş-tuğlası zeminde altın renkli metin",
    fg = "Gold",
    bg = "FireBrick",
    font = ("Segoe Script", 20, 'normal') ).pack()
kök.mainloop()
#----------------------------------------------------------------------------------------------------------

from tkinter import Tk, Frame
from p_315 import Renk

sayaç = 0
def sayacıBaşlat (yafta):
    def say():
        global sayaç
        sayaç += 1
        yafta.config (text=str (sayaç), fg=Renk.renk(), bg=Renk.renk() )
        yafta.after (1000, say) # Her 1000mS=1sn'de tekrar işlet...
    say()

kök = Tk()
kök.title ("Saniye Sayacı")
çerçeve = Frame (kök, bg="MidnightBlue")
etiket = tk.Label (çerçeve, font=("arial", 100, "bold") )
etiket.pack()
sayacıBaşlat (etiket)
düğme = tk.Button (çerçeve, text='Programı Sonlandır', width=50, height=2, bg="black", fg="yellow", command=kök.destroy).pack()
çerçeve.pack()
kök.mainloop()
