# coding:iso-8859-9 T�rk�e
# p_11005.py: S�zl�k items/birimler, keys/anahtarlar ve values/de�erler ile pop ve get i�lemleri �rne�i.

ba�kentler = {"Avusturya":"Viyana", "Almanya":"Berlin", "Hollanda":"Amsterdam"}
print (ba�kentler)
print ("\n", ba�kentler.items(), "\n", ba�kentler.keys(), "\n", ba�kentler.values(), sep="")

# pop(..) i�in s�zl�kten ��karaca�� mutlaka mevcut bir anahtar gereklidir...
ba�kent = ba�kentler.pop ("Avusturya")
print ("\n", ba�kent, "\n", ba�kentler, sep="")

print()
try: print (ba�kentler.pop ("�svi�re") )
except KeyError: print ("HATA: S�zl�kte girdi�iniz anahtar YOK!")

print()
print (ba�kentler.pop ("�svi�re", "Bern") ) # S�zl�kte yoksa, varsay�l� "Bern" g�sterilecek...

print()
print (ba�kentler.pop ("Fransa", "Paris") )

print()
print (ba�kentler.pop ("Almanya", "M�nih") ) # Bulursa, cevab�; bulamazsa "M�nih"i g�sterecek...
print (ba�kentler)

# "in" kontroluyla hata f�rlatma �nlenir...
if "�talya" in ba�kentler: print ("\n", ba�kentler.pop ("�talya"), "\n", ba�kentler, sep="")

print ("\n", ba�kentler.get ("�talya"), "\n", ba�kentler, sep="") # Get yoksa, hata k�rmaz, None d�nd�r�r...
print ("\n", ba�kentler.get ("Hollanda"), "\n", ba�kentler, sep="") # Get mevcudu ��karmaz, g�sterir...


"""��kt�:
>python p_11005.py
{'Avusturya': 'Viyana', 'Almanya': 'Berlin', 'Hollanda': 'Amsterdam'}

dict_items([('Avusturya', 'Viyana'), ('Almanya', 'Berlin'), ('Hollanda', 'Amsterdam')])
dict_keys(['Avusturya', 'Almanya', 'Hollanda'])
dict_values(['Viyana', 'Berlin', 'Amsterdam'])

Viyana
{'Almanya': 'Berlin', 'Hollanda': 'Amsterdam'}

HATA: S�zl�kte girdi�iniz anahtar YOK!

Bern

Paris

Berlin
{'Hollanda': 'Amsterdam'}

None
{'Hollanda': 'Amsterdam'}

Amsterdam
{'Hollanda': 'Amsterdam'}
"""