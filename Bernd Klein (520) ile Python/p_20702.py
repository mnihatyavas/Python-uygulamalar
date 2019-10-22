# coding:iso-8859-9 T�rk�e
# p_20702.py: Grafik s�n�f�yla, yumru, ba�lant�, izole, yeni yumru ve ba�lant� ekleme �rne�i.

class Grafik (object):
    def __init__ (self, grafikS�zl���=None):
        if grafikS�zl��� == None: grafikS�zl��� = {}
        self.__grafikS�zl��� = grafikS�zl���

    def yumrular (self): return list (self.__grafikS�zl���.keys() )

    def yumruEkle (self, yumru):
        if yumru not in self.__grafikS�zl���: self.__grafikS�zl���[yumru] = []

    def ba�lant�lar (self): return self.ba�lant�lar�Kur()

    def ba�lant�lar�Kur (self):
        ba�lant�lar = []
        for yumru in self.__grafikS�zl���:
            for kom�u in self.__grafikS�zl���[yumru]:
                if {kom�u, yumru} not in ba�lant�lar: ba�lant�lar.append ({yumru, kom�u})
        return ba�lant�lar

    def ba�lant�Ekle (self, ba�lant�):
        ba�lant� = set (ba�lant�)
        (yumru1, yumru2) = tuple (ba�lant�)
        if yumru1 in self.__grafikS�zl���: self.__grafikS�zl���[yumru1].append (yumru2)
        else: self.__grafikS�zl���[yumru1] = [yumru2]

    def patikaBul (self, ilkYumru, sonYumru, patika=None):
        if patika == None: patika = []
        grafik = self.__grafikS�zl���
        patika = patika + [ilkYumru]
        if ilkYumru == sonYumru: return patika
        if ilkYumru not in grafik: return None
        for yumru in grafik[ilkYumru]:
            if yumru not in patika:
                eklenenPatika = self.patikaBul (yumru, sonYumru, patika)
                if eklenenPatika: return eklenenPatika
        return None

    def t�mPatikalar�Bul (self, ilkYumru, sonYumru, patika=[]):
        grafik = self.__grafikS�zl���
        patika = patika + [ilkYumru]
        if ilkYumru == sonYumru: return [patika]
        if ilkYumru not in grafik: return []
        patikalar = []
        for yumru in grafik[ilkYumru]:
            if yumru not in patika:
                eklenenPatika = self.t�mPatikalar�Bul (yumru, sonYumru, patika)
                for p in eklenenPatika: patikalar.append (p)
        return patikalar

    def __str__ (self):
        sonu� = "Yumrular: "
        for y in self.__grafikS�zl���: sonu� += str (y) + " "
        sonu� += "\nBa�lant�lar: "
        for b in self.ba�lant�lar�Kur(): sonu� += str (b) + " "
        return sonu�

    # Sonraki �rneklerin eklenti fonksiyonlar�...
    def yumruDerecesi (self, yumru):
        kom�uYumrular =  self.__grafikS�zl���[yumru]
        derece = len (kom�uYumrular) + kom�uYumrular.count (yumru)
        return derece

    def izoleYumrular (self):
        grafik = self.__grafikS�zl���
        izoleListesi = []
        for yumru in grafik:
            if not grafik[yumru]: izoleListesi += [yumru]
        return izoleListesi

    def asgariDerece (self):
        asgari = 100000000
        for yumru in self.__grafikS�zl���:
            yumruDerecesi = self.yumruDerecesi (yumru)
            if yumruDerecesi < asgari: asgari = yumruDerecesi
        return asgari

    def azamiDerece (self):
        azami = 0
        for yumru in self.__grafikS�zl���:
            yumruDerecesi = self.yumruDerecesi (yumru)
            if yumruDerecesi > azami: azami = yumruDerecesi
        return azami

    def dereceSilsilesi (self):
        silsileListesi = []
        for yumru in self.__grafikS�zl���: silsileListesi.append (self.yumruDerecesi (yumru))
        silsileListesi.sort (reverse = True)
        return tuple (silsileListesi)

    @staticmethod
    def erdoes_gallai (silsile):
        if sum (silsile) % 2: return False
        for k in range (1, len (silsile) + 1):
            sol = sum (silsile[:k])
            sa� =  k * (k-1) + sum ([min (x, k) for x in silsile[k:]])
            if sol > sa�: return False
        return True

    def yo�unluk (self):
        g = self.__grafikS�zl���
        Y = len (g.keys())
        B = len (self.ba�lant�lar())
        return 2.0 * B / (Y *(Y - 1)) # Ba�lant� yo�unlu�u [0->1] aras�d�r...

    def ba�lant�l�M� (self, ba�lant�l�Yumrular = None, ilkYumru=None):
        if ba�lant�l�Yumrular is None: ba�lant�l�Yumrular = set()
        gS�z = self.__grafikS�zl���
        yumrular = list (gS�z.keys())
        if not ilkYumru: # �lk yumru belirtilmemi�se, 0.yumruyu se�...
            ilkYumru = yumrular[0]
        ba�lant�l�Yumrular.add (ilkYumru)
        if len (ba�lant�l�Yumrular) != len (yumrular):
            for yumru in gS�z[ilkYumru]:
                if yumru not in ba�lant�l�Yumrular:
                    if self.ba�lant�l�M� (ba�lant�l�Yumrular, yumru): return True
        else: return True
        return False

    def grafi�in�ap� (self):
        y = self.yumrular()
        �iftlerListesi = [(y[i], y[j]) for i in range (len (y) - 1) for j in range (i+1, len (y))]
        enk�saYol = []
        for (y1, y2) in �iftlerListesi:
            patikalar = self.t�mPatikalar�Bul (y1, y2)
            enk�sas� = sorted (patikalar, key=len)[0]
            enk�saYol.append (enk�sas�)
        enk�saYol.sort (key=len)
        grafi�in�ap� = len (enk�saYol[-1]) - 1 # Artan s�ralamada son yol enuzunudur...
        return grafi�in�ap�


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

    print ("Grafi�in mevcut yumrular�:")
    print (grafik.yumrular())

    print ("Grafi�in mevcut ba�lant�lar�:")
    print (grafik.ba�lant�lar())

    print ("Yeni bir yumru 'z' ekle:")
    grafik.yumruEkle ("z")

    print ("Grafi�in ilk g�ncel yumrular�:")
    print (grafik.yumrular())
 
    print ("Yeni bir ba�lant� {'a', 'z'} ekle:")
    grafik.ba�lant�Ekle ({"a", "z"})

    print ("Grafi�in ikinci g�ncel yumrular�:")
    print (grafik.yumrular() )

    print ("Grafi�in ikinci g�ncel ba�lant�lar�:")
    print (grafik.ba�lant�lar())

    print ('Yeni ba�lant�l� iki yumru {"x","y"} ekle:')
    grafik.ba�lant�Ekle ({"x", "y"})
    grafik.yumruEkle ("x")

    print ("Grafi�in son yumrular�:")
    print (grafik.yumrular())

    print ("Grafi�in son ba�lant�lar�:")
    print (grafik.ba�lant�lar())

"""��kt�:
>python p_20702.py
Grafi�in mevcut yumrular�:
['a', 'b', 'c', 'd', 'e', 'f', 'g']
Grafi�in mevcut ba�lant�lar�:
[{'a', 'd'}, {'b', 'c'}, {'c'}, {'c', 'd'}, {'c', 'e'}]
Yeni bir yumru 'z' ekle:
Grafi�in ilk g�ncel yumrular�:
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'z']
Yeni bir ba�lant� {'a', 'z'} ekle:
Grafi�in ikinci g�ncel yumrular�:
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'z']
Grafi�in ikinci g�ncel ba�lant�lar�:
[{'a', 'd'}, {'b', 'c'}, {'c'}, {'c', 'd'}, {'c', 'e'}, {'z', 'a'}]
Yeni ba�lant�l� iki yumru {"x","y"} ekle:
Grafi�in son yumrular�:
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'z', 'x']
Grafi�in son ba�lant�lar�:
[{'a', 'd'}, {'b', 'c'}, {'c'}, {'c', 'd'}, {'c', 'e'}, {'z', 'a'}, {'x', 'y'}]
"""