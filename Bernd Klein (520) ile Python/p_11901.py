#coding:iso-8859-9 T�rk�e
# p_11901.py: Print'le virg�ll�, art�l�, sep'li, %dizge bi�imli de�er yazd�rma �rne�i.

from random import random, randint

a = randint (0, 10000)
b= random()

print ("Arg�manlar�n virg�llerle ayr�ld��� print fonksiyonu:")
print (a, b, a*b, a/b, a**b)
print (a, b, a*b, a/b, a**b, sep=", ")
print (a, b, a*b, a/b, a**b, sep=" :-) ")
#--------------------------------------------------------------------------------------------

print ("\nDe�erleri dizge birle�meyle tek bir dizgeye d�n��en print:")
print (str (a) + " " + str (b) + " " + str (a*b) + " " + str (a/b) + " " + str (a**b) )
#--------------------------------------------------------------------------------------------

print ("\n%sembol bi�im dizgeli print:")
print ("a=%d, b=%.4f, a*b=%.4f, a/b=%.4f, a^b=%.4f" % (a, b, a*b, a/b, a**b) )
print ("\nTesad�fi ondal�k say�: %10.3e" % (a+b) )
print ("Tesad�fi ondal�k say�: %10.3E" % (a+b) )
print ("\nTesad�fi sekizlik say�: %10o" % (a) )
print ("Tesad�fi sekizlik say�: %.10o" % (a) )
print ("\nTesad�fi onalt�l�k say�: %10x" % (a) )
print ("Tesad�fi onalt�l�k say�: %10.8X" % (a) )
print ("\nSadece tek y�zde i�areti: %%" % () )

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

bi�imliDizge = "a=%d, b=%.4f, a*b=%.4f, a/b=%.4f, a^b=%.4f" % (a, b, a*b, a/b, a**b) 
print ("\nBi�imli dizge:", bi�imliDizge)


"""��kt�:
>python p_11901.py
Arg�manlar�n virg�llerle ayr�ld��� print fonksiyonu:
5170 0.22836314917871736 1180.6374812539689 22639.379508442275 7.04732653573342
5170, 0.22836314917871736, 1180.6374812539689, 22639.379508442275, 7.04732653573342
5170 :-) 0.22836314917871736 :-) 1180.6374812539689 :-) 22639.379508442275 :-) 7.04732653573342

De�erleri dizge birle�meyle tek bir dizgeye d�n��en print:
5170 0.22836314917871736 1180.6374812539689 22639.379508442275 7.04732653573342

%modulo/kalan semboll� bi�imli dizgeli print:
a=5170, b=0.2284, a*b=1180.6375, a/b=22639.3795, a^b=7.0473

Tesad�fi ondal�k say�:  5.170e+03
Tesad�fi ondal�k say�:  5.170E+03

Tesad�fi sekizlik say�:      12062
Tesad�fi sekizlik say�: 0000012062

Tesad�fi onalt�l�k say�:       1432
Tesad�fi onalt�l�k say�:   00001432

Sadece tek y�zde i�areti: %

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

Bi�imli dizge: a=5170, b=0.2284, a*b=1180.6375, a/b=22639.3795, a^b=7.0473
"""