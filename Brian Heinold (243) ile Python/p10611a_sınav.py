# coding:iso-8859-9 Türkçe

from math import trunc

cümle = input ("Herhangibir cümle girin: ")

print ("Cümlenin uzunluğu:", len (cümle))

print ("Cümlenin üçlemesi:", cümle*3)

if len (cümle) > 0: print ("Cümlenin ilk karakteri:", cümle[0])

print ("Cümlenin ilk 3 karakteri:", cümle[:3])

print ("Cümlenin son 3 karakteri:", cümle[-3:])

print ("Cümlenin tersi:", cümle[::-1])

if len (cümle) > 7: print ("Cümlenin 7.karakteri:", cümle[6])
else: print ("Cümlenin uzunluğu 7'den kısa!")

print ("İlk ve son karakter hariç cümleniz:", cümle[1:-1])

print ("Büyük harflerle cümleniz:", cümle.upper())

print ("[a<->ö] değişen cümleniz:", cümle.replace ('a', 'ö'))

print ("Harfleri yıldızlanan cümleniz: ", end="")
for k in cümle:
    if k.isalpha(): print ('*', end="")
    else: print (k, end="")

print ("\nCümlenizdeki tahmini kelime sayısı:", cümle.count (" ")+1)

print ("Cümledeki '(' ve ')' sayıları:", cümle.count ('('), cümle.count ('('))

sayaç=0
for k in 'aeıioöuü': sayaç += cümle.count (k)
print ("Cümlenizdeki toplam sesli harf sayısı:", sayaç)

print ("Küçük harfli ve nokta-virgülden ari cümleniz:", cümle.lower().replace (".", "").replace (",", ""))

ters = cümle[::-1]
if len (cümle) >2 and ters.lower() == cümle.lower(): print ("Cümleniz palindrom'dur!")
else: print ("Cümleniz palindrom değildir!")

print ("Cümlenizin ardışık genişleyen satır dökümü:")
for i in range (len (cümle)): print (" "*i, cümle[i], sep="")

print ("Her harfi çift büyük ve alt-alta şekilde cümleniz:")
for i in range (len (cümle)): print ((cümle[i]*2).upper())

print ("Harfaşırıları büyük olan cümleniz: ", end="")
for i in range (len (cümle)):
    if i % 2 == 0: print (cümle[i].lower(), end="")
    else: print (cümle[i].upper(), end="")

print ("\nİkinciyarının [", cümle[trunc(len(cümle)/2):], "] ilkyarıya [", cümle[:trunc(len(cümle)/2)], "] taraklandığı cümleniz: ", sep="", end="")
for i in range (trunc(len(cümle)/2)):
    print (cümle[i], cümle[i+(trunc(len(cümle)/2))], sep="", end="")
if len(cümle) % 2 != 0: print (cümle[len(cümle)-1])

print ("\nKelimelerin büyükharfle başladığı cümleniz: ", end="")
if len(cümle) > 0: print (cümle[0].upper(), end="")
for i in range (1, len(cümle)):
    if cümle[i-1] == ' ': print (cümle[i].upper(), end="")
    else: print (cümle[i], end="")
