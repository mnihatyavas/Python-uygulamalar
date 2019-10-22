# coding:iso-8859-9 Türkçe

from p21601 import Renk # Listede mevcut...
from tkinter import *
kök = Tk()
kök.title ("Fare tıkla-sürükle-konum Gösterisi")

def fareHareketiOlayı (olay):
    etiket.config (text='({}, {})'.format (olay.x, olay.y))

def fareTekeriOlayı (olay):
    global x1, x2, y1, y2
    if olay.delta > 0: fark = 1
    elif olay.delta < 0: fark = -1
    x1 +=fark
    x2 -=fark
    y1 +=fark
    y2 -=fark
    tuval.coords (kutu, x1,y1, x2,y2)

def solBasmaOlayı (olay): sürüklemeMi = False

def solSürüklemeOlayı (olay):
    global sürüklemeMi, x1, x2, y1, y2, fareX, fareY
    x = olay.x
    y = olay.y
    if not sürüklemeMi:
        fareX = x
        fareY = y
        sürüklemeMi = True
        return
    x1 +=(x-fareX)
    x2 +=(x-fareX)
    y1 +=(y-fareY)
    y2 +=(y-fareY)
    tuval.coords (kutu, x1,y1, x2,y2)
    fareX = x
    fareY = y

def solBırakmaOlayı (olay):
    global renk, sürüklemeMi
    if not sürüklemeMi:
        renk = 'Red' if renk=='Blue' else 'Blue'
        tuval.itemconfig (kutu, fill=renk)
    sürüklemeMi = False


if __name__ == "__main__":
    tuval = Canvas (kök, width=300, height=300, bg="maroon")
    tuval.grid (row=0, column=0)

    renk = 'blue'
    x1 = y1 = 50
    x2 = y2 = 100
    kutu = tuval.create_rectangle (x1,y1, x2,y2, fill=renk)

    tuval.bind ('<Motion>', fareHareketiOlayı)
    tuval.bind ('<MouseWheel>', fareTekeriOlayı)
    tuval.bind ('<ButtonPress-1>', solBasmaOlayı)
    tuval.bind ('<B1-Motion>', solSürüklemeOlayı)
    tuval.bind ('<ButtonRelease-1>', solBırakmaOlayı)

    #tuval.focus_set()

    etiket = Label (kök, bg="black", fg="yellow")
    etiket.grid (row=1, column=0)

    fareX = 0
    fareY = 0
    sürüklemeMi = False

mainloop()
