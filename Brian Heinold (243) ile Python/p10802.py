# coding:iso-8859-9 Türkçe

dizge = "M. Nihat Yavaş; 17 / 04 / 1957; Yeşilyurt - Malatya;"
print ("Orijinal dizgemiz:", dizge)
print ("\nsplit'le kelimeleri liste elemanına dönüştürme:", dizge.split())

from string import punctuation
print ("\nPunctuation/noktalama string değişkeni içeriği:", punctuation)
for k in punctuation: dizge = dizge.replace (k, ' ')
print ("\nNoktalamaları boşluklanmış dizgemiz:", dizge)
liste = dizge.split()
print ("\nYeni split listemiz:", liste)

dizge = """Split metodu ve punctuation özel string değişkeniyle metni
noktalamalarından arındırıp, küçük harfe çevirip, istediğimiz kelimelerin
metin içinde tekrarlanma sayısını, metni split kelime elemanlı listeye
dönüştürerek yapabiliriz."""
print ("\nMetnimiz:", dizge)
for k in punctuation: dizge = dizge.replace (k, " ")
liste = dizge.lower().split()
print ("\nListemiz:", liste)
print ("\nMetindeki 'split' kelime sayısı:", liste.count ("split"))
print ("Metindeki 'metni' kelime sayısı:", liste.count ("metni"))
print ("Metindeki 've' kelime sayısı:", liste.count ("ve"))

telefon = "0-90-551-555-94-64"
print ("\nTelefon no:", telefon)
print ("'-'lerden arınık telefon no:", telefon.replace ("-", " "))
print ("Listeye dönüşen telefon no elemanları:", telefon.split ("-"))