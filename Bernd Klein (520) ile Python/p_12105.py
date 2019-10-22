# coding:iso-8859-9 Türkçe
# p_12105.py: Erasto kevgiri ve kapsamlı liste yöntemli asal sayılar tesbiti örneği.

from random import randint

def ErastoKevgiri (n):
    asalSayılar = list (range (2, n+1))
    sayaç = 2
    while sayaç < n**0.5:
        i = sayaç
        while i <= n:
            i += sayaç
            if i in asalSayılar: asalSayılar.remove (i) # Bölünebilen katlı sayıları listeden siler...
        for j in asalSayılar:
            if j > sayaç:
                sayaç = j
                break            
    return asalSayılar

sayı = randint (2,1000)
print ("Erastotenes kevgiri algoritmasının tekrarlı döngüsüyle ilk ", sayı, "'e kadarki asal sayılar listesi:", sep="")
print (ErastoKevgiri (sayı))
#-----------------------------------------------------------------------------------------------------------

def asallar (n):
    if n == 0 or n == 1: return []
    else:
        asal = asallar (int (n**0.5))
        asalDeğil = [j for i in asal for j in range (i*2, n + 1, i)] # Katlı sayılar listesi...
        asal = [x for x in range (2, n + 1) if x not in asalDeğil] # Katlı hariç diğer sayılar listesi...
        return asal

print ("\nKapsamlı liste yöntemiyle ilk ", sayı, "'e kadarki asalların listesi:", sep="")
print (asallar (sayı))


"""Çıktı:
>python p_12105.py
Erastotenes kevgiri algoritmasının tekrarlı döngüsüyle ilk 195'e kadarki asal sayılar listesi:
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73,
 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157,
163, 167, 173, 179, 181, 191, 193]

Kapsamlı liste yöntemiyle ilk 195'e kadarki asalların listesi:
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73,
 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157,
163, 167, 173, 179, 181, 191, 193]
"""