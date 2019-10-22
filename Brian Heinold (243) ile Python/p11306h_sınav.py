# coding:iso-8859-9 Türkçe

def kontrol_satır (L):
    global sıralı;
    sıralı = "123456789"
    for i in range (len (L)):
        ekle = ""
        for j in range (len (L[0])):
            ekle = ekle + str (L[i][j])
        ekle = list (ekle)
        ekle.sort()
        if "".join (ekle) != sıralı: return "HATALI, satır: " + str (i+1)
    return "HATASIZ"

def kontrol_sütun (L):
    for j in range (len (L[0])):
        ekle = ""
        for i in range (len (L)):
            ekle = ekle + str (L[i][j])
        ekle = list (ekle)
        ekle.sort()
        if "".join (ekle) != sıralı: return "HATALI, sütun: " + str (j+1)
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
        if "".join (ekle) != sıralı: return "HATALI, blok: " + str (b+1)
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
print ("Satır kontrolu sonucu, bu sudoku hatasız mı çözülmüş?", kontrol_satır (L1) )
print ("Sütun kontrolu sonucu, bu sudoku hatasız mı çözülmüş?", kontrol_sütun (L1) )
print ("Blok kontrolu sonucu, bu sudoku hatasız mı çözülmüş?", kontrol_blok (L1) )

print()
pprint (L2)
print ("Satır kontrolu sonucu, bu sudoku hatasız mı çözülmüş?", kontrol_satır (L2) )
print ("Sütun kontrolu sonucu, bu sudoku hatasız mı çözülmüş?", kontrol_sütun (L2) )
print ("Blok kontrolu sonucu, bu sudoku hatasız mı çözülmüş?", kontrol_blok (L2) )
