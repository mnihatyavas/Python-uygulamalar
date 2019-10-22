# coding:iso-8859-9 Türkçe

sorular = [satır.strip() for satır in open ('sorular.txt')]
cevaplar = [satır.strip() for satır in open ('cevaplar.txt')]

doğru_sayısı = 0
for i in range (len (sorular)):
    cevap = input (sorular[i] + " ")
    if cevap.lower() == cevaplar[i].lower():
        print ('Aferin, bildiniz!')
        doğru_sayısı=doğru_sayısı+1
    else:
        print ('Maalesef yanlış! Doğrusu: [', cevaplar[i], '] olmalıydı.', sep="")
print ('\n', len(sorular), " sorudan toplam ", doğru_sayısı, "'unu doğru bildiniz.", sep="")
