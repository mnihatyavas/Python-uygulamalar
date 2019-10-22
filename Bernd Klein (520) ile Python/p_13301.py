# coding:iso-8859-9 Türkçe
# p_13301.py: For döngülü liste işlemlerinin tek satırlık kapsamlı listelenmesi örneği.

D = [-273, 0, 32, 100, 500]
F = list (map (lambda x: (float (9) / 5) * x + 32, D)) # Lambdalı map listeleri...
K = list (map (lambda x: (x + 459.4) * float (5) / 9, F))
S = list (map (lambda x: x - 273, K))

print ("[-273, 0, 32, 100, 500] derecelerin lambda anonim fonksiyonla harita'lanması:")
print ("\nD'ereceler fahrenhayt F'ye:", F)
print ("F'ler kelvin K'ye:", K)
print ("K'ler tekrar selsiyüs S'ye:", S)
print ("-"*75)
#---------------------------------------------------------------------------------------------------------

print ("\nŞimdi de aynı işlemleri 'Kapsamlı Liste' ile yapalım:")
F = [((float(9)/5)*x+32) for x in D]
K = [((x+459.4)*5.0/9) for x in F]
S = [(x-273) for x in K]

print ("\nD'ereceler fahrenhayt F'ye:", F)
print ("F'ler kelvin K'ye:", K)
print ("K'ler tekrar selsiyüs S'ye:", S)
print ("-"*75)
#---------------------------------------------------------------------------------------------------------

print ("\n1..100 arası a^2+b^2=c^2 Pisagor'a uyan rakamları listeleyelim:\n")
print ([(x, y, z) for x in range (1, 100) for y in range (x, 100) for z in range (y, 100) if x**2 + y**2 == z**2])
print ("-"*75)
#---------------------------------------------------------------------------------------------------------

print ("\nKartezyen AxB'yi [kırmızı,yeşil,mavi]x[ev,araba,çiçek] uyarlayıp listeleyelim:\n")
renkler = ["kırmızı", "sarı", "yeşil", "mavi"]
nesneler = ["ev", "araba", "ağaç", "kuş"]
renkliNesneler = [(x, y) for x in renkler for y in nesneler]
for k in range (len (renkliNesneler)): print ((k+1), ".nesne: ", renkliNesneler[k][0], " ", renkliNesneler[k][1], sep="")

"""Çıktı:
>python p_13301.py
[-273, 0, 32, 100, 500] derecelerin lambda anonim fonksiyonla harita'lanması:

D'ereceler fahrenhayt F'ye: [-459.40000000000003, 32.0, 89.6, 212.0, 932.0]
F'ler kelvin K'ye: [-3.157967714489334e-14, 273.0, 305.0, 373.0, 773.0]
K'ler tekrar selsiyüs S'ye: [-273.00000000000006, 0.0, 32.0, 100.0, 500.0]
---------------------------------------------------------------------------

Şimdi de aynı işlemleri 'Kapsamlı Liste' ile yapalım:

D'ereceler fahrenhayt F'ye: [-459.40000000000003, 32.0, 89.6, 212.0, 932.0]
F'ler kelvin K'ye: [-3.157967714489334e-14, 273.0, 305.0, 373.0, 773.0]
K'ler tekrar selsiyüs S'ye: [-273.00000000000006, 0.0, 32.0, 100.0, 500.0]
---------------------------------------------------------------------------

1..100 arası a^2+b^2=c^2 Pisagor'a uyan rakamları listeleyelim:

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

Kartezyen AxB'yi [kırmızı,yeşil,mavi]x[ev,araba,çiçek] uyarlayıp listeleyelim:

1.nesne: kırmızı ev
2.nesne: kırmızı araba
3.nesne: kırmızı ağaç
4.nesne: kırmızı kuş
5.nesne: sarı ev
6.nesne: sarı araba
7.nesne: sarı ağaç
8.nesne: sarı kuş
9.nesne: yeşil ev
10.nesne: yeşil araba
11.nesne: yeşil ağaç
12.nesne: yeşil kuş
13.nesne: mavi ev
14.nesne: mavi araba
15.nesne: mavi ağaç
16.nesne: mavi kuş
"""