# coding:iso-8859-9 T�rk�e
# Python3 - Dictionary

s�zl�k1 = {'Ad�': 'M.Nihat', 'soyad�': 'Yava�', 'Ya��': 62, 'do�um yeri': 'Ye�ilyurt'}
s�zl�k2 = {1: "Bir", 2:"�ki", "��":"��"}
s�zl�k3 = {}

print ("s�zl�k1['Ad�']:", s�zl�k1['Ad�'])
print ("s�zl�k1['Ya��']:", s�zl�k1['Ya��'])
print ("s�zl�k1['do�um yeri']:", s�zl�k1['do�um yeri'])

s�zl�k1 ['Ya��'] = 65; # g�ncelleme...
s�zl�k1['Do�um Y�l�'] = 1957 # Yeni i�erik giri�i...

print ("s�zl�k1['Ya��']: ", s�zl�k1['Ya��'])
print ("s�zl�k1['Do�um Y�l�']: ", s�zl�k1['Do�um Y�l�'])

del s�zl�k1['Ad�'] # Tek i�erik silinmesi...
print (s�zl�k1)
s�zl�k1.clear() # T�m i�eriklerin silinmesi...
print (s�zl�k1)
del s�zl�k1 # S�zl���n silinmesi...
# print (s�zl�k1) ==> NameError: name 's�zl�k1' is not defined

s�zl�k1 = {'Ad�': 'Mahmut', 'soyad�': 'Yava�', 'Ya��': 62, 'do�um yeri': 'Ye�ilyurt', 'Ad�': 'Nihat'}
print (s�zl�k1)
print (len (s�zl�k1))

print (s�zl�k2)

print (type (s�zl�k3))

print (s�zl�k1.keys())
print (s�zl�k1.values())
print (s�zl�k1.items())

s�zl�k1.update (s�zl�k2)
print (s�zl�k1)
