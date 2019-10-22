# coding:iso-8859-9 Türkçe
# Python3 - Strings

dizge1 = 'Merhaba, Dünya!'
dizge2 = "Python ile Programcılık Örnekleri"

print (dizge1 + "\n" + dizge2)
print ("dizge1[0]: ", dizge1[0])
print ("dizge2[1:5]: ", dizge2[1:5])
print ("Dizge güncelleme: ", dizge1[:7] + ' Python!')

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

print ("İsmim %s'dır ve kilom %d kg'dır!\n" % ('M.Nihat Yavaş', 58))

paragraf = """Bu, üçlü tek/çift tırnaklar içerisinde girilen
çok satırlı bir dizge olup, bazı esc/kaç
karakterlerini de içinde barındırmaktadır.
Bu özel karakterler yansımayıp, sadece etkisi görünecektir.
Örneğin TAB/KERTİK (\t) veya NEWLINE/YENİSATIR [ \n ]
ekranda sonucu itibarıyla etkili olacaktır.
"""
print (paragraf)
print()

print ('C:\\hiçbiryer')
print (r'C:\\hiçbiryer')