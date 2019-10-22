# coding:iso-8859-9 Türkçe
# p_11104.py: Kümelerde birleşim, kesişim, kesişimsiz, altküme ve üstküme örneği.

x = {"a", "b", "c", "d", "e"}
y = {"c", "d", "e", "f", "g"}

print ("x: ", x, "\ny: ", y, "\nx.union(y): ", x.union (y), sep="")
print ("union=|, yani or/veya'lı 'x | y':", x|y)
#---------------------------------------------------------------------------------------------------

print ("\n'x.intersection(y)' arakesit kümesi:", x.intersection (y) )
print ("intersection=&, yani and/ve'li'x&y':", x&y)
#---------------------------------------------------------------------------------------------------

x = {"a","b","c"}
y = {"c","d","e"}
print ("\nx: ", x, "\ny: ", y, "\nKesişimsiz mi? 'x.isdisjoint(y)': ", x.isdisjoint (y), sep="")

z = {"d","e","f"}
print ("\nz: ", z, "\nKesişimsiz mi? 'x.isdisjoint(z)': ", x.isdisjoint (z), sep="")
#---------------------------------------------------------------------------------------------------

x = {"a","b","c","d","e"}
y = {"c","d"}
print ("\nx: ", x, "\ny: ", y, "\n'y' altküme (<=) mi? 'y.issubset(x)': ", y.issubset (x), "\n'x' altküme mi? 'x.issubset(y): ", x.issubset (y), sep="")
print ("\n'y' tam altküme (<) mi? 'y<x':", y < x)
print ("\nBir küme asla kendisinin tam altkümesi (<) olamaz, 'x<x':", x < x)
print ("Ancak bir küme daima kendisinin altkümesi (<=)'dir, 'x.issubset(x)':", x.issubset (x) )
#---------------------------------------------------------------------------------------------------

print ("\n'y' üstküme (>=) mi? 'y.issuperset(x)': ", y.issuperset (x), "\n'x' üstküme mi? 'x.issuperset(y): ", x.issuperset (y), sep="")
print ("\n'y' tam üstküme (>) mi? 'x>y':", x > y)
print ("\nBir küme asla kendisinin tam üstkümesi (>) olamaz, 'y>y':", y > y)
print ("Ancak bir küme daima kendisinin üstkümesi (>=)'dir, 'y.issuperset(y)':", y.issuperset (y) )


"""Çıktı:
>python p_11104.py
x: {'d', 'b', 'e', 'a', 'c'}
y: {'d', 'e', 'c', 'g', 'f'}
x.union(y): {'b', 'd', 'e', 'a', 'c', 'g', 'f'}
union=|, yani or/veya'lı 'x | y': {'b', 'd', 'e', 'a', 'c', 'g', 'f'}

'x.intersection(y)' arakesit kümesi: {'e', 'c', 'd'}
intersection=&, yani and/ve'li'x&y': {'e', 'c', 'd'}

x: {'c', 'a', 'b'}
y: {'e', 'c', 'd'}
Kesişimsiz mi? 'x.isdisjoint(y)': False

z: {'e', 'f', 'd'}
Kesişimsiz mi? 'x.isdisjoint(z)': True

x: {'d', 'b', 'e', 'a', 'c'}
y: {'c', 'd'}
'y' altküme (<=) mi? 'y.issubset(x)': True
'x' altküme mi? 'x.issubset(y): False

'y' tam altküme (<) mi? 'y<x': True

Bir küme asla kendisinin tam altkümesi (<) olamaz, 'x<x': False
Ancak bir küme daima kendisinin altkümesi (<=)'dir, 'x.issubset(x)': True

'y' üstküme (>=) mi? 'y.issuperset(x)': False
'x' üstküme mi? 'x.issuperset(y): True

'y' tam üstküme (>) mi? 'x>y': True

Bir küme asla kendisinin tam üstkümesi (>) olamaz, 'y>y': False
Ancak bir küme daima kendisinin üstkümesi (>=)'dir, 'y.issuperset(y)': True
"""