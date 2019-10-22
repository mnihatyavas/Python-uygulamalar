# p10107.py
# coding:iso-8859-9 Türkçe

c_ısı = eval (input ('Bir selsiyüs santigrad derece girin: '))
f_ısı = 9/5*c_ısı+32

print (c_ısı, 'C derece:', f_ısı, "F derecedir.")
if f_ısı > 212: print ('Bu ısı kaynama noktasının üzerindedir.')
if f_ısı < 32: print ('Bu ısı donma noktasının altındadır.')
