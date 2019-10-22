# coding:iso-8859-9 T�rk�e
# p_21601.py: Tutulan renk dizilimini isabet ve yak�ns� adediyle tahminleme oyunu �rne�i.

# Mastermind: ustaak�l, bulls & cows: bo�alar ve inekler, blacks & whites: aklar ve karalar/isabetler ve yak�ns�lar...

import random
from p_21601x import t�mRenkler

def yeniDe�erleme (tutulanRenkler):
    global saya�
    do�ruKonumlu, yak�nKonumlu = de�erlemeyiAl()
    if do�ruKonumlu == renkAdedi:
        tahminler.append ((tutulanRenkler, (do�ruKonumlu, yak�nKonumlu)))
        �ncekiTahminleriG�ster()
        print ("\nAferin bana, tuttu�un renk dizilimini [", saya�, "] tahminde buldum...", sep="")
        return (tutulanRenkler, (do�ruKonumlu, yak�nKonumlu))

    if not girdilerinizTutarl�M� ((do�ruKonumlu, yak�nKonumlu)):
        print ("Veri Giri� Hatas�: �zg�n�m, girdi�iniz bilgiler tutars�z...")
        return (tutulanRenkler, (-1, yak�nKonumlu))
    tahminler.append ((tutulanRenkler, (do�ruKonumlu, yak�nKonumlu)))
    �ncekiTahminleriG�ster()

    tutulanRenkler = yeniTahminYarat() 
    if not tutulanRenkler: return (tutulanRenkler, (-1, yak�nKonumlu))
    return (tutulanRenkler, (do�ruKonumlu, yak�nKonumlu))

def de�erlemeyiAl():
   eldekiTahminiG�ster (ilkTahmin [0])
   do�ruKonumlu = abs (int (input ("Siyah adedi [do�ru konum]: ")))
   yak�nKonumlu = abs (int (input ("Beyaz adedi [yak�n konum]: ")))
   return (do�ruKonumlu, yak�nKonumlu)

def eldekiTahminiG�ster (ilkTahmin):
   print ("\nYeni Tahminim: ", end=" ")
   for renk in ilkTahmin: print (renk, end=" ")
   print()

def �ncekiTahminleriG�ster():
    print ("\n�nceki tahminler:")
    for tahmin in tahminler:
        tahminRenkleri = tahmin [0]
        print (" Renk dizilimi: [", end="")
        for r in tahminRenkleri: print (r, end=" ")
        print ("], (�sabet Yak�n): (", end="")
        for i in tahmin[1]: print (" %i " % i, end=" ")
        print (")")

def girdilerinizTutarl�M� (a):
    (do�ruKonumlu, yak�nKonumlu) = a
    if ((do�ruKonumlu + yak�nKonumlu) > renkAdedi) \
            or ((do�ruKonumlu + yak�nKonumlu) < (len (renkler) - renkAdedi)):
        return False
    if do�ruKonumlu == 4 and yak�nKonumlu == 1: return False
    return True

def yeniTahminYarat():
   sonrakiTahmin = next (taray�c�) 
   while �ncekilerleTutars�zM� (sonrakiTahmin, tahminler):
      try: sonrakiTahmin = next (taray�c�)
      except StopIteration:
         print ("Hata: Cevaplar�n�z aras�nda tutars�zl�k var!")
         return()
   return sonrakiTahmin

def �ncekilerleTutars�zM� (st, tahminler):
    for tahmin in tahminler:
        sonu� = kontrol (tahmin [0], st)
        (do�ruKonumlu, yak�nKonumlu) = tahmin [1]
        if sonu� != [do�ruKonumlu, yak�nKonumlu]: return True # �ncekilerle tutars�zl�k hatas�...
    return False # �ncekilerle tutarl�...

def kontrol (t1, t2):
    isabet = 0
    yak�n = 0
    for i in range (len (t1)):
        if t1 [i] == t2 [i]: isabet += 1
        else:
            if t1 [i] in t2: yak�n += 1
    return [isabet, yak�n]


if __name__ == "__main__":
   renkler = ["k�rm�z�", "ye�il", "mavi", "sar�", "turuncu", "pembe", "gri"]
   tahminler = []				
   renkAdedi = 5

   taray�c� = t�mRenkler (renkler, renkAdedi)
   tutulanRenkler = next (taray�c�)

   ilkTahmin = (tutulanRenkler, (0, 0) )
   saya� = 0
   while (ilkTahmin [1] [0] == -1) or (ilkTahmin [1] [0] != renkAdedi):
      saya� +=1
      ilkTahmin = yeniDe�erleme (ilkTahmin [0])



"""��kt�:
>python p_21601.py
(Tutulan renk dizilimi: k�rm�z�-ye�il-mavi-sar�-turuncu)

Yeni Tahminim:  turuncu gri ye�il mavi k�rm�z�
Siyah adedi [do�ru konum]: 0
Beyaz adedi [yak�n konum]: 4

�nceki tahminler:
 Renk dizilimi: [turuncu gri ye�il mavi k�rm�z� ], (�sabet Yak�n): ( 0   4  )

Yeni Tahminim:  gri turuncu mavi ye�il sar�
Siyah adedi [do�ru konum]: 1
Beyaz adedi [yak�n konum]: 3

�nceki tahminler:
 Renk dizilimi: [turuncu gri ye�il mavi k�rm�z� ], (�sabet Yak�n): ( 0   4  )
 Renk dizilimi: [gri turuncu mavi ye�il sar� ], (�sabet Yak�n): ( 1   3  )

Yeni Tahminim:  gri ye�il turuncu pembe mavi
Siyah adedi [do�ru konum]: 1
Beyaz adedi [yak�n konum]: 2

�nceki tahminler:
 Renk dizilimi: [turuncu gri ye�il mavi k�rm�z� ], (�sabet Yak�n): ( 0   4  )
 Renk dizilimi: [gri turuncu mavi ye�il sar� ], (�sabet Yak�n): ( 1   3  )
 Renk dizilimi: [gri ye�il turuncu pembe mavi ], (�sabet Yak�n): ( 1   2  )

Yeni Tahminim:  gri mavi k�rm�z� sar� turuncu
Siyah adedi [do�ru konum]: 2
Beyaz adedi [yak�n konum]: 2

�nceki tahminler:
 Renk dizilimi: [turuncu gri ye�il mavi k�rm�z� ], (�sabet Yak�n): ( 0   4  )
 Renk dizilimi: [gri turuncu mavi ye�il sar� ], (�sabet Yak�n): ( 1   3  )
 Renk dizilimi: [gri ye�il turuncu pembe mavi ], (�sabet Yak�n): ( 1   2  )
 Renk dizilimi: [gri mavi k�rm�z� sar� turuncu ], (�sabet Yak�n): ( 2   2  )

Yeni Tahminim:  gri mavi sar� k�rm�z� ye�il
Siyah adedi [do�ru konum]: 0
Beyaz adedi [yak�n konum]: 4

�nceki tahminler:
 Renk dizilimi: [turuncu gri ye�il mavi k�rm�z� ], (�sabet Yak�n): ( 0   4  )
 Renk dizilimi: [gri turuncu mavi ye�il sar� ], (�sabet Yak�n): ( 1   3  )
 Renk dizilimi: [gri ye�il turuncu pembe mavi ], (�sabet Yak�n): ( 1   2  )
 Renk dizilimi: [gri mavi k�rm�z� sar� turuncu ], (�sabet Yak�n): ( 2   2  )
 Renk dizilimi: [gri mavi sar� k�rm�z� ye�il ], (�sabet Yak�n): ( 0   4  )

Yeni Tahminim:  ye�il turuncu k�rm�z� sar� mavi
Siyah adedi [do�ru konum]: 1
Beyaz adedi [yak�n konum]: 4

�nceki tahminler:
 Renk dizilimi: [turuncu gri ye�il mavi k�rm�z� ], (�sabet Yak�n): ( 0   4  )
 Renk dizilimi: [gri turuncu mavi ye�il sar� ], (�sabet Yak�n): ( 1   3  )
 Renk dizilimi: [gri ye�il turuncu pembe mavi ], (�sabet Yak�n): ( 1   2  )
 Renk dizilimi: [gri mavi k�rm�z� sar� turuncu ], (�sabet Yak�n): ( 2   2  )
 Renk dizilimi: [gri mavi sar� k�rm�z� ye�il ], (�sabet Yak�n): ( 0   4  )
 Renk dizilimi: [ye�il turuncu k�rm�z� sar� mavi ], (�sabet Yak�n): ( 1   4  )

Yeni Tahminim:  k�rm�z� ye�il mavi sar� turuncu
Siyah adedi [do�ru konum]: 5
Beyaz adedi [yak�n konum]: 0

�nceki tahminler:
 Renk dizilimi: [turuncu gri ye�il mavi k�rm�z� ], (�sabet Yak�n): ( 0   4  )
 Renk dizilimi: [gri turuncu mavi ye�il sar� ], (�sabet Yak�n): ( 1   3  )
 Renk dizilimi: [gri ye�il turuncu pembe mavi ], (�sabet Yak�n): ( 1   2  )
 Renk dizilimi: [gri mavi k�rm�z� sar� turuncu ], (�sabet Yak�n): ( 2   2  )
 Renk dizilimi: [gri mavi sar� k�rm�z� ye�il ], (�sabet Yak�n): ( 0   4  )
 Renk dizilimi: [ye�il turuncu k�rm�z� sar� mavi ], (�sabet Yak�n): ( 1   4  )
 Renk dizilimi: [k�rm�z� ye�il mavi sar� turuncu ], (�sabet Yak�n): ( 5   0  )

Aferin bana, tuttu�un renk dizilimini [7] tahminde buldum...
"""