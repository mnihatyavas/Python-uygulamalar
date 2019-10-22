# coding:iso-8859-9 T�rk�e
# p_21404.py: LM fark�n� 2 kelime matrisinin son eleman� olarak bulma �rne�i.

"""
Matrisin sa� alt de�eri LM mesafe maliyeti fark�n� verir.
-soldan sa�a: sok,
-�stten alta: sil,
-�apraz: de�i�tir
Her birinin maliyeti = 1'dir.
"""

def LM_matrisi (d1, d2):
    sat�r = len (d1)+1
    s�tun = len (d2)+1
    mesafe = [[0 for x in range (s�tun)] for x in range (sat�r)]
    for i in range (1, sat�r): mesafe [i] [0] = i
    for i in range (1, s�tun): mesafe [0] [i] = i
    for kln in range (1, s�tun):
        for str in range (1, sat�r):
            if d1 [str-1] == d2 [kln-1]: maliyet = 0
            else: maliyet = 1
            mesafe [str] [kln] = min (mesafe [str-1] [kln]+1, # sil...
                    mesafe [str] [kln-1] + 1, # sok...
                    mesafe [str-1] [kln-1] + maliyet) # de�i�tir...
    for r in range (sat�r): print (mesafe [r]) # matrisi yazar....
    print()
    return mesafe [str] [kln] # LM fark�n� (matrisin son eleman�) d�nd�r�r...

print ("'bolu' ve 'oltu' i�in LM matrisi:\n", "-"*33, sep="")
print ("LM fark�:", LM_matrisi ("bolu", "oltu") )

print ("\n'�skenderun' ve 'Iskendurun' i�in LM matrisi:\n", "-"*45, sep="")
print ("LM fark�:", LM_matrisi ("�skenderun", "Iskendurun") )

print ("\n'�skenderun' ve '�sfendiyar' i�in LM matrisi:\n", "-"*45, sep="")
print ("LM fark�:", LM_matrisi ("�skenderun", "�sfendiyar") )

print ("\n'Ye�ilyurt' ve '��rm��t�' i�in LM matrisi:\n", "-"*42, sep="")
print ("LM fark�:", LM_matrisi ("Ye�ilyurt", "��rm��t�") )



"""��kt�:
>python p_21404.py
'bolu' ve 'oltu' i�in LM matrisi:
---------------------------------
[0, 1, 2, 3, 4]
[1, 1, 2, 3, 4]
[2, 1, 2, 3, 4]
[3, 2, 1, 2, 3]
[4, 3, 2, 2, 2]

LM fark�: 2

'�skenderun' ve 'Iskendurun' i�in LM matrisi:
---------------------------------------------
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[2, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[3, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8]
[4, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7]
[5, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6]
[6, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5]
[7, 7, 6, 5, 4, 3, 2, 2, 3, 4, 5]
[8, 8, 7, 6, 5, 4, 3, 3, 2, 3, 4]
[9, 9, 8, 7, 6, 5, 4, 3, 3, 2, 3]
[10, 10, 9, 8, 7, 6, 5, 4, 4, 3, 2]

LM fark�: 2

'�skenderun' ve '�sfendiyar' i�in LM matrisi:
---------------------------------------------
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8]
[3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8]
[4, 3, 2, 2, 1, 2, 3, 4, 5, 6, 7]
[5, 4, 3, 3, 2, 1, 2, 3, 4, 5, 6]
[6, 5, 4, 4, 3, 2, 1, 2, 3, 4, 5]
[7, 6, 5, 5, 4, 3, 2, 2, 3, 4, 5]
[8, 7, 6, 6, 5, 4, 3, 3, 3, 4, 4]
[9, 8, 7, 7, 6, 5, 4, 4, 4, 4, 5]
[10, 9, 8, 8, 7, 6, 5, 5, 5, 5, 5]

LM fark�: 5

'Ye�ilyurt' ve '��rm��t�' i�in LM matrisi:
------------------------------------------
[0, 1, 2, 3, 4, 5, 6, 7, 8]
[1, 1, 2, 3, 4, 5, 6, 7, 8]
[2, 2, 2, 3, 4, 5, 6, 7, 8]
[3, 3, 3, 3, 4, 5, 6, 7, 8]
[4, 4, 4, 4, 4, 5, 6, 7, 8]
[5, 5, 5, 5, 5, 5, 6, 7, 8]
[6, 6, 6, 6, 6, 6, 6, 7, 8]
[7, 7, 7, 7, 7, 7, 7, 7, 8]
[8, 8, 8, 7, 8, 8, 8, 8, 8]
[9, 9, 9, 8, 8, 9, 9, 8, 9]

LM fark�: 9
"""