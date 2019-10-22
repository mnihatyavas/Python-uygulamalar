# coding:iso-8859-9
# p_13707.py: Sınıf nesnesinin özelleştirilebilen str ve repr hazır dizge arşiv metodları örneği.

print ("str() ve repr-esent() arşiv fonksiyonları, veriyi dizgeye çevirir.")
print()
liste = ["Python", "Java", "C++", "Perl", "JS"]
print (liste, type (liste))
print (str (liste), type (str (liste)) )
print (repr (liste), type (repr (liste)) )
print()
sözlük = {"a":3497, "b":8011, "c":8300, "ç":1245}
print (sözlük, type (sözlük) )
print (str (sözlük), type (str (sözlük)) )
print (repr (sözlük), type (repr (sözlük)) )
print()
x = 587.78
print (x, type (x) )
print (str (x), type (str (x)) )
print (repr (x), type (repr (x)) )
print ("-"*75, "\n", sep="")
#--------------------------------------------------------------------------------------------------

print ("Sınıf __str__ veya __repr__ metodları içermiyorsa, arşivler kullanılır.")
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
print (a, type (A), "Otomatikmen __str__, ancak kendi tiplemesiyle kullanıldı.")
print (str (a), type (str (A)), "Mevcut __str__ ve tipi kullanıldı.")
print (repr (a), type (repr (A)), "Mevcut __repr__ ve str tipi kullanıldı." )

"""Çıktı:
>python p_13707.py
str() ve repr-esent() arşiv fonksiyonları, veriyi dizgeye çevirir.

['Python', 'Java', 'C++', 'Perl', 'JS'] <class 'list'>
['Python', 'Java', 'C++', 'Perl', 'JS'] <class 'str'>
['Python', 'Java', 'C++', 'Perl', 'JS'] <class 'str'>

{'a': 3497, 'b': 8011, 'c': 8300, 'ç': 1245} <class 'dict'>
{'a': 3497, 'b': 8011, 'c': 8300, 'ç': 1245} <class 'str'>
{'a': 3497, 'b': 8011, 'c': 8300, 'ç': 1245} <class 'str'>

587.78 <class 'float'>
587.78 <class 'str'>
587.78 <class 'str'>
---------------------------------------------------------------------------

Sınıf __str__ veya __repr__ metodları içermiyorsa, arşivler kullanılır.
<__main__.A object at 0x01331D10> <class 'type'>
<__main__.A object at 0x01331D10> <class 'str'>
<__main__.A object at 0x01331D10> <class 'str'>
---------------------------------------------------------------------------

41 <class 'type'> Otomatikmen __str__, ancak kendi tiplemesiyle kullanıldı.
41 <class 'str'> Mevcut __str__ ve tipi kullanıldı.
42 <class 'str'> Mevcut __repr__ ve str tipi kullanıldı.
"""