# coding:iso-8859-9 T�rk�e

from p21601 import Renk # Listede mevcut...
from tkinter import *
k�k = Tk()
k�k.title ("Fare t�kla-s�r�kle-konum G�sterisi")

def fareHareketiOlay� (olay):
    etiket.config (text='({}, {})'.format (olay.x, olay.y))

def fareTekeriOlay� (olay):
    global x1, x2, y1, y2
    if olay.delta > 0: fark = 1
    elif olay.delta < 0: fark = -1
    x1 +=fark
    x2 -=fark
    y1 +=fark
    y2 -=fark
    tuval.coords (kutu, x1,y1, x2,y2)

def solBasmaOlay� (olay): s�r�klemeMi = False

def solS�r�klemeOlay� (olay):
    global s�r�klemeMi, x1, x2, y1, y2, fareX, fareY
    x = olay.x
    y = olay.y
    if not s�r�klemeMi:
        fareX = x
        fareY = y
        s�r�klemeMi = True
        return
    x1 +=(x-fareX)
    x2 +=(x-fareX)
    y1 +=(y-fareY)
    y2 +=(y-fareY)
    tuval.coords (kutu, x1,y1, x2,y2)
    fareX = x
    fareY = y

def solB�rakmaOlay� (olay):
    global renk, s�r�klemeMi
    if not s�r�klemeMi:
        renk = 'Red' if renk=='Blue' else 'Blue'
        tuval.itemconfig (kutu, fill=renk)
    s�r�klemeMi = False


if __name__ == "__main__":
    tuval = Canvas (k�k, width=300, height=300, bg="maroon")
    tuval.grid (row=0, column=0)

    renk = 'blue'
    x1 = y1 = 50
    x2 = y2 = 100
    kutu = tuval.create_rectangle (x1,y1, x2,y2, fill=renk)

    tuval.bind ('<Motion>', fareHareketiOlay�)
    tuval.bind ('<MouseWheel>', fareTekeriOlay�)
    tuval.bind ('<ButtonPress-1>', solBasmaOlay�)
    tuval.bind ('<B1-Motion>', solS�r�klemeOlay�)
    tuval.bind ('<ButtonRelease-1>', solB�rakmaOlay�)

    #tuval.focus_set()

    etiket = Label (k�k, bg="black", fg="yellow")
    etiket.grid (row=1, column=0)

    fareX = 0
    fareY = 0
    s�r�klemeMi = False

mainloop()
