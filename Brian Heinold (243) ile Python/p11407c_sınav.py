# coding:iso-8859-9 T�rk�e
""" Bu program biraz �etrefillidir.
�lk giri� i�in "�ifreler.txt" dosyas� olu�turup i�ine de
ilk �ifrenizi yerle�tirmelisiniz...
"""

class �ifre_Y�neticisi:
    def __init__ (self):
        self.L = []

    def hesap_yarat (self, kod):
        dosya = open ("�ifreler.txt", "w")
        print (kod, file=dosya)

    def �ifre_do�ruMu (self, kod):
        self.L = [sat�r.strip() for sat�r in open ("�ifreler.txt", "r")]
        if kod == self.L[len (self.L)-1]: return True
        print ("Akt�el �ifreniz yanl��!")
        return False

    def oturum_a� (self):
        print ("\nOturumunuz a��ld�:\
            \nOturum formuna kat�labilir,\
            \n�ifrenizi de�i�tirebilir,\
            \n�ifrenizi unuttuysan�z yeni hesap yaratabilir,\
            \nMevcut �nceki �ifrelerinizi g�rebilirsiniz.")
        input ("Ent:")

    def �ifreyi_de�i�tir (self):
        while True:
            print ("\n�ifre de�i�ikli�i==>"); kod = �ifre_gir()
            mevcut = 0
            for i in range (len (self.L)):
                if kod == self.L[i]: mevcut = 1
            if mevcut == 1: input ("Bu �ifreniz eskiden kullan�lm��, yeniden deneyin [Ent]")
            else: break
        dosya = open ("�ifreler.txt", "a")
        print (kod, file=dosya)
        return kod

    def �ifreleri_g�r (self):
        self.L = [sat�r.strip() for sat�r in open ("�ifreler.txt", "r")]
        print (self.L); input ("Ent:")

def ana_men�():
    men� = "\n1. Yeni bir �ifreli hesap yarat\
        \n2. Mevcut �ifreli oturumu a�\
        \n3. �ifre de�i�ikli�i\
        \n4. �nceki �ifreleri g�rme\
        \n5. Son\
        \n\n   Se�iminiz==> "
    se� = 0
    while not (0 < se� < 6):
        try: se� = abs (int (eval (input (men�))))
        except Exception: se� = 0
    return se�

def �ifre_gir():
    while True:
        � = input ("\n�ifrenizi girin: ")
        if len (�) < 5 or not �[0].isalpha() or �.isalpha():
            print ("�ifreniz enaz 5 karakter, ilki harf, enaz da 1 rakam i�ermeli")
        else: return �

y�netim = �ifre_Y�neticisi()
�ifre = �ifre_gir()

while y�netim.�ifre_do�ruMu (�ifre):
    se�enek = ana_men�()
    if se�enek == 5:
        print ("\nOturumu sonland�rd�n�z, g�r��mek �zere!")
        break

    if se�enek == 1 and input ("\n�nceki �ifrelerin tamamen silinecek, emin misin ['e']: ").lower() == "e":
        y�netim.hesap_yarat (�ifre)
    elif se�enek == 2:
        if y�netim.�ifre_do�ruMu (�ifre): y�netim.oturum_a�()
    elif se�enek == 3:
        if y�netim.�ifre_do�ruMu (�ifre): �ifre = y�netim.�ifreyi_de�i�tir()
    elif se�enek == 4:
        if y�netim.�ifre_do�ruMu (�ifre): y�netim.�ifreleri_g�r()
