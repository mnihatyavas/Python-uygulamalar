# coding:iso-8859-9 Türkçe

s = 'M.Nihat Yavaş'

for i in range (len(s)): print (s[i], end=" ")
print()
for i in range (len(s)-1, -1, -1): print (s[i], end=" ")
print()
for i in range (len(s)-1, -len(s)-1, -1): print (s[i], end="-")

""" + endeks taşması hata verir; ancak - endeks taşması
     dizgeyi tamamen bir kez tarar, 2.ciye hata verir!
for i in range (len(s)+1): print (s[i], end="+")
print()
for i in range (len(s)-1, -len(s)*2-2, -1): print (s[i], end="-")
"""