# coding:iso-8859-9 T�rk�e

# p05.py -- Bir turtle-temelli Conway's Game of Life (Conway'in Hayat Oyunu) oyunu.
#
# �lk anda tesad�fi dolu bir ekran ve �u se�enekler sunulacakt�r:
#  S : Panoyu tamamen sil
#  G : Panoyu geli�ig�zel doldur
#  T : Tet tek ad�mlarla ilerle
#  D : Hareketli kare kalmay�ncaya kadar devaml� ilerle
#  K : Kapat
#  Fare : T�klanan h�creyi siler/doldurur
#

import sys
import turtle
import random

H�CRE_EBATI = 20 # Piksel �l��m�yle...

class HayatPanosu:
    """Geli�ig�zel bir hayat panosu (oyunu) kurar...

    S�n�f tip de�i�kenleri:
    xebat, yebat : Panonun yatay ve dikey ebatlar�...
    durum : Panodaki canl� h�crelerin (x,y) koordinatlar�n� i�eren bir set tip de�i�keni...

    Metodlar:
    g�ster (self) -- Pano durum set g�ncel i�eriklerini ekranda g�sterir...
    panoyuTamamenSil (self) -- T�m panoyu temizler...
    panoyuGeli�ig�zelDoldur (self) -- Panoyu (�nce siler) yeniba�tan geli�ig�zel doldurur...
    kur (self,x,y) -- Verili h�creyi set'e ekler; ancak ekran g�r�nt�s�n� g�ncellemez...
    ge�erlile (self,x,y) -- Tuklanan konumu doluysa bolat�r, bo�sa doldurur ve ekran g�r�nt�s�n� g�nceller...
    """
    def __init__  (self, xebat, yebat): # Kurucu...
        """Yeni bir HayatPanosu s�n�f nesne tipi yarat�l�r."""
        self.durum = set()
        self.xebat, self.yebat = xebat, yebat

    def panoyuTamamenSil (self):
        """T�m panoyu temizler."""
        self.durum.clear()

    def panoyuGeli�ig�zelDoldur (self):
        "Panoyu geli�ig�zel bir kal�pla doldurur..."
        self.panoyuTamamenSil()
        for i in range (0, self.xebat):
            for j in range (0, self.yebat):
                if random.random() > 0.5:
                    self.kur (i, j)

    def ad�mla (self):
        "Tek ad�m ilerler ve g�ster metodunu g�nceller."
        drm = set()
        for i in range (self.xebat):
            x_kapsam = range (max (0, i-1), min (self.xebat, i+2))
            for j in range (self.yebat):
                yeniSet = 0
                canl�Set = ((i,j) in self.durum)
                for ynokta in range (max (0, j-1), min (self.yebat, j+2)):
                    for xnokta in x_kapsam:
                        if (xnokta, ynokta) in self.durum:
                            yeniSet += 1
                # Merkezh�cre de�eri say�lmaz, d��elim...
                yeniSet -= canl�Set
                ##print (drm) ==>�stenirse bu bilgiler listelenebilir...
                ##print (i, j, yeniSet, canl�Set)
                if yeniSet == 3:
                    # Yeni do�um...
                    drm.add ((i,j))
                elif yeniSet == 2 and canl�Set:
                    # Hala ya��yor...
                    drm.add ((i,j))
                elif canl�Set:
                    # �ld�...
                    pass
        self.durum = drm

    def g�ster(self):
        """T�m pano g�ncellenerek g�sterilir"""
        turtle.clear()
        for i in range (self.xebat):
            for j in range (self.yebat):
                self.�iz (i, j)
        turtle.update()

    def ge�erlile (self, x, y):
        """Bir h�cre durumunu canl�/kare ve �l�/bo� aras�nda de�i�tirir..."""
        if not self.ge�erli_mi (x, y):
            raise ValueError ("Koordinatlar: {}, {} verili ekran kapsamlar� olan: {} ve {} de�erleri d���nda!"
                    .format (x, y, self.xebat, self.yebat))
        tu� = (x, y) # T�klanan h�cre bo�sa doldur, doluysa sil...
        if tu� in self.durum: self.durum.remove (tu�)
        else: self.durum.add (tu�)

    def ge�erli_mi (self, x, y):
        "E�er x,y koordinatlar� verili xebat/yebat pano kapsam�ndaysa 'True' d�nd�r�r."
        return (0 <= x < self.xebat) and (0 <= y < self.yebat)

    def kur (self, x, y):
        """Ge�erli konuma yeni bir durum set canl�s� kurar."""
        if not self.ge�erli_mi (x, y):
            raise ValueError ("Koordinatlar: {}, {} verili ekran kapsamlar� olan: {} ve {} de�erleri d���nda!"
                    .format (x, y, self.xebat, self.yebat))
        tu� = (x, y)
        self.durum.add(tu�)

    def �iz (self, x, y):
        "G�ster metodundaki ilgili (x,y) h�cresini istenen renkte �izer ve i�ini doldurur."
        turtle.penup()
        tu� = (x, y)
        if tu� in self.durum:
            turtle.setpos (x * H�CRE_EBATI, y * H�CRE_EBATI)
            turtle.color ('GREEN')
            turtle.pendown()
            turtle.setheading (0)
            turtle.pensize (3)
            turtle.begin_fill()
            for i in range (4):
                turtle.forward (H�CRE_EBATI - 1)
                turtle.left (90)
            turtle.color ('MAGENTA')
            turtle.end_fill()

def yard�m_penceresini_g�ster():
    from turtle import TK # S�n�f ithali...
    #k�k = TK.Tk() # Metod �a��rmal� nesne...
    #�er�eve = TK.Frame()
    tuval = TK.Canvas (TK.Tk(), width=400, height=200, bg="WHITE") # Yard�m ekran b�y�kl���...
    tuval.pack()

    yard�m_ekran� = turtle.TurtleScreen (tuval)
    en, boy = yard�m_ekran�.screensize() 

    yard�m_penceresi = turtle.RawTurtle (yard�m_ekran�)
    yard�m_penceresi.penup()
    yard�m_penceresi.hideturtle()
    yard�m_penceresi.speed ('fastest')

    sat�r_boyu = 20
    y = boy / 2 - 30
    for sat�r in ("Fareyle t�klanan h�cre canlan�r veya �l�r.",
            "Pano odakl�yken klavye komutlar�:", " ",
            " S)il panoyu tamamen",
            " G)eli�ig�zel pano dolacak",
            " T)ek tek ad�mlarla ilerlenir",
            " D)evaml� ilerlenir -- T ile tek teke d�nebilirsin", " ",
            " K)apat pencereleri ve ��k"):
        yard�m_penceresi.setpos (- en / 2, y)
        yard�m_penceresi.write (sat�r, font = ('sans-serif', 14, 'normal'))
        y -= sat�r_boyu


def anaProgram():
    yard�m_penceresini_g�ster()

    ekran = turtle.Screen()
    turtle.mode ('standard')
    xebat, yebat = ekran.screensize()
    turtle.setworldcoordinates (0, 0, xebat, yebat)

    turtle.hideturtle() # Kalem okunu gizler...
    turtle.speed ('fastest')
    turtle.tracer (0, 0)
    turtle.penup()

    # B�l�mlerde �ift "//" kullan�m, sonucu tamsay� yapar; yoksa float hatas� olu�ur...
    pano = HayatPanosu (xebat // H�CRE_EBATI, yebat // H�CRE_EBATI) # Kurucuyu �a��r�r...

    # Fare'yle h�cre t�klamas�n� ge�erlileyelim...
    def ge�erlile (x, y): # HayatPanosu s�n�f� ge�erlile(..) metodunu esge�er...
        h�cre_x = x // H�CRE_EBATI
        h�cre_y = y // H�CRE_EBATI
        if pano.ge�erli_mi (h�cre_x, h�cre_y):
            pano.ge�erlile (h�cre_x, h�cre_y) # HayatPanosu ge�erlile(..) fonksiyonunu �a��r�r...
            pano.g�ster()

    turtle.onscreenclick (turtle.listen) # Pano t�klamas� dinleyiciye duyarl�...
    turtle.onscreenclick (ge�erlile) # T�klama �nce dahili ge�erlile(..) fonksiyonunu �a��r�r...

    pano.panoyuGeli�ig�zelDoldur()
    pano.g�ster()

    # Men� harf tu�lar�n� kural�m...
    def panoyuTamamenSil():
        pano.panoyuTamamenSil() # Asl�nda �ncelikle durum set i�eriklerini silip sonra bo� ekran� g�steriyor...
        pano.g�ster()
    turtle.onkey (panoyuTamamenSil, 's')

    def panoyuGeli�ig�zelDoldur():
        pano.panoyuGeli�ig�zelDoldur()
        pano.g�ster()
    turtle.onkey (panoyuGeli�ig�zelDoldur, 'g')

    turtle.onkey (sys.exit, 'k') # "�" ile basmadan ��k�yor...

    # Men� harfleriyle tek ad�m veya daimi ad�mla ilerlemeyi kural�m...
    devaml� = False
    def tek_ad�m():
        nonlocal devaml�
        devaml� = False
        ad�m�_i�let()

    def daimi_ad�m():
        nonlocal devaml�
        devaml� = True
        ad�m�_i�let()

    def ad�m�_i�let():
        pano.ad�mla()
        pano.g�ster()
        # "devaml�"da 25 milisaniyede birsonraki ad�ma ge�er...
        if devaml�: turtle.ontimer (ad�m�_i�let, 25)

    turtle.onkey (tek_ad�m, 't')
    turtle.onkey (daimi_ad�m, 'd')

    # Tk s�n�f� mainloop() metodunu �a��ral�m...
    turtle.listen()
    turtle.mainloop()

if __name__ == '__main__':
    anaProgram()