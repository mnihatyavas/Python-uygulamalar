# coding:iso-8859-9 Türkçe
# p_13208.py: Günlük ve haftalık fişno, adet*tutar+%12 kdv, 100€ < 10€ ekle fatura toplamları örneği.

from functools import reduce

siparişler = [[190301, ("5464", 4, 9.99), ("8274",18,12.98), ("9744", 9, 44.95)],
    [190304, ("5464", 9, 9.99), ("9744", 9, 44.95)],
    [190305, ("5464", 9, 9.99), ("88112", 11, 24.99)],
    [190306, ("8732", 7, 11.99), ("7733",11,18.99), ("88112", 5, 39.95)],
    [190307, ("5464", 2, 15.75)],
    [1903011, ("88112", 1, 45.85), ("9744", 15, 30.05), ("8732", 10, 8.74), ("7733", 1, 32.65)] ]

toplamFatura = list (map (lambda x: [x[0]] + list (map (lambda y: y[1]*y[2]*1.12, x[1:])), siparişler)) # %12 KDV vergi...
toplamFatura = list (map (lambda x: [x[0]] + [reduce (lambda a,b: a + b, x[1:])], toplamFatura)) # Aynı günün çoklu siparişleri toplanır...
toplamFatura = list (map (lambda x: x if x[1] >= 100 else (x[0], x[1] + 10), toplamFatura)) # Sipariş tutarı <100€ ise 10€ eklenir...

toplam = 0
for eleman in toplamFatura:
    print ("Fatura tarihi:", eleman[0], "\tGünlük faturalar toplamı:", eleman[1])
    toplam += eleman[1]

print ("\t\t\t", "-"*35, "\n", " "*36, "Genel toplam: ", int (toplam*100)/100.0, " TL", sep="")

"""Çıktı:
>python p_13208.py
Fatura tarihi: 190301   Günlük faturalar toplamı: 759.528
Fatura tarihi: 190304   Günlük faturalar toplamı: 553.7952
Fatura tarihi: 190305   Günlük faturalar toplamı: 408.576
Fatura tarihi: 190306   Günlük faturalar toplamı: 551.6784
Fatura tarihi: 190307   Günlük faturalar toplamı: 45.28
Fatura tarihi: 1903011  Günlük faturalar toplamı: 690.648
                                       ---------------------------------------------------
                                                        Genel toplam: 3009.5 TL
"""