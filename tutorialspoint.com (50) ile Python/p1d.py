# coding:iso-8859-9 T�rk�e

kelime = 'kelime'
c�mle = "Bu, b�y�kharfle ba�lay�p noktayla biten tek sat�rl�k bir c�mledir."
paragraf = """Bu ise bir paragraft�r.
Bir c�mle 2 t�rnak aras�ndaki tek sat�rl�k metinken,
bir paragraf birden �ok sat�rl�k metinden olu�abilir.
Paragraf ba�lang�c� 3 t�rnakla ba�lar ve
biti�i de yine 3 t�rnakla olmal�d�r."""

# Tek sat�rl�k yorumumuz...
print (kelime, "\n") # Bu da bir yorumdur...
print (c�mle, "\n")
print (paragraf)

# Python'da �oklu yorum sat�r� sembol� yoktur.
# �oklu yorum sat�r� gireceksek,
# herbir yorum sat�r�n� teker teker yazmal�y�z.

input ("\n\nDevam i�in Ent tu�una bas�n: ")

import sys; x = '�oklu ifade sat�r�'; sys.stdout.write (x + '\n') # print(..) ile ayn�d�r...
