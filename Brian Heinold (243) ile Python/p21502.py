# coding:iso-8859-9 Türkçe

from tkinter import *

merhaba1 = Label (text ="Merhaba, normal fonlu tkinter gui etiketleri!")
merhaba1.grid (row = 0, column = 0)

merhaba2 = Label (text = 'Merhaba, özel fon ve renkler!', font = ('Verdana', 24, 'bold'), bg = 'blue', fg = 'pink')
merhaba2.grid (row=1, column=0)

merhaba3 = Label (text = "font= (fon_adı, fon_ebatı, fon_stili)", font = ('Verdana', 24, 'roman italic overstrike underline'), bg="green" )
merhaba3.grid (row=3, column=0)

merhaba4 = Label (text="1) Fadime Yavaş\n2) Bekir Yavaş\n3) Hanım Amanat Yavaş\n\
    4) Memet Yavaş\n5) Hatice Yavaş Kaçar\n6) Süheyla Yavaş Özbay\n7) Zeliha Yavaş Candan\n\
    8) M.Nihat Yavaş\n9) Songül Yavaş Göktürk\n10) M.Nedim Yavaş\n11) Sevim Yavaş",\
    font=("times new roman", 17, "normal"), bg="#b167df", fg="#ddd", width=20, height=12)
merhaba4.grid (row=4, column=0)

merhaba1.configure (bg="black", fg="white")

etiket1 = Label (font=("Arial", 20, "bold"), fg="cyan", bg="red")
etiket1.configure (text="{} * {} = {} eder." .format (8, 9, 8*9))
etiket1.grid (row=5, column=0)
 
mainloop()