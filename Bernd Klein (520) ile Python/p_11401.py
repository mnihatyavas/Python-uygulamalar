# coding:iso-8859-9 T�rk�e
# p_11401.py: if-elif-else ile farkl� dillerde konu�ma tercihi �rne�i.

ki�i = input ("Tabiyetiniz nedir? ").lower()
print()
if ki�i[:2] == "fr":
    print ("Pr�f�rez-vous parler fran�ais?")
elif ki�i[:2] == "it":
    print ("Preferisci parlare italiano?")
elif ki�i[:2] == "ge" or ki�i[:2] == "al":
    print ("Vorziehen Sie sprehen Deutch?")
elif ki�i[:2] == "tu" or ki�i[:2] == "t�":
    print ("T�rk�e mi konu�may� tercih edersiniz?")
else:
    print ("You are neither Turk nor German nor Italian nor French,")
    print ("so we have to speak English with each other.")


"""��kt�
>python p_11401.py
Tabiyetiniz nedir?

You are neither Turk nor German nor Italian nor French,
so we have to speak English with each other.

>python p_11401.py  ** TEKRAR **
Tabiyetiniz nedir? t�rk

T�rk�e mi konu�may� tercih edersiniz?

>python p_11401.py  ** TEKRAR **
Tabiyetiniz nedir? frans�z

Pr�f�rez-vous parler fran�ais?

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