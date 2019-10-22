# coding:iso-8859-9 Türkçe
# p_20103.py: Veri çıkış ve girişlerinde print ile sys.stdout.write ve input ile sys.stdin.readline() örneği.

import sys

print ("print ile varsayılı çıktı ekrandır.")
sys.stdout.write ("Ekrana yazdırmanın 'sys.stdout.write()' yöntemi.\n")

x = input ("\ninput ile varsayılı veri girişi klavyedir: ")
print ("Girdiğiniz veri:", x)

print ("\nKlavyeden 'sys.stdin.readline()' yöntemiyle giriş: ", end=""); x = sys.stdin.readline()
print ("Girdiğiniz veri:", x)



"""Çıktı:
>python p_20103.py
print ile varsayılı çıktı ekrandır.
Ekrana yazdırmanın 'sys.stdout.write()' yöntemi.

input ile varsayılı veri girişi klavyedir: M Nihat Yavaş
Girdiğiniz veri: M Nihat Yavaş

Klavyeden 'sys.stdin.readline()' yöntemiyle giriş: M.Nihat Yavaş
Girdiğiniz veri: M.Nihat Yavaş
"""