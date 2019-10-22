# coding:iso-8859-9 T�rk�e
# p_13301.py: For d�ng�l� liste i�lemlerinin tek sat�rl�k kapsaml� listelenmesi �rne�i.

D = [-273, 0, 32, 100, 500]
F = list (map (lambda x: (float (9) / 5) * x + 32, D)) # Lambdal� map listeleri...
K = list (map (lambda x: (x + 459.4) * float (5) / 9, F))
S = list (map (lambda x: x - 273, K))

print ("[-273, 0, 32, 100, 500] derecelerin lambda anonim fonksiyonla harita'lanmas�:")
print ("\nD'ereceler fahrenhayt F'ye:", F)
print ("F'ler kelvin K'ye:", K)
print ("K'ler tekrar selsiy�s S'ye:", S)
print ("-"*75)
#---------------------------------------------------------------------------------------------------------

print ("\n�imdi de ayn� i�lemleri 'Kapsaml� Liste' ile yapal�m:")
F = [((float(9)/5)*x+32) for x in D]
K = [((x+459.4)*5.0/9) for x in F]
S = [(x-273) for x in K]

print ("\nD'ereceler fahrenhayt F'ye:", F)
print ("F'ler kelvin K'ye:", K)
print ("K'ler tekrar selsiy�s S'ye:", S)
print ("-"*75)
#---------------------------------------------------------------------------------------------------------

print ("\n1..100 aras� a^2+b^2=c^2 Pisagor'a uyan rakamlar� listeleyelim:\n")
print ([(x, y, z) for x in range (1, 100) for y in range (x, 100) for z in range (y, 100) if x**2 + y**2 == z**2])
print ("-"*75)
#---------------------------------------------------------------------------------------------------------

print ("\nKartezyen AxB'yi [k�rm�z�,ye�il,mavi]x[ev,araba,�i�ek] uyarlay�p listeleyelim:\n")
renkler = ["k�rm�z�", "sar�", "ye�il", "mavi"]
nesneler = ["ev", "araba", "a�a�", "ku�"]
renkliNesneler = [(x, y) for x in renkler for y in nesneler]
for k in range (len (renkliNesneler)): print ((k+1), ".nesne: ", renkliNesneler[k][0], " ", renkliNesneler[k][1], sep="")

"""��kt�:
>python p_13301.py
[-273, 0, 32, 100, 500] derecelerin lambda anonim fonksiyonla harita'lanmas�:

D'ereceler fahrenhayt F'ye: [-459.40000000000003, 32.0, 89.6, 212.0, 932.0]
F'ler kelvin K'ye: [-3.157967714489334e-14, 273.0, 305.0, 373.0, 773.0]
K'ler tekrar selsiy�s S'ye: [-273.00000000000006, 0.0, 32.0, 100.0, 500.0]
---------------------------------------------------------------------------

�imdi de ayn� i�lemleri 'Kapsaml� Liste' ile yapal�m:

D'ereceler fahrenhayt F'ye: [-459.40000000000003, 32.0, 89.6, 212.0, 932.0]
F'ler kelvin K'ye: [-3.157967714489334e-14, 273.0, 305.0, 373.0, 773.0]
K'ler tekrar selsiy�s S'ye: [-273.00000000000006, 0.0, 32.0, 100.0, 500.0]
---------------------------------------------------------------------------

1..100 aras� a^2+b^2=c^2 Pisagor'a uyan rakamlar� listeleyelim:

[(3, 4, 5), (5, 12, 13), (6, 8, 10), (7, 24, 25), (8, 15, 17), (9, 12, 15), (9,40, 41),
(10, 24, 26), (11, 60, 61), (12, 16, 20), (12, 35, 37), (13, 84, 85), (14, 48, 50), 
(15, 20, 25), (15, 36, 39), (16, 30, 34), (16, 63, 65), (18, 24, 30), 
(18, 80, 82), (20, 21, 29), (20, 48, 52), (21, 28, 35), (21, 72, 75), (24, 32, 40), 
(24, 45, 51), (24, 70, 74), (25, 60, 65), (27, 36, 45), (28, 45, 53), (30, 40, 50), 
(30, 72, 78), (32, 60, 68), (33, 44, 55), (33, 56, 65), (35, 84, 91),
(36, 48, 60), (36, 77, 85), (39, 52, 65), (39, 80, 89), (40, 42, 58), (40, 75,85), 
(42, 56, 70), (45, 60, 75), (48, 55, 73), (48, 64, 80), (51, 68, 85), (54,72, 90), 
(57, 76, 95), (60, 63, 87), (65, 72, 97)]
---------------------------------------------------------------------------

Kartezyen AxB'yi [k�rm�z�,ye�il,mavi]x[ev,araba,�i�ek] uyarlay�p listeleyelim:

1.nesne: k�rm�z� ev
2.nesne: k�rm�z� araba
3.nesne: k�rm�z� a�a�
4.nesne: k�rm�z� ku�
5.nesne: sar� ev
6.nesne: sar� araba
7.nesne: sar� a�a�
8.nesne: sar� ku�
9.nesne: ye�il ev
10.nesne: ye�il araba
11.nesne: ye�il a�a�
12.nesne: ye�il ku�
13.nesne: mavi ev
14.nesne: mavi araba
15.nesne: mavi a�a�
16.nesne: mavi ku�
"""