# coding:iso-8859-9 Türkçe

import sys
import turtle

def sınır (t, ekran_x, ekran_y):
    """(Turtle, int, int)
    Canvas'ın çevresine kalın bir yeşil sınır çizer...
    """
    # Kalemi kaldır ve tosbağanın ortasına git...
    t.penup()
    t.home()

    t.forward (ekran_x / 2) # Ortadan ileri (sağa) tosbağa ekran genişliği yarısı kadar git...
    t.right (90) # Sağa yani aşağıya dön...
    t.forward (ekran_y / 2) # (Aşağıya doğru) tosbağa yarı yüksekliği in...
    t.setheading (180) # 180 derece konuma dön veya t.right (90) da aynısını yapar...

    # Sınırı çizmeye başlayalım...
    t.pencolor ("MAROON")
    t.pendown()
    t.pensize (10)
    for mesafe in (ekran_x, ekran_y, ekran_x, ekran_y):
        t.forward (mesafe)
        t.right (90)

    # Kalemi kaldır tosbağa ortasına getir ki başlangıç konumu bilinsin...
    t.penup()
    t.home()

def kare (t, uzunluk, renk):
    """(Turtle, int, str)
    Verili kenar ve renkle bir kare çizer...
    """
    t.pencolor (renk)
    t.pendown()
    for i in range (4):
        t.forward (uzunluk)
        t.right (90)

def anaProgram():
    # Ekranı ve tosbağayı yaratalım...
    ekran = turtle.Screen()
    ekran.title ("Kare Gösterisi")
    ekran_x, ekran_y = ekran.screensize()
    t = turtle.Turtle()

    # Grafiğin daha süratli/yavaş çizilmesini istiyorsanız alttakine değer değiştirin...
    t.speed (0)

    # Canvas komponenti çevresini kalın bir kırmızı sınırla çizelim...
    sınır (t, ekran_x, ekran_y)

    # Ortadan itibaren, herbiri ekran yüksekliğinin %10, %20.., %50 uzunlukta farklı renkte kareler çizelim...
    renkler = ['olive', 'navy', 'fuchsia', 'aqua', 'teal', 'pink', 'lime', 'silver']
    t.pensize (3)
    for i, renk in enumerate (renkler):
        kare (t, (ekran_y / 2) / 10 * (i+1), renk)

    print ("Programı sonlandırmak için Ent bas:")
    tuş = input()
    sys.exit (0)

if __name__ == '__main__':
    anaProgram()
