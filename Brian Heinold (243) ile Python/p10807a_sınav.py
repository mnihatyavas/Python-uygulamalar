# coding:iso-8859-9 T�rk�e

dizge1 = """Bu c�mle i�indeki 'bu', 've' ve 'a' ibarelerinin say�s�n� tespit
    etmek �zere count(..) metodu kullan�lacakt�r. Bu c�mlede aranan
    ibarelerin hi� biri olmayabilir ve yine de saya� bu takdirde hata vermeden
    sonucu s�f�r olarak de�erlendirecektir."""
print ("C�mledeki 'bu', 've', 'a' ibarelerinin say�s�:", dizge1.count ("bu"), dizge1.count ("ve"), dizge1.count ("a"))

dizge2 = input ("\nSay�lar i�eren dizge girin:")
if len (dizge2) == 0: dizge2 = "Tarih:17/04/1957, Saat:15:38"
d = ""
a=0
for i in range (len (dizge2)):
    if dizge2[i].isdigit():
        d = d + dizge2[i] + "+"
        a += eval (dizge2[i])
print ("Yeni say�sal dizgemiz:", d[:len (d)-1], "ve say�lar�n toplam�:", a)

liste = dizge1.split()
print ("\nDizgemizdeki t�m kelimeler:", liste)
print ("\nDizgemizdeki 3.kelime:", liste[2])
print ("\nDizgemizdeki her ard���k 3.kelimeler:", [liste[i] for i in range (0, len (liste), 3)])
print ("\nDizgemizdeki kelimelerin ilk harfi:", [k[0] for k in liste])
print ("\nDizgemizdeki kelimelerin son harfi:", [k[len (k)-1] for k in liste])

from random import shuffle
shuffle (liste)
print ("\nDizgemizdeki kelimeler geli�ig�zel kar�ld�:", liste)

dizge2 = " ".join (liste).lower().replace (".", "") + "."
dizge2 = dizge2[0].upper() + dizge2[1:]
print ("\nDizgele�en karma c�mlemiz:", dizge2)

from random import randint
liste = ["Pizza + Kola", "Lahmacun + Ayran", "Adana Kebap + Yo�urt",
    "Yo�urtlu �skender + �algamsuyu", "Pili� K�zartma + Kola", "Antep �i� + Salata",
    "Bumbar + Tur�usuyu"]
print ("\nG�n�n spesiyal yeme�i:", liste[randint (0, len (liste)-1)])
