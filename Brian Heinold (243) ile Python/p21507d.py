# coding:iso-8859-9 T�rk�e
# Program geneldir, L1'nun sat�r/s�tun ve oyuncu say�s�n� istedi�ince de�i�tirebilirsin...

from random import randint
from tkinter import *
Tk()

# Bilardo misali, (deli�i) tutturdu�un s�rece sen oynars�n, tutturamazsan oyuncu (s�ras�) de�i�ir...
def hamleyiYap():
    global sat�r, s�tun, oyuncu, L0
    m = randint (0, sat�r-1)
    n = randint (0, s�tun-1)

    if L0[m][n] == 0:
        L0[m][n] = oyuncu
        panoyuYaz (m, n)
    else: oyuncu = (oyuncu+3)%3+ 1

def kazanan�nTespiti():
    global saya�1, saya�2, saya�3
    saya�1 = saya�2 = saya�3 = 0
    for i in range (sat�r):
        for j in range (s�tun):
            if L0[i][j] == 1: saya�1 +=1
            if L0[i][j] == 2: saya�2 +=1
            if L0[i][j] == 3: saya�3 +=1
    if (saya�1+saya�2+saya�3) == sat�r*s�tun:
        if saya�1 == saya�2 == saya�3: return 0
        if saya�1 >= saya�2 and saya�1 >= saya�3: return 1
        if saya�2 >= saya�1 and saya�2 >= saya�3: return 2
        if saya�3 >= saya�1 and saya�3 >= saya�2: return 3
    return -1

def panoyuYaz (i, j):
    if oyuncu == 1: L1[i][j].configure (text=str (L2[oyuncu]), fg='blue', bg='pink')
    elif oyuncu == 2: L1[i][j].configure (text=str (L2[oyuncu]), fg='orange', bg='black')
    elif oyuncu == 3: L1[i][j].configure (text=str (L2[oyuncu]), fg='cyan', bg='green')
    else: L1[i][j].configure (text=str (L2[0]), fg='yellow', bg='blue')

def sonu�():
    sonu� = Label (font= ("times new roman", 25, "italic bold"), fg="maroon")
    if t == 0: sonu�.configure (text="BERABERE")
    else: sonu�.configure (text="({}, {}, {})==>Kazanan oyuncu: {}".format (saya�1, saya�2, saya�3, L2[t]) )
    sonu�.grid (row=sat�r+2, column=0, columnspan=s�tun, pady=5)
#===========================================================
oyuncu = randint (1,3) # Oyuna ba�lama s�ras� tesad�fidir...
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
sat�r = len (L0)
s�tun = len (L0[0])

for i in range (sat�r):
    for j in range (s�tun):
        L1[i][j] = Label (font=("verdana",20), width=4, bg="yellow")
        L1[i][j].grid (row=i, column=j, padx=1, pady=1)

t=-1
while t == -1:
    hamleyiYap()
    t = kazanan�nTespiti()
sonu�()
mainloop()
