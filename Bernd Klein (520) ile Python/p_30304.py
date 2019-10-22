# coding:iso-8859-9 T�rk�e
# p_30304.py: numpy.array ve dtype ile stok malzemelerin takibi �rne�i.

import numpy as np

tiplemem = [('�r�n no', np.int32), ("�r�n�n ad�", np.unicode, 10), ("Stok miktar�", np.int32), ('Fiyat�', np.float64)]
stok = np.array ([
    (34765, "Kalem", 15897, 6.76), 
    (45765, "�anta", 154, 149.93),
    (99661, "Silgi", 12367, 3.19),
    (125129, "Forma", 132, 729.39),
    (213765, "Defter", 8761, 24.65) ],
    dtype=tiplemem)

print ("2.stok:", stok [1])
print ("�r�n numaralar�:", stok ["�r�n no"])
print ("5.�r�n�n ad�:", stok [4] ["�r�n�n ad�"])
print ("Sonuncu �r�ne kadar adetler:", stok [:-1] ["Stok miktar�"])
print ("4.�r�n�n fiyat�:", stok [3] ["Fiyat�"])

print ("\nT�m malzemelerin ard���k tablosu:\n", stok, sep="")

print ("\nT�m malzemelerin alt-alta tablosu:")
for i in range (len (stok)): print (stok [i])

toplam = 0
print ("\nT�m malzemelerin bi�imli tablosu:\n", "-"*45, "\nSN �r�nNo �r�nAd� Miktar� Fiyat� ToplamDe�eri\n", "-"*45, sep="")
for i in range (len (stok)):
    de�er = stok [i] [2] * stok [i] [3]
    toplam +=de�er
    print ("{:2d} {:6d} {:6s} {:8,d} {:6.2f} {:12,.2f}" .format ((i+1), stok [i] [0], stok [i] [1], stok [i] [2], stok [i] [3], de�er) )
print ("{}\n{}Stok de�eri: {:10,.2f}" .format ("-"*45, " "*22, toplam) )



"""��kt�:
>python p_30304.py
2.stok: (45765, '�anta', 154, 149.93)
�r�n numaralar�: [ 34765  45765  99661 125129 213765]
5.�r�n�n ad�: Defter
Sonuncu �r�ne kadar adetler: [15897   154 12367   132]
4.�r�n�n fiyat�: 729.39

T�m malzemelerin ard���k tablosu:
[( 34765, 'Kalem', 15897,   6.76) ( 45765, '�anta',   154, 149.93)
 ( 99661, 'Silgi', 12367,   3.19) (125129, 'Forma',   132, 729.39)
 (213765, 'Defter',  8761,  24.65)]

T�m malzemelerin alt-alta tablosu:
(34765, 'Kalem', 15897, 6.76)
(45765, '�anta', 154, 149.93)
(99661, 'Silgi', 12367, 3.19)
(125129, 'Forma', 132, 729.39)
(213765, 'Defter', 8761, 24.65)

T�m malzemelerin bi�imli tablosu:
---------------------------------------------
SN �r�nNo �r�nAd� Miktar� Fiyat� ToplamDe�eri
---------------------------------------------
 1  34765 Kalem    15,897   6.76   107,463.72
 2  45765 �anta       154 149.93    23,089.22
 3  99661 Silgi    12,367   3.19    39,450.73
 4 125129 Forma       132 729.39    96,279.48
 5 213765 Defter    8,761  24.65   215,958.65
---------------------------------------------
                      Stok de�eri: 482,241.80
"""