# coding:iso-8859-9 T�rk�e
# p_12603.py: Elde (1,3,9,27) kilolarla 40 �e�it sol-sa� kefeleri e�itleme �rne�i.

def bellekle (f):
    bellek = {}
    def yard�mc� (n):
        if n not in bellek: bellek[n] = f (n)
        return bellek[n]
    return yard�mc�

def fakt�rlerK�mesi():
    fakt�rlerK�mesi = ((i, j, k, l)
        for i in [-1, 0, 1] 
        for j in [-1, 0, 1]
        for k in [-1, 0, 1]
        for l in [-1, 0, 1])
    for fakt�r in fakt�rlerK�mesi: yield fakt�r

@bellekle
def do�rusalBirle�im (n):
    # "n = i*1 + j*3 + k*9 + l*27" e�itli�ini sa�layan t�ple(i,j,k,l)'yi d�nd�r�r...
    a��rl�klar = (1, 3, 9, 27)
    for fakt�rler in fakt�rlerK�mesi():
       toplam = 0
       for i in range (len (fakt�rler)): toplam += fakt�rler [i] * a��rl�klar [i]
       if toplam == n: return fakt�rler

def tart (a��rl�k):
    kilolar = (1, 3, 9, 27)
    kefeler = do�rusalBirle�im (a��rl�k)
    solKefe = ""
    sa�Kefe = ""
    for i in range (len (kefeler)):
        if kefeler [i] == -1: solKefe += str (kilolar [i]) + " "
        elif kefeler [i] == 1: sa�Kefe += str (kilolar [i]) + " "
    return (solKefe, sa�Kefe)

print ("Bulmaca: [1->40] kilo �ekeri, kilolar� icab�nda her iki kefeye de payla�t�rarak, enaz ka� kilo �e�itlemesiyle ve nas�l yapars�n�z?\nNot: Elde (1,3,9,27) kilolar olabilece�ini hesaplad���m�z� farzedelim.")
for i in range (1, 41):
    kefeler = tart (i)
    print ("Sol kefe: " + str(i) + " art� " + kefeler [0])
    print ("Sa� kefe: " + kefeler [1] + "\n")
print ("\nBen nas�l yap�ld���n� anlayamad�m; anlayan varsa beri gelsin, bana da a��klas�n!..")



"""��kt�:
>python p_12603.py
Bulmaca: [1->40] kilo �ekeri, kilolar� icab�nda her iki kefeye de payla�t�rarak,
 enaz ka� kilo �e�itlemesiyle ve nas�l yapars�n�z?
Not: Elde (1,3,9,27) kilolar olabilece�ini hesaplad���m�z� farzedelim.

Sol kefe: 1 art�
Sa� kefe: 1

Sol kefe: 2 art� 1
Sa� kefe: 3

Sol kefe: 3 art�
Sa� kefe: 3

Sol kefe: 4 art�
Sa� kefe: 1 3

Sol kefe: 5 art� 1 3
Sa� kefe: 9

Sol kefe: 6 art� 3
Sa� kefe: 9

Sol kefe: 7 art� 3
Sa� kefe: 1 9

Sol kefe: 8 art� 1
Sa� kefe: 9

Sol kefe: 9 art�
Sa� kefe: 9

Sol kefe: 10 art�
Sa� kefe: 1 9

Sol kefe: 11 art� 1
Sa� kefe: 3 9

Sol kefe: 12 art�
Sa� kefe: 3 9

Sol kefe: 13 art�
Sa� kefe: 1 3 9

Sol kefe: 14 art� 1 3 9
Sa� kefe: 27

Sol kefe: 15 art� 3 9
Sa� kefe: 27

Sol kefe: 16 art� 3 9
Sa� kefe: 1 27

Sol kefe: 17 art� 1 9
Sa� kefe: 27

Sol kefe: 18 art� 9
Sa� kefe: 27

Sol kefe: 19 art� 9
Sa� kefe: 1 27

Sol kefe: 20 art� 1 9
Sa� kefe: 3 27

Sol kefe: 21 art� 9
Sa� kefe: 3 27

Sol kefe: 22 art� 9
Sa� kefe: 1 3 27

Sol kefe: 23 art� 1 3
Sa� kefe: 27

Sol kefe: 24 art� 3
Sa� kefe: 27

Sol kefe: 25 art� 3
Sa� kefe: 1 27

Sol kefe: 26 art� 1
Sa� kefe: 27

Sol kefe: 27 art�
Sa� kefe: 27

Sol kefe: 28 art�
Sa� kefe: 1 27

Sol kefe: 29 art� 1
Sa� kefe: 3 27

Sol kefe: 30 art�
Sa� kefe: 3 27

Sol kefe: 31 art�
Sa� kefe: 1 3 27

Sol kefe: 32 art� 1 3
Sa� kefe: 9 27

Sol kefe: 33 art� 3
Sa� kefe: 9 27

Sol kefe: 34 art� 3
Sa� kefe: 1 9 27

Sol kefe: 35 art� 1
Sa� kefe: 9 27

Sol kefe: 36 art�
Sa� kefe: 9 27

Sol kefe: 37 art�
Sa� kefe: 1 9 27

Sol kefe: 38 art� 1
Sa� kefe: 3 9 27

Sol kefe: 39 art�
Sa� kefe: 3 9 27

Sol kefe: 40 art�
Sa� kefe: 1 3 9 27


Ben nas�l yap�ld���n� anlayamad�m; anlayan varsa beri gelsin, bana da a��klas�n!..
"""