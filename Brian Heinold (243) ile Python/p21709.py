# coding:iso-8859-9 Türkçe

from tkinter import *
from p21601 import Renk
kök = Tk()
kök.title ("Yeni Pencereler")

def yeni():
    global sayaç
    sayaç +=1
    kök.title ("Pencere#: "+str(sayaç))
    yeni = Toplevel()
    Label (yeni, font=("arial black", 20, "bold"), text="Pencere no: "+str(sayaç), bg=Renk.renk(), fg=Renk.renk() ).pack()

if __name__ == "__main__":
    sayaç = 0
    Button (kök, text="Yeni Pencere", command=yeni, bg="black", fg="yellow" ).pack()

mainloop()
