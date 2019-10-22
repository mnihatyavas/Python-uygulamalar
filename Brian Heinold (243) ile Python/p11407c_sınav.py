# coding:iso-8859-9 Türkçe
""" Bu program biraz çetrefillidir.
İlk giriş için "şifreler.txt" dosyası oluşturup içine de
ilk şifrenizi yerleştirmelisiniz...
"""

class Şifre_Yöneticisi:
    def __init__ (self):
        self.L = []

    def hesap_yarat (self, kod):
        dosya = open ("şifreler.txt", "w")
        print (kod, file=dosya)

    def şifre_doğruMu (self, kod):
        self.L = [satır.strip() for satır in open ("şifreler.txt", "r")]
        if kod == self.L[len (self.L)-1]: return True
        print ("Aktüel şifreniz yanlış!")
        return False

    def oturum_aç (self):
        print ("\nOturumunuz açıldı:\
            \nOturum formuna katılabilir,\
            \nŞifrenizi değiştirebilir,\
            \nŞifrenizi unuttuysanız yeni hesap yaratabilir,\
            \nMevcut önceki şifrelerinizi görebilirsiniz.")
        input ("Ent:")

    def şifreyi_değiştir (self):
        while True:
            print ("\nŞifre değişikliği==>"); kod = şifre_gir()
            mevcut = 0
            for i in range (len (self.L)):
                if kod == self.L[i]: mevcut = 1
            if mevcut == 1: input ("Bu şifreniz eskiden kullanılmış, yeniden deneyin [Ent]")
            else: break
        dosya = open ("şifreler.txt", "a")
        print (kod, file=dosya)
        return kod

    def şifreleri_gör (self):
        self.L = [satır.strip() for satır in open ("şifreler.txt", "r")]
        print (self.L); input ("Ent:")

def ana_menü():
    menü = "\n1. Yeni bir şifreli hesap yarat\
        \n2. Mevcut şifreli oturumu aç\
        \n3. Şifre değişikliği\
        \n4. Önceki şifreleri görme\
        \n5. Son\
        \n\n   Seçiminiz==> "
    seç = 0
    while not (0 < seç < 6):
        try: seç = abs (int (eval (input (menü))))
        except Exception: seç = 0
    return seç

def şifre_gir():
    while True:
        ş = input ("\nŞifrenizi girin: ")
        if len (ş) < 5 or not ş[0].isalpha() or ş.isalpha():
            print ("Şifreniz enaz 5 karakter, ilki harf, enaz da 1 rakam içermeli")
        else: return ş

yönetim = Şifre_Yöneticisi()
şifre = şifre_gir()

while yönetim.şifre_doğruMu (şifre):
    seçenek = ana_menü()
    if seçenek == 5:
        print ("\nOturumu sonlandırdınız, görüşmek üzere!")
        break

    if seçenek == 1 and input ("\nÖnceki şifrelerin tamamen silinecek, emin misin ['e']: ").lower() == "e":
        yönetim.hesap_yarat (şifre)
    elif seçenek == 2:
        if yönetim.şifre_doğruMu (şifre): yönetim.oturum_aç()
    elif seçenek == 3:
        if yönetim.şifre_doğruMu (şifre): şifre = yönetim.şifreyi_değiştir()
    elif seçenek == 4:
        if yönetim.şifre_doğruMu (şifre): yönetim.şifreleri_gör()
