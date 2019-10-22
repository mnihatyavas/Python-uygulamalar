# coding:iso-8859-9 Türkçe

from tkinter import *
Tk()

def tıklandığınıBildir (x):
    global uz, L2, alfabe
    L2[x] +=1
    açıklama = Label (font=("Verdana", 20, "italic bold"), fg="green",\
        text='"{}" düğmesini <{:d}>.kez tıkladınız!' .format (alfabe[x], L2[x]))
    açıklama.grid (row=1, column=0, columnspan=uz, pady=20)

alfabe = 'ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ'

uz = len (alfabe)
L1 = [0]*uz
L2 = [0]*uz
for i in range (uz):
    L1[i] = Button (text=alfabe[i], command=lambda x=i: tıklandığınıBildir (x) )
    L1[i].grid (row=0, column=i, padx=1)

mainloop()