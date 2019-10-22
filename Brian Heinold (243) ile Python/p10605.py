# coding:iso-8859-9 Türkçe

s = "abcçdefgğhıijklmnoöprsştuüvyz"
print ("Alfabemiz:", s)
print ("s[2:5] =", s[2:5])
print ("s[:5] =", s[:5])
print ("s[2:] =", s[2:])
print ("s[:] =", s[:])
print ("s[-3:] =", s[-3:])
print ("s[1::3]:", s[1::3])
print ("s[::-1]:", s[::-1])

Çıktı="""
Alfabemiz: abcçdefgğhıijklmnoöprsştuüvyz
s[2:5] = cçd
s[:5] = abcçd
s[2:] = cçdefgğhıijklmnoöprsştuüvyz
s[:] = abcçdefgğhıijklmnoöprsştuüvyz
s[-2:] = vyz
s[1:len(s):3]: bdgıknpşüz
s[::-1]: zyvüutşsrpöonmlkjiıhğgfedçcba
"""