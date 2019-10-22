# coding:iso-8859-9 Türkçe
# p_21601.py: Tutulan renk dizilimini isabet ve yakınsı adediyle tahminleme oyunu örneği.

# Mastermind: ustaakıl, bulls & cows: boğalar ve inekler, blacks & whites: aklar ve karalar/isabetler ve yakınsılar...

import random
from p_21601x import tümRenkler

def yeniDeğerleme (tutulanRenkler):
    global sayaç
    doğruKonumlu, yakınKonumlu = değerlemeyiAl()
    if doğruKonumlu == renkAdedi:
        tahminler.append ((tutulanRenkler, (doğruKonumlu, yakınKonumlu)))
        öncekiTahminleriGöster()
        print ("\nAferin bana, tuttuğun renk dizilimini [", sayaç, "] tahminde buldum...", sep="")
        return (tutulanRenkler, (doğruKonumlu, yakınKonumlu))

    if not girdilerinizTutarlıMı ((doğruKonumlu, yakınKonumlu)):
        print ("Veri Giriş Hatası: Üzgünüm, girdiğiniz bilgiler tutarsız...")
        return (tutulanRenkler, (-1, yakınKonumlu))
    tahminler.append ((tutulanRenkler, (doğruKonumlu, yakınKonumlu)))
    öncekiTahminleriGöster()

    tutulanRenkler = yeniTahminYarat() 
    if not tutulanRenkler: return (tutulanRenkler, (-1, yakınKonumlu))
    return (tutulanRenkler, (doğruKonumlu, yakınKonumlu))

def değerlemeyiAl():
   eldekiTahminiGöster (ilkTahmin [0])
   doğruKonumlu = abs (int (input ("Siyah adedi [doğru konum]: ")))
   yakınKonumlu = abs (int (input ("Beyaz adedi [yakın konum]: ")))
   return (doğruKonumlu, yakınKonumlu)

def eldekiTahminiGöster (ilkTahmin):
   print ("\nYeni Tahminim: ", end=" ")
   for renk in ilkTahmin: print (renk, end=" ")
   print()

def öncekiTahminleriGöster():
    print ("\nÖnceki tahminler:")
    for tahmin in tahminler:
        tahminRenkleri = tahmin [0]
        print (" Renk dizilimi: [", end="")
        for r in tahminRenkleri: print (r, end=" ")
        print ("], (İsabet Yakın): (", end="")
        for i in tahmin[1]: print (" %i " % i, end=" ")
        print (")")

def girdilerinizTutarlıMı (a):
    (doğruKonumlu, yakınKonumlu) = a
    if ((doğruKonumlu + yakınKonumlu) > renkAdedi) \
            or ((doğruKonumlu + yakınKonumlu) < (len (renkler) - renkAdedi)):
        return False
    if doğruKonumlu == 4 and yakınKonumlu == 1: return False
    return True

def yeniTahminYarat():
   sonrakiTahmin = next (tarayıcı) 
   while öncekilerleTutarsızMı (sonrakiTahmin, tahminler):
      try: sonrakiTahmin = next (tarayıcı)
      except StopIteration:
         print ("Hata: Cevaplarınız arasında tutarsızlık var!")
         return()
   return sonrakiTahmin

def öncekilerleTutarsızMı (st, tahminler):
    for tahmin in tahminler:
        sonuç = kontrol (tahmin [0], st)
        (doğruKonumlu, yakınKonumlu) = tahmin [1]
        if sonuç != [doğruKonumlu, yakınKonumlu]: return True # öncekilerle tutarsızlık hatası...
    return False # öncekilerle tutarlı...

def kontrol (t1, t2):
    isabet = 0
    yakın = 0
    for i in range (len (t1)):
        if t1 [i] == t2 [i]: isabet += 1
        else:
            if t1 [i] in t2: yakın += 1
    return [isabet, yakın]


if __name__ == "__main__":
   renkler = ["kırmızı", "yeşil", "mavi", "sarı", "turuncu", "pembe", "gri"]
   tahminler = []				
   renkAdedi = 5

   tarayıcı = tümRenkler (renkler, renkAdedi)
   tutulanRenkler = next (tarayıcı)

   ilkTahmin = (tutulanRenkler, (0, 0) )
   sayaç = 0
   while (ilkTahmin [1] [0] == -1) or (ilkTahmin [1] [0] != renkAdedi):
      sayaç +=1
      ilkTahmin = yeniDeğerleme (ilkTahmin [0])



"""Çıktı:
>python p_21601.py
(Tutulan renk dizilimi: kırmızı-yeşil-mavi-sarı-turuncu)

Yeni Tahminim:  turuncu gri yeşil mavi kırmızı
Siyah adedi [doğru konum]: 0
Beyaz adedi [yakın konum]: 4

Önceki tahminler:
 Renk dizilimi: [turuncu gri yeşil mavi kırmızı ], (İsabet Yakın): ( 0   4  )

Yeni Tahminim:  gri turuncu mavi yeşil sarı
Siyah adedi [doğru konum]: 1
Beyaz adedi [yakın konum]: 3

Önceki tahminler:
 Renk dizilimi: [turuncu gri yeşil mavi kırmızı ], (İsabet Yakın): ( 0   4  )
 Renk dizilimi: [gri turuncu mavi yeşil sarı ], (İsabet Yakın): ( 1   3  )

Yeni Tahminim:  gri yeşil turuncu pembe mavi
Siyah adedi [doğru konum]: 1
Beyaz adedi [yakın konum]: 2

Önceki tahminler:
 Renk dizilimi: [turuncu gri yeşil mavi kırmızı ], (İsabet Yakın): ( 0   4  )
 Renk dizilimi: [gri turuncu mavi yeşil sarı ], (İsabet Yakın): ( 1   3  )
 Renk dizilimi: [gri yeşil turuncu pembe mavi ], (İsabet Yakın): ( 1   2  )

Yeni Tahminim:  gri mavi kırmızı sarı turuncu
Siyah adedi [doğru konum]: 2
Beyaz adedi [yakın konum]: 2

Önceki tahminler:
 Renk dizilimi: [turuncu gri yeşil mavi kırmızı ], (İsabet Yakın): ( 0   4  )
 Renk dizilimi: [gri turuncu mavi yeşil sarı ], (İsabet Yakın): ( 1   3  )
 Renk dizilimi: [gri yeşil turuncu pembe mavi ], (İsabet Yakın): ( 1   2  )
 Renk dizilimi: [gri mavi kırmızı sarı turuncu ], (İsabet Yakın): ( 2   2  )

Yeni Tahminim:  gri mavi sarı kırmızı yeşil
Siyah adedi [doğru konum]: 0
Beyaz adedi [yakın konum]: 4

Önceki tahminler:
 Renk dizilimi: [turuncu gri yeşil mavi kırmızı ], (İsabet Yakın): ( 0   4  )
 Renk dizilimi: [gri turuncu mavi yeşil sarı ], (İsabet Yakın): ( 1   3  )
 Renk dizilimi: [gri yeşil turuncu pembe mavi ], (İsabet Yakın): ( 1   2  )
 Renk dizilimi: [gri mavi kırmızı sarı turuncu ], (İsabet Yakın): ( 2   2  )
 Renk dizilimi: [gri mavi sarı kırmızı yeşil ], (İsabet Yakın): ( 0   4  )

Yeni Tahminim:  yeşil turuncu kırmızı sarı mavi
Siyah adedi [doğru konum]: 1
Beyaz adedi [yakın konum]: 4

Önceki tahminler:
 Renk dizilimi: [turuncu gri yeşil mavi kırmızı ], (İsabet Yakın): ( 0   4  )
 Renk dizilimi: [gri turuncu mavi yeşil sarı ], (İsabet Yakın): ( 1   3  )
 Renk dizilimi: [gri yeşil turuncu pembe mavi ], (İsabet Yakın): ( 1   2  )
 Renk dizilimi: [gri mavi kırmızı sarı turuncu ], (İsabet Yakın): ( 2   2  )
 Renk dizilimi: [gri mavi sarı kırmızı yeşil ], (İsabet Yakın): ( 0   4  )
 Renk dizilimi: [yeşil turuncu kırmızı sarı mavi ], (İsabet Yakın): ( 1   4  )

Yeni Tahminim:  kırmızı yeşil mavi sarı turuncu
Siyah adedi [doğru konum]: 5
Beyaz adedi [yakın konum]: 0

Önceki tahminler:
 Renk dizilimi: [turuncu gri yeşil mavi kırmızı ], (İsabet Yakın): ( 0   4  )
 Renk dizilimi: [gri turuncu mavi yeşil sarı ], (İsabet Yakın): ( 1   3  )
 Renk dizilimi: [gri yeşil turuncu pembe mavi ], (İsabet Yakın): ( 1   2  )
 Renk dizilimi: [gri mavi kırmızı sarı turuncu ], (İsabet Yakın): ( 2   2  )
 Renk dizilimi: [gri mavi sarı kırmızı yeşil ], (İsabet Yakın): ( 0   4  )
 Renk dizilimi: [yeşil turuncu kırmızı sarı mavi ], (İsabet Yakın): ( 1   4  )
 Renk dizilimi: [kırmızı yeşil mavi sarı turuncu ], (İsabet Yakın): ( 5   0  )

Aferin bana, tuttuğun renk dizilimini [7] tahminde buldum...
"""