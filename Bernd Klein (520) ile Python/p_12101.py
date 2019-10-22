# coding:iso-8859-9 T�rk�e
# p_12101.py: Fakt�ryel fonksiyonunun nihai ve arasonu�lu �zyinelemeli ile for d�ng�l� �rne�i.

from random import randint

def fakt�ryel1 (n):
    if n == 0: return 1
    else: return n * fakt�ryel1 (n-1)

say� = randint (0, 10)
print (say�, "say�s�n�n �zyinelemeli fakt�ryeli:", fakt�ryel1 (say�) )
#-----------------------------------------------------------------------------------------------------

def fakt�ryel (n):
    print ("Fakt�ryel fonksiyonu [n=" + str (n) + "] i�in �a��r�ld�")
    if n == 0:
        print()
        return 1
    else:
        sonu� = n * fakt�ryel (n-1)
        print ("Ara sonu�: ", n, "*fakt�ryel(", n-1, ")=", sonu�, sep="")
        return sonu�

print()
print ("\n", say�, " say�s�n�n �zyinelemeli ve arasonu� a��klamal� fakt�ryeli: ", fakt�ryel (say�), sep="")
#-----------------------------------------------------------------------------------------------------

def d�ng�l�Fakt�ryel (n):
    sonu� = 1
    for i in range (2, n+1): sonu� *= i
    return sonu�

print ("\n", say�, " say�s�n�n for d�ng�l� tekrarlamal� fakt�ryeli: ", d�ng�l�Fakt�ryel (say�), sep="")


"""��kt�:
>python p_12101.py
10 say�s�n�n �zyinelemeli fakt�ryeli: 3628800

Fakt�ryel fonksiyonu [n=10] i�in �a��r�ld�
Fakt�ryel fonksiyonu [n=9] i�in �a��r�ld�
Fakt�ryel fonksiyonu [n=8] i�in �a��r�ld�
Fakt�ryel fonksiyonu [n=7] i�in �a��r�ld�
Fakt�ryel fonksiyonu [n=6] i�in �a��r�ld�
Fakt�ryel fonksiyonu [n=5] i�in �a��r�ld�
Fakt�ryel fonksiyonu [n=4] i�in �a��r�ld�
Fakt�ryel fonksiyonu [n=3] i�in �a��r�ld�
Fakt�ryel fonksiyonu [n=2] i�in �a��r�ld�
Fakt�ryel fonksiyonu [n=1] i�in �a��r�ld�
Fakt�ryel fonksiyonu [n=0] i�in �a��r�ld�

Ara sonu�: 1*fakt�ryel(0)=1
Ara sonu�: 2*fakt�ryel(1)=2
Ara sonu�: 3*fakt�ryel(2)=6
Ara sonu�: 4*fakt�ryel(3)=24
Ara sonu�: 5*fakt�ryel(4)=120
Ara sonu�: 6*fakt�ryel(5)=720
Ara sonu�: 7*fakt�ryel(6)=5040
Ara sonu�: 8*fakt�ryel(7)=40320
Ara sonu�: 9*fakt�ryel(8)=362880
Ara sonu�: 10*fakt�ryel(9)=3628800

10 say�s�n�n �zyinelemeli ve arasonu� a��klamal� fakt�ryeli: 3628800

10 say�s�n�n for d�ng�l� tekrarlamal� fakt�ryeli: 3628800
"""