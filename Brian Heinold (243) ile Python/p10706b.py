# coding:iso-8859-9 T�rk�e

sorular = ["T�rkiye'nin ba��ehri neresidir?",
    "Hangi �ehrimiz Yunanistan s�n�r�ndad�r?",
    "S�n�ri�i en uzun nehrimiz hangisidir?",
    "En debili nehrimiz hangisidir?",
    "En b�y�k HES baraj�m�z hangisidir",
    "En y�ksek da��m�z hangisidir?",
    "N�fusu en kalabal�k �ehrimiz hangisidir?",
    "Alan� en b�y�k �ehrimiz hangisidir?",
    "En b�y�k g�l�m�z hangisidir?",
    "En k���k n�fuslu �ehrimiz hangisidir?"]
cevaplar = ['Ankara', 'Edirne', 'K�z�l�rmak', 'F�rat', 'Atat�rk', 'A�r�', 'istanbul', 'Konya', 'Van', 'Ardahan']
do�ru_say�s� = 0
for i in range (len (sorular)):
    cevap = input (sorular[i] + " ")
    if cevap.lower() == cevaplar[i].lower():
        print ('Aferin, bildiniz!')
        do�ru_say�s�=do�ru_say�s�+1
    else:
        print ('Maalesef yanl��! Do�rusu: [', cevaplar[i], '] olmal�yd�.', sep="")
print ('\n', len(sorular), " sorudan toplam ", do�ru_say�s�, "'unu do�ru bildiniz.", sep="")
