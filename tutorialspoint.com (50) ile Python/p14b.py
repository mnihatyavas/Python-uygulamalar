# coding:iso-8859-9 Türkçe

import os

print ("Şimdiki dizinimiz: [" + os.getcwd() + "]")

try:
    print ("'deneme' adlı bir dizin yaratalım==>")
    os.mkdir ("deneme")
except Exception:
    print()

print ("Yarattığımız 'deneme' dizini açalım==>")
os.chdir ("deneme")
print ("Şimdiki dizinimiz: [" + os.getcwd() + "]")

os.chdir ("..")
print ("Şimdiki dizinimiz: [" + os.getcwd() + "]")
print ("Yarattığımız 'deneme' adlı dizini silelim==>")
os.rmdir ("deneme")
