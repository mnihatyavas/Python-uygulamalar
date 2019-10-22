# coding:iso-8859-9
# p_13707.py: S�n�f nesnesinin �zelle�tirilebilen str ve repr haz�r dizge ar�iv metodlar� �rne�i.

print ("str() ve repr-esent() ar�iv fonksiyonlar�, veriyi dizgeye �evirir.")
print()
liste = ["Python", "Java", "C++", "Perl", "JS"]
print (liste, type (liste))
print (str (liste), type (str (liste)) )
print (repr (liste), type (repr (liste)) )
print()
s�zl�k = {"a":3497, "b":8011, "c":8300, "�":1245}
print (s�zl�k, type (s�zl�k) )
print (str (s�zl�k), type (str (s�zl�k)) )
print (repr (s�zl�k), type (repr (s�zl�k)) )
print()
x = 587.78
print (x, type (x) )
print (str (x), type (str (x)) )
print (repr (x), type (repr (x)) )
print ("-"*75, "\n", sep="")
#--------------------------------------------------------------------------------------------------

print ("S�n�f __str__ veya __repr__ metodlar� i�ermiyorsa, ar�ivler kullan�l�r.")
class A: pass

a = A()
print (a, type (A) )
print (str (a), type (str (A)) )
print (repr (a), type (repr (A)) )
print ("-"*75, "\n", sep="")
#--------------------------------------------------------------------------------------------------

class A:
    def __str__ (self): return "41"
    def __repr__ (self): return "42"

a = A()
print (a, type (A), "Otomatikmen __str__, ancak kendi tiplemesiyle kullan�ld�.")
print (str (a), type (str (A)), "Mevcut __str__ ve tipi kullan�ld�.")
print (repr (a), type (repr (A)), "Mevcut __repr__ ve str tipi kullan�ld�." )

"""��kt�:
>python p_13707.py
str() ve repr-esent() ar�iv fonksiyonlar�, veriyi dizgeye �evirir.

['Python', 'Java', 'C++', 'Perl', 'JS'] <class 'list'>
['Python', 'Java', 'C++', 'Perl', 'JS'] <class 'str'>
['Python', 'Java', 'C++', 'Perl', 'JS'] <class 'str'>

{'a': 3497, 'b': 8011, 'c': 8300, '�': 1245} <class 'dict'>
{'a': 3497, 'b': 8011, 'c': 8300, '�': 1245} <class 'str'>
{'a': 3497, 'b': 8011, 'c': 8300, '�': 1245} <class 'str'>

587.78 <class 'float'>
587.78 <class 'str'>
587.78 <class 'str'>
---------------------------------------------------------------------------

S�n�f __str__ veya __repr__ metodlar� i�ermiyorsa, ar�ivler kullan�l�r.
<__main__.A object at 0x01331D10> <class 'type'>
<__main__.A object at 0x01331D10> <class 'str'>
<__main__.A object at 0x01331D10> <class 'str'>
---------------------------------------------------------------------------

41 <class 'type'> Otomatikmen __str__, ancak kendi tiplemesiyle kullan�ld�.
41 <class 'str'> Mevcut __str__ ve tipi kullan�ld�.
42 <class 'str'> Mevcut __repr__ ve str tipi kullan�ld�.
"""