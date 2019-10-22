# coding:iso-8859-9 Türkçe
# p_11102.py: Değişir ve değişmez küme, silme ve kopyalama örneği.

başkentler = ["Ankara", "Atina", "Londra", "Berlin", "Paris", "Ankara", "Roma"]
küme1 = set (başkentler)
küme1.add ("Madrid")
print ("\nYalın değişir kümeye eleman eklenebilir:", küme1)

küme2 = frozenset (başkentler)
print ("\nDonuk değişmez kümeye eleman eklenemez:", küme2)
#-----------------------------------------------------------------------------------------------

sıfatlar = {"ucuz", "pahalı", "değerli", "ekonomik", "güzel"}
print ("\nSet kümeler sözlük gibi ancak anahtarsız tanımlanabilirler: ", sıfatlar, "\nTip: ", type (sıfatlar), sep="")

sıfatlar.clear()
print ("\n'clear' ile küme elemanları hepten silinir:",  sıfatlar)
#-----------------------------------------------------------------------------------------------

küme3 = küme1
küme4 = küme1.copy()

küme1.clear()
print ("\nElemanları temizlenen kaynak küme kopyası:", küme1)
print ("Kaynaktan atamalı küme:", küme3)
print ("Kaynaktan copy'li küme:", küme4)


"""Çıktı:
>python p_11102.py

Yalın değişir kümeye eleman eklenebilir: {'Paris', 'Roma', 'Berlin', 'Londra', 'Atina', 'Madrid', 'Ankara'}

Donuk değişmez kümeye eleman eklenemez: frozenset({'Paris', 'Roma', 'Berlin', 'Londra', 'Atina', 'Ankara'})

Set kümeler sözlük gibi ancak anahtarsız tanımlanabilirler: {'güzel', 'pahalı','ucuz', 'ekonomik', 'değerli'}
Tip: <class 'set'>

'clear' ile küme elemanları hepten silinir: set()

Elemanları temizlenen kaynak küme kopyası: set()
Kaynaktan atamalı küme: set()
Kaynaktan copy'li küme: {'Ankara', 'Paris', 'Atina', 'Madrid', 'Roma', 'Berlin', 'Londra'}
"""