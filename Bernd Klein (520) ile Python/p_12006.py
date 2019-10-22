# coding:iso-8859-9 Türkçe
# p_12006.py: Fonksiyon çoklu parametre ve argümanlarında *liste kullanılması örneği.

from random import randint, random

def aritmetikOrtalama1 (ilk, *diğerleri): return (ilk + sum (diğerleri)) / (1 + len (diğerleri))
def aritmetikOrtalama2 (liste): return sum (liste) / len (liste)

print ("4 sayının ortalaması:", aritmetikOrtalama1 (45, 32, 89, 78) )
print ("7 sayının ortalaması:", aritmetikOrtalama1 (0, 0, 8989.8, 78787.78, 3453, 78778.73, 0) )
print ("2 sayının ortalaması:", aritmetikOrtalama1 (45, 32) )
print ("Tek bir sayının ortalaması:", aritmetikOrtalama1 (45) )

a = randint (1,100)
print ("\nGelişigüzel", a, "elemanlı sayısal bir listenin ortalaması:", aritmetikOrtalama2 ([randint(0,100)+random() for i in range (a)]) )

b = randint (1,100)
liste = [randint (0, 100) + random() for i in range (b)]
print ("Gelişigüzel", b, "elemanlı sayısal argümanların ortalaması:", aritmetikOrtalama1 (*liste) )
#----------------------------------------------------------------------------------------------------------

listem = [('Nihat', 1047, 79.5), ('Sami', 1044, 35), ('İhsan', 1042, 67.5), ('Necati', 1048, 56), ("Hamit", 1057, 91.5), ("Zeki", 1039, 75.5)]
print ("\nOrijinal listem:", listem)

yeniListem = list (zip (*listem))
print ("\nZip'lenen listem:", yeniListem)
print ("\nSınıftaki toplam", len (listem), "öğrencinin not ortalaması:", aritmetikOrtalama1 (*yeniListem[2]) )


"""Çıktı:
>python p_12006.py
4 sayının ortalaması: 61.0
7 sayının ortalaması: 24287.044285714284
2 sayının ortalaması: 38.5
Tek bir sayının ortalaması: 45.0

Gelişigüzel 49 elemanlı sayısal bir listenin ortalaması: 52.51783109803962
Gelişigüzel 61 elemanlı sayısal argümanların ortalaması: 55.712565881134395

Orijinal listem: [('Nihat', 1047, 79.5), ('Sami', 1044, 35), ('İhsan', 1042, 67.5),
('Necati', 1048, 56), ('Hamit', 1057, 91.5), ('Zeki', 1039, 75.5)]

Zip'lenen listem: [('Nihat', 'Sami', 'İhsan', 'Necati', 'Hamit', 'Zeki'),
(1047, 1044, 1042, 1048, 1057, 1039), (79.5, 35, 67.5, 56, 91.5, 75.5)]

Sınıftaki toplam 6 öğrencinin not ortalaması: 67.5
"""