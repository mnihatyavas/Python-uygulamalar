# coding:iso-8859-9 Türkçe

L = [{'ad':'Todd', 'telefon':'505-555-1414', 'eposta':'todd@mail.net'},
    {'ad':'Belkıs', 'telefon':'534-885-1314', 'eposta':''},
    {'ad':'Helga', 'telefon':'535-555-1618', 'eposta':'helga@mail.net'},
    {'ad':'Princess', 'telefon':'525-555-3141', 'eposta':''},
    {'ad':'LJ', 'telefon':'545-555-2718', 'eposta':'lj@mail.net'},
    {'ad':'Nihat', 'telefon':'505-991-8460', 'eposta':'mnihatyavas@gmail.com'},
    {'ad':'Canan', 'telefon':'515-551-3442', 'eposta':''},
    {'ad':'Mahmut', 'telefon':'551-555-9464', 'eposta':'mnyavas@hotmail.com'}]
from pprint import pprint
pprint (L)
print ("\nToplam ", len (L), " kaydın biçimli dökümü:\n", "-"*43, sep="")
print ("İsim     Telefon      Eposta\n", "="*43, sep ="")
for k in L: print ("{:8s} {:12s} {:20s}" .format (k["ad"], k["telefon"], k["eposta"]) )

print ("\nEposta'sız kayıtların biçimli dökümü:\n", "-"*37, sep="")
print ("İsim     Telefon\n", "="*37, sep ="")
for k in L:
    if k["eposta"] == "": print ("{:8s} {:12s}" .format (k["ad"], k["telefon"]) )
