# coding:iso-8859-9 T�rk�e

from tkinter import *

merhaba1 = Label (text ="Merhaba, normal fonlu tkinter gui etiketleri!")
merhaba1.grid (row = 0, column = 0)

merhaba2 = Label (text = 'Merhaba, �zel fon ve renkler!', font = ('Verdana', 24, 'bold'), bg = 'blue', fg = 'pink')
merhaba2.grid (row=1, column=0)

merhaba3 = Label (text = "font= (fon_ad�, fon_ebat�, fon_stili)", font = ('Verdana', 24, 'roman italic overstrike underline'), bg="green" )
merhaba3.grid (row=3, column=0)

merhaba4 = Label (text="1) Fadime Yava�\n2) Bekir Yava�\n3) Han�m Amanat Yava�\n\
    4) Memet Yava�\n5) Hatice Yava� Ka�ar\n6) S�heyla Yava� �zbay\n7) Zeliha Yava� Candan\n\
    8) M.Nihat Yava�\n9) Song�l Yava� G�kt�rk\n10) M.Nedim Yava�\n11) Sevim Yava�",\
    font=("times new roman", 17, "normal"), bg="#b167df", fg="#ddd", width=20, height=12)
merhaba4.grid (row=4, column=0)

merhaba1.configure (bg="black", fg="white")

etiket1 = Label (font=("Arial", 20, "bold"), fg="cyan", bg="red")
etiket1.configure (text="{} * {} = {} eder." .format (8, 9, 8*9))
etiket1.grid (row=5, column=0)
 
mainloop()