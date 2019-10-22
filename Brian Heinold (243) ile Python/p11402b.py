# coding:iso-8859-9 Türkçe

from string import punctuation

class Analizci:
    def __init__ (self, d):
        for k in punctuation: d = d.replace (k,'')

        self.kelimeler = d.split()

    def kelime_sayısı (self): return len (self.kelimeler)
    def başlar (self, h): return len ([k for k in self.kelimeler if k[:len (h)] == h])
    def dört_harfli (self, n): return len ([k for k in self.kelimeler if len (k) == n])

dizge = 'Bu, bir Piton sınıfını test etme dizgesidir.'
print ("Orijinal dizgemiz:", dizge)

analiz = Analizci (dizge.lower())
print ("\nKelimeler:", analiz.kelimeler)
print ('Dizgedeki kelime sayısı:', analiz.kelime_sayısı())
print ('b ile başlayan kelime sayısı:', analiz.başlar ('b'))
print ('4-harfli kelime sayısı:', analiz.dört_harfli (4))
