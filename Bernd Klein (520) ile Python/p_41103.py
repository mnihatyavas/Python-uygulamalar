# coding:iso-8859-9 T�rk�e
# p_41103.py: Python colorchooser ile renk se�me diyalo�u �rne�i.

from tkinter import *
from tkinter.colorchooser import askcolor
from p_315 import Renk

k�k = Tk()
k�k.title ("Renk Se�me Diyalo�u")

def renkSe�():
    renk = askcolor (color="#6A9662", title = "MNYava�'�n Renk Se�eri")
    etiket.config (text="Se�ti�iniz yaz� rengi: " + str (renk), fg=renk[1], bg=Renk.renk() )
    
Button (k�k, text='Renk Se�', fg="darkgreen", command=renkSe�).pack (side=LEFT, padx=10)
Button (k�k, text='�IK', command=k�k.quit, fg="#c00").pack (side=LEFT, padx=10)

etiket = Label (k�k, font=("Segoe Script", 15, "bold", "italic"))
etiket.pack()

k�k.mainloop()