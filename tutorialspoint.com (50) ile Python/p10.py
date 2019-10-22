# coding:iso-8859-9 Türkçe
# Python3 - Dictionary

sözlük1 = {'Adı': 'M.Nihat', 'soyadı': 'Yavaş', 'Yaşı': 62, 'doğum yeri': 'Yeşilyurt'}
sözlük2 = {1: "Bir", 2:"İki", "Üç":"Üç"}
sözlük3 = {}

print ("sözlük1['Adı']:", sözlük1['Adı'])
print ("sözlük1['Yaşı']:", sözlük1['Yaşı'])
print ("sözlük1['doğum yeri']:", sözlük1['doğum yeri'])

sözlük1 ['Yaşı'] = 65; # güncelleme...
sözlük1['Doğum Yılı'] = 1957 # Yeni içerik girişi...

print ("sözlük1['Yaşı']: ", sözlük1['Yaşı'])
print ("sözlük1['Doğum Yılı']: ", sözlük1['Doğum Yılı'])

del sözlük1['Adı'] # Tek içerik silinmesi...
print (sözlük1)
sözlük1.clear() # Tüm içeriklerin silinmesi...
print (sözlük1)
del sözlük1 # Sözlüğün silinmesi...
# print (sözlük1) ==> NameError: name 'sözlük1' is not defined

sözlük1 = {'Adı': 'Mahmut', 'soyadı': 'Yavaş', 'Yaşı': 62, 'doğum yeri': 'Yeşilyurt', 'Adı': 'Nihat'}
print (sözlük1)
print (len (sözlük1))

print (sözlük2)

print (type (sözlük3))

print (sözlük1.keys())
print (sözlük1.values())
print (sözlük1.items())

sözlük1.update (sözlük2)
print (sözlük1)
