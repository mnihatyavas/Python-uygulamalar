# coding:iso-8859-9 Türkçe
# p_11103.py: Kümelerde difference, - ve difference_update ile discard, remove ve pop silme farkları örneği.

x = {"a", "b", "c", "d", "e"}
y = {"b", "c"}
z = {"c", "d"}

print ("difference'la 2 küme farkı:", x.difference (y) )
print ("Çifte difference'la 3 küme farkı:", x.difference (y).difference (z) )
print ("\n'-'yle 2 küme farkı:", x - y )
print ("Çift '-'yle 3 küme farkı:", x - y - z )
#---------------------------------------------------------------------------------------------------

x.difference_update (y)
print ("\nupdate'li difference fark sonucunu ilk kümeye günceller:", x)

x.add ("c"); x.add("b")
x = x - y
print ("'-' sonrası atama da aynısını yapar:", x)
#---------------------------------------------------------------------------------------------------

x = {"a", "b", "c", "d", "e"}
# discard'la verili set elemanı (namevcutsa ikazsız) silinir...
# remove'la da verili set elemanı (namevcutsa KeyError'lu) silinir...

print ("\nÖnce:", x)

x.discard ("d")
x.discard ("z")

x.remove ("a")
try: x.remove ("y")
except Exception as ist: print ("Namevcut eleman:", ist)

print ("discard ve remove sonrası:", x)
#---------------------------------------------------------------------------------------------------

print ("\n'x.pop()' gelişigüzel x küme elemanını çıkarır ve gösterir:", x.pop() )
print ("Tekrar 'x.pop()':", x.pop() ) # Kalan eleman yoksa KeyError hatası fırlatır...
print ("Kalan x küme elemanları::", x)


"""Çıktı:
>python p_11103.py
difference'la 2 küme farkı: {'e', 'a', 'd'}
Çifte difference'la 3 küme farkı: {'e', 'a'}

'-'yle 2 küme farkı: {'e', 'a', 'd'}
Çift '-'yle 3 küme farkı: {'e', 'a'}

update'li difference fark sonucunu ilk kümeye günceller: {'a', 'e', 'd'}
'-' sonrası atama da aynısını yapar: {'e', 'a', 'd'}

Önce: {'a', 'b', 'e', 'c', 'd'}
Namevcut eleman: 'y'
discard ve remove sonrası: {'b', 'e', 'c'}

'x.pop()' gelişigüzel x küme elemanını çıkarır ve gösterir: b
Tekrar 'x.pop()': e
Kalan x küme elemanları:: {'c'}
"""