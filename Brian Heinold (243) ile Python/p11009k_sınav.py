# coding:iso-8859-9 Türkçe

satır = 0
while not (0 < satır < 15):
    try: satır = int (eval (input ("Paskal üçgeni satır sayısını girin [1->14]: ")))
    except Exception: satır = 14

print ("\nPASKAL ÜÇGENİ: \"(x + y) ^ satır\" açılımı katsayıları:\n", "="*53, sep="")
# 1.deneme...
L1 = [0 for i in range (satır)]
L1 = L1 + [1] + L1
print ([L1[k] for k in range (satır*2+1) if L1[k] != 0])
L2=L1
for i in range (satır):
    for j in range (satır*2):
        L2[j] = L1[j] + L1[j+1]
    print ([L2[k] for k in range (satır*2+1) if L2[k] != 0])
    L1 = L2

print("-"*79)
# 2.deneme...
L1 = [0 for i in range (satır)]
L1 = L1 + [1]
for i in range (satır+1):
    if L1[i] == 0: print ("{:4s}" .format (" "), end=" " )
    else: print ("{:4d}" .format (L1[i]), end=" " )
L2=L1
print()
for i in range (satır):
    for j in range (satır):
        L2[j] = L1[j] + L1[j+1]
    for k in range (satır+1):
        if L2[k] == 0: print ("{:4s}" .format (" "), end=" " )
        else: print ("{:4d}" .format (L2[k]), end=" " )
    print()
    L1 = L2

print("-"*79)
# 3.deneme...
L1 = [0 for i in range (satır)]
L1 = L1 + [1]
for i in range (satır+1):
    if L1[i] == 0: print ("{:2s}" .format (" "), end=" " )
    else: print ("{:4d}" .format (L1[i]), end=" " )
L2=L1
print()
for i in range (satır):
    for j in range (satır):
        L2[j] = L1[j] + L1[j+1]
    for k in range (satır+1):
        if L2[k] == 0: print ("{:2s}" .format (" "), end=" " )
        else: print ("{:4d}" .format (L2[k]), end=" " )
    print()
    L1 = L2
