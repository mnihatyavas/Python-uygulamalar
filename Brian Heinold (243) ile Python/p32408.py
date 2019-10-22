# coding:iso-8859-9 T�rk�e

from collections import defaultdict

metin = open ("p32406x1.txt").read()
dd1 = defaultdict (int)
print ("Orijinal defaultdict/varsay�l�s�zl�k:\n", dd1)

for k in metin: dd1[k] +=1

print ("\nMetindeki karakterler s�kl��� SAYISAL i�lenen s�zl�k listesi:\n", list (dd1.items()) )
#----------------------------------------------------------------------------------------------

dd2 = defaultdict (str)
for k in metin: dd2[k] +="*"
print ("\nMetindeki karakterler s�kl��� D�ZGESEL i�lenen s�zl�k listesi:\n", list (dd2.items()) )
#----------------------------------------------------------------------------------------------

dd2 = defaultdict (list)
for k in metin: dd2[k] +=[1]
print ("\nMetindeki karakterler s�kl��� L�STESEL i�lenen s�zl�k d�k�m�:\n", dd2)
#----------------------------------------------------------------------------------------------

dd2 = defaultdict (float)
for k in metin: dd2[k] +=1.0
print ("\nMetindeki karakterler s�kl��� KAYANNOKTALI i�lenen s�zl�k d�k�m�:\n", dd2)
#----------------------------------------------------------------------------------------------

dd2 = defaultdict (lambda:100)
for k in metin: dd2[k] +=1
print ("\nMetindeki karakterler s�kl��� LAMBDA:100 i�lenen s�zl�k d�k�m�:\n", dd2)

# tuple, set ve dict'i �al��t�ramad�m...
