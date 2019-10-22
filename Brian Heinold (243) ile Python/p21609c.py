# coding:iso-8859-9 T�rk�e

from tkinter import *
k�k = Tk()

def fareOynad� (olay):
    etiket.config (text="({:d},{:d})".format (olay.x, olay.y) )

def tekerOynad� (olay):
    global ebat,x,y
    if olay.delta > 0: fark = +1
    else: fark = -1
    ebat +=fark
    tuval.coords (kutu, x,y, x+ebat,y+ebat)

def kutuS�r�klendi (olay):
    global x,y,ebat,s�r�klendiMi
    x = olay.x
    y = olay.y
    tuval.coords (kutu, x,y, x+ebat,y+ebat)
    s�r�klendiMi = True

def renkDe�i�tir (olay):
    global renk
    if not s�r�klendiMi:
        renk = "pink" if renk == "blue" else "blue"
        tuval.itemconfig (kutu, fill=renk)

def durumDe�i�tir (olay):
    global s�r�klendiMi
    s�r�klendiMi = False

if __name__ == "__main__":
    tuval = Canvas (k�k, width=300, height=300, bg="maroon")
    tuval.pack()

    #tuval.focus_set() ==>Gerekmez, zira tekerin tuval i�inde ilk d�n��� odaklanmay� etkinle�tiriyor...
    s�r�klendiMi = False
    x = 50
    y = 100
    ebat = 50
    renk = "blue"
    kutu = tuval.create_rectangle (x,y, x+ebat, y+ebat, fill=renk)

    tuval.bind ("<Motion>", fareOynad�)
    tuval.bind ("<MouseWheel>", tekerOynad�)
    tuval.tag_bind (kutu, "<B1-Motion>", kutuS�r�klendi)
    tuval.bind ("<ButtonRelease-1>", renkDe�i�tir)
    tuval.bind ("<ButtonPress-1>", durumDe�i�tir)

    etiket = Label (k�k, bg="black", fg="yellow")
    etiket.pack()

mainloop()
