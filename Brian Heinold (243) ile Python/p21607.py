# coding:iso-8859-9 T�rk�e

from tkinter import *
k�k = Tk()

def g�ster():
    print ("%", �l�ek.get() )
    etiket.config (text="% "+str (�l�ek.get()) )

�l�ek = Scale (k�k, from_=1, to_=100, length=300, showvalue=NO, orient=HORIZONTAL)
�l�ek.pack()

etiket=Label (k�k)
etiket.pack()

d��me = Button (k�k, text="G�ster", command=g�ster).pack()

mainloop()
