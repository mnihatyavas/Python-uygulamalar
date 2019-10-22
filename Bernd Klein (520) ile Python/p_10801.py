# coding:iso-8859-9 Türkçe
# p_10801.py: Listelerle apend, extend ve pop işlemleri örneği.

L = ["Ankara", "İstanbul", "İzmir", "Mersin", "Antalya"]
print ("Liste:", L, "\nEbatı:", len (L), "\nSon elemanı:", L[-1] )

"""
append listeyi "NoneType" nesneye çevirir, listelenmez, pop'lanmaz?..
Bu yüzden = atamasız append/extend yapılmalıdır.
= atamalı ekleme yine ancak = ile yapılır...
L = L.append ("Bursa")
print ("append'li liste:", L)
print (L.pop (0) )
"""
print ("\nİlk ve son elemanı pop'lu liste:", L.pop (0), L.pop (-1), L )
print ("pop() son elemanı alır:", L.pop(), L) # pop() = pop (-1)

L += ["Mersin", "Antalya"]
print ("\nEklemeli liste:", L)

L.append (["Ankara", "Bursa"])
print ("2 append'li liste:", L)
L.pop (-1)

L.append ("Ankara")
print ("Tek append'li liste:", L)

L.extend (["Eskişehir", "Bursa"])
print ("2 extend'li liste:", L)

L.extend ("Adana")
print ("Tek extend'li liste:", L)
for i in range (len ("Adana")): L.pop ()

L.extend (["Adana"])
print ("[Tek] extend'li liste:", L)

for i in range (len (L)): L.pop () # Tüm listeyi pop()/siler...

tüple = ("Ankara", "İstanbul")
liste = ["İzmir", "Adana"]
dizge = "Mersin"
L.extend (tüple)
L.extend (liste)
L.extend ([dizge])
print ("\nTüple, liste ve dizge extend'li liste:", L)


"""Çıktı:
>python p_10801.py
Liste: ['Ankara', 'İstanbul', 'İzmir', 'Mersin', 'Antalya']
Ebatı: 5
Son elemanı: Antalya

İlk ve son elemanı pop'lu liste: Ankara Antalya ['İstanbul', 'İzmir', 'Mersin']
pop() son elemanı alır: Mersin ['İstanbul', 'İzmir']

Eklemeli liste: ['İstanbul', 'İzmir', 'Mersin', 'Antalya']
2 append'li liste: ['İstanbul', 'İzmir', 'Mersin', 'Antalya', ['Ankara', 'Bursa']]
Tek append'li liste: ['İstanbul', 'İzmir', 'Mersin', 'Antalya', 'Ankara']
2 extend'li liste: ['İstanbul', 'İzmir', 'Mersin', 'Antalya', 'Ankara', 'Eskişehir', 'Bursa']
Tek extend'li liste: ['İstanbul', 'İzmir', 'Mersin', 'Antalya', 'Ankara', 'Eskişehir', 'Bursa', 'A', 'd', 'a', 'n', 'a']
[Tek] extend'li liste: ['İstanbul', 'İzmir', 'Mersin', 'Antalya', 'Ankara', 'Eskişehir', 'Bursa', 'Adana']

Tüple, liste ve dizge extend'li liste: ['Ankara', 'İstanbul', 'İzmir', 'Adana','Mersin']
"""