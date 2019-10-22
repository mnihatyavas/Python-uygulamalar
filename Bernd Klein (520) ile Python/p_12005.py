# coding:iso-8859-9 T�rk�e
# p_12005.py: Fonksiyonlarda lokal, genel ve global de�i�kenler �rne�i.

def f():
    # Aksi bir ifade yoksa, genel "s", lokal olarak kullan�l�r...
    print (s)

s = "Python"
f()
#---------------------------------------------------------------------------------------------------

def f():
    # Ayr�ca lokal "s" tan�mlan�nca, �ncelik lokaldedir...
    s = "JavaScript"
    print (s)

print()
s = "Python"
f()
print (s)
#---------------------------------------------------------------------------------------------------
"""
def f():
    # Program "s"in lokal mi genel mi oldu�una karar veremez, UnboundLocalError derleme hatas� verir...
    print (s)
    s = "JavaScript"
    print (s)

print()
s = "Python"
f()
print (s)
"""
#---------------------------------------------------------------------------------------------------

def f():
    global s
    # Art�k "s" global'dir, fonksiyondaki de d��ardaki de ayn�d�r...
    print (s)
    s = "JavaScript"
    print (s)

print()
s = "Python" 
f()
print (s)


"""��kt�:
>python p_12005.py
Python

JavaScript
Python

Python
JavaScript
JavaScript
"""