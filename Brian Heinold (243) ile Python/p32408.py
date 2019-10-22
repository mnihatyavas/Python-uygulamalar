# coding:iso-8859-9 Türkçe

from collections import defaultdict

metin = open ("p32406x1.txt").read()
dd1 = defaultdict (int)
print ("Orijinal defaultdict/varsayılısözlük:\n", dd1)

for k in metin: dd1[k] +=1

print ("\nMetindeki karakterler sıklığı SAYISAL işlenen sözlük listesi:\n", list (dd1.items()) )
#----------------------------------------------------------------------------------------------

dd2 = defaultdict (str)
for k in metin: dd2[k] +="*"
print ("\nMetindeki karakterler sıklığı DİZGESEL işlenen sözlük listesi:\n", list (dd2.items()) )
#----------------------------------------------------------------------------------------------

dd2 = defaultdict (list)
for k in metin: dd2[k] +=[1]
print ("\nMetindeki karakterler sıklığı LİSTESEL işlenen sözlük dökümü:\n", dd2)
#----------------------------------------------------------------------------------------------

dd2 = defaultdict (float)
for k in metin: dd2[k] +=1.0
print ("\nMetindeki karakterler sıklığı KAYANNOKTALI işlenen sözlük dökümü:\n", dd2)
#----------------------------------------------------------------------------------------------

dd2 = defaultdict (lambda:100)
for k in metin: dd2[k] +=1
print ("\nMetindeki karakterler sıklığı LAMBDA:100 işlenen sözlük dökümü:\n", dd2)

# tuple, set ve dict'i çalıştıramadım...
