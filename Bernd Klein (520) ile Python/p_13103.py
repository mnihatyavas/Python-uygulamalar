# coding:iso-8859-9 T�rk�e
# p_13103.py: dizge.split(ayra�, adet) ile dizge kelimelerini listeye �evirme �rne�i.

hukukKurslar� = "Let reverence for the laws be breathed by every American mother to the lisping babe that prattles on her lap. Let it be taught in schools, in seminaries, and in colleges. Let it be written in primers, spelling books, and in almanacs. Let it be preached from the pulpit, proclaimed in legislative halls, and enforced in the courts of justice. And, in short, let it become the political religion of the nation."
print ("Dizge kelimelerini listeye �evirme:", hukukKurslar�.split() )

sat�r = "James;Miller;��retmen;Python;JavaScript"
print ("\nVarsay�l� bo�luk yerine ';' ayrac�yla dizgeden listeye �evirme:", sat�r.split (";") )

mormonDini = "The god of the world's leading religion. The chief temple is in the holy city of New York."
print ("\n�lk 3 kelime ayr���r, kalan� ayr��madan listelenir:", mormonDini.split (" ", 3) )

mormonDini = "The god  \t of the world's leading religion. The chief temple is in the holy city of New York."
print ("\n' ' ayrac� �oklu bo�lukta ve '\\t'de �a��r�r:", mormonDini.split (" ", 5) )

print ("\nBu �a��rma 'None' ayrac�yla d�zeltilir:", mormonDini.split (None, 5) )

"""��kt�:
>python p_13103.py
Dizge kelimelerini listeye �evirme: ['Let', 'reverence', 'for', 'the', 'laws',
'be', 'breathed', 'by', 'every', 'American', 'mother', 'to', 'the', 'lisping',
'babe', 'that', 'prattles', 'on', 'her', 'lap.', 'Let', 'it', 'be', 'taught', 'in',
'schools,', 'in', 'seminaries,', 'and', 'in', 'colleges.', 'Let', 'it', 'be',
'written', 'in', 'primers,', 'spelling', 'books,', 'and', 'in', 'almanacs.', 'Let',
 'it', 'be', 'preached', 'from', 'the', 'pulpit,', 'proclaimed', 'in', 'legislative', 
'halls,', 'and', 'enforced', 'in', 'the', 'courts', 'of', 'justice.', 'And,', 'in',
'short,', 'let', 'it', 'become', 'the', 'political', 'religion', 'of', 'the', 'nation.']

Varsay�l� bo�luk yerine ';' ayrac�yla dizgeden listeye �evirme: ['James', 'Miller',
 '��retmen', 'Python', 'JavaScript']

�lk 3 kelime ayr���r, kalan� ayr��madan listelenir: ['The', 'god', 'of', 
"the world's leading religion. The chief temple is in the holy city of New York."]

' ' ayrac� �oklu bo�lukta ve '\t'de �a��r�r: ['The', 'god', '', '\t', 'of',
"the world's leading religion. The chief temple is in the holy city of New York."]

Bu �a��rma 'None' ayrac�yla d�zeltilir: ['The', 'god', 'of', 'the', "world's", 
'leading religion. The chief temple is in the holy city of New York.']

"""