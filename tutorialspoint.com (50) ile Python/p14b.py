# coding:iso-8859-9 T�rk�e

import os

print ("�imdiki dizinimiz: [" + os.getcwd() + "]")

try:
    print ("'deneme' adl� bir dizin yaratal�m==>")
    os.mkdir ("deneme")
except Exception:
    print()

print ("Yaratt���m�z 'deneme' dizini a�al�m==>")
os.chdir ("deneme")
print ("�imdiki dizinimiz: [" + os.getcwd() + "]")

os.chdir ("..")
print ("�imdiki dizinimiz: [" + os.getcwd() + "]")
print ("Yaratt���m�z 'deneme' adl� dizini silelim==>")
os.rmdir ("deneme")
