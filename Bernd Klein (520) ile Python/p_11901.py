#coding:iso-8859-9 Türkçe
# p_11901.py: Print'le virgüllü, artılı, sep'li, %dizge biçimli değer yazdırma örneği.

from random import random, randint

a = randint (0, 10000)
b= random()

print ("Argümanların virgüllerle ayrıldığı print fonksiyonu:")
print (a, b, a*b, a/b, a**b)
print (a, b, a*b, a/b, a**b, sep=", ")
print (a, b, a*b, a/b, a**b, sep=" :-) ")
#--------------------------------------------------------------------------------------------

print ("\nDeğerleri dizge birleşmeyle tek bir dizgeye dönüşen print:")
print (str (a) + " " + str (b) + " " + str (a*b) + " " + str (a/b) + " " + str (a**b) )
#--------------------------------------------------------------------------------------------

print ("\n%sembol biçim dizgeli print:")
print ("a=%d, b=%.4f, a*b=%.4f, a/b=%.4f, a^b=%.4f" % (a, b, a*b, a/b, a**b) )
print ("\nTesadüfi ondalık sayı: %10.3e" % (a+b) )
print ("Tesadüfi ondalık sayı: %10.3E" % (a+b) )
print ("\nTesadüfi sekizlik sayı: %10o" % (a) )
print ("Tesadüfi sekizlik sayı: %.10o" % (a) )
print ("\nTesadüfi onaltılık sayı: %10x" % (a) )
print ("Tesadüfi onaltılık sayı: %10.8X" % (a) )
print ("\nSadece tek yüzde işareti: %%" % () )

print ("\n%#10d" % (a) )
print ("%#10X" % (a) )
print ("%10X" % (a) )
print ("%10.8X" % (a) )
print ("%#10.8X" % (a) )
print ("%#10o" % (a) )
print ("%+10d" % (a) )
print ("%+10d" % (-a) )
print ("%-10d" % (a) )
print ("% 10d" % (a) )
print ("%10.10d" % (a) )

biçimliDizge = "a=%d, b=%.4f, a*b=%.4f, a/b=%.4f, a^b=%.4f" % (a, b, a*b, a/b, a**b) 
print ("\nBiçimli dizge:", biçimliDizge)


"""Çıktı:
>python p_11901.py
Argümanların virgüllerle ayrıldığı print fonksiyonu:
5170 0.22836314917871736 1180.6374812539689 22639.379508442275 7.04732653573342
5170, 0.22836314917871736, 1180.6374812539689, 22639.379508442275, 7.04732653573342
5170 :-) 0.22836314917871736 :-) 1180.6374812539689 :-) 22639.379508442275 :-) 7.04732653573342

Değerleri dizge birleşmeyle tek bir dizgeye dönüşen print:
5170 0.22836314917871736 1180.6374812539689 22639.379508442275 7.04732653573342

%modulo/kalan sembollü biçimli dizgeli print:
a=5170, b=0.2284, a*b=1180.6375, a/b=22639.3795, a^b=7.0473

Tesadüfi ondalık sayı:  5.170e+03
Tesadüfi ondalık sayı:  5.170E+03

Tesadüfi sekizlik sayı:      12062
Tesadüfi sekizlik sayı: 0000012062

Tesadüfi onaltılık sayı:       1432
Tesadüfi onaltılık sayı:   00001432

Sadece tek yüzde işareti: %

      5170
    0X1432
      1432
  00001432
0X00001432
   0o12062
     +5170
     -5170
5170
      5170
0000005170

Biçimli dizge: a=5170, b=0.2284, a*b=1180.6375, a/b=22639.3795, a^b=7.0473
"""