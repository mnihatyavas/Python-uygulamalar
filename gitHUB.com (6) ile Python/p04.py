# coding:iso-8859-9 Türkçe
# güneş->merkür->venüs->dünya->mars->uranüs->jüpiter->neptün->satürn..

import math
from turtle import * # Turtle dahil tüm sınıfları...

# Evrensel kütle çekim/gravitational sabitesi G
G = 6.67428e-11

# Bu programda kullanılan birim: 100 pixels = 1ADIM.
ADIM = (149.6e6 * 1000)     # 149.6 million km, in meters.
ÖLÇEK = 250 / ADIM

class Gezegen (Turtle):
    """Turtle'ın altsınıfı bir yerçekimsel gezegeni temsil etmektedir...
    Değişken tanımları:
    kütlesi : ağırlık->kg
    vx, vy: x-yatay ve y-dikey hız->m/s
    px, py: x-yatay ve y-d,key konum/uzaklık->m
    """

    adı = 'Gezegen'
    kütlesi = None
    vx = vy = 0.0
    px = py = 0.0

    def çekim (self, diğeri):
        """(Gezegen): (fx, fy)
        Diğer gezegenin bu gezegen üzerindeki çekim gücünü dönderir...
        """
        # Eğer diğeriyle bu yanlışlıkla aynı gezegense hata mesajı verir...
        if self is diğeri: raise ValueError ("%r gezegeninin kendi üzerindeki çekimi soruluyor!" % self.adı)

        # İki gezegen arası mesafe hesaplanıyor...
        sx, sy = self.px, self.py
        ox, oy = diğeri.px, diğeri.py
        dx = (ox - sx)
        dy = (oy - sy)
        d = math.sqrt (dx**2 + dy**2)

        # Mesafe sıfırsa hata bildir, yoksa birazdan sıfıra bölüm oluşacak...
        # get a ZeroDivisionError exception further down.
        if d == 0: raise ValueError ("%r ve %r gezegenlerde çarpışma var!" % (self.adı, diğeri.adı))

        # Çekim gücü hesaplanıyor...
        f = G * self.kütlesi * diğeri.kütlesi / (d**2)

        # Çekim gücünün yönü hesaplanıyor...
        theta = math.atan2 (dy, dx)
        fx = math.cos (theta) * f
        fy = math.sin (theta) * f
        return fx, fy

def bilgileriGüncelle (adım, gezegenler):
    """(int, [Gezegen])
    Simülasyonun son durumu hakkındaki bilgileri gösterir...
    """
    print ('Adım #{}' .format (adım))
    for gezegen in gezegenler:
        dizge = '{:<8}  Konum={:>6.2f} {:>6.2f} Hız={:>10.3f} {:>10.3f}' .format (
                gezegen.adı, gezegen.px / ADIM, gezegen.py / ADIM, gezegen.vx, gezegen.vy)
        print (dizge)
    print()

def döngüyüBaşlat (gezegenler):
    """([Gezegen])
    Sonsuz döngü, çıkmak için ^C bas. Verili gezegen konum bilgileri sürekli
    güncellenip turtle çizimi süregider...
    """
    zamanAralığı = 7 * 24 * 3600 # Bir hafta...

    for gezegen in gezegenler:
        gezegen.penup()
        #gezegen.hideturtle() #Çizim kalemimiz görünedursun...

    adım = 1
    while True:
        bilgileriGüncelle (adım, gezegenler)
        adım += 1

        kuvvet = {}
        for gezegen in gezegenler:
            # Verili 'gezegen' üzerine uygulanan tüm yatay ve dikey kuvvetler hesaplanır...
            toplam_fx = toplam_fy = 0.0
            for diğeri in gezegenler:
                # Bir gezegenin kendi üzerine olan çekimi hesaplanmamalı...
                if gezegen is diğeri: continue
                fx, fy = gezegen.çekim (diğeri)
                toplam_fx += fx
                toplam_fy += fy

            # Toplam uygulanan kuvvet kaydedilir...
            kuvvet [gezegen] = (toplam_fx, toplam_fy)

        # Kuvvete temelli dönüş hızları güncellenir...
        for gezegen in gezegenler:
            fx, fy = kuvvet [gezegen]
            gezegen.vx += fx / gezegen.kütlesi * zamanAralığı
            gezegen.vy += fy / gezegen.kütlesi * zamanAralığı

            # Yeni gezegen konumları güncellenir...
            gezegen.px += gezegen.vx * zamanAralığı
            gezegen.py += gezegen.vy * zamanAralığı
            gezegen.goto (gezegen.px * ÖLÇEK, gezegen.py * ÖLÇEK)
            gezegen.dot (5) # 5 derece kalınlıklı noktalama konulur...


def anaProgram():
    güneş = Gezegen() # Sınıf nesnesi...
    güneş.adı = 'GÜNEŞ'
    güneş.kütlesi = 1.98892 * 10**30
    güneş.pencolor ('RED')

    dünya = Gezegen() # Sınıf nesnesi...
    dünya.adı = 'DÜNYA'
    dünya.kütlesi = 5.9742 * 10**24 # Dünya ile venüs'ün kütleleri yakın...
    dünya.px = -1*ADIM # Dünya yarıçapı: 1 Adım=149.6 milyon-km...
    dünya.vy = 29.783 * 1000 # Dünya'nın güneş çevresindeki dönüş hızı=29.78 km/sn
    dünya.pencolor ('BLUE')

    # http://nssdc.gsfc.nasa.gov/planetary/factsheet/venüsfact.html
    venüs = Gezegen() # Sınıf nesnesi...
    venüs.adı = 'VENÜS'
    venüs.kütlesi = 4.8685 * 10**24
    venüs.px = 0.723 * ADIM # Venüs yarıçapı=149.6 * 0.723=108.16 milyon-km...
    venüs.vy = -35.02 * 1000 # Venüs'ün hızı=35.02 km/sn
    venüs.pencolor ('ORANGE')

    döngüyüBaşlat ([güneş, dünya, venüs])

if __name__ == '__main__':
    anaProgram()