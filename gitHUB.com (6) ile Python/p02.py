# coding:iso-8859-9 T�rk�e

import sys
import turtle

def s�n�r (t, ekran_x, ekran_y):
    """(Turtle, int, int)
    Canvas'�n �evresine kal�n bir ye�il s�n�r �izer...
    """
    # Kalemi kald�r ve tosba�an�n ortas�na git...
    t.penup()
    t.home()

    t.forward (ekran_x / 2) # Ortadan ileri (sa�a) tosba�a ekran geni�li�i yar�s� kadar git...
    t.right (90) # Sa�a yani a�a��ya d�n...
    t.forward (ekran_y / 2) # (A�a��ya do�ru) tosba�a yar� y�ksekli�i in...
    t.setheading (180) # 180 derece konuma d�n veya t.right (90) da ayn�s�n� yapar...

    # S�n�r� �izmeye ba�layal�m...
    t.pencolor ("MAROON")
    t.pendown()
    t.pensize (10)
    for mesafe in (ekran_x, ekran_y, ekran_x, ekran_y):
        t.forward (mesafe)
        t.right (90)

    # Kalemi kald�r tosba�a ortas�na getir ki ba�lang�� konumu bilinsin...
    t.penup()
    t.home()

def kare (t, uzunluk, renk):
    """(Turtle, int, str)
    Verili kenar ve renkle bir kare �izer...
    """
    t.pencolor (renk)
    t.pendown()
    for i in range (4):
        t.forward (uzunluk)
        t.right (90)

def anaProgram():
    # Ekran� ve tosba�ay� yaratal�m...
    ekran = turtle.Screen()
    ekran.title ("Kare G�sterisi")
    ekran_x, ekran_y = ekran.screensize()
    t = turtle.Turtle()

    # Grafi�in daha s�ratli/yava� �izilmesini istiyorsan�z alttakine de�er de�i�tirin...
    t.speed (0)

    # Canvas komponenti �evresini kal�n bir k�rm�z� s�n�rla �izelim...
    s�n�r (t, ekran_x, ekran_y)

    # Ortadan itibaren, herbiri ekran y�ksekli�inin %10, %20.., %50 uzunlukta farkl� renkte kareler �izelim...
    renkler = ['olive', 'navy', 'fuchsia', 'aqua', 'teal', 'pink', 'lime', 'silver']
    t.pensize (3)
    for i, renk in enumerate (renkler):
        kare (t, (ekran_y / 2) / 10 * (i+1), renk)

    print ("Program� sonland�rmak i�in Ent bas:")
    tu� = input()
    sys.exit (0)

if __name__ == '__main__':
    anaProgram()
