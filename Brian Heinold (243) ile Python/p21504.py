# coding:iso-8859-9 T�rk�e

from tkinter import *
Tk()

giri�1 = Label (text="Ad ve soyad�n�z� girin:")
giri�1.grid (row=0, column=0)
i�erik1 = Entry (width=20)
i�erik1.insert (0, "M.Nihat Yava�")
i�erik1.grid (row=0, column=1)
i�erik11 = i�erik1.get()

giri�2 = Label (text="Do�um y�l�n�z� girin:" )
giri�2.grid (row=1, column=0)
i�erik2 = Entry (width=10)
i�erik2.insert (0, 1957)
i�erik2.grid (row=1, column=1)
try: i�erik22 = eval (i�erik2.get() )
except Exception: i�erik22 = 0

sonu� = Label()
sonu�.grid (row=5, column=0)
sonu�.configure (text="Say�n: {}, ya��n�z: {}'dir.".format (i�erik11, (2018- i�erik22)) )

mainloop()
