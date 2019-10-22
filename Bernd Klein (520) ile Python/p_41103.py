# coding:iso-8859-9 Türkçe
# p_41103.py: Python colorchooser ile renk seçme diyaloğu örneği.

from tkinter import *
from tkinter.colorchooser import askcolor
from p_315 import Renk

kök = Tk()
kök.title ("Renk Seçme Diyaloğu")

def renkSeç():
    renk = askcolor (color="#6A9662", title = "MNYavaş'ın Renk Seçeri")
    etiket.config (text="Seçtiğiniz yazı rengi: " + str (renk), fg=renk[1], bg=Renk.renk() )
    
Button (kök, text='Renk Seç', fg="darkgreen", command=renkSeç).pack (side=LEFT, padx=10)
Button (kök, text='ÇIK', command=kök.quit, fg="#c00").pack (side=LEFT, padx=10)

etiket = Label (kök, font=("Segoe Script", 15, "bold", "italic"))
etiket.pack()

kök.mainloop()