# coding:iso-8859-9 T�rk�e

from tkinter import *
from random import randint
Tk()

def ya��Hesapla ():
    sonu� = Label (fg="green", font=("arial", 20, "italic"))
    sonu�.grid (row=3, column=0, pady=15)
    i�erik11 = i�erik1.get()
    try: i�erik22 = eval (i�erik2.get() )
    except Exception: i�erik22 = randint (1900, 2017)
    sonu�.configure (text="Say�n: {}, ya��n�z: {}'dir.".format (i�erik11, (2018- i�erik22)) )
    i�erik1.delete (0, END)
    i�erik2.delete (0, END)

giri�1 = Label (text="Ad ve soyad�n�z� girin:", font=(15))
giri�1.grid (row=0, column=0)
i�erik1 = Entry (width=25)
i�erik1.insert (0, "M.Nihat Yava�")
i�erik1.grid (row=0, column=1)

giri�2 = Label (text="Do�um y�l�n�z� girin:", font=(15))
giri�2.grid (row=1, column=0)
i�erik2 = Entry (width=10)
i�erik2.insert (0, 1957)
i�erik2.grid (row=1, column=1)

d��me = Button (text='T�kla Beni', command = ya��Hesapla, bg="red", fg="yellow")
d��me.grid (row=2, column=0, columnspan=2, pady=10)

mainloop()
