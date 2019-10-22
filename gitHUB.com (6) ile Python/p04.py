# coding:iso-8859-9 T�rk�e
# g�ne�->merk�r->ven�s->d�nya->mars->uran�s->j�piter->nept�n->sat�rn..

import math
from turtle import * # Turtle dahil t�m s�n�flar�...

# Evrensel k�tle �ekim/gravitational sabitesi G
G = 6.67428e-11

# Bu programda kullan�lan birim: 100 pixels = 1ADIM.
ADIM = (149.6e6 * 1000)     # 149.6 million km, in meters.
�L�EK = 250 / ADIM

class Gezegen (Turtle):
    """Turtle'�n alts�n�f� bir yer�ekimsel gezegeni temsil etmektedir...
    De�i�ken tan�mlar�:
    k�tlesi : a��rl�k->kg
    vx, vy: x-yatay ve y-dikey h�z->m/s
    px, py: x-yatay ve y-d,key konum/uzakl�k->m
    """

    ad� = 'Gezegen'
    k�tlesi = None
    vx = vy = 0.0
    px = py = 0.0

    def �ekim (self, di�eri):
        """(Gezegen): (fx, fy)
        Di�er gezegenin bu gezegen �zerindeki �ekim g�c�n� d�nderir...
        """
        # E�er di�eriyle bu yanl��l�kla ayn� gezegense hata mesaj� verir...
        if self is di�eri: raise ValueError ("%r gezegeninin kendi �zerindeki �ekimi soruluyor!" % self.ad�)

        # �ki gezegen aras� mesafe hesaplan�yor...
        sx, sy = self.px, self.py
        ox, oy = di�eri.px, di�eri.py
        dx = (ox - sx)
        dy = (oy - sy)
        d = math.sqrt (dx**2 + dy**2)

        # Mesafe s�f�rsa hata bildir, yoksa birazdan s�f�ra b�l�m olu�acak...
        # get a ZeroDivisionError exception further down.
        if d == 0: raise ValueError ("%r ve %r gezegenlerde �arp��ma var!" % (self.ad�, di�eri.ad�))

        # �ekim g�c� hesaplan�yor...
        f = G * self.k�tlesi * di�eri.k�tlesi / (d**2)

        # �ekim g�c�n�n y�n� hesaplan�yor...
        theta = math.atan2 (dy, dx)
        fx = math.cos (theta) * f
        fy = math.sin (theta) * f
        return fx, fy

def bilgileriG�ncelle (ad�m, gezegenler):
    """(int, [Gezegen])
    Sim�lasyonun son durumu hakk�ndaki bilgileri g�sterir...
    """
    print ('Ad�m #{}' .format (ad�m))
    for gezegen in gezegenler:
        dizge = '{:<8}  Konum={:>6.2f} {:>6.2f} H�z={:>10.3f} {:>10.3f}' .format (
                gezegen.ad�, gezegen.px / ADIM, gezegen.py / ADIM, gezegen.vx, gezegen.vy)
        print (dizge)
    print()

def d�ng�y�Ba�lat (gezegenler):
    """([Gezegen])
    Sonsuz d�ng�, ��kmak i�in ^C bas. Verili gezegen konum bilgileri s�rekli
    g�ncellenip turtle �izimi s�regider...
    """
    zamanAral��� = 7 * 24 * 3600 # Bir hafta...

    for gezegen in gezegenler:
        gezegen.penup()
        #gezegen.hideturtle() #�izim kalemimiz g�r�nedursun...

    ad�m = 1
    while True:
        bilgileriG�ncelle (ad�m, gezegenler)
        ad�m += 1

        kuvvet = {}
        for gezegen in gezegenler:
            # Verili 'gezegen' �zerine uygulanan t�m yatay ve dikey kuvvetler hesaplan�r...
            toplam_fx = toplam_fy = 0.0
            for di�eri in gezegenler:
                # Bir gezegenin kendi �zerine olan �ekimi hesaplanmamal�...
                if gezegen is di�eri: continue
                fx, fy = gezegen.�ekim (di�eri)
                toplam_fx += fx
                toplam_fy += fy

            # Toplam uygulanan kuvvet kaydedilir...
            kuvvet [gezegen] = (toplam_fx, toplam_fy)

        # Kuvvete temelli d�n�� h�zlar� g�ncellenir...
        for gezegen in gezegenler:
            fx, fy = kuvvet [gezegen]
            gezegen.vx += fx / gezegen.k�tlesi * zamanAral���
            gezegen.vy += fy / gezegen.k�tlesi * zamanAral���

            # Yeni gezegen konumlar� g�ncellenir...
            gezegen.px += gezegen.vx * zamanAral���
            gezegen.py += gezegen.vy * zamanAral���
            gezegen.goto (gezegen.px * �L�EK, gezegen.py * �L�EK)
            gezegen.dot (5) # 5 derece kal�nl�kl� noktalama konulur...


def anaProgram():
    g�ne� = Gezegen() # S�n�f nesnesi...
    g�ne�.ad� = 'G�NE�'
    g�ne�.k�tlesi = 1.98892 * 10**30
    g�ne�.pencolor ('RED')

    d�nya = Gezegen() # S�n�f nesnesi...
    d�nya.ad� = 'D�NYA'
    d�nya.k�tlesi = 5.9742 * 10**24 # D�nya ile ven�s'�n k�tleleri yak�n...
    d�nya.px = -1*ADIM # D�nya yar��ap�: 1 Ad�m=149.6 milyon-km...
    d�nya.vy = 29.783 * 1000 # D�nya'n�n g�ne� �evresindeki d�n�� h�z�=29.78 km/sn
    d�nya.pencolor ('BLUE')

    # http://nssdc.gsfc.nasa.gov/planetary/factsheet/ven�sfact.html
    ven�s = Gezegen() # S�n�f nesnesi...
    ven�s.ad� = 'VEN�S'
    ven�s.k�tlesi = 4.8685 * 10**24
    ven�s.px = 0.723 * ADIM # Ven�s yar��ap�=149.6 * 0.723=108.16 milyon-km...
    ven�s.vy = -35.02 * 1000 # Ven�s'�n h�z�=35.02 km/sn
    ven�s.pencolor ('ORANGE')

    d�ng�y�Ba�lat ([g�ne�, d�nya, ven�s])

if __name__ == '__main__':
    anaProgram()