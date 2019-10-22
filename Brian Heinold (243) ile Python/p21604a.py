# coding:iso-8859-9 Türkçe
# Gereken resim dosyası: 2.gif

from tkinter import *
kök = Tk()

def hepsiniÇizSil():
    global sayaç1, tüval, resim, res, oval, kutu
    sayaç1 +=1
    if sayaç1%2==1:
        tüval.create_rectangle (20,20, 50,70)
        kutu = tüval.create_rectangle (20,100, 50,150, fill="orange")

        tüval.create_line (70,20, 100,70); tüval.create_line (100,20, 70,70)
        tüval.create_line (70,100, 100,150, fill="red"); tüval.create_line (100,100, 70,150, fill="red")

        tüval.create_oval (120,20, 150,70)
        oval = tüval.create_oval (120,100, 150,150, fill="maroon")

        tüval.create_line (170,20, 200,70); tüval.create_line (200,20, 170,70)
        tüval.create_rectangle (170,20, 200,70); tüval.create_oval (170,20, 200,70)

        tüval.create_rectangle (170,100, 200,150, fill="yellow"); tüval.create_oval (170,100, 200,150, fill="maroon")
        tüval.create_line (170,100, 200,150, fill="orange"); tüval.create_line (200,100, 170,150, fill="orange")

        # merkez (x,y)=(300,85), yarıçap (i)=70, bir çember: "tüval.create_oval (x-i,y-i, x+i,y+i)"
        tüval.create_oval (300-70,85-70, 300+70,85+70, fill="black")
        daire (300, 85, 60, "pink"); daire (300, 85, 50, "blue")
        daire (300, 85, 40, "green"); daire (300, 85, 30, "yellow")
        daire (300, 85, 20, "maroon"); daire (300, 85, 10, "white")
        daire (300, 85, 2, "red")

        res = tüval.create_image (500, 85, image=resim) # Resmin merkezi (x,y)=(500,85)
    else: tüval.delete (ALL)

def resimSağaSola():
    global sayaç2
    sayaç2 +=1
    if sayaç2%2==1: tüval.coords (res, 400,85)
    else: tüval.coords (res, 500,85)

def renkDeğiştir():
    global sayaç3
    sayaç3 +=1
    if sayaç3%3==1: tüval.itemconfigure (oval, fill="green")
    elif sayaç3%3==2: tüval.itemconfigure (oval, fill="blue")
    else: tüval.itemconfigure (oval, fill="maroon")

def kutuyuÇizSil():
    global sayaç4, kutu
    sayaç4 +=1
    if sayaç4%2==0: kutu = tüval.create_rectangle (20,100, 50,150, fill="orange")
    else: tüval.delete (kutu)

def daire (x, y, i, renk): tüval.create_oval (x-i,y-i, x+i,y+i, fill=renk)

sayaç1 = sayaç2 = sayaç3 = sayaç4 = 0
tüval = Canvas (width=600, height=170, bg='cyan')
tüval.grid(row=0, column=0) # veya: "tüval.pack()"
resim = PhotoImage (file="2.gif")

çerçeve = Frame()
düğme1= Button (çerçeve, text="Tümünü:Çiz/Sil", bg="black", fg="yellow", command=hepsiniÇizSil)
düğme2= Button (çerçeve, text="Kutuyu:Çiz/Sil", bg="black", fg="yellow", command=kutuyuÇizSil)
düğme3= Button (çerçeve, text="Oval:Bordo/Yeşil/Mavi", bg="black", fg="yellow", command=renkDeğiştir)
düğme4= Button (çerçeve, text="Resim:Sola/Sağa", bg="black", fg="yellow", command=resimSağaSola)

düğme1.grid (row=1, column=0)
düğme2.grid (row=1, column=1, padx=2)
düğme3.grid (row=1, column=2)
düğme4.grid (row=1, column=3, padx=2)
çerçeve.grid (row=1, column=0, pady=5)

kök.mainloop()
