# coding:iso-8859-9 Türkçe

from p21601 import Renk # Listede mevcut...
from tkinter import *
kök = Tk()

def taşı (olay):
    global taşıX, taşıY
    if olay.keysym == 'Right': taşıX +=1
    elif olay.keysym=='Left': taşıX -=1
    elif olay.keysym=='Up': taşıY -=1
    elif olay.keysym == 'Down': taşıY +=1
    tuval.coords (kutu, 50+taşıX,50+taşıY, 100+taşıX,100+taşıY)

if __name__ == "__main__":
    kök.bind ('<Key>', taşı)
    tuval = Canvas (width=400, height=400, bg=Renk.renk())
    tuval.grid()
    tuval.create_text (200,10, text="Yön oklarıyla kutuyu taşıyın", fill="yellow") # (Alt_24-25-26-27: ^v›‹ )
    kutu = tuval.create_rectangle (50,50, 100,100, fill=Renk.renk())

    tuval.focus_set()
    taşıX = taşıY = 0

mainloop()