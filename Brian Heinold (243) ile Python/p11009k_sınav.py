# coding:iso-8859-9 T�rk�e

sat�r = 0
while not (0 < sat�r < 15):
    try: sat�r = int (eval (input ("Paskal ��geni sat�r say�s�n� girin [1->14]: ")))
    except Exception: sat�r = 14

print ("\nPASKAL ��GEN�: \"(x + y) ^ sat�r\" a��l�m� katsay�lar�:\n", "="*53, sep="")
# 1.deneme...
L1 = [0 for i in range (sat�r)]
L1 = L1 + [1] + L1
print ([L1[k] for k in range (sat�r*2+1) if L1[k] != 0])
L2=L1
for i in range (sat�r):
    for j in range (sat�r*2):
        L2[j] = L1[j] + L1[j+1]
    print ([L2[k] for k in range (sat�r*2+1) if L2[k] != 0])
    L1 = L2

print("-"*79)
# 2.deneme...
L1 = [0 for i in range (sat�r)]
L1 = L1 + [1]
for i in range (sat�r+1):
    if L1[i] == 0: print ("{:4s}" .format (" "), end=" " )
    else: print ("{:4d}" .format (L1[i]), end=" " )
L2=L1
print()
for i in range (sat�r):
    for j in range (sat�r):
        L2[j] = L1[j] + L1[j+1]
    for k in range (sat�r+1):
        if L2[k] == 0: print ("{:4s}" .format (" "), end=" " )
        else: print ("{:4d}" .format (L2[k]), end=" " )
    print()
    L1 = L2

print("-"*79)
# 3.deneme...
L1 = [0 for i in range (sat�r)]
L1 = L1 + [1]
for i in range (sat�r+1):
    if L1[i] == 0: print ("{:2s}" .format (" "), end=" " )
    else: print ("{:4d}" .format (L1[i]), end=" " )
L2=L1
print()
for i in range (sat�r):
    for j in range (sat�r):
        L2[j] = L1[j] + L1[j+1]
    for k in range (sat�r+1):
        if L2[k] == 0: print ("{:2s}" .format (" "), end=" " )
        else: print ("{:4d}" .format (L2[k]), end=" " )
    print()
    L1 = L2
