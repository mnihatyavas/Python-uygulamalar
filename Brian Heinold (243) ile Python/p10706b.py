# coding:iso-8859-9 Türkçe

sorular = ["Türkiye'nin başşehri neresidir?",
    "Hangi şehrimiz Yunanistan sınırındadır?",
    "Sınıriçi en uzun nehrimiz hangisidir?",
    "En debili nehrimiz hangisidir?",
    "En büyük HES barajımız hangisidir",
    "En yüksek dağımız hangisidir?",
    "Nüfusu en kalabalık şehrimiz hangisidir?",
    "Alanı en büyük şehrimiz hangisidir?",
    "En büyük gölümüz hangisidir?",
    "En küçük nüfuslu şehrimiz hangisidir?"]
cevaplar = ['Ankara', 'Edirne', 'Kızılırmak', 'Fırat', 'Atatürk', 'Ağrı', 'istanbul', 'Konya', 'Van', 'Ardahan']
doğru_sayısı = 0
for i in range (len (sorular)):
    cevap = input (sorular[i] + " ")
    if cevap.lower() == cevaplar[i].lower():
        print ('Aferin, bildiniz!')
        doğru_sayısı=doğru_sayısı+1
    else:
        print ('Maalesef yanlış! Doğrusu: [', cevaplar[i], '] olmalıydı.', sep="")
print ('\n', len(sorular), " sorudan toplam ", doğru_sayısı, "'unu doğru bildiniz.", sep="")
