# coding:iso-8859-9 Türkçe
# p_11401.py: if-elif-else ile farklı dillerde konuşma tercihi örneği.

kişi = input ("Tabiyetiniz nedir? ").lower()
print()
if kişi[:2] == "fr":
    print ("Préférez-vous parler français?")
elif kişi[:2] == "it":
    print ("Preferisci parlare italiano?")
elif kişi[:2] == "ge" or kişi[:2] == "al":
    print ("Vorziehen Sie sprehen Deutch?")
elif kişi[:2] == "tu" or kişi[:2] == "tü":
    print ("Türkçe mi konuşmayı tercih edersiniz?")
else:
    print ("You are neither Turk nor German nor Italian nor French,")
    print ("so we have to speak English with each other.")


"""Çıktı
>python p_11401.py
Tabiyetiniz nedir?

You are neither Turk nor German nor Italian nor French,
so we have to speak English with each other.

>python p_11401.py  ** TEKRAR **
Tabiyetiniz nedir? türk

Türkçe mi konuşmayı tercih edersiniz?

>python p_11401.py  ** TEKRAR **
Tabiyetiniz nedir? fransız

Préférez-vous parler français?

>python p_11401.py  ** TEKRAR **
Tabiyetiniz nedir? italyan

Preferisci parlare italiano?

>python p_11401.py  ** TEKRAR **
Tabiyetiniz nedir? german

Vorziehen Sie sprehen Deutch?
>python p_11401.py  ** TEKRAR **
Tabiyetiniz nedir? Alman

Vorziehen Sie sprehen Deutch?
"""