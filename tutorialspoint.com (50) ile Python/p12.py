# coding:iso-8859-9 T�rk�e
# Python3 - Functions

# Fonksiyonlar�m�z�n tan�mlanmas�...
def yaz (dizge):
    "Bu fonksiyona aktar�lan dizgeyi ekrana yazd�r�r."
    print (dizge)
    return

def de�i�tirBeni1 (listem):
    "Bu fonksiyona ge�irilen listenin bir eleman�n� de�i�tirir."
    print ("Fonksiyon i�inde, de�i�iklik �ncesi liste i�erikleri:", listem)
    listem[1]=1957
    print ("Fonksiyon i�inde, de�i�iklik sonras� liste i�erikleri:", listem)
    return

def de�i�tirBeni2 (listem):
    "Bu fonksiyon listem'e silba�tan de�erler atar."
    print ("Fonksiyon i�inde, de�i�iklik �ncesi liste i�erikleri:", listem)
    listem = [45, 67, 93]
    print ("Fonksiyon i�inde, de�i�iklik sonras� liste i�erikleri:", listem)
    return

def kimlik (isim, ya�, do�umYeri, �lkesi = "T�rkiye", *de�i�ken):
    "Bu fonksiyona aktar�lan bilgileri ekrana yazd�r�r."
    print ("Ad� ve soyad�:", isim)
    print ("Ya��:", ya�)
    print ("Do�um yeri:", do�umYeri)
    print ("Memleketi:", �lkesi)
    for x in de�i�ken:
        print (x, end=" ")
    return

def toplam1 (*a):
    "Olas� t�m de�erleri toplar ve �a��rana d�nd�r�r."
    b = 0
    for x in a: b += x
    return b

toplam = lambda a1,a2,a3: a1 + a2 + a3

#
# Tan�ml� yaz(..) fonksiyonumuzun kullan�lmas�...
yaz ("Bu, kullan�c� tan�ml� fonksiyonumuza ilk �a��r�d�r!")
yaz ("Ayn� fonksiyona tekrar ikinci �a�r�m�z� yap�yoruz.\n")

# Tan�ml� de�i�tirBeni1(..) fonksiyonumuzun kullan�lmas�...
liste1 = [10,20,30]
de�i�tirBeni1 (liste1)
print ("Fonksiyon d���nda, liste i�erikleri:", liste1)

print()
# Tan�ml� de�i�tirBeni2(..) fonksiyonumuzun kullan�lmas�...
liste2 = [30,10,20]
de�i�tirBeni2 (liste2)
print ("Fonksiyon d���nda, liste i�erikleri:", liste2)

print()
# Tan�ml� kimlik(..) fonksiyonumuzun kullan�lmas�...
kimlik (�lkesi="TR", ya� = 60, do�umYeri = "Ye�ilyurt", isim="M.Nihat Yava�")
print()
kimlik (ya� = 60, do�umYeri = "Ye�ilyurt", isim="M.Nihat Yava�")
print()
kimlik ("M.Nihat Yava�", 62, "Malatya", "TR", "Hobileri:", "Gezinti", "Okuma", "Bisiklet", "Y�zme")

print("\n")
print ("Toplam(5, 10, 15):", toplam (5, 10, 15))
print ("Toplam(1.5, 2.13, 15):", toplam (1.5, 2.13, 15))

print("\n")
print ("Toplam():", toplam1 ())
print ("Toplam(5):", toplam1 (5))
print ("Toplam(5, 10, 2, 3.75):", toplam1 (5, 10, 2, 3.75))
