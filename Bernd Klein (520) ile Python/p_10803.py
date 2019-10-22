# coding:iso-8859-9 T�rk�e
# p_10803.py: Listelerle remove/sil ve insert/sok i�lemleri �rne�i.

L =["Ankara", "�stanbul", "�zmir", "Adana", "Mersin"]

try: print ("'�stanbul' listeden siliniyor:", L.remove ("�stanbul") )
except Exception: pass

try: L.remove ("Bursa")
except ValueError: print ("Silmek istedi�iniz 'Bursa' listede YOK")

print ("Kalan liste:", L)

try: print ("\nListede aranan '�zmir'in endeksi:", L.index ("�zmir") )
except ValueError: pass

try: print (L.remove ("Bursa") )
except ValueError: print ("Endeksini bulmak istedi�iniz 'Bursa' listede YOK")

from random import randint
# append gibi insert(len(L)) de eleman� liste sonuna ekler...
print ("'\nAntalya' listeye geli�ig�zel sokuluyor:", L.insert (randint(0,len(L)), "Antalya") )
print ("Listemiz:", L)


"""��kt�:
>python p_10803.py
'�stanbul' listeden siliniyor: None
Silmek istedi�iniz 'Bursa' listede YOK
Kalan liste: ['Ankara', '�zmir', 'Adana', 'Mersin']

Listede aranan '�zmir'in endeksi: 1
Endeksini bulmak istedi�iniz 'Bursa' listede YOK'
Antalya' listeye geli�ig�zel sokuluyor: None
Listemiz: ['Ankara', '�zmir', 'Antalya', 'Adana', 'Mersin']
"""