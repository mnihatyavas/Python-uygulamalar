# coding:iso-8859-9 T�rk�e
# p_11008.py: S�zl�klerde update/g�ncelle, zip/t�plede-birle�tir ve t�ple-liste-s�zl�k �evrimleri �rne�i.

s�zl�k1 = {"Sevim":{"JS"}, "Hatice":{"Java", "Python", "CSS"}, "Zeliha":{"ACCESS"} }
s�zl�k2 = {"Song�l":{"HTML"}, "Hatice":{"WORD"}, "Nedim":{"MASM", "HTML", "JS", "CSS"}, "Sevim":{"HTML", "CSS"} }

s�zl�k1.update (s�zl�k2)
# G�ncellemede 2.de de olan esas al�n�yor ve ilki at�l�yor, 2.yoksa ilki esas al�n�yor; karma ekleme yapm�yor (sakat!)...

print ("G�ncellenen s�zl�k:", s�zl�k1)
#----------------------------------------------------------------------------------------------------

print ("\nSadece anahtarlar�n d�k�m�:")
for anahtar in s�zl�k1: print (anahtar, end=" ")
print()
for anahtar in s�zl�k1.keys(): print (anahtar, end=" ") # Ayn� sonu�...
#----------------------------------------------------------------------------------------------------

print ("\n\nSadece de�erlerin d�k�m�:")
for de�er in s�zl�k1.values(): print (de�er, end=" ")
print()
for anahtar in s�zl�k1.keys(): print (s�zl�k1[anahtar], end=" ") # Ayn� sonu�, ancak ilki daha h�zl�d�r...
#----------------------------------------------------------------------------------------------------

print ("\n\nAnahtar-de�er �iftinin birlikte d�k�m�:")
for �ift in s�zl�k1.items(): print (�ift, end=" ")
#----------------------------------------------------------------------------------------------------

print ("\n\nS�zl�kten listeye �evrim:")
L = list (s�zl�k1.items() )
print (L)
#----------------------------------------------------------------------------------------------------

print ("\nS�zl�k anahtar-de�er �iftini 2 ayr� listeye ay�r�p, " +
    "sonra zip'le birle�ik t�ple liste yap�p, " +
    "onu da dict'le tekrar s�zl��e �evirelim:\n", "-"*79, sep="")
L1 = list (s�zl�k1.keys() )
L2 = list (s�zl�k1.values() )
L3 = list (zip (L1, L2) )
S = dict (L3)
print ("Anahtarlar listesi:\n", L1, "\n\nDe�erler listesi:\n", L2,
    "\n\nBirle�ik t�ple listesi:\n", L3, "\n\nS�zl�k:\n", S, sep="")

print ("\nL1 ve L2 listeleriyle direk zip'ten s�zl��e �evrim:\n", dict (zip (L1, L2)), sep="")
# Zip'te listelerden k�sas� esas al�n�p, art�k k�rp�l�r...

print ("\nListesiz direk zip'ten s�zl��e �evrim:\n", dict (zip (['Sevim', 'Hatice',
     'Zeliha', 'Song�l', 'Nedim'], [{'CSS', 'HTML'}, {'WORD'}, {'ACCESS'},
    {'HTML'}, {'CSS', 'MASM', 'HTML', 'JS'}])), sep="")


"""��kt�:
>python p_11008.py
G�ncellenen s�zl�k: {'Sevim': {'CSS', 'HTML'}, 'Hatice': {'WORD'},
'Zeliha': {'ACCESS'}, 'Song�l': {'HTML'}, 'Nedim': {'JS', 'CSS', 'HTML', 'MASM'}}

Sadece anahtarlar�n d�k�m�:
Sevim Hatice Zeliha Song�l Nedim
Sevim Hatice Zeliha Song�l Nedim

Sadece de�erlerin d�k�m�:
{'CSS', 'HTML'} {'WORD'} {'ACCESS'} {'HTML'} {'JS', 'CSS', 'HTML', 'MASM'}
{'CSS', 'HTML'} {'WORD'} {'ACCESS'} {'HTML'} {'JS', 'CSS', 'HTML', 'MASM'}

Anahtar-de�er �iftinin birlikte d�k�m�:
('Sevim', {'CSS', 'HTML'}) ('Hatice', {'WORD'}) ('Zeliha', {'ACCESS'})
('Song�l', {'HTML'}) ('Nedim', {'JS', 'CSS', 'HTML', 'MASM'})

S�zl�kten listeye �evrim:
[('Sevim', {'CSS', 'HTML'}), ('Hatice', {'WORD'}), ('Zeliha', {'ACCESS'}),
('Song�l', {'HTML'}), ('Nedim', {'JS', 'CSS', 'HTML', 'MASM'})]

S�zl�k anahtar-de�er �iftini 2 ayr� listeye ay�r�p, sonra zip'le birle�ik t�ple
liste yap�p, onu da dict'le tekrar s�zl��e �evirelim:
-------------------------------------------------------------------------------
Anahtarlar listesi:
['Sevim', 'Hatice', 'Zeliha', 'Song�l', 'Nedim']

De�erler listesi:
[{'CSS', 'HTML'}, {'WORD'}, {'ACCESS'}, {'HTML'}, {'JS', 'CSS', 'HTML', 'MASM'}]


Birle�ik t�ple listesi:
[('Sevim', {'CSS', 'HTML'}), ('Hatice', {'WORD'}), ('Zeliha', {'ACCESS'}),
('Song�l', {'HTML'}), ('Nedim', {'JS', 'CSS', 'HTML', 'MASM'})]

S�zl�k:
{'Sevim': {'CSS', 'HTML'}, 'Hatice': {'WORD'}, 'Zeliha': {'ACCESS'},
'Song�l': {'HTML'}, 'Nedim': {'JS', 'CSS', 'HTML', 'MASM'}}

L1 ve L2 listeleriyle direk zip'ten s�zl��e �evrim:
{'Sevim': {'CSS', 'HTML'}, 'Hatice': {'WORD'}, 'Zeliha': {'ACCESS'},
'Song�l': {'HTML'}, 'Nedim': {'JS', 'CSS', 'HTML', 'MASM'}}

Listesiz direk zip'ten s�zl��e �evrim:
{'Sevim': {'CSS', 'HTML'}, 'Hatice': {'WORD'}, 'Zeliha': {'ACCESS'},
'Song�l': {'HTML'}, 'Nedim': {'JS', 'CSS', 'HTML', 'MASM'}}
"""