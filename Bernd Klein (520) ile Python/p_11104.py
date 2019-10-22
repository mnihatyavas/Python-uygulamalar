# coding:iso-8859-9 T�rk�e
# p_11104.py: K�melerde birle�im, kesi�im, kesi�imsiz, altk�me ve �stk�me �rne�i.

x = {"a", "b", "c", "d", "e"}
y = {"c", "d", "e", "f", "g"}

print ("x: ", x, "\ny: ", y, "\nx.union(y): ", x.union (y), sep="")
print ("union=|, yani or/veya'l� 'x | y':", x|y)
#---------------------------------------------------------------------------------------------------

print ("\n'x.intersection(y)' arakesit k�mesi:", x.intersection (y) )
print ("intersection=&, yani and/ve'li'x&y':", x&y)
#---------------------------------------------------------------------------------------------------

x = {"a","b","c"}
y = {"c","d","e"}
print ("\nx: ", x, "\ny: ", y, "\nKesi�imsiz mi? 'x.isdisjoint(y)': ", x.isdisjoint (y), sep="")

z = {"d","e","f"}
print ("\nz: ", z, "\nKesi�imsiz mi? 'x.isdisjoint(z)': ", x.isdisjoint (z), sep="")
#---------------------------------------------------------------------------------------------------

x = {"a","b","c","d","e"}
y = {"c","d"}
print ("\nx: ", x, "\ny: ", y, "\n'y' altk�me (<=) mi? 'y.issubset(x)': ", y.issubset (x), "\n'x' altk�me mi? 'x.issubset(y): ", x.issubset (y), sep="")
print ("\n'y' tam altk�me (<) mi? 'y<x':", y < x)
print ("\nBir k�me asla kendisinin tam altk�mesi (<) olamaz, 'x<x':", x < x)
print ("Ancak bir k�me daima kendisinin altk�mesi (<=)'dir, 'x.issubset(x)':", x.issubset (x) )
#---------------------------------------------------------------------------------------------------

print ("\n'y' �stk�me (>=) mi? 'y.issuperset(x)': ", y.issuperset (x), "\n'x' �stk�me mi? 'x.issuperset(y): ", x.issuperset (y), sep="")
print ("\n'y' tam �stk�me (>) mi? 'x>y':", x > y)
print ("\nBir k�me asla kendisinin tam �stk�mesi (>) olamaz, 'y>y':", y > y)
print ("Ancak bir k�me daima kendisinin �stk�mesi (>=)'dir, 'y.issuperset(y)':", y.issuperset (y) )


"""��kt�:
>python p_11104.py
x: {'d', 'b', 'e', 'a', 'c'}
y: {'d', 'e', 'c', 'g', 'f'}
x.union(y): {'b', 'd', 'e', 'a', 'c', 'g', 'f'}
union=|, yani or/veya'l� 'x | y': {'b', 'd', 'e', 'a', 'c', 'g', 'f'}

'x.intersection(y)' arakesit k�mesi: {'e', 'c', 'd'}
intersection=&, yani and/ve'li'x&y': {'e', 'c', 'd'}

x: {'c', 'a', 'b'}
y: {'e', 'c', 'd'}
Kesi�imsiz mi? 'x.isdisjoint(y)': False

z: {'e', 'f', 'd'}
Kesi�imsiz mi? 'x.isdisjoint(z)': True

x: {'d', 'b', 'e', 'a', 'c'}
y: {'c', 'd'}
'y' altk�me (<=) mi? 'y.issubset(x)': True
'x' altk�me mi? 'x.issubset(y): False

'y' tam altk�me (<) mi? 'y<x': True

Bir k�me asla kendisinin tam altk�mesi (<) olamaz, 'x<x': False
Ancak bir k�me daima kendisinin altk�mesi (<=)'dir, 'x.issubset(x)': True

'y' �stk�me (>=) mi? 'y.issuperset(x)': False
'x' �stk�me mi? 'x.issuperset(y): True

'y' tam �stk�me (>) mi? 'x>y': True

Bir k�me asla kendisinin tam �stk�mesi (>) olamaz, 'y>y': False
Ancak bir k�me daima kendisinin �stk�mesi (>=)'dir, 'y.issuperset(y)': True
"""