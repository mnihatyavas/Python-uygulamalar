# coding:iso-8859-9 Türkçe
# p_11005.py: Sözlük items/birimler, keys/anahtarlar ve values/değerler ile pop ve get işlemleri örneği.

başkentler = {"Avusturya":"Viyana", "Almanya":"Berlin", "Hollanda":"Amsterdam"}
print (başkentler)
print ("\n", başkentler.items(), "\n", başkentler.keys(), "\n", başkentler.values(), sep="")

# pop(..) için sözlükten çıkaracağı mutlaka mevcut bir anahtar gereklidir...
başkent = başkentler.pop ("Avusturya")
print ("\n", başkent, "\n", başkentler, sep="")

print()
try: print (başkentler.pop ("İsviçre") )
except KeyError: print ("HATA: Sözlükte girdiğiniz anahtar YOK!")

print()
print (başkentler.pop ("İsviçre", "Bern") ) # Sözlükte yoksa, varsayılı "Bern" gösterilecek...

print()
print (başkentler.pop ("Fransa", "Paris") )

print()
print (başkentler.pop ("Almanya", "Münih") ) # Bulursa, cevabı; bulamazsa "Münih"i gösterecek...
print (başkentler)

# "in" kontroluyla hata fırlatma önlenir...
if "İtalya" in başkentler: print ("\n", başkentler.pop ("İtalya"), "\n", başkentler, sep="")

print ("\n", başkentler.get ("İtalya"), "\n", başkentler, sep="") # Get yoksa, hata kırmaz, None döndürür...
print ("\n", başkentler.get ("Hollanda"), "\n", başkentler, sep="") # Get mevcudu çıkarmaz, gösterir...


"""Çıktı:
>python p_11005.py
{'Avusturya': 'Viyana', 'Almanya': 'Berlin', 'Hollanda': 'Amsterdam'}

dict_items([('Avusturya', 'Viyana'), ('Almanya', 'Berlin'), ('Hollanda', 'Amsterdam')])
dict_keys(['Avusturya', 'Almanya', 'Hollanda'])
dict_values(['Viyana', 'Berlin', 'Amsterdam'])

Viyana
{'Almanya': 'Berlin', 'Hollanda': 'Amsterdam'}

HATA: Sözlükte girdiğiniz anahtar YOK!

Bern

Paris

Berlin
{'Hollanda': 'Amsterdam'}

None
{'Hollanda': 'Amsterdam'}

Amsterdam
{'Hollanda': 'Amsterdam'}
"""