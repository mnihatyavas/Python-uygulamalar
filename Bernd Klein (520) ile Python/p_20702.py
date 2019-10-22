# coding:iso-8859-9 Türkçe
# p_20702.py: Grafik sınıfıyla, yumru, bağlantı, izole, yeni yumru ve bağlantı ekleme örneği.

class Grafik (object):
    def __init__ (self, grafikSözlüğü=None):
        if grafikSözlüğü == None: grafikSözlüğü = {}
        self.__grafikSözlüğü = grafikSözlüğü

    def yumrular (self): return list (self.__grafikSözlüğü.keys() )

    def yumruEkle (self, yumru):
        if yumru not in self.__grafikSözlüğü: self.__grafikSözlüğü[yumru] = []

    def bağlantılar (self): return self.bağlantılarıKur()

    def bağlantılarıKur (self):
        bağlantılar = []
        for yumru in self.__grafikSözlüğü:
            for komşu in self.__grafikSözlüğü[yumru]:
                if {komşu, yumru} not in bağlantılar: bağlantılar.append ({yumru, komşu})
        return bağlantılar

    def bağlantıEkle (self, bağlantı):
        bağlantı = set (bağlantı)
        (yumru1, yumru2) = tuple (bağlantı)
        if yumru1 in self.__grafikSözlüğü: self.__grafikSözlüğü[yumru1].append (yumru2)
        else: self.__grafikSözlüğü[yumru1] = [yumru2]

    def patikaBul (self, ilkYumru, sonYumru, patika=None):
        if patika == None: patika = []
        grafik = self.__grafikSözlüğü
        patika = patika + [ilkYumru]
        if ilkYumru == sonYumru: return patika
        if ilkYumru not in grafik: return None
        for yumru in grafik[ilkYumru]:
            if yumru not in patika:
                eklenenPatika = self.patikaBul (yumru, sonYumru, patika)
                if eklenenPatika: return eklenenPatika
        return None

    def tümPatikalarıBul (self, ilkYumru, sonYumru, patika=[]):
        grafik = self.__grafikSözlüğü
        patika = patika + [ilkYumru]
        if ilkYumru == sonYumru: return [patika]
        if ilkYumru not in grafik: return []
        patikalar = []
        for yumru in grafik[ilkYumru]:
            if yumru not in patika:
                eklenenPatika = self.tümPatikalarıBul (yumru, sonYumru, patika)
                for p in eklenenPatika: patikalar.append (p)
        return patikalar

    def __str__ (self):
        sonuç = "Yumrular: "
        for y in self.__grafikSözlüğü: sonuç += str (y) + " "
        sonuç += "\nBağlantılar: "
        for b in self.bağlantılarıKur(): sonuç += str (b) + " "
        return sonuç

    # Sonraki örneklerin eklenti fonksiyonları...
    def yumruDerecesi (self, yumru):
        komşuYumrular =  self.__grafikSözlüğü[yumru]
        derece = len (komşuYumrular) + komşuYumrular.count (yumru)
        return derece

    def izoleYumrular (self):
        grafik = self.__grafikSözlüğü
        izoleListesi = []
        for yumru in grafik:
            if not grafik[yumru]: izoleListesi += [yumru]
        return izoleListesi

    def asgariDerece (self):
        asgari = 100000000
        for yumru in self.__grafikSözlüğü:
            yumruDerecesi = self.yumruDerecesi (yumru)
            if yumruDerecesi < asgari: asgari = yumruDerecesi
        return asgari

    def azamiDerece (self):
        azami = 0
        for yumru in self.__grafikSözlüğü:
            yumruDerecesi = self.yumruDerecesi (yumru)
            if yumruDerecesi > azami: azami = yumruDerecesi
        return azami

    def dereceSilsilesi (self):
        silsileListesi = []
        for yumru in self.__grafikSözlüğü: silsileListesi.append (self.yumruDerecesi (yumru))
        silsileListesi.sort (reverse = True)
        return tuple (silsileListesi)

    @staticmethod
    def erdoes_gallai (silsile):
        if sum (silsile) % 2: return False
        for k in range (1, len (silsile) + 1):
            sol = sum (silsile[:k])
            sağ =  k * (k-1) + sum ([min (x, k) for x in silsile[k:]])
            if sol > sağ: return False
        return True

    def yoğunluk (self):
        g = self.__grafikSözlüğü
        Y = len (g.keys())
        B = len (self.bağlantılar())
        return 2.0 * B / (Y *(Y - 1)) # Bağlantı yoğunluğu [0->1] arasıdır...

    def bağlantılıMı (self, bağlantılıYumrular = None, ilkYumru=None):
        if bağlantılıYumrular is None: bağlantılıYumrular = set()
        gSöz = self.__grafikSözlüğü
        yumrular = list (gSöz.keys())
        if not ilkYumru: # İlk yumru belirtilmemişse, 0.yumruyu seç...
            ilkYumru = yumrular[0]
        bağlantılıYumrular.add (ilkYumru)
        if len (bağlantılıYumrular) != len (yumrular):
            for yumru in gSöz[ilkYumru]:
                if yumru not in bağlantılıYumrular:
                    if self.bağlantılıMı (bağlantılıYumrular, yumru): return True
        else: return True
        return False

    def grafiğinÇapı (self):
        y = self.yumrular()
        çiftlerListesi = [(y[i], y[j]) for i in range (len (y) - 1) for j in range (i+1, len (y))]
        enkısaYol = []
        for (y1, y2) in çiftlerListesi:
            patikalar = self.tümPatikalarıBul (y1, y2)
            enkısası = sorted (patikalar, key=len)[0]
            enkısaYol.append (enkısası)
        enkısaYol.sort (key=len)
        grafiğinÇapı = len (enkısaYol[-1]) - 1 # Artan sıralamada son yol enuzunudur...
        return grafiğinÇapı


if __name__ == "__main__":
    g = {
        "a" : ["d"],
        "b" : ["c"],
        "c" : ["b", "c", "d", "e"],
        "d" : ["a", "c"],
        "e" : ["c"],
        "f" : [], 
        "g" : []
        }

    grafik = Grafik (g)

    print ("Grafiğin mevcut yumruları:")
    print (grafik.yumrular())

    print ("Grafiğin mevcut bağlantıları:")
    print (grafik.bağlantılar())

    print ("Yeni bir yumru 'z' ekle:")
    grafik.yumruEkle ("z")

    print ("Grafiğin ilk güncel yumruları:")
    print (grafik.yumrular())
 
    print ("Yeni bir bağlantı {'a', 'z'} ekle:")
    grafik.bağlantıEkle ({"a", "z"})

    print ("Grafiğin ikinci güncel yumruları:")
    print (grafik.yumrular() )

    print ("Grafiğin ikinci güncel bağlantıları:")
    print (grafik.bağlantılar())

    print ('Yeni bağlantılı iki yumru {"x","y"} ekle:')
    grafik.bağlantıEkle ({"x", "y"})
    grafik.yumruEkle ("x")

    print ("Grafiğin son yumruları:")
    print (grafik.yumrular())

    print ("Grafiğin son bağlantıları:")
    print (grafik.bağlantılar())

"""Çıktı:
>python p_20702.py
Grafiğin mevcut yumruları:
['a', 'b', 'c', 'd', 'e', 'f', 'g']
Grafiğin mevcut bağlantıları:
[{'a', 'd'}, {'b', 'c'}, {'c'}, {'c', 'd'}, {'c', 'e'}]
Yeni bir yumru 'z' ekle:
Grafiğin ilk güncel yumruları:
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'z']
Yeni bir bağlantı {'a', 'z'} ekle:
Grafiğin ikinci güncel yumruları:
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'z']
Grafiğin ikinci güncel bağlantıları:
[{'a', 'd'}, {'b', 'c'}, {'c'}, {'c', 'd'}, {'c', 'e'}, {'z', 'a'}]
Yeni bağlantılı iki yumru {"x","y"} ekle:
Grafiğin son yumruları:
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'z', 'x']
Grafiğin son bağlantıları:
[{'a', 'd'}, {'b', 'c'}, {'c'}, {'c', 'd'}, {'c', 'e'}, {'z', 'a'}, {'x', 'y'}]
"""