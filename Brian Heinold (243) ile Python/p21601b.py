# coding:iso-8859-9 Türkçe

from tkinter import *
Tk()

def açıkla1 (k):
    global düğmeler2
    düğmeler2[k] +=1
    açıkla = Label (text=alfabe[k]+" harfini " + str (düğmeler2[k]) + ".kere tıkladınız")
    açıkla.grid (row=2, column=1, columnspan=10, pady=10)

def açıkla2 (k):
    global sayaç
    sayaç +=1
    açıkla = Label (text=k+" düğmesini " + str (sayaç) + ".kere tıkladınız")
    açıkla.grid (row=2, column=15, columnspan=10, pady=10)

alfabe = 'ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ'
uz = len (alfabe)
düğmeler1 = [0]*uz
düğmeler2 = [0]*uz

for i in range (uz):
    düğmeler1[i] = Button (text=alfabe[i], command=lambda x=i: açıkla1 (x))
    düğmeler1[i].grid (row=0, column=i)

sayaç = 0
tamam = Button (text='Tamam', font=('Verdana', 24), command=lambda: açıkla2 ("Tamam"))
tamam.grid (row=1, column=0,columnspan=26)

mainloop()