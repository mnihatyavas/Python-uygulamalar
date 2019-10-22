# coding:iso-8859-9 T�rk�e
# p_12105.py: Erasto kevgiri ve kapsaml� liste y�ntemli asal say�lar tesbiti �rne�i.

from random import randint

def ErastoKevgiri (n):
    asalSay�lar = list (range (2, n+1))
    saya� = 2
    while saya� < n**0.5:
        i = saya�
        while i <= n:
            i += saya�
            if i in asalSay�lar: asalSay�lar.remove (i) # B�l�nebilen katl� say�lar� listeden siler...
        for j in asalSay�lar:
            if j > saya�:
                saya� = j
                break            
    return asalSay�lar

say� = randint (2,1000)
print ("Erastotenes kevgiri algoritmas�n�n tekrarl� d�ng�s�yle ilk ", say�, "'e kadarki asal say�lar listesi:", sep="")
print (ErastoKevgiri (say�))
#-----------------------------------------------------------------------------------------------------------

def asallar (n):
    if n == 0 or n == 1: return []
    else:
        asal = asallar (int (n**0.5))
        asalDe�il = [j for i in asal for j in range (i*2, n + 1, i)] # Katl� say�lar listesi...
        asal = [x for x in range (2, n + 1) if x not in asalDe�il] # Katl� hari� di�er say�lar listesi...
        return asal

print ("\nKapsaml� liste y�ntemiyle ilk ", say�, "'e kadarki asallar�n listesi:", sep="")
print (asallar (say�))


"""��kt�:
>python p_12105.py
Erastotenes kevgiri algoritmas�n�n tekrarl� d�ng�s�yle ilk 195'e kadarki asal say�lar listesi:
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73,
 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157,
163, 167, 173, 179, 181, 191, 193]

Kapsaml� liste y�ntemiyle ilk 195'e kadarki asallar�n listesi:
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73,
 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157,
163, 167, 173, 179, 181, 191, 193]
"""