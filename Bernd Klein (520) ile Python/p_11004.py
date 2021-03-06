# coding:iso-8859-9 T�rk�e
# p_11004.py: K�sa(.) ve uzun(-) sinyallerle A->Z ve 0->9 mors alfabesi s�zl��� �rne�i.

mors = {
"A" : ".-",
"B" : "-...",
"C" : "-.-.",
"D" : "-..",
"E" : ".",
"F" : "..-.",
"G" : "--.",
"H" : "....",
"I" : "..",
"J" : ".---",
"K" : "-.-",
"L" : ".-..",
"M" : "--",
"N" : "-.",
"O" : "---",
"P" : ".--.",
"Q" : "--.-",
"R" : ".-.",
"S" : "...",
"T" : "-",
"U" : "..-",
"V" : "...-",
"W" : ".--",
"X" : "-..-",
"Y" : "-.--",
"Z" : "--..",
"0" : "-----",
"1" : ".----",
"2" : "..---",
"3" : "...--",
"4" : "....-",
"5" : ".....",
"6" : "-....",
"7" : "--...",
"8" : "---..",
"9" : "----.",
"." : ".-.-.-",
"," : "--..--"
}

print ("Mors alfabesi:", mors)
print ("Anahtar-de�er �ifti say�s�:", len (mors) )
print ("'a' in mors:", "a" in mors)
print ("'a' not in mors:", "a" not in mors)
print ("'A' in mors:", "A" in mors)


"""��kt�:
>python p_11004.py
Mors alfabesi: {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F':
'..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..'
, 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '
...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', '
Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-'
, '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-
.-.-', ',': '--..--'}
Anahtar-de�er �ifti say�s�: 38
'a' in mors: False
'a' not in mors: True
'A' in mors: True
"""