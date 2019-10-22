# coding:iso-8859-9 T�rk�e
# p_13408.py: for-yield ve yield-from'la ayn� �retimi �rne�i.

def �rete�1():
    for krk in "Python": yield krk
    for i in range (5): yield i

def �rete�2():
    yield from "Python"
    yield from range (5)

# Her iki �rete� de ayn�d�r...
x1 = �rete�1()
x2 = �rete�2()

print ("�rete�1: ", end="")
for x in x1: print (x, end="-")

print ("\n�rete�2: ", end="")
for x in x2: print (x, end="-")
print ("\n", "-"*75, "\n", sep="")
#-------------------------------------------------------------------------------------------------

def �ehirler():
    for �ehir in ["Ankara", "�stanbul", "�zmir", "Bursa", "Mersin"]: yield �ehir

def kareler():
    for say� in range (10): yield say� ** 2

def birle�ik_�rete�():
    for �ehir in �ehirler(): yield �ehir
    for say� in kareler(): yield say�

def ayr�k_�rete�():
    yield from �ehirler()
    yield from kareler()

liste1 = [eleman for eleman in birle�ik_�rete�()]
liste2 = [eleman for eleman in ayr�k_�rete�()]

print ([� for � in �ehirler()] )
print ([k for k in kareler()] )

print()
print (liste1)
print (liste2)

print ("\nListe1 ile Liste2 e�it mi? ", end="")
print (liste1 == liste2)
print ("-"*75, "\n", sep="")
#--------------------------------------------------------------------------------------------

def �rete�():
    yield 1
    yield 5
    yield 27
    return 42

def temsilci():
    x = yield from �rete�()
    print (x)
    print (x)
    print (x)

print ("return'siz yield'leri verir:")
for x in �rete�(): print (x)

print ("\nyield'leri ve tekrarl� return'� verir:")
for x in temsilci(): print (x)

"""��kt�:
>python p_13408.py
�rete�1: P-y-t-h-o-n-0-1-2-3-4-
�rete�2: P-y-t-h-o-n-0-1-2-3-4-
---------------------------------------------------------------------------

['Ankara', '�stanbul', '�zmir', 'Bursa', 'Mersin']
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

['Ankara', '�stanbul', '�zmir', 'Bursa', 'Mersin', 0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
['Ankara', '�stanbul', '�zmir', 'Bursa', 'Mersin', 0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

Liste1 ile Liste2 e�it mi? True
---------------------------------------------------------------------------

return'siz yield'leri verir:
1
5
27

yield'leri ve tekrarl� return'� verir:
1
5
27
42
42
42
"""