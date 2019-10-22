# coding:iso-8859-9 T�rk�e
# p_11002.py: Yabanc� dil s�zl�kleri aras�nda aranan kelime ili�kileri �rne�i.

# S�zl�kler aras� ili�ki m�mk�nd�r. �n_Fr veya Tr_Al ve Tr_Fr yokken
# bu kelimelerin e�de�erleri ili�kisel elde edilebilir...

�n_Al = {"red" : "rot", "green" : "gr�n", "blue" : "blau", "yellow":"gelb"}
Al_Fr = {"rot" : "rouge", "gr�n" : "vert", "blau" : "bleu", "gelb":"jaune"}
Tr_�n = {"k�rm�z�" : "red", "ye�il" : "green", "mavi" : "blue", "sar�":"yellow"}

print ("\nT�rk�e('ye�il')->�ngilizce:", Tr_�n["ye�il"], "\n�ngilizce('ye�il')->Almanca:", �n_Al["green"],
    "\nAlmanca('ye�il')->Frans�zca:", Al_Fr["gr�n"], "\n�ngilizce('ye�il')->Frans�zca:", Al_Fr[�n_Al["green"] ],
    "\nT�rk�e('ye�il')->Frans�zca:", Al_Fr[�n_Al[Tr_�n["ye�il"] ] ] )

print ("\nT�rk�e('sar�')->�ngilizce:", Tr_�n["sar�"], "\n�ngilizce('sar�')->Almanca:", �n_Al["yellow"],
    "\nAlmanca('sar�')->Frans�zca:", Al_Fr["gelb"], "\n�ngilizce('sar�')->Frans�zca:", Al_Fr[�n_Al["yellow"] ],
    "\nT�rk�e('sar�')->Frans�zca:", Al_Fr[�n_Al[Tr_�n["sar�"] ] ] )

print()
# S�zl�klerin s�zl�kleri yap�labilir...
S = {"tr_in": Tr_�n, "in_al" : �n_Al, "al_fr" : Al_Fr}
print ("Mavi->Fr->Alm->�ng:", S["al_fr"]["blau"], S["in_al"]["blue"], S["tr_in"]["mavi"])


"""��kt�:
>python p_11002.py

T�rk�e('ye�il')->�ngilizce: green
�ngilizce('ye�il')->Almanca: gr�n
Almanca('ye�il')->Frans�zca: vert
�ngilizce('ye�il')->Frans�zca: vert
T�rk�e('ye�il')->Frans�zca: vert

T�rk�e('sar�')->�ngilizce: yellow
�ngilizce('sar�')->Almanca: gelb
Almanca('sar�')->Frans�zca: jaune
�ngilizce('sar�')->Frans�zca: jaune
T�rk�e('sar�')->Frans�zca: jaune

Mavi->Fr->Alm->�ng: bleu blau blue
"""