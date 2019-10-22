# coding:iso-8859-9 Türkçe
# p_10803.py: Listelerle remove/sil ve insert/sok işlemleri örneği.

L =["Ankara", "İstanbul", "İzmir", "Adana", "Mersin"]

try: print ("'İstanbul' listeden siliniyor:", L.remove ("İstanbul") )
except Exception: pass

try: L.remove ("Bursa")
except ValueError: print ("Silmek istediğiniz 'Bursa' listede YOK")

print ("Kalan liste:", L)

try: print ("\nListede aranan 'İzmir'in endeksi:", L.index ("İzmir") )
except ValueError: pass

try: print (L.remove ("Bursa") )
except ValueError: print ("Endeksini bulmak istediğiniz 'Bursa' listede YOK")

from random import randint
# append gibi insert(len(L)) de elemanı liste sonuna ekler...
print ("'\nAntalya' listeye gelişigüzel sokuluyor:", L.insert (randint(0,len(L)), "Antalya") )
print ("Listemiz:", L)


"""Çıktı:
>python p_10803.py
'İstanbul' listeden siliniyor: None
Silmek istediğiniz 'Bursa' listede YOK
Kalan liste: ['Ankara', 'İzmir', 'Adana', 'Mersin']

Listede aranan 'İzmir'in endeksi: 1
Endeksini bulmak istediğiniz 'Bursa' listede YOK'
Antalya' listeye gelişigüzel sokuluyor: None
Listemiz: ['Ankara', 'İzmir', 'Antalya', 'Adana', 'Mersin']
"""