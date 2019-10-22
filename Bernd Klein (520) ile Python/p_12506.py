# coding:iso-8859-9 Türkçe
# p_12506.py: Özyinelelemeli ve değişken argümanlı dekoratör fonksiyonlarında sayaç örneği.

def tamsayılı_argüman_kontrolü (f):
    def yardımcı (x):
        if type (x) == int and x >= 0: return f (x)
        else:
            print ("HATA: Argüman geçerli bir tamsayı değildir!..")
            return "***"
    return yardımcı

@tamsayılı_argüman_kontrolü
def ardılÇarp (n):
    if n == 1 or n == 0: return 1
    else: return n * ardılÇarp (n-1)

tüple = (10, 1, 10, 20, 3.8, -15, 9, 0)
for (i, j) in enumerate (tüple): print (i+1, j, ardılÇarp (j) )
print ("-"*75, "\n")
#------------------------------------------------------------------------------------------------------

def sayalım (fonk):
    def yardımcı (x):
        yardımcı.sayaç += 1
        return fonk (x)
    yardımcı.sayaç = 0
    return yardımcı

@sayalım
def birsonraki (x): return x+1

print ("sayalım(..) dekoratörü kaç kez çağrıldı:", birsonraki.sayaç)
for i in range (10): birsonraki (i)
print ("sayalım(..) dekoratörü kaç kez çağrıldı:", birsonraki.sayaç)
for i in range (15): birsonraki (i)
print ("sayalım(..) dekoratörü toplamda kaç kez çağrıldı:", birsonraki.sayaç)
print ("-"*75, "\n")
#------------------------------------------------------------------------------------------------------

def sayalım2 (fonk):
    def yardımcı (*a, **b):
        yardımcı.sayaç += 1
        return fonk (*a, **b)
    yardımcı.sayaç = 0
    return yardımcı

@sayalım2
def birsonraki (x): return x+1

@sayalım2
def çarp (x, y=1):
    if y==1: return x*y + 1 # birsonraki(x)'yle aynı...
    else: return x*y # İki sayının çarpımı...

print ("birsonraki(..) kaç kez çağrıldı:", birsonraki.sayaç)

for i in range (10): birsonraki (i)
çarp (3, 4)
çarp (4)
çarp (y=3, x=2)

print ("birsonraki(..) kaç kez çağrıldı:", birsonraki.sayaç)
print ("çarp(..) kaç kez çağrıldı:", çarp.sayaç)

for i in range (15): birsonraki (i)
çarp (5, 5)
çarp (10)
çarp (y=5, x=7.9)
çarp (x=-3.5, y=0.59)

print ("birsonraki(..) toplamda kaç kez çağrıldı:", birsonraki.sayaç)
print ("çarp(..) toplamda kaç kez çağrıldı:", çarp.sayaç)



"""Çıktı:
>python p_12506.py
1 10 3628800
2 1 1
3 10 3628800
4 20 2432902008176640000
HATA: Argüman geçerli bir tamsayı değildir!..
5 3.8 ***
HATA: Argüman geçerli bir tamsayı değildir!..
6 -15 ***
7 9 362880
8 0 1
---------------------------------------------------------------------------

sayalım(..) dekoratörü kaç kez çağrıldı: 0
sayalım(..) dekoratörü kaç kez çağrıldı: 10
sayalım(..) dekoratörü toplamda kaç kez çağrıldı: 25
---------------------------------------------------------------------------

birsonraki(..) kaç kez çağrıldı: 0
birsonraki(..) kaç kez çağrıldı: 10
çarp(..) kaç kez çağrıldı: 3
birsonraki(..) toplamda kaç kez çağrıldı: 25
çarp(..) toplamda kaç kez çağrıldı: 7
"""