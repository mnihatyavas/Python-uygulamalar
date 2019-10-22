# coding:iso-8859-9 Türkçe

from tkinter import *
Tk()

def açıkla1 (k):
    açıkla = Label (text=alfabe[k]+" harfini tıkladınız")
    açıkla.grid (row=1, column=1, columnspan=10)

def açıkla2 (k):
    global sayaç
    sayaç +=1
    açıkla = Label (text=k+" düğmesini " + str (sayaç) + ".kere tıkladınız")
    açıkla.grid (row=1, column=10, columnspan=10)

alfabe = 'ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ'
uz = len (alfabe)
düğmeler = [0]*uz

for i in range (uz):
    düğmeler[i] = Button (text=alfabe[i], command=lambda x=i: açıkla1 (x))
    düğmeler[i].grid (row=0, column=i)

sayaç = 0
tamam = Button (text='Tamam', font=('Verdana', 24), command=lambda: açıkla2 ("Tamam"))
tamam.grid (row=1, column=0)

mainloop()