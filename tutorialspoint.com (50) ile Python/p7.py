# coding:iso-8859-9 T�rk�e
# Python3 - Strings

dizge1 = 'Merhaba, D�nya!'
dizge2 = "Python ile Programc�l�k �rnekleri"

print (dizge1 + "\n" + dizge2)
print ("dizge1[0]: ", dizge1[0])
print ("dizge2[1:5]: ", dizge2[1:5])
print ("Dizge g�ncelleme: ", dizge1[:7] + ' Python!')

del dizge1, dizge2
a = 'Selam'
b = "Python"

print (a+b)
print (a*3)
print (a[0])
print (a[1:4])
print ("S" in a)
print ("M" not in a)
print (r'\n')
print (R"\r")

print ("�smim %s'd�r ve kilom %d kg'd�r!\n" % ('M.Nihat Yava�', 58))

paragraf = """Bu, ��l� tek/�ift t�rnaklar i�erisinde girilen
�ok sat�rl� bir dizge olup, baz� esc/ka�
karakterlerini de i�inde bar�nd�rmaktad�r.
Bu �zel karakterler yans�may�p, sadece etkisi g�r�necektir.
�rne�in TAB/KERT�K (\t) veya NEWLINE/YEN�SATIR [ \n ]
ekranda sonucu itibar�yla etkili olacakt�r.
"""
print (paragraf)
print()

print ('C:\\hi�biryer')
print (r'C:\\hi�biryer')