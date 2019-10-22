# coding:iso-8859-9 Türkçe
# p_40101b.py: Python tkinter'le etiket, resim, buton, çerçeve ve sayaç tek-ekran örneği.

from tkinter import *
kök=Tk()
kök.title ("Karma örnekler")

Label (text="  MERHABA TKİNTER  ", pady=5, bg="Navy", fg="Lime").pack()
#-----------------------------------------------------------------------------

logo = PhotoImage (file="resim/pythonLogosu.gif")

açıklama = """
Önceleri sadece GIF ve PPM/PGM resim biçemleri
destekleniyordu, ancak güncel python 3.8 sürümünde
diğer resim dosya biçemlerine de görüntü imkanı
sağlayan GUI grafiksel kullanıcı arayüz geliştirilmiştir."""

Label (compound = CENTER, # Metin ve resim bileşik ve resim ortada olacak. BOTTOM/TOP/LEFT/RIGHT/CENTER olabilir...
    text=açıklama, # justify hizalama varsayılı center/ortala'dır...
    image=logo).pack()
#-----------------------------------------------------------------------------
çerçeve = Frame() # açıklamayı ve logoyu bir arada tutar...
Label (çerçeve,
    justify=LEFT,
    padx = 10,
    text=açıklama).pack (side="left")
Label (çerçeve, image=logo).pack (side="right")
çerçeve.pack()
#-----------------------------------------------------------------------------

Label (justify=RIGHT,
    compound = BOTTOM,
    padx = 10, pady=10,
    text=açıklama, 
    image=logo).pack()
#-----------------------------------------------------------------------------

Label (text="Koyu haki zeminli kırmızı metin 'Times' yazı fonuyla",
    fg="red",
    bg="DarkKhaki",
    font="Times").pack()
Label (text="Yeşil metin 'Helvetica 10 koyu yatık' yazı fonuyla",
    fg="light green",
    bg="dark green",
    font="Helvetica 10 bold italic").pack()
Label (text="Mavi metin 'Verdana 10 koyu' yazı fonuyla",
    fg="blue",
    bg="yellow",
    font="Verdana 10 bold").pack()
Label (text="Siyah zeminde altın yazılı metin 'Segoe Script 10 koyu' fonuyla",
    fg="Gold",
    bg="Black",
    font=("Segoe Script", 10, "bold") ).pack()
Label (pady=5, width=80, bg="Navy").pack()
#-----------------------------------------------------------------------------
from p_315 import Renk

sayaç = 0 
def sayacıBaşlat (fiş):
    def say():
        global sayaç
        sayaç +=1
        fiş.config (text=str (sayaç), fg=Renk.renk(), bg=Renk.renk() )
        fiş.after (1000, say)
    say()
  
çerçeve = Frame (kök, bg=Renk.renk())
çerçeve.pack()
etiket = Label (çerçeve, font=("arial", 80, "bold") )
etiket.pack()
sayacıBaşlat (etiket)
Button (çerçeve, text="Programı Sonlandır", width=50, bg=Renk.renk(), fg=Renk.renk(), command=kök.destroy).pack()
#-----------------------------------------------------------------------------

mainloop()
