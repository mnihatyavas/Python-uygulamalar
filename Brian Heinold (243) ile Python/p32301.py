# coding:iso-8859-9 T�rk�e

def f(x): return x*x

kopya1 = f # Python fonksiyon nesneleri de�i�ken adlar�na kopyalanabilir...
kopya2 = kopya1

print ('f(3) =', f (3), '\nkopya1(3) =', kopya1(3), "\nkopya2(4) =", kopya2 (4))
#-------------------------------------------------------------------------------------------

def g(x): return x*x*x
def h(x): return x**0.5

L = [f, g, h]
print ("\nL[2](64) =", L[2](64), "\nL[0](5) =", L[0](5), "\nL[1](3) =", L[1](3) )
#-------------------------------------------------------------------------------------------

i = 0
while not(0 < i < 4):
    try: i = abs (int (eval (input ("\n1->3 aras� bir tamsay� girin: "))))
    except Exception: i = 2

print ("L[", i-1, "](4) = ", L[i-1](4), sep="")
#-------------------------------------------------------------------------------------------

# 5 ��rencinin (�dev, ara, final) notlu t�pleli listesi...
L = [(45, 67, 52), (87, 75, 92), (62, 53, 79), (91, 85, 91), (42, 67, 35)]
print ("\n5 ��rencinin, �dev-ara-final notlar� (SIRASIZ):", L)
L.sort()
print ("\n5 ��rencinin, �dev-ara-final notlar� (�DEV'e g�re artan SIRALI):", L)

def kar��la�t�r (x): return x[1]
L.sort (key=kar��la�t�r)
print ("\n5 ��rencinin, �dev-ara-final notlar� (ARASINAV'a g�re artan SIRALI):", L)

def kar��la�t�r (x): return -x[2]
L.sort (key=kar��la�t�r)
print ("\n5 ��rencinin, �dev-ara-final notlar� (F�NAL'e g�re AZALAN SIRALI):", L)
#-------------------------------------------------------------------------------------------

L = "Bu, kelimeleri dizgeden listeye d�n��en ve artan veya azalan s�ralama y�ntemidir.".split()
print ("\nOrijinal liste:", L)

L.sort()
print ("\nKelimeleri artan s�ral� liste:", L)

L.reverse()
print ("\nKelimeleri azalan s�ral� liste:", L)

L.sort (key=len)
print ("\nKelimeleri uzunluklar�na g�re artan s�ral� liste:", L)

L.reverse()
print ("\nKelimeleri uzunluklar�na g�re azalan s�ral� liste:", L)