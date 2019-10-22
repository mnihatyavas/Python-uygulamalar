# coding:iso-8859-9 T�rk�e

def kontrol_sat�r (L):
    global s�ral�;
    s�ral� = "123456789"
    for i in range (len (L)):
        ekle = ""
        for j in range (len (L[0])):
            ekle = ekle + str (L[i][j])
        ekle = list (ekle)
        ekle.sort()
        if "".join (ekle) != s�ral�: return "HATALI, sat�r: " + str (i+1)
    return "HATASIZ"

def kontrol_s�tun (L):
    for j in range (len (L[0])):
        ekle = ""
        for i in range (len (L)):
            ekle = ekle + str (L[i][j])
        ekle = list (ekle)
        ekle.sort()
        if "".join (ekle) != s�ral�: return "HATALI, s�tun: " + str (j+1)
    return "HATASIZ"

def kontrol_blok (L):
    blok = [ [(0, 3), (0, 3)], [(0, 3), (3, 6)], [(0, 3), (6, 9)],
        [(3, 6), (0, 3)], [(3, 6), (3, 6)], [(3, 6), (6, 9)],
        [(6, 9), (0, 3)], [(6, 9), (3, 6)], [(6, 9), (6, 9)] ]
    for b in range (9):
        ekle = ""
        for i in range (blok[b][0][0], blok[b][0][1]):
            for j in range (blok[b][1][0], blok[b][1][1]):
                ekle = ekle + str (L[i][j])
        ekle = list (ekle)
        ekle.sort()
        if "".join (ekle) != s�ral�: return "HATALI, blok: " + str (b+1)
    return "HATASIZ"

L1 = [ [7,4,9, 1,5,6, 3,8,2],
    [2,3,5, 8,4,9, 7,6,1],
    [1,8,6, 3,2,7, 9,4,5],
    [5,7,4, 2,6,8, 1,9,3],
    [9,2,8, 7,3,1, 6,5,4],
    [3,6,1, 5,9,4, 2,7,8],
    [4,1,2, 9,7,5, 8,3,6],
    [6,9,3, 4,8,2, 5,1,7],
    [8,5,7, 6,1,3, 4,2,9] ]

L2 = [ [1,2,8, 9,6,5, 7,3,4],
    [5,9,4, 1,7,3, 6,8,2],
    [6,3,7, 2,8,4, 1,5,9],
    [2,6,9, 7,5,1, 8,4,3],
    [4,7,5, 8,3,2, 9,6,1],
    [3,8,1, 4,9,6, 5,2,7],
    [8,5,2, 3,1,9, 4,7,6],
    [7,1,3, 6,4,8, 2,9,5],
    [9,4,6, 5,2,7, 3,1,8] ]

from pprint import pprint
pprint (L1)
print ("Sat�r kontrolu sonucu, bu sudoku hatas�z m� ��z�lm��?", kontrol_sat�r (L1) )
print ("S�tun kontrolu sonucu, bu sudoku hatas�z m� ��z�lm��?", kontrol_s�tun (L1) )
print ("Blok kontrolu sonucu, bu sudoku hatas�z m� ��z�lm��?", kontrol_blok (L1) )

print()
pprint (L2)
print ("Sat�r kontrolu sonucu, bu sudoku hatas�z m� ��z�lm��?", kontrol_sat�r (L2) )
print ("S�tun kontrolu sonucu, bu sudoku hatas�z m� ��z�lm��?", kontrol_s�tun (L2) )
print ("Blok kontrolu sonucu, bu sudoku hatas�z m� ��z�lm��?", kontrol_blok (L2) )
