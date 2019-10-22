# coding:iso-8859-9 Türkçe
# p_41301.py: Aşağı-açılan menü ve altseçenekleri örneği.

from tkinter import *
from tkinter.filedialog import askopenfilename as aof

def YeniDosya(): mesaj.config (text="Yeni bir dosya yaratılacak.")
def DosyaAç():
    dosyaAdı = aof()
    mesaj.config (text=dosyaAdı)

def Hakkında(): mesaj.config (text="Bu basit bir aşağı-açılan menü örneğidir.")

kök = Tk()
kök.title ("Aşağıya-açılan Menü")
kök.geometry ("250x85")

menü = Menu (kök)
kök.config (menu=menü, bg="DarkKhaki")

dosyaMenüsü = Menu (menü, bg="Navy", fg="Coral")
menü.add_cascade (label="Dosya", menu=dosyaMenüsü)
dosyaMenüsü.add_command (label="Yeni", command=YeniDosya)
dosyaMenüsü.add_command (label="Aç...", command=DosyaAç)
dosyaMenüsü.add_separator()
dosyaMenüsü.add_command (label="ÇIK", command=kök.quit)

yardımMenüsü = Menu (menü, bg="DarkRed", fg="Yellow")
menü.add_cascade (label="Yardım", menu=yardımMenüsü)
yardımMenüsü.add_command (label="Hakkımızda...", command=Hakkında)

mesaj = Message (kök, bg="Purple", fg="Gold")
mesaj.pack (side=BOTTOM)

kök.mainloop()