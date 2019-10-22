# coding:iso-8859-9 T�rk�e
# p_12205.py: **parametre'ye s�zl�k, (a,b,c,d) parametreye *liste ve **s�zl�k arg�manlar� ge�irme �rne�i.

def fonk1 (**x): print (x) # �ift y�ld�zl� de�i�ken s�zl�k parametresi...

print (fonk1)
print ("Bo� arg�man: ", end=""); fonk1()
print ("Yabanc� diller: ", end=""); fonk1 (de="Almanca", en="�ngilizce", fr="Frans�zca", tr = "T�rk�e")
print ("�ehir plakalar�: ", end=""); fonk1 (tr_01="Adana", tr_06="Ankara", tr_16="Bursa", tr_33="Mersin", tr_34="�stanbul", tr_44="Malatya")
#---------------------------------------------------------------------------------------------------------

def fonk2 (a, b, c, d): print (a, b, c, d) # Anahtar kelimeli s�zl�k de�erleri...

s�zl�k1 = {'a':'Almanca', 'c':'�ngilizce', 'd':'Frans�zca', "b" : "T�rk�e"}
print ("Yabanc� diller: ", end=""); fonk2 (**s�zl�k1)

s�zl�k2 = {"a":"Adana", "b":"Ankara", "c":"Bursa", "d" : "Mersin"}
print ("�ehir plakalar�: ", end=""); fonk2 (**s�zl�k2)
#---------------------------------------------------------------------------------------------------------

liste = [33, 44]
s�zl�k = {"c":"Mersin", "d" : "Malatya"}

print ("Plakalar listesi ve �ehirler s�zl���:", end= " "); fonk2 (*liste, **s�zl�k)


"""��kt�:
>python p_12205.py
<function fonk1 at 0x0132B5D0>
Bo� arg�man: {}
Yabanc� diller: {'de': 'Almanca', 'en': '�ngilizce', 'fr': 'Frans�zca', 'tr': 'T�rk�e'}
�ehir plakalar�: {'tr_01': 'Adana', 'tr_06': 'Ankara', 'tr_16': 'Bursa', 'tr_33': 'Mersin', 'tr_34': '�stanbul', 'tr_44': 'Malatya'}
Yabanc� diller: Almanca T�rk�e �ngilizce Frans�zca
�ehir plakalar�: Adana Ankara Bursa Mersin
Plakalar listesi ve �ehirler s�zl���: 33 44 Mersin Malatya
"""