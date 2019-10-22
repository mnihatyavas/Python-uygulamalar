# coding:iso-8859-9 Türkçe
# p_10901.py: =atama, =[:]atama ve =deepcopy[:]atama'lardaki id bellek adresi durumları örneği.

x = 3
y = x
print ("x = y, id(x) = id(y):", x, y, id(x), id(y) )

x = 4
print ("x != y, id(x) != id(y):", x, y, id(x), id(y) )

y = 4
print ("x = y, id(x) =  id(y):", x, y, id(x), id(y) )
# tamsayılı y=x iken hafıza adresleri de aynı, ama x ve y değeri
# değişince adresi de değişmek zorunda kaldı...
#-------------------------------------------------------------------------------------------

renk1 = ["kırmızı", "mavi"]
renk2 = renk1
print ("\nrenk1 = renk2, id(renk1) = id(renk2):", renk1, renk2, id (renk1), id (renk2) )

renk1 = ["al", "yeşil"]
print ("renk1 != renk2, id(renk1) != id(renk2):", renk1, renk2, id (renk1), id (renk2) )

renk2 = ["al", "yeşil"]
print ("renk1 = renk2, id(renk1) != id(renk2):", renk1, renk2, id (renk1), id (renk2) )
# İlkinde aynıyken, 2.kez renk2 = renk1 olsa da adresleri farklılaştı...
#-------------------------------------------------------------------------------------------

renk1 = ["kırmızı", "mavi"]
renk2 = renk1
print ("\nrenk1 = renk2, id(renk1) = id(renk2):", renk1, renk2, id (renk1), id (renk2) )

renk2[1] = "yeşil"
print ("renk1 = renk2, id(renk1) = id(renk2):", renk1, renk2, id (renk1), id(renk2) )
# renk2'ye yeni değer atanmadı, sadece renk2[1] yerinde-içerik değiştirildi,
# ama her iki rengin de adresleri aynı kaldı...
#-------------------------------------------------------------------------------------------

L1 = ['a','b','c','d']
L2 = L1[:] # Dilim [:] operatörlü kopyalama, baştan ayrı adresler yaratır...
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
# Hata: L2[2][0] değişikliği, ayrı adresler olmasına rağmen L1[2][0] da
# değişti. Çözümü, copy modülünün deepcopy fonksiyonu'dur...
#-------------------------------------------------------------------------------------------

from copy import deepcopy

L1 = ['a','b',['ab','ba']]
L2 = deepcopy (L1[:])
print ("\nL1 = L2, id(L1) != id(L2):", L1, L2, id (L1), id (L2) )

L2[2][0] = 'ac'
print ("L1 != L2, id(L1) != id(L2):", L1, L2, id (L1), id (L2) )


"""Çıktı:
>python p_10901.py
x = y, id(x) = id(y): 3 3 1627666720 1627666720
x != y, id(x) != id(y): 4 3 1627666736 1627666720
x = y, id(x) =  id(y): 4 4 1627666736 1627666736

renk1 = renk2, id(renk1) = id(renk2): ['kırmızı', 'mavi'] ['kırmızı', 'mavi'] 3884456 3884456
renk1 != renk2, id(renk1) != id(renk2): ['al', 'yeşil'] ['kırmızı', 'mavi'] 3885616 3884456
renk1 = renk2, id(renk1) != id(renk2): ['al', 'yeşil'] ['al', 'yeşil'] 3885616 4244784

renk1 = renk2, id(renk1) = id(renk2): ['kırmızı', 'mavi'] ['kırmızı', 'mavi'] 3884456 3884456
renk1 = renk2, id(renk1) = id(renk2): ['kırmızı', 'yeşil'] ['kırmızı', 'yeşil']3884456 3884456

L1 = L2, id(L1) != id(L2): ['a', 'b', 'c', 'd'] ['a', 'b', 'c', 'd'] 4244784 3885616
L1 != L2, id(L1) != id(L2): ['a', 'b', 'c', 'd'] ['x', 'b', 'c', 'd'] 4244784 3885616

L1 = L2, id(L1) != id(L2): ['a', 'b', ['ab', 'ba']] ['a', 'b', ['ab', 'ba']] 24784408 4244784
L1 != L2, id(L1) != id(L2): ['a', 'b', ['ab', 'ba']] ['a', 'c', ['ab', 'ba']] 24784408 4244784
L1 != L2, id(L1) != id(L2): ['a', 'b', ['ac', 'ba']] ['a', 'c', ['ac', 'ba']] 24784408 4244784

L1 = L2, id(L1) != id(L2): ['a', 'b', ['ab', 'ba']] ['a', 'b', ['ab', 'ba']] 24837976 24783928
L1 != L2, id(L1) != id(L2): ['a', 'b', ['ab', 'ba']] ['a', 'b', ['ac', 'ba']] 24837976 24783928

"""