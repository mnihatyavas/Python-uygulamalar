# coding:iso-8859-9
# p_13703.py: Fonksiyon nesnesinin özelliği, parametresi ve return'ü örneği.

def fonk1 (x): return 42

fonk1.x = 42
print ("Sınıf nesnesine olduğu gibi fonksiyon nesnesine de attribute:atıf/özellik verilebilir")
print (fonk1 (10), fonk1.x)
#----------------------------------------------------------------------------------

def fonk2 (x):
    fonk2.sayaç = getattr (fonk2, "sayaç",  0) + 1 
    return "MontyPython"

for i in range (20): fonk2 (i)

print (fonk2.sayaç, fonk2 (10) )

"""Çıktı:
>python p_13703.py
Sınıf nesnesine olduğu gibi fonksiyon nesnesine de attribute:atıf/özellik verilebilir
42 42
20 MontyPython
"""