# coding:iso-8859-9 T�rk�e
# Python3 - Tuples

t�ple1 = ('Fizik', 'Kimya', 1997, 2000)
t�ple2 = (3, 1, 5, 2, 4 )
t�ple3 = "a", "b", "c", "d"
t�ple4 = ()
t�ple5 = (63,)

print ("t�ple1[0]:", t�ple1[0])
print ("t�ple2[1:3]", t�ple2[1:3])
print (t�ple2 + t�ple3)
print (len (t�ple2 + t�ple3))
print (t�ple3 * 2)
print (t�ple4)
print (t�ple5)

del t�ple4
# print (t�ple4) ==> Hata: silinen yazd�r�lamaz...
# NameError: name 't�ple4' is not defined

print ("t�ple1[-3]:", t�ple1[-3]) # Sondan geriye 3.eleman
for x in t�ple2: print (x, end=" ")
