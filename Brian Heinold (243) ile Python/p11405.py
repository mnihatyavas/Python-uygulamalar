# coding:iso-8859-9 Türkçe

# Program geneldir, Pano'nun satır/sütun ve oyuncu sayısını istediğince değiştirebilirsin...
class Kazı_Kazan:
    def __init__ (self):
        self.Pano = [
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0] ]
        self.oyuncu = randint (1,3)
        global satır, sütun
        satır = len (self.Pano)
        sütun = len (self.Pano[0])

    def geçerliHamleMi (self, i, j):
        if 0<=i<=satır and 0<=j<=sütun and self.Pano[i][j] == 0: return True
        return False

    # Bilardo misali, (deliği) tutturduğun sürece sen oynarsın, tutturamazsan oyuncu (sırası) değişir...
    def hamleyiYap (self, i, j):
        if self.geçerliHamleMi (i, j): self.Pano[i][j] = self.oyuncu
        else: self.oyuncu = (self.oyuncu+3)%3+ 1

    def kazananınTespiti (self):
        global sayaç1, sayaç2, sayaç3
        sayaç1 = sayaç2 = sayaç3 = 0
        for i in range (satır):
            for j in range (sütun):
                if self.Pano[i][j] == 1: sayaç1 +=1
                if self.Pano[i][j] == 2: sayaç2 +=1
                if self.Pano[i][j] == 3: sayaç3 +=1
        if (sayaç1+sayaç2+sayaç3) == satır*sütun:
            if sayaç1 == sayaç2 == sayaç3: return 0
            if sayaç1 >= sayaç2 and sayaç1 >= sayaç3: return 1
            if sayaç2 >= sayaç1 and sayaç2 >= sayaç3: return 2
            if sayaç3 >= sayaç1 and sayaç3 >= sayaç2: return 3
        return -1

def panoyuYaz():
    k = ['-', 'X', 'Y', 'Z']
    for i in range (satır):
        for j in range (sütun): print (k[oyun.Pano[i][j]], end=' ')
        print()

from random import randint
oyun = Kazı_Kazan()
panoyuYaz(); print()
# Hatalı girişte tesadüfi tutturma devreye girer...
# Oynarken Pano'yu göremezsin, hafızana güvenmelisin...
while oyun.kazananınTespiti() == -1:
    try: i, j = eval (input ('Konum gir, (oyuncu ' + str (oyun.oyuncu) + '): '))
    except Exception:
        i = randint (0, satır-1)
        j = randint (0, sütun-1)
    if not (0<=i<=satır): i = randint (0, satır-1)
    if not (0<=j<=sütun): j = randint (0, sütun-1)
    oyun.hamleyiYap (i, j)

print()
panoyuYaz()
x = oyun.kazananınTespiti()
print ("\nSkor: (X,Y,Z = ", sayaç1, ",", sayaç2, ",", sayaç3, ")", sep="")
if x == 0: print ("BERABERE.")
else: print (x, '.oyuncu KAZANDI!', sep="")
