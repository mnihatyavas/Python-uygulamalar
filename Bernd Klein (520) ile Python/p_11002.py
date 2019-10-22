# coding:iso-8859-9 Türkçe
# p_11002.py: Yabancı dil sözlükleri arasında aranan kelime ilişkileri örneği.

# Sözlükler arası ilişki mümkündür. İn_Fr veya Tr_Al ve Tr_Fr yokken
# bu kelimelerin eşdeğerleri ilişkisel elde edilebilir...

İn_Al = {"red" : "rot", "green" : "grün", "blue" : "blau", "yellow":"gelb"}
Al_Fr = {"rot" : "rouge", "grün" : "vert", "blau" : "bleu", "gelb":"jaune"}
Tr_İn = {"kırmızı" : "red", "yeşil" : "green", "mavi" : "blue", "sarı":"yellow"}

print ("\nTürkçe('yeşil')->İngilizce:", Tr_İn["yeşil"], "\nİngilizce('yeşil')->Almanca:", İn_Al["green"],
    "\nAlmanca('yeşil')->Fransızca:", Al_Fr["grün"], "\nİngilizce('yeşil')->Fransızca:", Al_Fr[İn_Al["green"] ],
    "\nTürkçe('yeşil')->Fransızca:", Al_Fr[İn_Al[Tr_İn["yeşil"] ] ] )

print ("\nTürkçe('sarı')->İngilizce:", Tr_İn["sarı"], "\nİngilizce('sarı')->Almanca:", İn_Al["yellow"],
    "\nAlmanca('sarı')->Fransızca:", Al_Fr["gelb"], "\nİngilizce('sarı')->Fransızca:", Al_Fr[İn_Al["yellow"] ],
    "\nTürkçe('sarı')->Fransızca:", Al_Fr[İn_Al[Tr_İn["sarı"] ] ] )

print()
# Sözlüklerin sözlükleri yapılabilir...
S = {"tr_in": Tr_İn, "in_al" : İn_Al, "al_fr" : Al_Fr}
print ("Mavi->Fr->Alm->İng:", S["al_fr"]["blau"], S["in_al"]["blue"], S["tr_in"]["mavi"])


"""Çıktı:
>python p_11002.py

Türkçe('yeşil')->İngilizce: green
İngilizce('yeşil')->Almanca: grün
Almanca('yeşil')->Fransızca: vert
İngilizce('yeşil')->Fransızca: vert
Türkçe('yeşil')->Fransızca: vert

Türkçe('sarı')->İngilizce: yellow
İngilizce('sarı')->Almanca: gelb
Almanca('sarı')->Fransızca: jaune
İngilizce('sarı')->Fransızca: jaune
Türkçe('sarı')->Fransızca: jaune

Mavi->Fr->Alm->İng: bleu blau blue
"""