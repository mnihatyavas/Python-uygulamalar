#coding:iso-8859-9 Türkçe
# p_11904.py: şablon.format(**locals()) ile lokal değişken değerlerinin biçimli yazdırılması örneği.

from random import random, randint

a = randint (0, 10000) + random()
b = randint (-5000, 5000) + random()
def f(): return a%b
c= f()

print ("locals() yerel değişkenler sözlük içeriği==>\n", locals() )
print ("\nİstenilen değerlerin dökümü:\na=", locals()["a"], "\nb=", locals()["b"], "\nf=", locals()["f"], "\nc=", locals()["c"] )

print ("\nFormat'lı döküm:\na={a:,.2f}\nb={b:,.2f}\nf={f}\nc={c:,.2f}" .format (**locals()) )


"""Çıktı:
>python p_11904.py
locals() yerel değişkenler sözlük içeriği==>
 {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_
frozen_importlib_external.SourceFileLoader object at 0x003CDC10>, '__spec__':
None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__':
'p_11904.py', '__cached__': None, 'random': <built-in method random of Random
object at 0x00558298>, 'randint': <bound method Random.randint of <random.Random
object at 0x00558298>>, 'a': 8138.476597872549, 'b': -4141.95136819669,
'f': <function f at 0x00C17F18>, 'c': -145.42613852083105}

İstenilen değerlerin dökümü:
a= 8138.476597872549
b= -4141.95136819669
f= <function f at 0x00C17F18>
c= -145.42613852083105

Format'lı döküm:
a=8,138.48
b=-4,141.95
f=<function f at 0x00C17F18>
c=-145.43
"""