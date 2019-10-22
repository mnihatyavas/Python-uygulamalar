# coding:iso-8859-9 Türkçe

class Kelimeler:
    def __init__ (self, L):
        self.L = L
        self.uz = len (self.L)

    def kelimelerVeUzunlukları (self):
        print ("Kelime      Uzunluğu\n", "="*20, sep="");
        for i in range (self.uz):
            for j in range (len (self.L[i])):
                print ("{}{}{:2d}" .format (self.L[i][j], "."*(18-len (self.L[i][j])), len (self.L[i][j])) )

    def ilki_sş_kelimeler (self):
        print ("İlk harfi \"s veya ş\" ile başlayan kelimeler:\n", "="*44, sep="");
        for i in range (self.uz):
            for j in range (len (self.L[i])):
                if self.L[i][j][0] == "s" or self.L[i][j][0] == "ş": print (self.L[i][j], end=" ")
        print()

    def sonu_soruİşaretli_kelimeler (self):
        print ("Sonu \"?\" ile biten kelimeler:\n", "="*29, sep="");
        for i in range (self.uz):
            for j in range (len (self.L[i])):
                if self.L[i][j][len (self.L[i][j])-1] == "?": print (self.L[i][j], end=" ")
        print()

    def palindrom_kelimeler (self):
        print ("Palindrom kelimeler:\n", "="*20, sep="");
        for i in range (self.uz):
            for j in range (len (self.L[i])):
                if self.L[i][j] == self.L[i][j][::-1]: print (self.L[i][j], end=" ")
        print()

    def sadeceKarakterli_kelimeler (self, krk):
        print ("Sadece [", krk, "] karakterlerini içeren kelimeler:\n", "="*50, sep="");
        for i in range (self.uz):
            for j in range (len (self.L[i])):
                for k in krk:
                    if k not in self.L[i][j]: break
                else: print (self.L[i][j], end=" ")
        print()

    def sadeceKaraktersiz_kelimeler (self, krk):
        print ("[", krk, "] karakterlerini İÇERMEYEN kelimeler:\n", "="*45, sep="");
        for i in range (self.uz):
            for j in range (len (self.L[i])):
                for k in krk:
                    if k in self.L[i][j]: break
                else: print (self.L[i][j], end=" ")
        print()

L = [satır.lower().strip().split(" ") for satır in open ("sorular.txt", "r") ]
from pprint import pprint
pprint (L)

kelimeOyunu = Kelimeler (L)
print()
kelimeOyunu.kelimelerVeUzunlukları()

print()
kelimeOyunu.ilki_sş_kelimeler()

print()
kelimeOyunu.sonu_soruİşaretli_kelimeler()

print()
kelimeOyunu.palindrom_kelimeler()

karakterler = input ("\nHangi karakterlerin na/mevcudiyeti kontrol edilecek: ").lower()
if len (karakterler) == 0: karakterler = "ai"
print()
kelimeOyunu.sadeceKarakterli_kelimeler (karakterler)

print()
kelimeOyunu.sadeceKaraktersiz_kelimeler (karakterler)
