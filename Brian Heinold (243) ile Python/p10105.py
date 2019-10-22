# p10105.py
# coding:iso-8859-9 Türkçe

isim = input ('İsminizi girin: ')
print ('Merhaba,', isim)

sayı = eval (input ('\nBoyunuzu girin (sm): '))
print ('Olması gereken uygun kilonuz:', sayı % 100 - 10)
