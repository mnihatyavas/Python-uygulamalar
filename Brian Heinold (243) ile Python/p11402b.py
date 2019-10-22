# coding:iso-8859-9 T�rk�e

from string import punctuation

class Analizci:
    def __init__ (self, d):
        for k in punctuation: d = d.replace (k,'')

        self.kelimeler = d.split()

    def kelime_say�s� (self): return len (self.kelimeler)
    def ba�lar (self, h): return len ([k for k in self.kelimeler if k[:len (h)] == h])
    def d�rt_harfli (self, n): return len ([k for k in self.kelimeler if len (k) == n])

dizge = 'Bu, bir Piton s�n�f�n� test etme dizgesidir.'
print ("Orijinal dizgemiz:", dizge)

analiz = Analizci (dizge.lower())
print ("\nKelimeler:", analiz.kelimeler)
print ('Dizgedeki kelime say�s�:', analiz.kelime_say�s�())
print ('b ile ba�layan kelime say�s�:', analiz.ba�lar ('b'))
print ('4-harfli kelime say�s�:', analiz.d�rt_harfli (4))
