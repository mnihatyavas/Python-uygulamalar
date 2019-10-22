# coding:iso-8859-9 Türkçe

dizge1 = """Bu cümle içindeki 'bu', 've' ve 'a' ibarelerinin sayısını tespit
    etmek üzere count(..) metodu kullanılacaktır. Bu cümlede aranan
    ibarelerin hiç biri olmayabilir ve yine de sayaç bu takdirde hata vermeden
    sonucu sıfır olarak değerlendirecektir."""
print ("Cümledeki 'bu', 've', 'a' ibarelerinin sayısı:", dizge1.count ("bu"), dizge1.count ("ve"), dizge1.count ("a"))

dizge2 = input ("\nSayılar içeren dizge girin:")
if len (dizge2) == 0: dizge2 = "Tarih:17/04/1957, Saat:15:38"
d = ""
a=0
for i in range (len (dizge2)):
    if dizge2[i].isdigit():
        d = d + dizge2[i] + "+"
        a += eval (dizge2[i])
print ("Yeni sayısal dizgemiz:", d[:len (d)-1], "ve sayıların toplamı:", a)

liste = dizge1.split()
print ("\nDizgemizdeki tüm kelimeler:", liste)
print ("\nDizgemizdeki 3.kelime:", liste[2])
print ("\nDizgemizdeki her ardışık 3.kelimeler:", [liste[i] for i in range (0, len (liste), 3)])
print ("\nDizgemizdeki kelimelerin ilk harfi:", [k[0] for k in liste])
print ("\nDizgemizdeki kelimelerin son harfi:", [k[len (k)-1] for k in liste])

from random import shuffle
shuffle (liste)
print ("\nDizgemizdeki kelimeler gelişigüzel karıldı:", liste)

dizge2 = " ".join (liste).lower().replace (".", "") + "."
dizge2 = dizge2[0].upper() + dizge2[1:]
print ("\nDizgeleşen karma cümlemiz:", dizge2)

from random import randint
liste = ["Pizza + Kola", "Lahmacun + Ayran", "Adana Kebap + Yoğurt",
    "Yoğurtlu İskender + Şalgamsuyu", "Piliç Kızartma + Kola", "Antep Şiş + Salata",
    "Bumbar + Turşusuyu"]
print ("\nGünün spesiyal yemeği:", liste[randint (0, len (liste)-1)])
