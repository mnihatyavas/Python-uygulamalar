# coding:iso-8859-9 T�rk�e

a = 3
try:
    b = eval (input ('Bir say� giriniz: '))
    print (a / b)
except NameError: print ('HATA: L�tfen say� girin, karakter de�il!..')
except ZeroDivisionError: print ('S�f�ra b�l�m hatas�; s�f�r girmeyin!..')

print ('...\n�stisna hatas� y�netildi ve program ak��� devam ediyor...')
try:
    b = eval (input ('\nTekrar d�zg�n bir say� giriniz: '))
    print (a / b)
except: print ("H A T A : Herhangi bir sebeple TEKRAR hata olu�tu!..")

print ('...\n�stisna hatas� TEKRAR y�netildi ve program ak��� halen devam ediyor...')

try:
    b = eval (input ('\nTekrar d�zg�n bir say� giriniz: '))
    print (a / b)
except Exception as ist: print ("H A T A :", ist)

print ('...\n�stisna hatas� 3.kez y�netildi ve program ak��� kesintisiz devam etmektedir...')
