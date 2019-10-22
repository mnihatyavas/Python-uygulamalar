# coding:iso-8859-9 T�rk�e
# p_10901.py: =atama, =[:]atama ve =deepcopy[:]atama'lardaki id bellek adresi durumlar� �rne�i.

x = 3
y = x
print ("x = y, id(x) = id(y):", x, y, id(x), id(y) )

x = 4
print ("x != y, id(x) != id(y):", x, y, id(x), id(y) )

y = 4
print ("x = y, id(x) =  id(y):", x, y, id(x), id(y) )
# tamsay�l� y=x iken haf�za adresleri de ayn�, ama x ve y de�eri
# de�i�ince adresi de de�i�mek zorunda kald�...
#-------------------------------------------------------------------------------------------

renk1 = ["k�rm�z�", "mavi"]
renk2 = renk1
print ("\nrenk1 = renk2, id(renk1) = id(renk2):", renk1, renk2, id (renk1), id (renk2) )

renk1 = ["al", "ye�il"]
print ("renk1 != renk2, id(renk1) != id(renk2):", renk1, renk2, id (renk1), id (renk2) )

renk2 = ["al", "ye�il"]
print ("renk1 = renk2, id(renk1) != id(renk2):", renk1, renk2, id (renk1), id (renk2) )
# �lkinde ayn�yken, 2.kez renk2 = renk1 olsa da adresleri farkl�la�t�...
#-------------------------------------------------------------------------------------------

renk1 = ["k�rm�z�", "mavi"]
renk2 = renk1
print ("\nrenk1 = renk2, id(renk1) = id(renk2):", renk1, renk2, id (renk1), id (renk2) )

renk2[1] = "ye�il"
print ("renk1 = renk2, id(renk1) = id(renk2):", renk1, renk2, id (renk1), id(renk2) )
# renk2'ye yeni de�er atanmad�, sadece renk2[1] yerinde-i�erik de�i�tirildi,
# ama her iki rengin de adresleri ayn� kald�...
#-------------------------------------------------------------------------------------------

L1 = ['a','b','c','d']
L2 = L1[:] # Dilim [:] operat�rl� kopyalama, ba�tan ayr� adresler yarat�r...
print ("\nL1 = L2, id(L1) != id(L2):", L1, L2, id (L1), id (L2) )

L2[0] = 'x'
print ("L1 != L2, id(L1) != id(L2):", L1, L2, id (L1), id (L2) )
#-------------------------------------------------------------------------------------------

L1 = ['a','b',['ab','ba']]
L2 = L1[:]
print ("\nL1 = L2, id(L1) != id(L2):", L1, L2, id (L1), id (L2) )

L2[1] = 'c'
print ("L1 != L2, id(L1) != id(L2):", L1, L2, id (L1), id (L2) )

L2[2][0] = 'ac'
print ("L1 != L2, id(L1) != id(L2):", L1, L2, id (L1), id (L2) )
# Hata: L2[2][0] de�i�ikli�i, ayr� adresler olmas�na ra�men L1[2][0] da
# de�i�ti. ��z�m�, copy mod�l�n�n deepcopy fonksiyonu'dur...
#-------------------------------------------------------------------------------------------

from copy import deepcopy

L1 = ['a','b',['ab','ba']]
L2 = deepcopy (L1[:])
print ("\nL1 = L2, id(L1) != id(L2):", L1, L2, id (L1), id (L2) )

L2[2][0] = 'ac'
print ("L1 != L2, id(L1) != id(L2):", L1, L2, id (L1), id (L2) )


"""��kt�:
>python p_10901.py
x = y, id(x) = id(y): 3 3 1627666720 1627666720
x != y, id(x) != id(y): 4 3 1627666736 1627666720
x = y, id(x) =  id(y): 4 4 1627666736 1627666736

renk1 = renk2, id(renk1) = id(renk2): ['k�rm�z�', 'mavi'] ['k�rm�z�', 'mavi'] 3884456 3884456
renk1 != renk2, id(renk1) != id(renk2): ['al', 'ye�il'] ['k�rm�z�', 'mavi'] 3885616 3884456
renk1 = renk2, id(renk1) != id(renk2): ['al', 'ye�il'] ['al', 'ye�il'] 3885616 4244784

renk1 = renk2, id(renk1) = id(renk2): ['k�rm�z�', 'mavi'] ['k�rm�z�', 'mavi'] 3884456 3884456
renk1 = renk2, id(renk1) = id(renk2): ['k�rm�z�', 'ye�il'] ['k�rm�z�', 'ye�il']3884456 3884456

L1 = L2, id(L1) != id(L2): ['a', 'b', 'c', 'd'] ['a', 'b', 'c', 'd'] 4244784 3885616
L1 != L2, id(L1) != id(L2): ['a', 'b', 'c', 'd'] ['x', 'b', 'c', 'd'] 4244784 3885616

L1 = L2, id(L1) != id(L2): ['a', 'b', ['ab', 'ba']] ['a', 'b', ['ab', 'ba']] 24784408 4244784
L1 != L2, id(L1) != id(L2): ['a', 'b', ['ab', 'ba']] ['a', 'c', ['ab', 'ba']] 24784408 4244784
L1 != L2, id(L1) != id(L2): ['a', 'b', ['ac', 'ba']] ['a', 'c', ['ac', 'ba']] 24784408 4244784

L1 = L2, id(L1) != id(L2): ['a', 'b', ['ab', 'ba']] ['a', 'b', ['ab', 'ba']] 24837976 24783928
L1 != L2, id(L1) != id(L2): ['a', 'b', ['ab', 'ba']] ['a', 'b', ['ac', 'ba']] 24837976 24783928

"""