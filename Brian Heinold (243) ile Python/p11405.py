# coding:iso-8859-9 T�rk�e

# Program geneldir, Pano'nun sat�r/s�tun ve oyuncu say�s�n� istedi�ince de�i�tirebilirsin...
class Kaz�_Kazan:
    def __init__ (self):
        self.Pano = [
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0] ]
        self.oyuncu = randint (1,3)
        global sat�r, s�tun
        sat�r = len (self.Pano)
        s�tun = len (self.Pano[0])

    def ge�erliHamleMi (self, i, j):
        if 0<=i<=sat�r and 0<=j<=s�tun and self.Pano[i][j] == 0: return True
        return False

    # Bilardo misali, (deli�i) tutturdu�un s�rece sen oynars�n, tutturamazsan oyuncu (s�ras�) de�i�ir...
    def hamleyiYap (self, i, j):
        if self.ge�erliHamleMi (i, j): self.Pano[i][j] = self.oyuncu
        else: self.oyuncu = (self.oyuncu+3)%3+ 1

    def kazanan�nTespiti (self):
        global saya�1, saya�2, saya�3
        saya�1 = saya�2 = saya�3 = 0
        for i in range (sat�r):
            for j in range (s�tun):
                if self.Pano[i][j] == 1: saya�1 +=1
                if self.Pano[i][j] == 2: saya�2 +=1
                if self.Pano[i][j] == 3: saya�3 +=1
        if (saya�1+saya�2+saya�3) == sat�r*s�tun:
            if saya�1 == saya�2 == saya�3: return 0
            if saya�1 >= saya�2 and saya�1 >= saya�3: return 1
            if saya�2 >= saya�1 and saya�2 >= saya�3: return 2
            if saya�3 >= saya�1 and saya�3 >= saya�2: return 3
        return -1

def panoyuYaz():
    k = ['-', 'X', 'Y', 'Z']
    for i in range (sat�r):
        for j in range (s�tun): print (k[oyun.Pano[i][j]], end=' ')
        print()

from random import randint
oyun = Kaz�_Kazan()
panoyuYaz(); print()
# Hatal� giri�te tesad�fi tutturma devreye girer...
# Oynarken Pano'yu g�remezsin, haf�zana g�venmelisin...
while oyun.kazanan�nTespiti() == -1:
    try: i, j = eval (input ('Konum gir, (oyuncu ' + str (oyun.oyuncu) + '): '))
    except Exception:
        i = randint (0, sat�r-1)
        j = randint (0, s�tun-1)
    if not (0<=i<=sat�r): i = randint (0, sat�r-1)
    if not (0<=j<=s�tun): j = randint (0, s�tun-1)
    oyun.hamleyiYap (i, j)

print()
panoyuYaz()
x = oyun.kazanan�nTespiti()
print ("\nSkor: (X,Y,Z = ", saya�1, ",", saya�2, ",", saya�3, ")", sep="")
if x == 0: print ("BERABERE.")
else: print (x, '.oyuncu KAZANDI!', sep="")
