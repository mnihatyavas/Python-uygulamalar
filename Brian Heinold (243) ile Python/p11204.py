# coding:iso-8859-9 Türkçe

L1 = [satır.strip() for satır in open ('sorular.txt')]
L2 = [satır.split (' ') for satır in L1]
L3 = [L2[i][j] for i in range (len (L2)) for j in range (len (L2[0])) ]
print (L3)
print ("\nListe kelimelerini uzunluklarına göre artan döküm:\n", "-"*50, sep="")
for i in range (20):
    yazdı= False
    for j in range (len (L3)):
        if len (L3[j]) == i + 1:
            print ((i+1), ":", L3[j])
            yazdı = True
    if yazdı: print()
print ("="*61)
sayaç = 0
for kelime in L3:
    if kelime[0].lower() in 'aeioöuü': sayaç +=1
print ("Listedeki SESLİ harfle başlayan kelimelerin yüzdesi: % {:.2f}" .format (100 * sayaç / len (L3)) )

sayaç = 0
for kelime in L3:
    if kelime[0].lower() not in 'aeioöuü': sayaç +=1
print ("Listedeki SESSİZ harfle başlayan kelimelerin yüzdesi: % {:.2f}" .format (100 * sayaç / len (L3)) )
print ("="*61)

enuzun = 0
for kelime in L3:
    for k in kelime:
        if k not in 'znu': break
    else:
        if len (kelime) > enuzun:
            enuzun = len (kelime)
            enuzunKelime = kelime
print ("\n'znu' içeren enuzun kelime ve uzunluğu:", enuzunKelime, "-->", enuzun)
