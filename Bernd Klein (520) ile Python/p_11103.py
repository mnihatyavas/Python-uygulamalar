# coding:iso-8859-9 T�rk�e
# p_11103.py: K�melerde difference, - ve difference_update ile discard, remove ve pop silme farklar� �rne�i.

x = {"a", "b", "c", "d", "e"}
y = {"b", "c"}
z = {"c", "d"}

print ("difference'la 2 k�me fark�:", x.difference (y) )
print ("�ifte difference'la 3 k�me fark�:", x.difference (y).difference (z) )
print ("\n'-'yle 2 k�me fark�:", x - y )
print ("�ift '-'yle 3 k�me fark�:", x - y - z )
#---------------------------------------------------------------------------------------------------

x.difference_update (y)
print ("\nupdate'li difference fark sonucunu ilk k�meye g�nceller:", x)

x.add ("c"); x.add("b")
x = x - y
print ("'-' sonras� atama da ayn�s�n� yapar:", x)
#---------------------------------------------------------------------------------------------------

x = {"a", "b", "c", "d", "e"}
# discard'la verili set eleman� (namevcutsa ikazs�z) silinir...
# remove'la da verili set eleman� (namevcutsa KeyError'lu) silinir...

print ("\n�nce:", x)

x.discard ("d")
x.discard ("z")

x.remove ("a")
try: x.remove ("y")
except Exception as ist: print ("Namevcut eleman:", ist)

print ("discard ve remove sonras�:", x)
#---------------------------------------------------------------------------------------------------

print ("\n'x.pop()' geli�ig�zel x k�me eleman�n� ��kar�r ve g�sterir:", x.pop() )
print ("Tekrar 'x.pop()':", x.pop() ) # Kalan eleman yoksa KeyError hatas� f�rlat�r...
print ("Kalan x k�me elemanlar�::", x)


"""��kt�:
>python p_11103.py
difference'la 2 k�me fark�: {'e', 'a', 'd'}
�ifte difference'la 3 k�me fark�: {'e', 'a'}

'-'yle 2 k�me fark�: {'e', 'a', 'd'}
�ift '-'yle 3 k�me fark�: {'e', 'a'}

update'li difference fark sonucunu ilk k�meye g�nceller: {'a', 'e', 'd'}
'-' sonras� atama da ayn�s�n� yapar: {'e', 'a', 'd'}

�nce: {'a', 'b', 'e', 'c', 'd'}
Namevcut eleman: 'y'
discard ve remove sonras�: {'b', 'e', 'c'}

'x.pop()' geli�ig�zel x k�me eleman�n� ��kar�r ve g�sterir: b
Tekrar 'x.pop()': e
Kalan x k�me elemanlar�:: {'c'}
"""