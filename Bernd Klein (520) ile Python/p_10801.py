# coding:iso-8859-9 T�rk�e
# p_10801.py: Listelerle apend, extend ve pop i�lemleri �rne�i.

L = ["Ankara", "�stanbul", "�zmir", "Mersin", "Antalya"]
print ("Liste:", L, "\nEbat�:", len (L), "\nSon eleman�:", L[-1] )

"""
append listeyi "NoneType" nesneye �evirir, listelenmez, pop'lanmaz?..
Bu y�zden = atamas�z append/extend yap�lmal�d�r.
= atamal� ekleme yine ancak = ile yap�l�r...
L = L.append ("Bursa")
print ("append'li liste:", L)
print (L.pop (0) )
"""
print ("\n�lk ve son eleman� pop'lu liste:", L.pop (0), L.pop (-1), L )
print ("pop() son eleman� al�r:", L.pop(), L) # pop() = pop (-1)

L += ["Mersin", "Antalya"]
print ("\nEklemeli liste:", L)

L.append (["Ankara", "Bursa"])
print ("2 append'li liste:", L)
L.pop (-1)

L.append ("Ankara")
print ("Tek append'li liste:", L)

L.extend (["Eski�ehir", "Bursa"])
print ("2 extend'li liste:", L)

L.extend ("Adana")
print ("Tek extend'li liste:", L)
for i in range (len ("Adana")): L.pop ()

L.extend (["Adana"])
print ("[Tek] extend'li liste:", L)

for i in range (len (L)): L.pop () # T�m listeyi pop()/siler...

t�ple = ("Ankara", "�stanbul")
liste = ["�zmir", "Adana"]
dizge = "Mersin"
L.extend (t�ple)
L.extend (liste)
L.extend ([dizge])
print ("\nT�ple, liste ve dizge extend'li liste:", L)


"""��kt�:
>python p_10801.py
Liste: ['Ankara', '�stanbul', '�zmir', 'Mersin', 'Antalya']
Ebat�: 5
Son eleman�: Antalya

�lk ve son eleman� pop'lu liste: Ankara Antalya ['�stanbul', '�zmir', 'Mersin']
pop() son eleman� al�r: Mersin ['�stanbul', '�zmir']

Eklemeli liste: ['�stanbul', '�zmir', 'Mersin', 'Antalya']
2 append'li liste: ['�stanbul', '�zmir', 'Mersin', 'Antalya', ['Ankara', 'Bursa']]
Tek append'li liste: ['�stanbul', '�zmir', 'Mersin', 'Antalya', 'Ankara']
2 extend'li liste: ['�stanbul', '�zmir', 'Mersin', 'Antalya', 'Ankara', 'Eski�ehir', 'Bursa']
Tek extend'li liste: ['�stanbul', '�zmir', 'Mersin', 'Antalya', 'Ankara', 'Eski�ehir', 'Bursa', 'A', 'd', 'a', 'n', 'a']
[Tek] extend'li liste: ['�stanbul', '�zmir', 'Mersin', 'Antalya', 'Ankara', 'Eski�ehir', 'Bursa', 'Adana']

T�ple, liste ve dizge extend'li liste: ['Ankara', '�stanbul', '�zmir', 'Adana','Mersin']
"""