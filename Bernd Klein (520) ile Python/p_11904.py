#coding:iso-8859-9 T�rk�e
# p_11904.py: �ablon.format(**locals()) ile lokal de�i�ken de�erlerinin bi�imli yazd�r�lmas� �rne�i.

from random import random, randint

a = randint (0, 10000) + random()
b = randint (-5000, 5000) + random()
def f(): return a%b
c= f()

print ("locals() yerel de�i�kenler s�zl�k i�eri�i==>\n", locals() )
print ("\n�stenilen de�erlerin d�k�m�:\na=", locals()["a"], "\nb=", locals()["b"], "\nf=", locals()["f"], "\nc=", locals()["c"] )

print ("\nFormat'l� d�k�m:\na={a:,.2f}\nb={b:,.2f}\nf={f}\nc={c:,.2f}" .format (**locals()) )


"""��kt�:
>python p_11904.py
locals() yerel de�i�kenler s�zl�k i�eri�i==>
 {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_
frozen_importlib_external.SourceFileLoader object at 0x003CDC10>, '__spec__':
None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__':
'p_11904.py', '__cached__': None, 'random': <built-in method random of Random
object at 0x00558298>, 'randint': <bound method Random.randint of <random.Random
object at 0x00558298>>, 'a': 8138.476597872549, 'b': -4141.95136819669,
'f': <function f at 0x00C17F18>, 'c': -145.42613852083105}

�stenilen de�erlerin d�k�m�:
a= 8138.476597872549
b= -4141.95136819669
f= <function f at 0x00C17F18>
c= -145.42613852083105

Format'l� d�k�m:
a=8,138.48
b=-4,141.95
f=<function f at 0x00C17F18>
c=-145.43
"""