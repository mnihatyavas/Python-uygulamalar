# coding:iso-8859-9 Türkçe

from random import randint, shuffle
L0 = list ("abcçdefgğhıijklmnoöpqrsştuüvwxyz")
L1= []
for i in range (randint (0,10), randint (15, 30)):
    shuffle (L0)
    alfabe = "".join (L0)
    L1.append (alfabe[:randint (2, 10)])
print ("Uzunluklarıyla toplam", len (L1), "adet liste elemanları:\n", [k for k in L1], "\n", [len (k) for k in L1])
print ("\nİlk harfleri kırpılı tüm dizgesel liste elemanları:\n", [k[1:] for k in L1])
print ("\nAynı uzunluktaki elemanların ardışık listeleri:")
for i in range (2, 11): print ([k for k in L1 if len (k) == i])

print ("\n[10->10000] arası tüm palindromik rakamlar:", [i for i in range (10, 10000) if str (i) == str (i)[::-1]])

print ("\n10 adet 0'a kadar artan 1-0'lı dizi:", [("1" + "0"*i) for i in range (1, 11)])

print ("\n10 adet 0'a kadar artan 1-0'lı diğer bir dizi:", [("1" + ",0"*i) for i in range (1, 11)])

print ("\n10 adet 0'a kadar artan 1-0'lı diğer bir dizi:", [eval("1" + ",0"*i) for i in range (1, 11)])
print ("\n[", end="")
for i in range (11):
    print ("1,", end="")
    for j in range (i):
        print("0,", end="")
print ("]")
print ("\n1,0,1,0,0,..azami 10 0'a kadar artan dizi:", [eval("1"+ "0"*j) for i in range (11) for j in range (i)])

L1=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
print ("\nListemiz ve eleman sayısı:", L1, len (L1))
print ("Liste elemanları arasındaki boşluklar:", [L1[i+1]-L1[i] for i in range (len (L1)-1)])
print ("Liste elemanları arasındaki azami boşluk:", max ([L1[i+1]-L1[i] for i in range (len (L1)-1)]))
print ("Liste elemanları arasındaki asgari boşluk:", min ([L1[i+1]-L1[i] for i in range (len (L1)-1)]))
print ("2 boşluklu liste elemanlarının sayısı:", len ( [L1[i+1]-L1[i] for i in range (len (L1)-1) if L1[i+1]-L1[i] == 2] ))
print ("2 boşluklu liste elemanlarının %'si:", len ([L1[i+1]-L1[i] for i in range (len (L1)-1) if L1[i+1]-L1[i] == 2]) * 100 / len (L1))
