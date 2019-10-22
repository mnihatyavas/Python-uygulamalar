# coding:iso-8859-9 Türkçe
# Python3 - Tuples

tüple1 = ('Fizik', 'Kimya', 1997, 2000)
tüple2 = (3, 1, 5, 2, 4 )
tüple3 = "a", "b", "c", "d"
tüple4 = ()
tüple5 = (63,)

print ("tüple1[0]:", tüple1[0])
print ("tüple2[1:3]", tüple2[1:3])
print (tüple2 + tüple3)
print (len (tüple2 + tüple3))
print (tüple3 * 2)
print (tüple4)
print (tüple5)

del tüple4
# print (tüple4) ==> Hata: silinen yazdırılamaz...
# NameError: name 'tüple4' is not defined

print ("tüple1[-3]:", tüple1[-3]) # Sondan geriye 3.eleman
for x in tüple2: print (x, end=" ")
