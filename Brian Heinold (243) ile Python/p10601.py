# coding:iso-8859-9 T�rk�e

# String dizge'ler de�i�tirilemez, ancak yeniden yarat�labilirler...
dizge1 = 'Selam'
dizge2 = "Merhaba"
dizge3 = """Bu tek sat�r� ikinciye ta��ran uzun
bir dizge �rne�idir. �stedi�iniz kadar uzatabilirsiniz!"""

gir_say� = eval (input ('Do�um y�l�n�z� 4 rakaml� girin: '))
gir_dizge = input ('Ad ve soyad�n�z� girin: ')

print ("\n�lk dizge: [", dizge1, "] ve uzunlu�u: [", len (dizge1), "]", sep="")
print ("�kinci dizge: [", dizge2, "] ve uzunlu�u: [", len (dizge2), "]", sep="")
print ("���nc� dizge: [", dizge3, "] ve uzunlu�u: [", len (dizge3), "]", sep="")
print ("\nSay�sal veri giri�i: [", gir_say�, "]", sep="")
print ("Dizgesel veri giri�i: [", gir_dizge, "] ve uzunlu�u: [", len (gir_dizge), "]", sep="")