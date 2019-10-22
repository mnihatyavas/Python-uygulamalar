# coding:iso-8859-9 Türkçe
# p_13401.py: Liste, iter-next tarayıcı ve sözlük dökümleri örneği.

şehirler = ["Ankara", "İstanbul", "İzmir", "Mersin", "Adana", "Bursa", "Samsun", "Konya", "Diyarbakır", "Antalya"]
print ("Şehirler listesi:")
for şehir in şehirler: print ("-->Şehir: " + şehir)
#----------------------------------------------------------------------------------------------------

uzmanlıklar = ["Acemi", "Başlangıç", "Orta", "Usta", "Tecrübeli", "İleri"]
tarayıcı = iter (uzmanlıklar)
print ("\nUzmanlık dereceleri:")
try:
    print ("-->Derece: " + next (tarayıcı) )
    print ("-->Derece: " + next (tarayıcı) )
    print ("-->Derece: " + next (tarayıcı) )
    print ("-->Derece: " + next (tarayıcı) )
    print ("-->Derece: " + next (tarayıcı) )
    print ("-->Derece: " + next (tarayıcı) )
    print ("-->Derece: " + next (tarayıcı) )
except StopIteration: print ("Tarayıcı listesi sonuna ulaşıldı...")
#----------------------------------------------------------------------------------------------------

şehirler2 = ["Malatya", "Muğla", "Nevşehir", "Erzincan", "Amasya", "Iğdır", "Sinop", "Edirne", "Hatay", "Rize"]

tarayıcı2 = iter (şehirler2)
print ("\nDiğer şehirler:")
while tarayıcı2:
    try: print (next (tarayıcı2))
    except: break
#----------------------------------------------------------------------------------------------------

başşehirler = {"Fransa":"Paris", "Hollanda":"Amsterdam", "Almanya":"Berlin", "İsviçre":"Bern", "Avusturya":"Viyana", "Türkiye":"Ankara", "İngiltere":"Londra", "İtalya":"Roma", "Yunanistan":"Atina", "Ukrayna":"Kiev"}
print ("\nÇeşitli başşehirler:")
for ülke in başşehirler: print ("-->" + ülke + "'nın başkenti: " + başşehirler [ülke] )


"""Çıktı:
>python p_13401.py
Şehirler listesi:
-->Şehir: Ankara
-->Şehir: İstanbul
-->Şehir: İzmir
-->Şehir: Mersin
-->Şehir: Adana
-->Şehir: Bursa
-->Şehir: Samsun
-->Şehir: Konya
-->Şehir: Diyarbakır
-->Şehir: Antalya

Uzmanlık dereceleri:
-->Derece: Acemi
-->Derece: Başlangıç
-->Derece: Orta
-->Derece: Usta
-->Derece: Tecrübeli
-->Derece: İleri
Tarayıcı listesi sonuna ulaşıldı...

Diğer şehirler:
Malatya
Muğla
Nevşehir
Erzincan
Amasya
Iğdır
Sinop
Edirne
Hatay
Rize

Çeşitli başşehirler:
-->Fransa'nın başkenti: Paris
-->Hollanda'nın başkenti: Amsterdam
-->Almanya'nın başkenti: Berlin
-->İsviçre'nın başkenti: Bern
-->Avusturya'nın başkenti: Viyana
-->Türkiye'nın başkenti: Ankara
-->İngiltere'nın başkenti: Londra
-->İtalya'nın başkenti: Roma
-->Yunanistan'nın başkenti: Atina
-->Ukrayna'nın başkenti: Kiev
"""