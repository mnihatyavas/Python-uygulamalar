# coding:iso-8859-9 Türkçe

from tkinter import *
kök = Tk()

def göster():
    print ("%", ölçek.get() )
    etiket.config (text="% "+str (ölçek.get()) )

ölçek = Scale (kök, from_=1, to_=100, length=300, showvalue=NO, orient=HORIZONTAL)
ölçek.pack()

etiket=Label (kök)
etiket.pack()

düğme = Button (kök, text="Göster", command=göster).pack()

mainloop()
