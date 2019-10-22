# coding:iso-8859-9 T�rk�e

L1 = [[0]*10 for i in range (8)]
print ("[8x10]'li listemiz:", L1)

from random import randint
for i in range (8):
    for j in range (10):
        L1[i][j] = randint (-10, 50)
print ("De�er atal� listemiz:", L1)

print ("Formatl� listemiz:")
for i in range (len (L1)):
    for j in range (len (L1[0])):
        print ("{:4d}" .format (L1[i][j]), end="")
    print()

print ("Listemizin ortalama de�eri:", sum ([L1[i][j] for i in range (len (L1)) for j in range (len (L1[0]))]) / (len (L1) * len (L1[0])) )

from pprint import pprint
print ("pprint'li listemiz:")
pprint (L1)

print ("Listemizin enb�y�k eleman�:", max ([L1[i][j] for i in range (len(L1)) for j in range (len(L1[0])) ]))
print ("Listemizin enk���k eleman�:", min ([L1[i][j] for i in range (len(L1)) for j in range (len(L1[0])) ]))
sat�r = randint (0, len (L1)-1)
kolon = randint (0, len (L1[0])-1)
print ("Listemizin", sat�r+1, ".sat�rdaki enb�y�k eleman�:", max ([L1[sat�r][j] for j in range (len(L1[0])) ]))
print ("Listemizin", kolon+1, ".kolondaki enk���k eleman�:", min ([L1[i][kolon] for i in range (len(L1)) ]))

L1 = [[0]*8 for i in range (8)]
for i in range (len(L1)):
    for j in range(len(L1[0])):
        if (j+1)%2 == 1: L1[i][j] = 1
        else: L1[i][j] = 2
pprint (L1)

toplam1 = sum([L1[i][i] for i in range(len(L1))])
toplam2 = sum ([L1[i][i] for i in range (len(L1[0])-1,-1,-1)] )
e�it = (toplam1== toplam2)
for i in range(len(L1)):
    e�it = (toplam1 == sum ([L1[i][j] for j in range(len(L1[0]))] ))
if e�it: print ("[8x8] L1 listemiz sihirli kare (k��egen, sat�r ve kolonlar toplam� e�it=", toplam1, ") matrisD�R!")
else: print ("[8x8] L1 listemiz sihirli kare matris DE��LD�R!")
