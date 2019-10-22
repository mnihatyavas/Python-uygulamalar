# coding:iso-8859-9 T�rk�e
# p_14801.py: Bir mod�l�n korunakl� �a�r�lamaz ve genel �a�r�labilir vas�flar�n�n listelenmesi �rne�i.

import random

s�n�fAd� = "random"
�zellikler = [x for x in dir (eval (s�n�fAd�)) if not x.startswith ("__")]
print ("�zellikler listesi:\n", �zellikler)

�a�r�lamaz�zellikler = [x for x in dir (eval (s�n�fAd�)) if not x.startswith ("__") and not callable (eval (s�n�fAd� + "." + x))]
print ("\n�a�r�lamaz �zellikler listesi:\n", �a�r�lamaz�zellikler)

metodlar = [x for x in dir (eval (s�n�fAd�)) if not x.startswith ("__") and callable (eval (s�n�fAd� + "." + x))]
print ("\n�a�r�labilir metodlar listesi:\n", metodlar)



"""��kt�:
>python p_14801.py
�zellikler listesi:
 ['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST',
'SystemRandom', 'TWOPI', '_BuiltinMethodType', '_MethodType', '_Sequence', '_Set',
'_acos', '_bisect', '_ceil', '_cos', '_e', '_exp', '_inst', '_itertools', '_log', '
_os', '_pi', '_random', '_sha512', '_sin', '_sqrt', '_test', '_test_generator',
'_urandom', '_warn', 'betavariate', 'choice', 'choices', 'expovariate', 'gammavariate',
'gauss', 'getrandbits', 'getstate', 'lognormvariate', 'normalvariate', 'paretovariate',
'randint', 'random', 'randrange', 'sample', 'seed', 'setstate','shuffle', 'triangular', 'uniform',
'vonmisesvariate', 'weibullvariate']

�a�r�lamaz �zellikler listesi:
 ['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'SG_MAGICCONST', 'TWOPI',
'_bisect', '_e', '_inst', '_itertools', '_os', '_pi', '_random']

�a�r�labilir metodlar listesi:
 ['Random', 'SystemRandom', '_BuiltinMethodType', '_MethodType', '_Sequence',
'_Set', '_acos', '_ceil', '_cos', '_exp', '_log', '_sha512', '_sin', '_sqrt', '_test',
'_test_generator', '_urandom', '_warn', 'betavariate', 'choice', 'choices',
 'expovariate', 'gammavariate', 'gauss', 'getrandbits', 'getstate', 'lognormvariate',
'normalvariate', 'paretovariate', 'randint', 'random', 'randrange', 'sample', 'seed',
'setstate', 'shuffle', 'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate']
"""