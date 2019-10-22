# coding:iso-8859-9 Türkçe
# p_12701.py: Metin dosyasından okuma ve yazma çeşitlemesi örneği.

dosyaNesnesi = open ("p_12701x.txt") # Mevcut dosyadan varsayılı , "r": okur...
for satır in dosyaNesnesi: print (satır)
dosyaNesnesi.close()
print ("-"*75, "\n")
#---------------------------------------------------------------------------------------------------------

dosyaNesnesi = open ("p_12701x.txt", "r")
for satır in dosyaNesnesi: print (satır.rstrip() )
dosyaNesnesi.close()
print ("-"*75, "\n")
#---------------------------------------------------------------------------------------------------------

with open ("p_12701x.txt") as dosyaNesnesi:
    for satır in dosyaNesnesi: print (satır.rstrip() )
# close() burada gerekmez, zira with'le açılan dosyalar, tamamlanınca kendiliğinden kapanır...
print ("-"*75, "\n")
#---------------------------------------------------------------------------------------------------------

dosyaOku = open ("p_12701x.txt", "r")
dosyaYaz = open ("örnek1.txt", "w")
i = 1
for satır in dosyaOku:
    print (i, ": ", satır.rstrip(), sep="")
    print (i, ": ", satır.rstrip(), sep="", file=dosyaYaz)
    i +=1
dosyaOku.close()
dosyaYaz.close()
print ("-"*75, "\n")
#---------------------------------------------------------------------------------------------------------

with open ("p_12701x.txt", "r") as dosyaOku, open ("örnek1.txt", "w") as dosyaYaz:
    i = 1
    for satır in dosyaOku:
        print (i, ": ", satır.rstrip(), sep="")
        dosyaYaz.write (str(i) + ": " + satır) # write ile rstrip() ve close() gerekmez...
        i +=1
print ("-"*75, "\n")
#---------------------------------------------------------------------------------------------------------

dosyaListesi = open ("örnek1.txt", "r").readlines() # Tek kerede liste olarak okudu...
print (dosyaListesi)
print ("\n", dosyaListesi[0], dosyaListesi[len (dosyaListesi)-1], sep="", end="\n")
for i in range (len (dosyaListesi)): print (dosyaListesi[i], end="")
print ("-"*75, "\n")
#---------------------------------------------------------------------------------------------------------

dosyaMetni = open ("örnek1.txt", "r").read() # Tek kerede metin olarak okudu...
print (dosyaMetni)
print (dosyaMetni [::-1] ) # Metni tersten yazar...



"""Çıktı
>python p_12701.py
V. ad Lesbiam



VIVAMUS mea Lesbia, atque amemus,

rumoresque senum severiorum

omnes unius aestimemus assis!

soles occidere et redire possunt:

nobis cum semel occidit breuis lux,

nox est perpetua una dormienda.

da mi basia mille, deinde centum,

dein mille altera, dein secunda centum,

deinde usque altera mille, deinde centum.

dein, cum milia multa fecerimus,

conturbabimus illa, ne sciamus,

aut ne quis malus inuidere possit,

cum tantum sciat esse basiorum.

(GAIUS VALERIUS CATULLUS)

---------------------------------------------------------------------------

V. ad Lesbiam

VIVAMUS mea Lesbia, atque amemus,
rumoresque senum severiorum
omnes unius aestimemus assis!
soles occidere et redire possunt:
nobis cum semel occidit breuis lux,
nox est perpetua una dormienda.
da mi basia mille, deinde centum,
dein mille altera, dein secunda centum,
deinde usque altera mille, deinde centum.
dein, cum milia multa fecerimus,
conturbabimus illa, ne sciamus,
aut ne quis malus inuidere possit,
cum tantum sciat esse basiorum.
(GAIUS VALERIUS CATULLUS)
---------------------------------------------------------------------------

V. ad Lesbiam

VIVAMUS mea Lesbia, atque amemus,
rumoresque senum severiorum
omnes unius aestimemus assis!
soles occidere et redire possunt:
nobis cum semel occidit breuis lux,
nox est perpetua una dormienda.
da mi basia mille, deinde centum,
dein mille altera, dein secunda centum,
deinde usque altera mille, deinde centum.
dein, cum milia multa fecerimus,
conturbabimus illa, ne sciamus,
aut ne quis malus inuidere possit,
cum tantum sciat esse basiorum.
(GAIUS VALERIUS CATULLUS)
---------------------------------------------------------------------------

1: V. ad Lesbiam
2:
3: VIVAMUS mea Lesbia, atque amemus,
4: rumoresque senum severiorum
5: omnes unius aestimemus assis!
6: soles occidere et redire possunt:
7: nobis cum semel occidit breuis lux,
8: nox est perpetua una dormienda.
9: da mi basia mille, deinde centum,
10: dein mille altera, dein secunda centum,
11: deinde usque altera mille, deinde centum.
12: dein, cum milia multa fecerimus,
13: conturbabimus illa, ne sciamus,
14: aut ne quis malus inuidere possit,
15: cum tantum sciat esse basiorum.
16: (GAIUS VALERIUS CATULLUS)
---------------------------------------------------------------------------

1: V. ad Lesbiam
2:
3: VIVAMUS mea Lesbia, atque amemus,
4: rumoresque senum severiorum
5: omnes unius aestimemus assis!
6: soles occidere et redire possunt:
7: nobis cum semel occidit breuis lux,
8: nox est perpetua una dormienda.
9: da mi basia mille, deinde centum,
10: dein mille altera, dein secunda centum,
11: deinde usque altera mille, deinde centum.
12: dein, cum milia multa fecerimus,
13: conturbabimus illa, ne sciamus,
14: aut ne quis malus inuidere possit,
15: cum tantum sciat esse basiorum.
16: (GAIUS VALERIUS CATULLUS)
---------------------------------------------------------------------------

['1: V. ad Lesbiam\n', '2: \n', '3: VIVAMUS mea Lesbia, atque amemus,\n', '4: ru
moresque senum severiorum\n', '5: omnes unius aestimemus assis!\n', '6: soles oc
cidere et redire possunt:\n', '7: nobis cum semel occidit breuis lux,\n', '8: no
x est perpetua una dormienda.\n', '9: da mi basia mille, deinde centum,\n', '10:
 dein mille altera, dein secunda centum,\n', '11: deinde usque altera mille, dei
nde centum.\n', '12: dein, cum milia multa fecerimus,\n', '13: conturbabimus ill
a, ne sciamus,\n', '14: aut ne quis malus inuidere possit,\n', '15: cum tantum s
ciat esse basiorum.\n', '16: (GAIUS VALERIUS CATULLUS)\n']

1: V. ad Lesbiam
16: (GAIUS VALERIUS CATULLUS)

1: V. ad Lesbiam
2:
3: VIVAMUS mea Lesbia, atque amemus,
4: rumoresque senum severiorum
5: omnes unius aestimemus assis!
6: soles occidere et redire possunt:
7: nobis cum semel occidit breuis lux,
8: nox est perpetua una dormienda.
9: da mi basia mille, deinde centum,
10: dein mille altera, dein secunda centum,
11: deinde usque altera mille, deinde centum.
12: dein, cum milia multa fecerimus,
13: conturbabimus illa, ne sciamus,
14: aut ne quis malus inuidere possit,
15: cum tantum sciat esse basiorum.
16: (GAIUS VALERIUS CATULLUS)
---------------------------------------------------------------------------

1: V. ad Lesbiam
2:
3: VIVAMUS mea Lesbia, atque amemus,
4: rumoresque senum severiorum
5: omnes unius aestimemus assis!
6: soles occidere et redire possunt:
7: nobis cum semel occidit breuis lux,
8: nox est perpetua una dormienda.
9: da mi basia mille, deinde centum,
10: dein mille altera, dein secunda centum,
11: deinde usque altera mille, deinde centum.
12: dein, cum milia multa fecerimus,
13: conturbabimus illa, ne sciamus,
14: aut ne quis malus inuidere possit,
15: cum tantum sciat esse basiorum.
16: (GAIUS VALERIUS CATULLUS)


)SULLUTAC SUIRELAV SUIAG( :61
.muroisab esse taics mutnat muc :51
,tissop erediuni sulam siuq en tua :41
,sumaics en ,alli sumibabrutnoc :31
,sumirecef atlum ailim muc ,nied :21
.mutnec ednied ,ellim aretla euqsu ednied :11
,mutnec adnuces nied ,aretla ellim nied :01
,mutnec ednied ,ellim aisab im ad :9
.adneimrod anu auteprep tse xon :8
,xul siuerb tidicco lemes muc sibon :7
:tnussop erider te eredicco selos :6
!sissa sumemitsea suinu senmo :5
muroireves munes euqseromur :4
,sumema euqta ,aibseL aem SUMAVIV :3
 :2
maibseL da .V :1
"""