# coding:iso-8859-9 Türkçe

L = [satır.strip().split ("\t") for satır in open ("öğrenci2.txt")]
from pprint import pprint
print (len (L), " kişilik ÖĞRENCİ listesinin dosyadan dökümü:\n", "="*48, sep="")
pprint (L)

sorgu = input ("\nGörmek istediğin öğrencinin herhangi ARDIŞIK isim içeriğini gir: ").lower()
print ("\nİsim içeriğinde ARDIŞIK [", sorgu, "] bulunan kayıtların listesi:\n", "-"*60, sep="")
for k in L:
    if sorgu in str (k[0]).lower(): print (k)

sorgu = input ("\nGörmek istediğin öğrencinin herhangi ardışık-SIZ isim içeriğini gir: ").lower()
print ("\nİsim içeriğinde ardışık-SIZ [", sorgu, "] bulunan kayıtların listesi:\n", "-"*63, sep="")
for k in L:
    isim = str (k[0]).lower()
    kontrol = 0
    j = -1
    for i in range (len (sorgu)):
        while j < len (isim)-1:
            j +=1
            if sorgu[i] == isim[j]:
                kontrol +=1
                break
    if kontrol == len (sorgu): print (k)
