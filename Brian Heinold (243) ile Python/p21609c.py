# coding:iso-8859-9 Türkçe

from tkinter import *
kök = Tk()

def fareOynadı (olay):
    etiket.config (text="({:d},{:d})".format (olay.x, olay.y) )

def tekerOynadı (olay):
    global ebat,x,y
    if olay.delta > 0: fark = +1
    else: fark = -1
    ebat +=fark
    tuval.coords (kutu, x,y, x+ebat,y+ebat)

def kutuSürüklendi (olay):
    global x,y,ebat,sürüklendiMi
    x = olay.x
    y = olay.y
    tuval.coords (kutu, x,y, x+ebat,y+ebat)
    sürüklendiMi = True

def renkDeğiştir (olay):
    global renk
    if not sürüklendiMi:
        renk = "pink" if renk == "blue" else "blue"
        tuval.itemconfig (kutu, fill=renk)

def durumDeğiştir (olay):
    global sürüklendiMi
    sürüklendiMi = False

if __name__ == "__main__":
    tuval = Canvas (kök, width=300, height=300, bg="maroon")
    tuval.pack()

    #tuval.focus_set() ==>Gerekmez, zira tekerin tuval içinde ilk dönüşü odaklanmayı etkinleştiriyor...
    sürüklendiMi = False
    x = 50
    y = 100
    ebat = 50
    renk = "blue"
    kutu = tuval.create_rectangle (x,y, x+ebat, y+ebat, fill=renk)

    tuval.bind ("<Motion>", fareOynadı)
    tuval.bind ("<MouseWheel>", tekerOynadı)
    tuval.tag_bind (kutu, "<B1-Motion>", kutuSürüklendi)
    tuval.bind ("<ButtonRelease-1>", renkDeğiştir)
    tuval.bind ("<ButtonPress-1>", durumDeğiştir)

    etiket = Label (kök, bg="black", fg="yellow")
    etiket.pack()

mainloop()
