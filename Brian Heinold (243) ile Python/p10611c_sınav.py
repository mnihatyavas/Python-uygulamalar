# coding:iso-8859-9 T�rk�e

from random import randint

alfabe ="abc�defg�h�ijklmno�prs�tu�vyz"
print (len (alfabe), "harf'li ard���k eksik harfli blok:")
print (alfabe)
for i in range (1, len (alfabe)):
    print (alfabe[i:], alfabe[:i], sep="")

print()
i = 0
while i < 5:
    endeks = randint (0,28)
    print ("Alfabenin ", endeks+1, ".inci harfi: ", alfabe[endeks], "'dir.", sep="")
    i +=1

print ("\nAlfabedeki t�rk�e harf say�s�: ", alfabe.count("�")+alfabe.count("�")+
    alfabe.count("�")+alfabe.count("�")+alfabe.count("�")+alfabe.count("�"), "'dir.", sep="")
print()
t�rk�e="������������"
for i in range (len (alfabe)):
    for t in range (len (t�rk�e)):
        if alfabe[i] == t�rk�e[t]:
            print (t�rk�e[t], " harfinin alfabedeki konumu: ", i+1, "'dir.", sep="");
            break
