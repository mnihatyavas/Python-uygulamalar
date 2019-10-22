# coding:iso-8859-9 Türkçe

from random import randint

alfabe ="abcçdefgğhıijklmnoöprsştuüvyz"
print (len (alfabe), "harf'li ardışık eksik harfli blok:")
print (alfabe)
for i in range (1, len (alfabe)):
    print (alfabe[i:], alfabe[:i], sep="")

print()
i = 0
while i < 5:
    endeks = randint (0,28)
    print ("Alfabenin ", endeks+1, ".inci harfi: ", alfabe[endeks], "'dir.", sep="")
    i +=1

print ("\nAlfabedeki türkçe harf sayısı: ", alfabe.count("ı")+alfabe.count("ı")+
    alfabe.count("ğ")+alfabe.count("ö")+alfabe.count("ü")+alfabe.count("ş"), "'dir.", sep="")
print()
türkçe="çığöüşÇİĞÖÜŞ"
for i in range (len (alfabe)):
    for t in range (len (türkçe)):
        if alfabe[i] == türkçe[t]:
            print (türkçe[t], " harfinin alfabedeki konumu: ", i+1, "'dir.", sep="");
            break
