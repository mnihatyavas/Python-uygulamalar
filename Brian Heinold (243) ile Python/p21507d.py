# coding:iso-8859-9 Türkçe
# Program geneldir, L1'nun satır/sütun ve oyuncu sayısını istediğince değiştirebilirsin...

from random import randint
from tkinter import *
Tk()

# Bilardo misali, (deliği) tutturduğun sürece sen oynarsın, tutturamazsan oyuncu (sırası) değişir...
def hamleyiYap():
    global satır, sütun, oyuncu, L0
    m = randint (0, satır-1)
    n = randint (0, sütun-1)

    if L0[m][n] == 0:
        L0[m][n] = oyuncu
        panoyuYaz (m, n)
    else: oyuncu = (oyuncu+3)%3+ 1

def kazananınTespiti():
    global sayaç1, sayaç2, sayaç3
    sayaç1 = sayaç2 = sayaç3 = 0
    for i in range (satır):
        for j in range (sütun):
            if L0[i][j] == 1: sayaç1 +=1
            if L0[i][j] == 2: sayaç2 +=1
            if L0[i][j] == 3: sayaç3 +=1
    if (sayaç1+sayaç2+sayaç3) == satır*sütun:
        if sayaç1 == sayaç2 == sayaç3: return 0
        if sayaç1 >= sayaç2 and sayaç1 >= sayaç3: return 1
        if sayaç2 >= sayaç1 and sayaç2 >= sayaç3: return 2
        if sayaç3 >= sayaç1 and sayaç3 >= sayaç2: return 3
    return -1

def panoyuYaz (i, j):
    if oyuncu == 1: L1[i][j].configure (text=str (L2[oyuncu]), fg='blue', bg='pink')
    elif oyuncu == 2: L1[i][j].configure (text=str (L2[oyuncu]), fg='orange', bg='black')
    elif oyuncu == 3: L1[i][j].configure (text=str (L2[oyuncu]), fg='cyan', bg='green')
    else: L1[i][j].configure (text=str (L2[0]), fg='yellow', bg='blue')

def sonuç():
    sonuç = Label (font= ("times new roman", 25, "italic bold"), fg="maroon")
    if t == 0: sonuç.configure (text="BERABERE")
    else: sonuç.configure (text="({}, {}, {})==>Kazanan oyuncu: {}".format (sayaç1, sayaç2, sayaç3, L2[t]) )
    sonuç.grid (row=satır+2, column=0, columnspan=sütun, pady=5)
#===========================================================
oyuncu = randint (1,3) # Oyuna başlama sırası tesadüfidir...
L0 = [[0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0] ]
L1 = [[0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0] ]
L2 = ["-", "A", "B", "C"]
satır = len (L0)
sütun = len (L0[0])

for i in range (satır):
    for j in range (sütun):
        L1[i][j] = Label (font=("verdana",20), width=4, bg="yellow")
        L1[i][j].grid (row=i, column=j, padx=1, pady=1)

t=-1
while t == -1:
    hamleyiYap()
    t = kazananınTespiti()
sonuç()
mainloop()
