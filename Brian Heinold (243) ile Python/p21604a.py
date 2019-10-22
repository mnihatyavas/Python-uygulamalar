# coding:iso-8859-9 T�rk�e
# Gereken resim dosyas�: 2.gif

from tkinter import *
k�k = Tk()

def hepsini�izSil():
    global saya�1, t�val, resim, res, oval, kutu
    saya�1 +=1
    if saya�1%2==1:
        t�val.create_rectangle (20,20, 50,70)
        kutu = t�val.create_rectangle (20,100, 50,150, fill="orange")

        t�val.create_line (70,20, 100,70); t�val.create_line (100,20, 70,70)
        t�val.create_line (70,100, 100,150, fill="red"); t�val.create_line (100,100, 70,150, fill="red")

        t�val.create_oval (120,20, 150,70)
        oval = t�val.create_oval (120,100, 150,150, fill="maroon")

        t�val.create_line (170,20, 200,70); t�val.create_line (200,20, 170,70)
        t�val.create_rectangle (170,20, 200,70); t�val.create_oval (170,20, 200,70)

        t�val.create_rectangle (170,100, 200,150, fill="yellow"); t�val.create_oval (170,100, 200,150, fill="maroon")
        t�val.create_line (170,100, 200,150, fill="orange"); t�val.create_line (200,100, 170,150, fill="orange")

        # merkez (x,y)=(300,85), yar��ap (i)=70, bir �ember: "t�val.create_oval (x-i,y-i, x+i,y+i)"
        t�val.create_oval (300-70,85-70, 300+70,85+70, fill="black")
        daire (300, 85, 60, "pink"); daire (300, 85, 50, "blue")
        daire (300, 85, 40, "green"); daire (300, 85, 30, "yellow")
        daire (300, 85, 20, "maroon"); daire (300, 85, 10, "white")
        daire (300, 85, 2, "red")

        res = t�val.create_image (500, 85, image=resim) # Resmin merkezi (x,y)=(500,85)
    else: t�val.delete (ALL)

def resimSa�aSola():
    global saya�2
    saya�2 +=1
    if saya�2%2==1: t�val.coords (res, 400,85)
    else: t�val.coords (res, 500,85)

def renkDe�i�tir():
    global saya�3
    saya�3 +=1
    if saya�3%3==1: t�val.itemconfigure (oval, fill="green")
    elif saya�3%3==2: t�val.itemconfigure (oval, fill="blue")
    else: t�val.itemconfigure (oval, fill="maroon")

def kutuyu�izSil():
    global saya�4, kutu
    saya�4 +=1
    if saya�4%2==0: kutu = t�val.create_rectangle (20,100, 50,150, fill="orange")
    else: t�val.delete (kutu)

def daire (x, y, i, renk): t�val.create_oval (x-i,y-i, x+i,y+i, fill=renk)

saya�1 = saya�2 = saya�3 = saya�4 = 0
t�val = Canvas (width=600, height=170, bg='cyan')
t�val.grid(row=0, column=0) # veya: "t�val.pack()"
resim = PhotoImage (file="2.gif")

�er�eve = Frame()
d��me1= Button (�er�eve, text="T�m�n�:�iz/Sil", bg="black", fg="yellow", command=hepsini�izSil)
d��me2= Button (�er�eve, text="Kutuyu:�iz/Sil", bg="black", fg="yellow", command=kutuyu�izSil)
d��me3= Button (�er�eve, text="Oval:Bordo/Ye�il/Mavi", bg="black", fg="yellow", command=renkDe�i�tir)
d��me4= Button (�er�eve, text="Resim:Sola/Sa�a", bg="black", fg="yellow", command=resimSa�aSola)

d��me1.grid (row=1, column=0)
d��me2.grid (row=1, column=1, padx=2)
d��me3.grid (row=1, column=2)
d��me4.grid (row=1, column=3, padx=2)
�er�eve.grid (row=1, column=0, pady=5)

k�k.mainloop()
