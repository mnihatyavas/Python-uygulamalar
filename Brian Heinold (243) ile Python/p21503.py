# coding:iso-8859-9 Türkçe

from tkinter import *

Tk()
etiket1=Label (text="Merhaba-1", bg="lightgray")
etiket2=Label (text="Merhaba-2", bg="lightgray")
etiket3=Label (text="Merhaba-3", bg="lightgray")
etiket4=Label (text="Merhaba-4", bg="lightgray")
etiket5=Label (text="Merhaba-5", bg="lightgray")

etiket1.grid (row=0, column=0, padx=2, pady=2) # yatay_x ve dikey_y aralıklar...
etiket2.grid (row=0, column=1, padx=2, pady=2)
etiket3.grid (row=1, column=0, columnspan=2, padx=2, pady=2)
etiket4.grid (row=1, column=2, padx=2, pady=2)
etiket5.grid (row=2, column=2, padx=2, pady=2)

mainloop()