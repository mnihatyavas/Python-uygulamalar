# coding:iso-8859-9 T�rk�e

from itertools import *

print ("[1] liste'sinin permutations/�e�itlemesi:", list (permutations ([1])), "\n�e�it say�s�:", len (list (permutations ([1]))) )
print ("\n[1,2] liste'sinin permutations/�e�itlemesi:", list (permutations ([1,2])), "\n�e�it say�s�:", len (list (permutations ([1,2]))) )
print ("\n[1,2,3] liste'sinin permutations/�e�itlemesi:", list (permutations ([1,2,3])), "\n�e�it say�s�:", len (list (permutations ([1,2,3]))) )
print ("\n[1,2,3,4] liste'sinin permutations/�e�itlemesi:", list (permutations ([1,2,3,4])), "\n�e�it say�s�:", len (list (permutations ([1,2,3,4]))) )

L = [''.join(p) for p in permutations('123')]
print ("\n'123' dizge'sinin �e�itlemesi:", L, "\n�e�it say�s�:", len (L) )

L = [''.join(p) for p in permutations('12345')]
print ("\n'12345' dizge'sinin �e�itlemesi:", L, "\n�e�it say�s�:", len (L) )

L = [''.join(p) for p in permutations('12345', 4)]
print ("\n'12345' dizge'sinin 4'l� �e�itlemesi:", L, "\n�e�it say�s�:", len (L) )

L = [''.join(p) for p in permutations('12345', 3)]
print ("\n'12345' dizge'sinin 3'l� �e�itlemesi:", L, "\n�e�it say�s�:", len (L) )

L = [''.join(p) for p in permutations('12345', 2)]
print ("\n'12345' dizge'sinin 2'li �e�itlemesi:", L, "\n�e�it say�s�:", len (L) )

L = [''.join(p) for p in permutations('12345', 1)]
print ("\n'12345' dizge'sinin 1'li �e�itlemesi:", L, "\n�e�it say�s�:", len (L) )

L = [''.join(p) for p in permutations('12345', 0)]
print ("\n'12345' dizge'sinin 0'l� �e�itlemesi:", L, "\n�e�it say�s�:", len (L) )
#------------------------------------------------------------------------------------------

print ("-"*75)
L = [''.join(b) for b in combinations("12345", 5)]
print ("\n('12345',5) dizge'sinin combinations/bile�imi:", L, "\nBile�im say�s�:", len (L) )

L = [''.join(b) for b in combinations("12345", 4)]
print ("\n('12345',4) dizge'sinin combinations/bile�imi:", L, "\nBile�im say�s�:", len (L) )

L = [''.join(b) for b in combinations("12345", 3)]
print ("\n('12345',3) dizge'sinin combinations/bile�imi:", L, "\nBile�im say�s�:", len (L) )

L = [''.join(b) for b in combinations("12345", 2)]
print ("\n('12345',2) dizge'sinin combinations/bile�imi:", L, "\nBile�im say�s�:", len (L) )

L = [''.join(b) for b in combinations("12345", 1)]
print ("\n('12345',1) dizge'sinin combinations/bile�imi:", L, "\nBile�im say�s�:", len (L) )

L = [''.join(b) for b in combinations("12345", 0)]
print ("\n('12345',0) dizge'sinin combinations/bile�imi:", L, "\nBile�im say�s�:", len (L) )

L = [''.join(b) for b in combinations_with_replacement("12345", 2)]
print ("\n('12345',2) dizge'sinin combinations_with_replacement/yerde�i�tirmeli_bile�imi:", L, "\nBile�im say�s�:", len (L) )
