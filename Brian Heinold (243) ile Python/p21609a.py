# coding:iso-8859-9 T�rk�e

from p21601 import Renk # Listede mevcut...
from tkinter import *
k�k = Tk()

def ta�� (olay):
    global ta��X, ta��Y
    if olay.keysym == 'Right': ta��X +=1
    elif olay.keysym=='Left': ta��X -=1
    elif olay.keysym=='Up': ta��Y -=1
    elif olay.keysym == 'Down': ta��Y +=1
    tuval.coords (kutu, 50+ta��X,50+ta��Y, 100+ta��X,100+ta��Y)

if __name__ == "__main__":
    k�k.bind ('<Key>', ta��)
    tuval = Canvas (width=400, height=400, bg=Renk.renk())
    tuval.grid()
    tuval.create_text (200,10, text="Y�n oklar�yla kutuyu ta��y�n", fill="yellow") # (Alt_24-25-26-27: ^v�� )
    kutu = tuval.create_rectangle (50,50, 100,100, fill=Renk.renk())

    tuval.focus_set()
    ta��X = ta��Y = 0

mainloop()