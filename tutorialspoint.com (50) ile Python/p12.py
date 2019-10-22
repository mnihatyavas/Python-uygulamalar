# coding:iso-8859-9 Türkçe
# Python3 - Functions

# Fonksiyonlarımızın tanımlanması...
def yaz (dizge):
    "Bu fonksiyona aktarılan dizgeyi ekrana yazdırır."
    print (dizge)
    return

def değiştirBeni1 (listem):
    "Bu fonksiyona geçirilen listenin bir elemanını değiştirir."
    print ("Fonksiyon içinde, değişiklik öncesi liste içerikleri:", listem)
    listem[1]=1957
    print ("Fonksiyon içinde, değişiklik sonrası liste içerikleri:", listem)
    return

def değiştirBeni2 (listem):
    "Bu fonksiyon listem'e silbaştan değerler atar."
    print ("Fonksiyon içinde, değişiklik öncesi liste içerikleri:", listem)
    listem = [45, 67, 93]
    print ("Fonksiyon içinde, değişiklik sonrası liste içerikleri:", listem)
    return

def kimlik (isim, yaş, doğumYeri, ülkesi = "Türkiye", *değişken):
    "Bu fonksiyona aktarılan bilgileri ekrana yazdırır."
    print ("Adı ve soyadı:", isim)
    print ("Yaşı:", yaş)
    print ("Doğum yeri:", doğumYeri)
    print ("Memleketi:", ülkesi)
    for x in değişken:
        print (x, end=" ")
    return

def toplam1 (*a):
    "Olası tüm değerleri toplar ve çağırana döndürür."
    b = 0
    for x in a: b += x
    return b

toplam = lambda a1,a2,a3: a1 + a2 + a3

#
# Tanımlı yaz(..) fonksiyonumuzun kullanılması...
yaz ("Bu, kullanıcı tanımlı fonksiyonumuza ilk çağırıdır!")
yaz ("Aynı fonksiyona tekrar ikinci çağrımızı yapıyoruz.\n")

# Tanımlı değiştirBeni1(..) fonksiyonumuzun kullanılması...
liste1 = [10,20,30]
değiştirBeni1 (liste1)
print ("Fonksiyon dışında, liste içerikleri:", liste1)

print()
# Tanımlı değiştirBeni2(..) fonksiyonumuzun kullanılması...
liste2 = [30,10,20]
değiştirBeni2 (liste2)
print ("Fonksiyon dışında, liste içerikleri:", liste2)

print()
# Tanımlı kimlik(..) fonksiyonumuzun kullanılması...
kimlik (ülkesi="TR", yaş = 60, doğumYeri = "Yeşilyurt", isim="M.Nihat Yavaş")
print()
kimlik (yaş = 60, doğumYeri = "Yeşilyurt", isim="M.Nihat Yavaş")
print()
kimlik ("M.Nihat Yavaş", 62, "Malatya", "TR", "Hobileri:", "Gezinti", "Okuma", "Bisiklet", "Yüzme")

print("\n")
print ("Toplam(5, 10, 15):", toplam (5, 10, 15))
print ("Toplam(1.5, 2.13, 15):", toplam (1.5, 2.13, 15))

print("\n")
print ("Toplam():", toplam1 ())
print ("Toplam(5):", toplam1 (5))
print ("Toplam(5, 10, 2, 3.75):", toplam1 (5, 10, 2, 3.75))
