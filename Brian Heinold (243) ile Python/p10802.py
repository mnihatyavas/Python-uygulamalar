# coding:iso-8859-9 T�rk�e

dizge = "M. Nihat Yava�; 17 / 04 / 1957; Ye�ilyurt - Malatya;"
print ("Orijinal dizgemiz:", dizge)
print ("\nsplit'le kelimeleri liste eleman�na d�n��t�rme:", dizge.split())

from string import punctuation
print ("\nPunctuation/noktalama string de�i�keni i�eri�i:", punctuation)
for k in punctuation: dizge = dizge.replace (k, ' ')
print ("\nNoktalamalar� bo�luklanm�� dizgemiz:", dizge)
liste = dizge.split()
print ("\nYeni split listemiz:", liste)

dizge = """Split metodu ve punctuation �zel string de�i�keniyle metni
noktalamalar�ndan ar�nd�r�p, k���k harfe �evirip, istedi�imiz kelimelerin
metin i�inde tekrarlanma say�s�n�, metni split kelime elemanl� listeye
d�n��t�rerek yapabiliriz."""
print ("\nMetnimiz:", dizge)
for k in punctuation: dizge = dizge.replace (k, " ")
liste = dizge.lower().split()
print ("\nListemiz:", liste)
print ("\nMetindeki 'split' kelime say�s�:", liste.count ("split"))
print ("Metindeki 'metni' kelime say�s�:", liste.count ("metni"))
print ("Metindeki 've' kelime say�s�:", liste.count ("ve"))

telefon = "0-90-551-555-94-64"
print ("\nTelefon no:", telefon)
print ("'-'lerden ar�n�k telefon no:", telefon.replace ("-", " "))
print ("Listeye d�n��en telefon no elemanlar�:", telefon.split ("-"))