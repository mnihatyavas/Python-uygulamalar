# coding:iso-8859-9 Türkçe

alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"
L = list (alfabe)
from random import shuffle
from random import randint
shuffle (L)
L1 = [L[i] for i in range (15)]
L1 = L1 * 2
shuffle (L1)
L = [[" " for i in range (5)] for j in range (6)]
from pprint import pprint
i = j = 0
for h in L1:
    L[i][j] = h
    j +=1
    if j > 4:
        j = 0
        i +=1
L1 = [["*" for i in range (5)] for j in range (6)]
Devam = True
while Devam:
    s1=k1=9
    try:
        while not ((0 <= s1 <=5) and (0 <= k1 <=4)): s1, k1 = eval (input ("Virgülle ayrık bir kordinat girin [0->5, 0->4]: "))
        L1[s1][k1] = L[s1][k1]
    except Exception: s1 = randint (0,5); k1 = randint (0,4); L1[s1][k1] = L[s1][k1]
    s2=k2=9
    try:
        while not ((0 <= s2 <=5) and (0 <= k2 <=4)): s2, k2 = eval (input ("Virgülle ayrık başka bir kordinat girin [0->5, 0->4]: "))
        L1[s2][k2] = L[s2][k2]
    except Exception: s2 = randint (0,5); k2 = randint (0,4); L1[s2][k2] = L[s2][k2]
    print ("Çıkış: Ctrl-C")
    pprint (L1)
    if L1[s1][k1] != L1[s2][k2]: L1[s1][k1] = "*"; L1[s2][k2] = "*"
    if len (["*" for j in range (4) for i in range (5) if L1[i][j] == "*"]) == 0: Devam = False

