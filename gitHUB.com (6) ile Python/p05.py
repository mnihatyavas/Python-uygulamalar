# coding:iso-8859-9 Türkçe

# p05.py -- Bir turtle-temelli Conway's Game of Life (Conway'in Hayat Oyunu) oyunu.
#
# İlk anda tesadüfi dolu bir ekran ve şu seçenekler sunulacaktır:
#  S : Panoyu tamamen sil
#  G : Panoyu gelişigüzel doldur
#  T : Tet tek adımlarla ilerle
#  D : Hareketli kare kalmayıncaya kadar devamlı ilerle
#  K : Kapat
#  Fare : Tıklanan hücreyi siler/doldurur
#

import sys
import turtle
import random

HÜCRE_EBATI = 20 # Piksel ölçümüyle...

class HayatPanosu:
    """Gelişigüzel bir hayat panosu (oyunu) kurar...

    Sınıf tip değişkenleri:
    xebat, yebat : Panonun yatay ve dikey ebatları...
    durum : Panodaki canlı hücrelerin (x,y) koordinatlarını içeren bir set tip değişkeni...

    Metodlar:
    göster (self) -- Pano durum set güncel içeriklerini ekranda gösterir...
    panoyuTamamenSil (self) -- Tüm panoyu temizler...
    panoyuGelişigüzelDoldur (self) -- Panoyu (önce siler) yenibaştan gelişigüzel doldurur...
    kur (self,x,y) -- Verili hücreyi set'e ekler; ancak ekran görüntüsünü güncellemez...
    geçerlile (self,x,y) -- Tuklanan konumu doluysa bolatır, boşsa doldurur ve ekran görüntüsünü günceller...
    """
    def __init__  (self, xebat, yebat): # Kurucu...
        """Yeni bir HayatPanosu sınıf nesne tipi yaratılır."""
        self.durum = set()
        self.xebat, self.yebat = xebat, yebat

    def panoyuTamamenSil (self):
        """Tüm panoyu temizler."""
        self.durum.clear()

    def panoyuGelişigüzelDoldur (self):
        "Panoyu gelişigüzel bir kalıpla doldurur..."
        self.panoyuTamamenSil()
        for i in range (0, self.xebat):
            for j in range (0, self.yebat):
                if random.random() > 0.5:
                    self.kur (i, j)

    def adımla (self):
        "Tek adım ilerler ve göster metodunu günceller."
        drm = set()
        for i in range (self.xebat):
            x_kapsam = range (max (0, i-1), min (self.xebat, i+2))
            for j in range (self.yebat):
                yeniSet = 0
                canlıSet = ((i,j) in self.durum)
                for ynokta in range (max (0, j-1), min (self.yebat, j+2)):
                    for xnokta in x_kapsam:
                        if (xnokta, ynokta) in self.durum:
                            yeniSet += 1
                # Merkezhücre değeri sayılmaz, düşelim...
                yeniSet -= canlıSet
                ##print (drm) ==>İstenirse bu bilgiler listelenebilir...
                ##print (i, j, yeniSet, canlıSet)
                if yeniSet == 3:
                    # Yeni doğum...
                    drm.add ((i,j))
                elif yeniSet == 2 and canlıSet:
                    # Hala yaşıyor...
                    drm.add ((i,j))
                elif canlıSet:
                    # Öldü...
                    pass
        self.durum = drm

    def göster(self):
        """Tüm pano güncellenerek gösterilir"""
        turtle.clear()
        for i in range (self.xebat):
            for j in range (self.yebat):
                self.çiz (i, j)
        turtle.update()

    def geçerlile (self, x, y):
        """Bir hücre durumunu canlı/kare ve ölü/boş arasında değiştirir..."""
        if not self.geçerli_mi (x, y):
            raise ValueError ("Koordinatlar: {}, {} verili ekran kapsamları olan: {} ve {} değerleri dışında!"
                    .format (x, y, self.xebat, self.yebat))
        tuş = (x, y) # Tıklanan hücre boşsa doldur, doluysa sil...
        if tuş in self.durum: self.durum.remove (tuş)
        else: self.durum.add (tuş)

    def geçerli_mi (self, x, y):
        "Eğer x,y koordinatları verili xebat/yebat pano kapsamındaysa 'True' döndürür."
        return (0 <= x < self.xebat) and (0 <= y < self.yebat)

    def kur (self, x, y):
        """Geçerli konuma yeni bir durum set canlısı kurar."""
        if not self.geçerli_mi (x, y):
            raise ValueError ("Koordinatlar: {}, {} verili ekran kapsamları olan: {} ve {} değerleri dışında!"
                    .format (x, y, self.xebat, self.yebat))
        tuş = (x, y)
        self.durum.add(tuş)

    def çiz (self, x, y):
        "Göster metodundaki ilgili (x,y) hücresini istenen renkte çizer ve içini doldurur."
        turtle.penup()
        tuş = (x, y)
        if tuş in self.durum:
            turtle.setpos (x * HÜCRE_EBATI, y * HÜCRE_EBATI)
            turtle.color ('GREEN')
            turtle.pendown()
            turtle.setheading (0)
            turtle.pensize (3)
            turtle.begin_fill()
            for i in range (4):
                turtle.forward (HÜCRE_EBATI - 1)
                turtle.left (90)
            turtle.color ('MAGENTA')
            turtle.end_fill()

def yardım_penceresini_göster():
    from turtle import TK # Sınıf ithali...
    #kök = TK.Tk() # Metod çağırmalı nesne...
    #çerçeve = TK.Frame()
    tuval = TK.Canvas (TK.Tk(), width=400, height=200, bg="WHITE") # Yardım ekran büyüklüğü...
    tuval.pack()

    yardım_ekranı = turtle.TurtleScreen (tuval)
    en, boy = yardım_ekranı.screensize() 

    yardım_penceresi = turtle.RawTurtle (yardım_ekranı)
    yardım_penceresi.penup()
    yardım_penceresi.hideturtle()
    yardım_penceresi.speed ('fastest')

    satır_boyu = 20
    y = boy / 2 - 30
    for satır in ("Fareyle tıklanan hücre canlanır veya ölür.",
            "Pano odaklıyken klavye komutları:", " ",
            " S)il panoyu tamamen",
            " G)elişigüzel pano dolacak",
            " T)ek tek adımlarla ilerlenir",
            " D)evamlı ilerlenir -- T ile tek teke dönebilirsin", " ",
            " K)apat pencereleri ve çık"):
        yardım_penceresi.setpos (- en / 2, y)
        yardım_penceresi.write (satır, font = ('sans-serif', 14, 'normal'))
        y -= satır_boyu


def anaProgram():
    yardım_penceresini_göster()

    ekran = turtle.Screen()
    turtle.mode ('standard')
    xebat, yebat = ekran.screensize()
    turtle.setworldcoordinates (0, 0, xebat, yebat)

    turtle.hideturtle() # Kalem okunu gizler...
    turtle.speed ('fastest')
    turtle.tracer (0, 0)
    turtle.penup()

    # Bölümlerde çift "//" kullanım, sonucu tamsayı yapar; yoksa float hatası oluşur...
    pano = HayatPanosu (xebat // HÜCRE_EBATI, yebat // HÜCRE_EBATI) # Kurucuyu çağırır...

    # Fare'yle hücre tıklamasını geçerlileyelim...
    def geçerlile (x, y): # HayatPanosu sınıfı geçerlile(..) metodunu esgeçer...
        hücre_x = x // HÜCRE_EBATI
        hücre_y = y // HÜCRE_EBATI
        if pano.geçerli_mi (hücre_x, hücre_y):
            pano.geçerlile (hücre_x, hücre_y) # HayatPanosu geçerlile(..) fonksiyonunu çağırır...
            pano.göster()

    turtle.onscreenclick (turtle.listen) # Pano tıklaması dinleyiciye duyarlı...
    turtle.onscreenclick (geçerlile) # Tıklama önce dahili geçerlile(..) fonksiyonunu çağırır...

    pano.panoyuGelişigüzelDoldur()
    pano.göster()

    # Menü harf tuşlarını kuralım...
    def panoyuTamamenSil():
        pano.panoyuTamamenSil() # Aslında öncelikle durum set içeriklerini silip sonra boş ekranı gösteriyor...
        pano.göster()
    turtle.onkey (panoyuTamamenSil, 's')

    def panoyuGelişigüzelDoldur():
        pano.panoyuGelişigüzelDoldur()
        pano.göster()
    turtle.onkey (panoyuGelişigüzelDoldur, 'g')

    turtle.onkey (sys.exit, 'k') # "ç" ile basmadan çıkıyor...

    # Menü harfleriyle tek adım veya daimi adımla ilerlemeyi kuralım...
    devamlı = False
    def tek_adım():
        nonlocal devamlı
        devamlı = False
        adımı_işlet()

    def daimi_adım():
        nonlocal devamlı
        devamlı = True
        adımı_işlet()

    def adımı_işlet():
        pano.adımla()
        pano.göster()
        # "devamlı"da 25 milisaniyede birsonraki adıma geçer...
        if devamlı: turtle.ontimer (adımı_işlet, 25)

    turtle.onkey (tek_adım, 't')
    turtle.onkey (daimi_adım, 'd')

    # Tk sınıfı mainloop() metodunu çağıralım...
    turtle.listen()
    turtle.mainloop()

if __name__ == '__main__':
    anaProgram()