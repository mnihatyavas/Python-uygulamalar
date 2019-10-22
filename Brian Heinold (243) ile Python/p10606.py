# coding:iso-8859-9 T�rk�e

s1 = "ABCDEFGHIJKLMNOPQRSTUVXWYZ"
print ("�ngiliz alfabesi:", s1)
print ("Tersten:", s1[::-1])
print ("Harf say�s�:", len(s1))

# Dizge de�i�tirilemez, fakat yeniden/de�i�ik yarat�l�r...
s2 = s1[:3] + "�" + s1[3:7] + "�" + s1[7:9] + "�" + s1[9:15] + "�"
s2 += s1[15] + s1[17:21] + "�" + s1[21] + s1[-2:]
print ("\nT�rk alfabesi:", end="")
for k in s2: print (k,end="")
print ("\nTersten:", end="")
for k in range (len(s2)-1, -1, -1): print (s2[k], end="")
print ("\nHarf say�s�:", len(s2))

��kt�="""
�ngiliz alfabesi: ABCDEFGHIJKLMNOPQRSTUVXWYZ
Tersten: ZYWXVUTSRQPONMLKJIHGFEDCBA
Harf say�s�: 26

T�rk alfabesi: ABC�DEFG�HI�JKLMNO�PRSTU�VYZ
Tersten: ZYV�UTSRP�ONMLKJ�IH�GFED�CBA
Harf say�s�: 28
"""