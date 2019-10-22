# coding:iso-8859-9 Türkçe

a = 3
try:
    b = eval (input ('Bir sayı giriniz: '))
    print (a / b)
except NameError: print ('HATA: Lütfen sayı girin, karakter değil!..')
except ZeroDivisionError: print ('Sıfıra bölüm hatası; sıfır girmeyin!..')

print ('...\nİstisna hatası yönetildi ve program akışı devam ediyor...')
try:
    b = eval (input ('\nTekrar düzgün bir sayı giriniz: '))
    print (a / b)
except: print ("H A T A : Herhangi bir sebeple TEKRAR hata oluştu!..")

print ('...\nİstisna hatası TEKRAR yönetildi ve program akışı halen devam ediyor...')

try:
    b = eval (input ('\nTekrar düzgün bir sayı giriniz: '))
    print (a / b)
except Exception as ist: print ("H A T A :", ist)

print ('...\nİstisna hatası 3.kez yönetildi ve program akışı kesintisiz devam etmektedir...')
