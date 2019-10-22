# coding:iso-8859-9 Türkçe
# p_40601.py: Çentik kutusuyla cinsiyet, yaş ve medeni durum çoklu seçenek örneği.

from tkinter import *
from p_315 import Renk

kök = Tk()
kök.title ("Çokseçenekli Çentik Kutuları")

def göster():
    metin = ""
    if değişken1.get() == 1: metin += "Kadın, " # 0=false/çentiksiz, 1=true/çentikli
    if değişken2.get() == 1: metin += "Erkek, "
    if değişken3.get() == 1: metin += "Çocuk, "
    if değişken4.get() == 1: metin += "Genç, "
    if değişken5.get() == 1: metin += "Kamil, "
    if değişken6.get() == 1: metin += "Yaşlı, "
    if değişken7.get() == 1: metin += "Bekar, "
    if değişken8.get() == 1: metin += "Evli, "
    if değişken9.get() == 1: metin += "Dul, "
    etiket.config (text=metin, bg=Renk.renk(), fg=Renk.renk() )

çerçeve = Frame (kök, bg=Renk.renk() )
çerçeve.grid()

Label (çerçeve, text="Lütfen aşağıdakilerden\nenaz birini işaretleyin:", bg=Renk.renk(), fg=Renk.renk(), font=("Arial", 15, "bold") ).grid (row=0, stick=W, pady=10)

değişken1 = IntVar()
Checkbutton (çerçeve, text="Kadın", variable=değişken1, fg="Coral", bg="Black" ).grid (row=1, sticky=W)

değişken2 = IntVar()
Checkbutton (çerçeve, text="Erkek", variable=değişken2, fg="Coral", bg="Black" ).grid (row=2, sticky=W)

Label (çerçeve, text="-"*20, bg="Brown", fg="Yellow").grid (row=3, stick=W)

değişken3 = IntVar()
Checkbutton (çerçeve, text="Çocuk", variable=değişken3, fg="Coral", bg="Black" ).grid (row=4, sticky=W)

değişken4 = IntVar()
Checkbutton (çerçeve, text="Genç", variable=değişken4, fg="Coral", bg="Black" ).grid (row=5, sticky=W)

değişken5 = IntVar()
Checkbutton (çerçeve, text="Kamil", variable=değişken5, fg="Coral", bg="Black" ).grid (row=6, sticky=W)

değişken6 = IntVar()
Checkbutton (çerçeve, text="Yaşlı", variable=değişken6, fg="Coral", bg="Black" ).grid (row=7, sticky=W)

Label (çerçeve, text="-"*20, bg="Brown", fg="Yellow").grid (row=8, stick=W)

değişken7 = IntVar()
Checkbutton (çerçeve, text="Bekar", variable=değişken7, fg="Coral", bg="Black" ).grid (row=9, sticky=W)

değişken8 = IntVar()
Checkbutton (çerçeve, text="Evli", variable=değişken8, fg="Coral", bg="Black" ).grid (row=10, sticky=W)

değişken9 = IntVar()
Checkbutton (çerçeve, text="Dul", variable=değişken9, fg="Coral", bg="Black" ).grid (row=11, sticky=W)

Button (çerçeve, text="Seçilenleri Göster", command=göster, bg=Renk.renk(), fg=Renk.renk() ).grid (row=12, column=0, sticky=W, pady=5)
Button (çerçeve, text="Çık", command=kök.quit, bg=Renk.renk(), fg=Renk.renk() ).grid (row=12, column=0, pady=5)

etiket = Label (çerçeve, font=("Verdana", 15, "bold") )
etiket.grid (row=13, stick=W)

kök.mainloop()