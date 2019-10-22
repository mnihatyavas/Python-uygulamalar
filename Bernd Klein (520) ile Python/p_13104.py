# coding:iso-8859-9 T�rk�e
# p_13104.py: re.split'le se�ici ayr��t�rma ve re.sub'la kelimeleri de�i�tirme �rne�i.

import re

ba�kala��m = "OF bodies chang'd to various forms, I sing: Ye Gods, from whom these miracles did spring, Inspire my numbers with coelestial heat;..."
print ("Ayr��an noktalamas�z sadece harfli kelimeler listesi:", re.split ("\W+", ba�kala��m) )
print ("-"*75, "\n")
#---------------------------------------------------------------------------------------------------------

sat�rlar = ["soyad�: Obama, ad�: Barack, mesle�i: ABD Ba�kan�",
    "soyad�: Merkel, ad�: Angela, mesle�i: Alman �ans�ylesi",
    "soyad�: Ak�ener, ad�: Meral, mesle�i: �Y� Parti Ba�kan�"]

print ("re.split'le se�ici ayr��t�rma:")
for sat�r in sat�rlar: print (re.split (",* *\w*: ", sat�r) )

print ("\nre.split[1:]'le ilk elemans�z se�ici ayr��t�rma:")
for sat�r in sat�rlar: print (re.split (",* *\w*: ", sat�r)[1:] )
print ("-"*75, "\n")
#---------------------------------------------------------------------------------------------------------

dizge = "Evet, ben evet dedim ve tekrar Evet diyece�im."
sonu� = re.sub ("[eE]vet", "hay�r", dizge)
print ("Bulunan�n ba�ka ibareyle de�i�tirilmesi:", sonu�)

"""��kt�:
>python p_13104.py
Ayr��an noktalamas�z sadece harfli kelimeler listesi: ['OF', 'bodies', 'chang',
'd', 'to', 'various', 'forms', 'I', 'sing', 'Ye', 'Gods', 'from', 'whom', 'these',
'miracles', 'did', 'spring', 'Inspire', 'my', 'numbers', 'with', 'coelestial', 'heat', '']
---------------------------------------------------------------------------

re.split'le se�ici ayr��t�rma:
['', 'Obama', 'Barack', 'ABD Ba�kan�']
['', 'Merkel', 'Angela', 'Alman �ans�ylesi']
['', 'Ak�ener', 'Meral', '�Y� Parti Ba�kan�']

re.split[1:]'le ilk elemans�z se�ici ayr��t�rma:
['Obama', 'Barack', 'ABD Ba�kan�']
['Merkel', 'Angela', 'Alman �ans�ylesi']
['Ak�ener', 'Meral', '�Y� Parti Ba�kan�']
---------------------------------------------------------------------------

Bulunan�n ba�ka ibareyle de�i�tirilmesi: hay�r, ben hay�r dedim ve tekrar hay�r
diyece�im.
"""