# coding:iso-8859-9 Türkçe
# p_14501.py: Sınıfların sınıfadı, miras listesi ve özellikler sözlüğü tipli yaratılabilmesi örneği.

x = [4, 5, 9]
y = "Merhaba"

print (x, y)
print (type (x), type (y) )
print (type (list), type (str) )
print (type (type (x)), type (type (y)) ) # Bir üstekiyle aynıdır...
#--------------------------------------------------------------------------------------------------

class A: pass

print()
x = A()
print (x, type (x) )
#--------------------------------------------------------------------------------------------------

A = type ("A", (), {}) # type (sınıf, süpersınıf listesi/tüplesi, özellikler sözlüğü)
# "class A: pass" ile aynıdır...

print()
x = A()
print (x, type (x) )



"""Çıktı.
>python p_14501.py
[4, 5, 9] Merhaba
<class 'list'> <class 'str'>
<class 'type'> <class 'type'>
<class 'type'> <class 'type'>

<__main__.A object at 0x013F1A10> <class '__main__.A'>

<__main__.A object at 0x013F1950> <class '__main__.A'>
"""