# coding:iso-8859-9 T�rk�e

from tkinter import *
from p21601 import Renk
k�k = Tk()
k�k.title ("Yeni Pencereler")

def yeni():
    global saya�
    saya� +=1
    k�k.title ("Pencere#: "+str(saya�))
    yeni = Toplevel()
    Label (yeni, font=("arial black", 20, "bold"), text="Pencere no: "+str(saya�), bg=Renk.renk(), fg=Renk.renk() ).pack()

if __name__ == "__main__":
    saya� = 0
    Button (k�k, text="Yeni Pencere", command=yeni, bg="black", fg="yellow" ).pack()

mainloop()
