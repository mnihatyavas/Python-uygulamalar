# coding:iso-8859-9 Türkçe
# p_21404.py: LM farkını 2 kelime matrisinin son elemanı olarak bulma örneği.

"""
Matrisin sağ alt değeri LM mesafe maliyeti farkını verir.
-soldan sağa: sok,
-üstten alta: sil,
-çapraz: değiştir
Her birinin maliyeti = 1'dir.
"""

def LM_matrisi (d1, d2):
    satır = len (d1)+1
    sütun = len (d2)+1
    mesafe = [[0 for x in range (sütun)] for x in range (satır)]
    for i in range (1, satır): mesafe [i] [0] = i
    for i in range (1, sütun): mesafe [0] [i] = i
    for kln in range (1, sütun):
        for str in range (1, satır):
            if d1 [str-1] == d2 [kln-1]: maliyet = 0
            else: maliyet = 1
            mesafe [str] [kln] = min (mesafe [str-1] [kln]+1, # sil...
                    mesafe [str] [kln-1] + 1, # sok...
                    mesafe [str-1] [kln-1] + maliyet) # değiştir...
    for r in range (satır): print (mesafe [r]) # matrisi yazar....
    print()
    return mesafe [str] [kln] # LM farkını (matrisin son elemanı) döndürür...

print ("'bolu' ve 'oltu' için LM matrisi:\n", "-"*33, sep="")
print ("LM farkı:", LM_matrisi ("bolu", "oltu") )

print ("\n'İskenderun' ve 'Iskendurun' için LM matrisi:\n", "-"*45, sep="")
print ("LM farkı:", LM_matrisi ("İskenderun", "Iskendurun") )

print ("\n'İskenderun' ve 'İsfendiyar' için LM matrisi:\n", "-"*45, sep="")
print ("LM farkı:", LM_matrisi ("İskenderun", "İsfendiyar") )

print ("\n'Yeşilyurt' ve 'Çırmığtı' için LM matrisi:\n", "-"*42, sep="")
print ("LM farkı:", LM_matrisi ("Yeşilyurt", "Çırmığtı") )



"""Çıktı:
>python p_21404.py
'bolu' ve 'oltu' için LM matrisi:
---------------------------------
[0, 1, 2, 3, 4]
[1, 1, 2, 3, 4]
[2, 1, 2, 3, 4]
[3, 2, 1, 2, 3]
[4, 3, 2, 2, 2]

LM farkı: 2

'İskenderun' ve 'Iskendurun' için LM matrisi:
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

LM farkı: 2

'İskenderun' ve 'İsfendiyar' için LM matrisi:
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

LM farkı: 5

'Yeşilyurt' ve 'Çırmığtı' için LM matrisi:
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

LM farkı: 9
"""