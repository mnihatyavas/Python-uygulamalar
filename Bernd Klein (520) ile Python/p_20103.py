# coding:iso-8859-9 T�rk�e
# p_20103.py: Veri ��k�� ve giri�lerinde print ile sys.stdout.write ve input ile sys.stdin.readline() �rne�i.

import sys

print ("print ile varsay�l� ��kt� ekrand�r.")
sys.stdout.write ("Ekrana yazd�rman�n 'sys.stdout.write()' y�ntemi.\n")

x = input ("\ninput ile varsay�l� veri giri�i klavyedir: ")
print ("Girdi�iniz veri:", x)

print ("\nKlavyeden 'sys.stdin.readline()' y�ntemiyle giri�: ", end=""); x = sys.stdin.readline()
print ("Girdi�iniz veri:", x)



"""��kt�:
>python p_20103.py
print ile varsay�l� ��kt� ekrand�r.
Ekrana yazd�rman�n 'sys.stdout.write()' y�ntemi.

input ile varsay�l� veri giri�i klavyedir: M Nihat Yava�
Girdi�iniz veri: M Nihat Yava�

Klavyeden 'sys.stdin.readline()' y�ntemiyle giri�: M.Nihat Yava�
Girdi�iniz veri: M.Nihat Yava�
"""