# coding:iso-8859-9 T�rk�e

sorular = [sat�r.strip() for sat�r in open ('sorular.txt')]
cevaplar = [sat�r.strip() for sat�r in open ('cevaplar.txt')]

do�ru_say�s� = 0
for i in range (len (sorular)):
    cevap = input (sorular[i] + " ")
    if cevap.lower() == cevaplar[i].lower():
        print ('Aferin, bildiniz!')
        do�ru_say�s�=do�ru_say�s�+1
    else:
        print ('Maalesef yanl��! Do�rusu: [', cevaplar[i], '] olmal�yd�.', sep="")
print ('\n', len(sorular), " sorudan toplam ", do�ru_say�s�, "'unu do�ru bildiniz.", sep="")
