# coding:iso-8859-9 Türkçe
# p_30304.py: numpy.array ve dtype ile stok malzemelerin takibi örneği.

import numpy as np

tiplemem = [('Ürün no', np.int32), ("Ürünün adı", np.unicode, 10), ("Stok miktarı", np.int32), ('Fiyatı', np.float64)]
stok = np.array ([
    (34765, "Kalem", 15897, 6.76), 
    (45765, "Çanta", 154, 149.93),
    (99661, "Silgi", 12367, 3.19),
    (125129, "Forma", 132, 729.39),
    (213765, "Defter", 8761, 24.65) ],
    dtype=tiplemem)

print ("2.stok:", stok [1])
print ("Ürün numaraları:", stok ["Ürün no"])
print ("5.ürünün adı:", stok [4] ["Ürünün adı"])
print ("Sonuncu ürüne kadar adetler:", stok [:-1] ["Stok miktarı"])
print ("4.ürünün fiyatı:", stok [3] ["Fiyatı"])

print ("\nTüm malzemelerin ardışık tablosu:\n", stok, sep="")

print ("\nTüm malzemelerin alt-alta tablosu:")
for i in range (len (stok)): print (stok [i])

toplam = 0
print ("\nTüm malzemelerin biçimli tablosu:\n", "-"*45, "\nSN ÜrünNo ÜrünAdı Miktarı Fiyatı ToplamDeğeri\n", "-"*45, sep="")
for i in range (len (stok)):
    değer = stok [i] [2] * stok [i] [3]
    toplam +=değer
    print ("{:2d} {:6d} {:6s} {:8,d} {:6.2f} {:12,.2f}" .format ((i+1), stok [i] [0], stok [i] [1], stok [i] [2], stok [i] [3], değer) )
print ("{}\n{}Stok değeri: {:10,.2f}" .format ("-"*45, " "*22, toplam) )



"""Çıktı:
>python p_30304.py
2.stok: (45765, 'Çanta', 154, 149.93)
Ürün numaraları: [ 34765  45765  99661 125129 213765]
5.ürünün adı: Defter
Sonuncu ürüne kadar adetler: [15897   154 12367   132]
4.ürünün fiyatı: 729.39

Tüm malzemelerin ardışık tablosu:
[( 34765, 'Kalem', 15897,   6.76) ( 45765, 'Çanta',   154, 149.93)
 ( 99661, 'Silgi', 12367,   3.19) (125129, 'Forma',   132, 729.39)
 (213765, 'Defter',  8761,  24.65)]

Tüm malzemelerin alt-alta tablosu:
(34765, 'Kalem', 15897, 6.76)
(45765, 'Çanta', 154, 149.93)
(99661, 'Silgi', 12367, 3.19)
(125129, 'Forma', 132, 729.39)
(213765, 'Defter', 8761, 24.65)

Tüm malzemelerin biçimli tablosu:
---------------------------------------------
SN ÜrünNo ÜrünAdı Miktarı Fiyatı ToplamDeğeri
---------------------------------------------
 1  34765 Kalem    15,897   6.76   107,463.72
 2  45765 Çanta       154 149.93    23,089.22
 3  99661 Silgi    12,367   3.19    39,450.73
 4 125129 Forma       132 729.39    96,279.48
 5 213765 Defter    8,761  24.65   215,958.65
---------------------------------------------
                      Stok değeri: 482,241.80
"""