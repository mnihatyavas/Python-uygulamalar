# coding:iso-8859-9 Türkçe
# p_40901.py: Yatay ve dikey ölçekli sürgüler ve değerlerinin gösterimi örneği

from tkinter import *
from p_315 import Renk

kök = Tk()
kök.title ("Ölçekli Sürgüler")

def göster (olay): etiket.config (text="(" + str (sürgü2.get()) + ", " + str (sürgü1.get()) + ")")

çerçeve = Frame (kök, bg=Renk.renk() )
çerçeve.pack()

sürgü1 = Scale (çerçeve, from_=-20, to=50, tickinterval=5, length=250, bg="Sienna", fg="Azure") # Varsayılı orient=VERTICAL...
sürgü1.pack()
sürgü1.set (-20) # Belirtilmezse varsayılı ilk değer=0'dır...

sürgü2 = Scale (çerçeve, from_=0, to=200, orient=HORIZONTAL, tickinterval=10, length=500, bg="Teal", fg="Cyan")
sürgü2.pack()
sürgü2.set (100)

sürgü1.bind ("<B1-Motion>", göster)
sürgü2.bind ("<B1-Motion>", göster)

çerçeve2 = Frame (çerçeve)
çerçeve2.pack()
Button (çerçeve2, text='Hassas Göster', command=(lambda x=0: göster (x) ), bg="Navy", fg="Gold").pack(side=LEFT)
Button (çerçeve2, text='ÇIK', command=çerçeve.quit, bg="Orange", fg="Blue").pack(side=LEFT)

etiket = Label (çerçeve, bg="black", fg="Yellow")
etiket.pack()

kök.mainloop()