# coding:iso-8859-9 T�rk�e
# p_13208.py: G�nl�k ve haftal�k fi�no, adet*tutar+%12 kdv, 100� < 10� ekle fatura toplamlar� �rne�i.

from functools import reduce

sipari�ler = [[190301, ("5464", 4, 9.99), ("8274",18,12.98), ("9744", 9, 44.95)],
    [190304, ("5464", 9, 9.99), ("9744", 9, 44.95)],
    [190305, ("5464", 9, 9.99), ("88112", 11, 24.99)],
    [190306, ("8732", 7, 11.99), ("7733",11,18.99), ("88112", 5, 39.95)],
    [190307, ("5464", 2, 15.75)],
    [1903011, ("88112", 1, 45.85), ("9744", 15, 30.05), ("8732", 10, 8.74), ("7733", 1, 32.65)] ]

toplamFatura = list (map (lambda x: [x[0]] + list (map (lambda y: y[1]*y[2]*1.12, x[1:])), sipari�ler)) # %12 KDV vergi...
toplamFatura = list (map (lambda x: [x[0]] + [reduce (lambda a,b: a + b, x[1:])], toplamFatura)) # Ayn� g�n�n �oklu sipari�leri toplan�r...
toplamFatura = list (map (lambda x: x if x[1] >= 100 else (x[0], x[1] + 10), toplamFatura)) # Sipari� tutar� <100� ise 10� eklenir...

toplam = 0
for eleman in toplamFatura:
    print ("Fatura tarihi:", eleman[0], "\tG�nl�k faturalar toplam�:", eleman[1])
    toplam += eleman[1]

print ("\t\t\t", "-"*35, "\n", " "*36, "Genel toplam: ", int (toplam*100)/100.0, " TL", sep="")

"""��kt�:
>python p_13208.py
Fatura tarihi: 190301   G�nl�k faturalar toplam�: 759.528
Fatura tarihi: 190304   G�nl�k faturalar toplam�: 553.7952
Fatura tarihi: 190305   G�nl�k faturalar toplam�: 408.576
Fatura tarihi: 190306   G�nl�k faturalar toplam�: 551.6784
Fatura tarihi: 190307   G�nl�k faturalar toplam�: 45.28
Fatura tarihi: 1903011  G�nl�k faturalar toplam�: 690.648
                                       ---------------------------------------------------
                                                        Genel toplam: 3009.5 TL
"""