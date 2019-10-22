# coding:iso-8859-9 Türkçe

liste = []
liste = eval (input ("Virgüllerle ayrık liste elemanları girin: "))
# Dizge elemanları tırnaklı, sayıları yalın, altlisteleri []'li girebilirsiniz...
if len(liste) > 0: print ('Listemizin ilk elemanı:', liste[0])
print ('Listemizin tüm elemanları:', liste)
for i in range (len(liste)): print ("Listemizin ", i, "'nici elemanı: ", liste[i], sep="")
for x in liste: print (x, end=" ")
print()
if 4 in liste: print ("Listemizde sayısal 4 elemanı vardır.")
if not 0 in liste: print ("Listemizde 0-sıfır değerli eleman yoktur.")
print()
print ("[7,8]+[3,4,5]:", [7,8]+[3,4,5])
print ("[7,8]*3:", [7,8]*3)
print ("[0]*5:", [0]*5)
print()
liste = []
for i in range(10): liste.append (i**2) # liste[] = i; tuple gibi atama yapılamaz...
# Hazır built-in liste metodları:
print (liste)
liste.reverse()
print (liste)
liste.sort()
print (liste)
print("\nListe elemanları toplamı:", round (sum (liste), 2))
print("Liste elemanları ortalaması:", round (sum (liste) / len (liste), 2))
print("En küçük liste elemanı:", round (min (liste), 2))
print("En büyük liste elemanı:", round (max (liste), 2))
print()
liste2 = liste[:]
liste2[6] = 9
liste2.insert (5, 19)
del liste2[4]
del liste2[:2]
print (liste2)
liste2.sort()
print (liste2)
print()
print ("\nListe metodları:", dir(list))

çıktı="""
Liste metodları: ['__add__', '__class__', '__contains__', '__delattr__', '__deli
tem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute_
_', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__
init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__'
, '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul_
_', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', '
append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove',
 'reverse', 'sort']
"""
