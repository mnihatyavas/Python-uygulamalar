# coding:iso-8859-9 Türkçe
# p_12005.py: Fonksiyonlarda lokal, genel ve global değişkenler örneği.

def f():
    # Aksi bir ifade yoksa, genel "s", lokal olarak kullanılır...
    print (s)

s = "Python"
f()
#---------------------------------------------------------------------------------------------------

def f():
    # Ayrıca lokal "s" tanımlanınca, öncelik lokaldedir...
    s = "JavaScript"
    print (s)

print()
s = "Python"
f()
print (s)
#---------------------------------------------------------------------------------------------------
"""
def f():
    # Program "s"in lokal mi genel mi olduğuna karar veremez, UnboundLocalError derleme hatası verir...
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
    # Artık "s" global'dir, fonksiyondaki de dışardaki de aynıdır...
    print (s)
    s = "JavaScript"
    print (s)

print()
s = "Python" 
f()
print (s)


"""Çıktı:
>python p_12005.py
Python

JavaScript
Python

Python
JavaScript
JavaScript
"""