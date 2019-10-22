# coding:iso-8859-9
# p_13703.py: Fonksiyon nesnesinin �zelli�i, parametresi ve return'� �rne�i.

def fonk1 (x): return 42

fonk1.x = 42
print ("S�n�f nesnesine oldu�u gibi fonksiyon nesnesine de attribute:at�f/�zellik verilebilir")
print (fonk1 (10), fonk1.x)
#----------------------------------------------------------------------------------

def fonk2 (x):
    fonk2.saya� = getattr (fonk2, "saya�",  0) + 1 
    return "MontyPython"

for i in range (20): fonk2 (i)

print (fonk2.saya�, fonk2 (10) )

"""��kt�:
>python p_13703.py
S�n�f nesnesine oldu�u gibi fonksiyon nesnesine de attribute:at�f/�zellik verilebilir
42 42
20 MontyPython
"""