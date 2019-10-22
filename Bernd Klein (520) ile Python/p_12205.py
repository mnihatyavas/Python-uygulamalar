# coding:iso-8859-9 Türkçe
# p_12205.py: **parametre'ye sözlük, (a,b,c,d) parametreye *liste ve **sözlük argümanları geçirme örneği.

def fonk1 (**x): print (x) # Çift yıldızlı değişken sözlük parametresi...

print (fonk1)
print ("Boş argüman: ", end=""); fonk1()
print ("Yabancı diller: ", end=""); fonk1 (de="Almanca", en="İngilizce", fr="Fransızca", tr = "Türkçe")
print ("Şehir plakaları: ", end=""); fonk1 (tr_01="Adana", tr_06="Ankara", tr_16="Bursa", tr_33="Mersin", tr_34="İstanbul", tr_44="Malatya")
#---------------------------------------------------------------------------------------------------------

def fonk2 (a, b, c, d): print (a, b, c, d) # Anahtar kelimeli sözlük değerleri...

sözlük1 = {'a':'Almanca', 'c':'İngilizce', 'd':'Fransızca', "b" : "Türkçe"}
print ("Yabancı diller: ", end=""); fonk2 (**sözlük1)

sözlük2 = {"a":"Adana", "b":"Ankara", "c":"Bursa", "d" : "Mersin"}
print ("Şehir plakaları: ", end=""); fonk2 (**sözlük2)
#---------------------------------------------------------------------------------------------------------

liste = [33, 44]
sözlük = {"c":"Mersin", "d" : "Malatya"}

print ("Plakalar listesi ve şehirler sözlüğü:", end= " "); fonk2 (*liste, **sözlük)


"""Çıktı:
>python p_12205.py
<function fonk1 at 0x0132B5D0>
Boş argüman: {}
Yabancı diller: {'de': 'Almanca', 'en': 'İngilizce', 'fr': 'Fransızca', 'tr': 'Türkçe'}
Şehir plakaları: {'tr_01': 'Adana', 'tr_06': 'Ankara', 'tr_16': 'Bursa', 'tr_33': 'Mersin', 'tr_34': 'İstanbul', 'tr_44': 'Malatya'}
Yabancı diller: Almanca Türkçe İngilizce Fransızca
Şehir plakaları: Adana Ankara Bursa Mersin
Plakalar listesi ve şehirler sözlüğü: 33 44 Mersin Malatya
"""