# coding:iso-8859-9 Türkçe

from tkinter import *
Tk()

def tıklandığınıBildir (x):
    açıklama = Label (font=("Verdana", 20, "italic bold"), fg="blue",\
        text='"{}" düğmesini tıkladınız!' .format (alfabe[x]))
    açıklama.grid (row=1, column=0, columnspan=29, pady=20)

alfabe = 'ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ'

L = [0]*29 # 29 düğmeyi kapsayan bir liste...
for i in range (29):
    L[i] = Button (text=alfabe[i], command=lambda x=i: tıklandığınıBildir (x) )
    L[i].grid (row=0, column=i, padx=1)

mainloop()