# coding:iso-8859-9 Türkçe

from itertools import *

print ("[1] liste'sinin permutations/çeşitlemesi:", list (permutations ([1])), "\nÇeşit sayısı:", len (list (permutations ([1]))) )
print ("\n[1,2] liste'sinin permutations/çeşitlemesi:", list (permutations ([1,2])), "\nÇeşit sayısı:", len (list (permutations ([1,2]))) )
print ("\n[1,2,3] liste'sinin permutations/çeşitlemesi:", list (permutations ([1,2,3])), "\nÇeşit sayısı:", len (list (permutations ([1,2,3]))) )
print ("\n[1,2,3,4] liste'sinin permutations/çeşitlemesi:", list (permutations ([1,2,3,4])), "\nÇeşit sayısı:", len (list (permutations ([1,2,3,4]))) )

L = [''.join(p) for p in permutations('123')]
print ("\n'123' dizge'sinin çeşitlemesi:", L, "\nÇeşit sayısı:", len (L) )

L = [''.join(p) for p in permutations('12345')]
print ("\n'12345' dizge'sinin çeşitlemesi:", L, "\nÇeşit sayısı:", len (L) )

L = [''.join(p) for p in permutations('12345', 4)]
print ("\n'12345' dizge'sinin 4'lü çeşitlemesi:", L, "\nÇeşit sayısı:", len (L) )

L = [''.join(p) for p in permutations('12345', 3)]
print ("\n'12345' dizge'sinin 3'lü çeşitlemesi:", L, "\nÇeşit sayısı:", len (L) )

L = [''.join(p) for p in permutations('12345', 2)]
print ("\n'12345' dizge'sinin 2'li çeşitlemesi:", L, "\nÇeşit sayısı:", len (L) )

L = [''.join(p) for p in permutations('12345', 1)]
print ("\n'12345' dizge'sinin 1'li çeşitlemesi:", L, "\nÇeşit sayısı:", len (L) )

L = [''.join(p) for p in permutations('12345', 0)]
print ("\n'12345' dizge'sinin 0'lı çeşitlemesi:", L, "\nÇeşit sayısı:", len (L) )
#------------------------------------------------------------------------------------------

print ("-"*75)
L = [''.join(b) for b in combinations("12345", 5)]
print ("\n('12345',5) dizge'sinin combinations/bileşimi:", L, "\nBileşim sayısı:", len (L) )

L = [''.join(b) for b in combinations("12345", 4)]
print ("\n('12345',4) dizge'sinin combinations/bileşimi:", L, "\nBileşim sayısı:", len (L) )

L = [''.join(b) for b in combinations("12345", 3)]
print ("\n('12345',3) dizge'sinin combinations/bileşimi:", L, "\nBileşim sayısı:", len (L) )

L = [''.join(b) for b in combinations("12345", 2)]
print ("\n('12345',2) dizge'sinin combinations/bileşimi:", L, "\nBileşim sayısı:", len (L) )

L = [''.join(b) for b in combinations("12345", 1)]
print ("\n('12345',1) dizge'sinin combinations/bileşimi:", L, "\nBileşim sayısı:", len (L) )

L = [''.join(b) for b in combinations("12345", 0)]
print ("\n('12345',0) dizge'sinin combinations/bileşimi:", L, "\nBileşim sayısı:", len (L) )

L = [''.join(b) for b in combinations_with_replacement("12345", 2)]
print ("\n('12345',2) dizge'sinin combinations_with_replacement/yerdeğiştirmeli_bileşimi:", L, "\nBileşim sayısı:", len (L) )
