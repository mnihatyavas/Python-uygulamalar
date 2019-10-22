# coding:iso-8859-9 T�rk�e
# p_14501.py: S�n�flar�n s�n�fad�, miras listesi ve �zellikler s�zl��� tipli yarat�labilmesi �rne�i.

x = [4, 5, 9]
y = "Merhaba"

print (x, y)
print (type (x), type (y) )
print (type (list), type (str) )
print (type (type (x)), type (type (y)) ) # Bir �stekiyle ayn�d�r...
#--------------------------------------------------------------------------------------------------

class A: pass

print()
x = A()
print (x, type (x) )
#--------------------------------------------------------------------------------------------------

A = type ("A", (), {}) # type (s�n�f, s�pers�n�f listesi/t�plesi, �zellikler s�zl���)
# "class A: pass" ile ayn�d�r...

print()
x = A()
print (x, type (x) )



"""��kt�.
>python p_14501.py
[4, 5, 9] Merhaba
<class 'list'> <class 'str'>
<class 'type'> <class 'type'>
<class 'type'> <class 'type'>

<__main__.A object at 0x013F1A10> <class '__main__.A'>

<__main__.A object at 0x013F1950> <class '__main__.A'>
"""