# coding:iso-8859-9 Türkçe

# String dizge'ler değiştirilemez, ancak yeniden yaratılabilirler...
dizge1 = 'Selam'
dizge2 = "Merhaba"
dizge3 = """Bu tek satırı ikinciye taşıran uzun
bir dizge örneğidir. İstediğiniz kadar uzatabilirsiniz!"""

gir_sayı = eval (input ('Doğum yılınızı 4 rakamlı girin: '))
gir_dizge = input ('Ad ve soyadınızı girin: ')

print ("\nİlk dizge: [", dizge1, "] ve uzunluğu: [", len (dizge1), "]", sep="")
print ("İkinci dizge: [", dizge2, "] ve uzunluğu: [", len (dizge2), "]", sep="")
print ("Üçüncü dizge: [", dizge3, "] ve uzunluğu: [", len (dizge3), "]", sep="")
print ("\nSayısal veri girişi: [", gir_sayı, "]", sep="")
print ("Dizgesel veri girişi: [", gir_dizge, "] ve uzunluğu: [", len (gir_dizge), "]", sep="")