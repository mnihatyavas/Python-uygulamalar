# coding:iso-8859-9 T�rk�e

L = [{'ad':'Todd', 'telefon':'505-555-1414', 'eposta':'todd@mail.net'},
    {'ad':'Belk�s', 'telefon':'534-885-1314', 'eposta':''},
    {'ad':'Helga', 'telefon':'535-555-1618', 'eposta':'helga@mail.net'},
    {'ad':'Princess', 'telefon':'525-555-3141', 'eposta':''},
    {'ad':'LJ', 'telefon':'545-555-2718', 'eposta':'lj@mail.net'},
    {'ad':'Nihat', 'telefon':'505-991-8460', 'eposta':'mnihatyavas@gmail.com'},
    {'ad':'Canan', 'telefon':'515-551-3442', 'eposta':''},
    {'ad':'Mahmut', 'telefon':'551-555-9464', 'eposta':'mnyavas@hotmail.com'}]
from pprint import pprint
pprint (L)
print ("\nToplam ", len (L), " kayd�n bi�imli d�k�m�:\n", "-"*43, sep="")
print ("�sim     Telefon      Eposta\n", "="*43, sep ="")
for k in L: print ("{:8s} {:12s} {:20s}" .format (k["ad"], k["telefon"], k["eposta"]) )

print ("\nEposta's�z kay�tlar�n bi�imli d�k�m�:\n", "-"*37, sep="")
print ("�sim     Telefon\n", "="*37, sep ="")
for k in L:
    if k["eposta"] == "": print ("{:8s} {:12s}" .format (k["ad"], k["telefon"]) )
