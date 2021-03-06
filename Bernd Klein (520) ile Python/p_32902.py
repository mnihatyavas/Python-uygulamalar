#coding:iso-8859-9 T�rk�e
# p_32901.py: Kendi t�retti�imiz do�rusal birle�tirme �rne�i.

def fakt�rK�mesi():
    k�me = ( (i, j, k, l)
        for i in [-1, 0, 1]
        for j in [-1, 0, 1]
        for k in [-1, 0, 1]
        for l in [-1, 0, 1])
    for fakt�r in k�me: yield fakt�r

def belle (f):
    sonu�lar = {}
    def yard�mc� (n):
        if n not in sonu�lar: sonu�lar [n] = f (n)
        return sonu�lar [n]
    return yard�mc�

@belle
def do�rusalBirle�tirme (n):
    # n = i*1 + j*3 + k*9 + l*27 sonucunu d�nd�recek t�ple (i,j,k,l) �retir...
    a��rl�klar = (1, 3, 9, 27)
    for elemanlar in fakt�rK�mesi():
       toplam = 0
       uz = len (elemanlar)
       for i in range (uz): toplam += elemanlar [i] * a��rl�klar [i]
       if toplam == n: return elemanlar

y = ([1, 3, 9, 27])
print ("y:", y)
uz = len (y)
print ("\n-40-->40 aras� [1,3,9,27] elemanlar�yla olu�turulabilecek do�rusal birle�tirme t�pleleri d�k�m�:\n", "-"*79, sep="")
for i in range (-40, 41):
    x = do�rusalBirle�tirme (i)
    t = 0
    for j in range (uz): t += x[j] * y[j]
    print (t, "==>", x)



"""��kt�:
>python p_32902.py
y: [1, 3, 9, 27]

-40-->40 aras� [1,3,9,27] elemanlar�yla olu�turulabilecek do�rusal birle�tirme t
�pleleri d�k�m�:
-------------------------------------------------------------------------------
-40 ==> (-1, -1, -1, -1)
-39 ==> (0, -1, -1, -1)
-38 ==> (1, -1, -1, -1)
-37 ==> (-1, 0, -1, -1)
-36 ==> (0, 0, -1, -1)
-35 ==> (1, 0, -1, -1)
-34 ==> (-1, 1, -1, -1)
-33 ==> (0, 1, -1, -1)
-32 ==> (1, 1, -1, -1)
-31 ==> (-1, -1, 0, -1)
-30 ==> (0, -1, 0, -1)
-29 ==> (1, -1, 0, -1)
-28 ==> (-1, 0, 0, -1)
-27 ==> (0, 0, 0, -1)
-26 ==> (1, 0, 0, -1)
-25 ==> (-1, 1, 0, -1)
-24 ==> (0, 1, 0, -1)
-23 ==> (1, 1, 0, -1)
-22 ==> (-1, -1, 1, -1)
-21 ==> (0, -1, 1, -1)
-20 ==> (1, -1, 1, -1)
-19 ==> (-1, 0, 1, -1)
-18 ==> (0, 0, 1, -1)
-17 ==> (1, 0, 1, -1)
-16 ==> (-1, 1, 1, -1)
-15 ==> (0, 1, 1, -1)
-14 ==> (1, 1, 1, -1)
-13 ==> (-1, -1, -1, 0)
-12 ==> (0, -1, -1, 0)
-11 ==> (1, -1, -1, 0)
-10 ==> (-1, 0, -1, 0)
-9 ==> (0, 0, -1, 0)
-8 ==> (1, 0, -1, 0)
-7 ==> (-1, 1, -1, 0)
-6 ==> (0, 1, -1, 0)
-5 ==> (1, 1, -1, 0)
-4 ==> (-1, -1, 0, 0)
-3 ==> (0, -1, 0, 0)
-2 ==> (1, -1, 0, 0)
-1 ==> (-1, 0, 0, 0)
0 ==> (0, 0, 0, 0)
1 ==> (1, 0, 0, 0)
2 ==> (-1, 1, 0, 0)
3 ==> (0, 1, 0, 0)
4 ==> (1, 1, 0, 0)
5 ==> (-1, -1, 1, 0)
6 ==> (0, -1, 1, 0)
7 ==> (1, -1, 1, 0)
8 ==> (-1, 0, 1, 0)
9 ==> (0, 0, 1, 0)
10 ==> (1, 0, 1, 0)
11 ==> (-1, 1, 1, 0)
12 ==> (0, 1, 1, 0)
13 ==> (1, 1, 1, 0)
14 ==> (-1, -1, -1, 1)
15 ==> (0, -1, -1, 1)
16 ==> (1, -1, -1, 1)
17 ==> (-1, 0, -1, 1)
18 ==> (0, 0, -1, 1)
19 ==> (1, 0, -1, 1)
20 ==> (-1, 1, -1, 1)
21 ==> (0, 1, -1, 1)
22 ==> (1, 1, -1, 1)
23 ==> (-1, -1, 0, 1)
24 ==> (0, -1, 0, 1)
25 ==> (1, -1, 0, 1)
26 ==> (-1, 0, 0, 1)
27 ==> (0, 0, 0, 1)
28 ==> (1, 0, 0, 1)
29 ==> (-1, 1, 0, 1)
30 ==> (0, 1, 0, 1)
31 ==> (1, 1, 0, 1)
32 ==> (-1, -1, 1, 1)
33 ==> (0, -1, 1, 1)
34 ==> (1, -1, 1, 1)
35 ==> (-1, 0, 1, 1)
36 ==> (0, 0, 1, 1)
37 ==> (1, 0, 1, 1)
38 ==> (-1, 1, 1, 1)
39 ==> (0, 1, 1, 1)
40 ==> (1, 1, 1, 1)
"""