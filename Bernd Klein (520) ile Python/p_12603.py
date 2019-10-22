# coding:iso-8859-9 Türkçe
# p_12603.py: Elde (1,3,9,27) kilolarla 40 çeşit sol-sağ kefeleri eşitleme örneği.

def bellekle (f):
    bellek = {}
    def yardımcı (n):
        if n not in bellek: bellek[n] = f (n)
        return bellek[n]
    return yardımcı

def faktörlerKümesi():
    faktörlerKümesi = ((i, j, k, l)
        for i in [-1, 0, 1] 
        for j in [-1, 0, 1]
        for k in [-1, 0, 1]
        for l in [-1, 0, 1])
    for faktör in faktörlerKümesi: yield faktör

@bellekle
def doğrusalBirleşim (n):
    # "n = i*1 + j*3 + k*9 + l*27" eşitliğini sağlayan tüple(i,j,k,l)'yi döndürür...
    ağırlıklar = (1, 3, 9, 27)
    for faktörler in faktörlerKümesi():
       toplam = 0
       for i in range (len (faktörler)): toplam += faktörler [i] * ağırlıklar [i]
       if toplam == n: return faktörler

def tart (ağırlık):
    kilolar = (1, 3, 9, 27)
    kefeler = doğrusalBirleşim (ağırlık)
    solKefe = ""
    sağKefe = ""
    for i in range (len (kefeler)):
        if kefeler [i] == -1: solKefe += str (kilolar [i]) + " "
        elif kefeler [i] == 1: sağKefe += str (kilolar [i]) + " "
    return (solKefe, sağKefe)

print ("Bulmaca: [1->40] kilo şekeri, kiloları icabında her iki kefeye de paylaştırarak, enaz kaç kilo çeşitlemesiyle ve nasıl yaparsınız?\nNot: Elde (1,3,9,27) kilolar olabileceğini hesapladığımızı farzedelim.")
for i in range (1, 41):
    kefeler = tart (i)
    print ("Sol kefe: " + str(i) + " artı " + kefeler [0])
    print ("Sağ kefe: " + kefeler [1] + "\n")
print ("\nBen nasıl yapıldığını anlayamadım; anlayan varsa beri gelsin, bana da açıklasın!..")



"""Çıktı:
>python p_12603.py
Bulmaca: [1->40] kilo şekeri, kiloları icabında her iki kefeye de paylaştırarak,
 enaz kaç kilo çeşitlemesiyle ve nasıl yaparsınız?
Not: Elde (1,3,9,27) kilolar olabileceğini hesapladığımızı farzedelim.

Sol kefe: 1 artı
Sağ kefe: 1

Sol kefe: 2 artı 1
Sağ kefe: 3

Sol kefe: 3 artı
Sağ kefe: 3

Sol kefe: 4 artı
Sağ kefe: 1 3

Sol kefe: 5 artı 1 3
Sağ kefe: 9

Sol kefe: 6 artı 3
Sağ kefe: 9

Sol kefe: 7 artı 3
Sağ kefe: 1 9

Sol kefe: 8 artı 1
Sağ kefe: 9

Sol kefe: 9 artı
Sağ kefe: 9

Sol kefe: 10 artı
Sağ kefe: 1 9

Sol kefe: 11 artı 1
Sağ kefe: 3 9

Sol kefe: 12 artı
Sağ kefe: 3 9

Sol kefe: 13 artı
Sağ kefe: 1 3 9

Sol kefe: 14 artı 1 3 9
Sağ kefe: 27

Sol kefe: 15 artı 3 9
Sağ kefe: 27

Sol kefe: 16 artı 3 9
Sağ kefe: 1 27

Sol kefe: 17 artı 1 9
Sağ kefe: 27

Sol kefe: 18 artı 9
Sağ kefe: 27

Sol kefe: 19 artı 9
Sağ kefe: 1 27

Sol kefe: 20 artı 1 9
Sağ kefe: 3 27

Sol kefe: 21 artı 9
Sağ kefe: 3 27

Sol kefe: 22 artı 9
Sağ kefe: 1 3 27

Sol kefe: 23 artı 1 3
Sağ kefe: 27

Sol kefe: 24 artı 3
Sağ kefe: 27

Sol kefe: 25 artı 3
Sağ kefe: 1 27

Sol kefe: 26 artı 1
Sağ kefe: 27

Sol kefe: 27 artı
Sağ kefe: 27

Sol kefe: 28 artı
Sağ kefe: 1 27

Sol kefe: 29 artı 1
Sağ kefe: 3 27

Sol kefe: 30 artı
Sağ kefe: 3 27

Sol kefe: 31 artı
Sağ kefe: 1 3 27

Sol kefe: 32 artı 1 3
Sağ kefe: 9 27

Sol kefe: 33 artı 3
Sağ kefe: 9 27

Sol kefe: 34 artı 3
Sağ kefe: 1 9 27

Sol kefe: 35 artı 1
Sağ kefe: 9 27

Sol kefe: 36 artı
Sağ kefe: 9 27

Sol kefe: 37 artı
Sağ kefe: 1 9 27

Sol kefe: 38 artı 1
Sağ kefe: 3 9 27

Sol kefe: 39 artı
Sağ kefe: 3 9 27

Sol kefe: 40 artı
Sağ kefe: 1 3 9 27


Ben nasıl yapıldığını anlayamadım; anlayan varsa beri gelsin, bana da açıklasın!..
"""