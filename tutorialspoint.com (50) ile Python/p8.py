# coding:iso-8859-9 Türkçe
# Python3 - Lists

liste1 = ['fizik', 'kimya', 1997, 2000];
liste2 = [1, 5, 2, 4, 3 ];
liste3 = ["a", "b", "c", "d"];

print ("liste1[0]:", liste1[0])
print ("liste2[1:4]:", liste2[1:4])
print ("liste3:", liste3)
print ("liste3[2:]:", liste3[2:])

liste1[2] = 2018
del liste1[1]
liste1.append ("matematik")
print ("liste1:", liste1)
print ("len(liste1):", len (liste1))
print ("liste1 * 3:", liste1 * 3)
print ("liste1 + liste3:", liste1 + liste3)
print ("2018 in liste1:", 2018 in liste1)

for x in liste1: print (x, end=" ")
print()
print (max (liste2))
print (min (liste3))

liste1.append (2018)
print (liste1.count (2018))
print (liste1.index (2018))

liste1.insert (1, "kimya")
print ("liste1:", liste1)

liste1.reverse()
print ("liste1:", liste1)

liste2.sort()
print ("liste2:", liste2)
