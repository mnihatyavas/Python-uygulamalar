# coding:iso-8859-9 Türkçe
# p_13103.py: dizge.split(ayraç, adet) ile dizge kelimelerini listeye çevirme örneği.

hukukKursları = "Let reverence for the laws be breathed by every American mother to the lisping babe that prattles on her lap. Let it be taught in schools, in seminaries, and in colleges. Let it be written in primers, spelling books, and in almanacs. Let it be preached from the pulpit, proclaimed in legislative halls, and enforced in the courts of justice. And, in short, let it become the political religion of the nation."
print ("Dizge kelimelerini listeye çevirme:", hukukKursları.split() )

satır = "James;Miller;öğretmen;Python;JavaScript"
print ("\nVarsayılı boşluk yerine ';' ayracıyla dizgeden listeye çevirme:", satır.split (";") )

mormonDini = "The god of the world's leading religion. The chief temple is in the holy city of New York."
print ("\nİlk 3 kelime ayrışır, kalanı ayrışmadan listelenir:", mormonDini.split (" ", 3) )

mormonDini = "The god  \t of the world's leading religion. The chief temple is in the holy city of New York."
print ("\n' ' ayracı çoklu boşlukta ve '\\t'de şaşırır:", mormonDini.split (" ", 5) )

print ("\nBu şaşırma 'None' ayracıyla düzeltilir:", mormonDini.split (None, 5) )

"""Çıktı:
>python p_13103.py
Dizge kelimelerini listeye çevirme: ['Let', 'reverence', 'for', 'the', 'laws',
'be', 'breathed', 'by', 'every', 'American', 'mother', 'to', 'the', 'lisping',
'babe', 'that', 'prattles', 'on', 'her', 'lap.', 'Let', 'it', 'be', 'taught', 'in',
'schools,', 'in', 'seminaries,', 'and', 'in', 'colleges.', 'Let', 'it', 'be',
'written', 'in', 'primers,', 'spelling', 'books,', 'and', 'in', 'almanacs.', 'Let',
 'it', 'be', 'preached', 'from', 'the', 'pulpit,', 'proclaimed', 'in', 'legislative', 
'halls,', 'and', 'enforced', 'in', 'the', 'courts', 'of', 'justice.', 'And,', 'in',
'short,', 'let', 'it', 'become', 'the', 'political', 'religion', 'of', 'the', 'nation.']

Varsayılı boşluk yerine ';' ayracıyla dizgeden listeye çevirme: ['James', 'Miller',
 'öğretmen', 'Python', 'JavaScript']

İlk 3 kelime ayrışır, kalanı ayrışmadan listelenir: ['The', 'god', 'of', 
"the world's leading religion. The chief temple is in the holy city of New York."]

' ' ayracı çoklu boşlukta ve '\t'de şaşırır: ['The', 'god', '', '\t', 'of',
"the world's leading religion. The chief temple is in the holy city of New York."]

Bu şaşırma 'None' ayracıyla düzeltilir: ['The', 'god', 'of', 'the', "world's", 
'leading religion. The chief temple is in the holy city of New York.']

"""