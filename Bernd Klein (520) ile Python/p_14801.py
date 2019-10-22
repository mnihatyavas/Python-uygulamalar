# coding:iso-8859-9 Türkçe
# p_14801.py: Bir modülün korunaklı çağrılamaz ve genel çağrılabilir vasıflarının listelenmesi örneği.

import random

sınıfAdı = "random"
özellikler = [x for x in dir (eval (sınıfAdı)) if not x.startswith ("__")]
print ("Özellikler listesi:\n", özellikler)

çağrılamazÖzellikler = [x for x in dir (eval (sınıfAdı)) if not x.startswith ("__") and not callable (eval (sınıfAdı + "." + x))]
print ("\nÇağrılamaz özellikler listesi:\n", çağrılamazÖzellikler)

metodlar = [x for x in dir (eval (sınıfAdı)) if not x.startswith ("__") and callable (eval (sınıfAdı + "." + x))]
print ("\nÇağrılabilir metodlar listesi:\n", metodlar)



"""Çıktı:
>python p_14801.py
Özellikler listesi:
 ['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST',
'SystemRandom', 'TWOPI', '_BuiltinMethodType', '_MethodType', '_Sequence', '_Set',
'_acos', '_bisect', '_ceil', '_cos', '_e', '_exp', '_inst', '_itertools', '_log', '
_os', '_pi', '_random', '_sha512', '_sin', '_sqrt', '_test', '_test_generator',
'_urandom', '_warn', 'betavariate', 'choice', 'choices', 'expovariate', 'gammavariate',
'gauss', 'getrandbits', 'getstate', 'lognormvariate', 'normalvariate', 'paretovariate',
'randint', 'random', 'randrange', 'sample', 'seed', 'setstate','shuffle', 'triangular', 'uniform',
'vonmisesvariate', 'weibullvariate']

Çağrılamaz özellikler listesi:
 ['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'SG_MAGICCONST', 'TWOPI',
'_bisect', '_e', '_inst', '_itertools', '_os', '_pi', '_random']

Çağrılabilir metodlar listesi:
 ['Random', 'SystemRandom', '_BuiltinMethodType', '_MethodType', '_Sequence',
'_Set', '_acos', '_ceil', '_cos', '_exp', '_log', '_sha512', '_sin', '_sqrt', '_test',
'_test_generator', '_urandom', '_warn', 'betavariate', 'choice', 'choices',
 'expovariate', 'gammavariate', 'gauss', 'getrandbits', 'getstate', 'lognormvariate',
'normalvariate', 'paretovariate', 'randint', 'random', 'randrange', 'sample', 'seed',
'setstate', 'shuffle', 'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate']
"""