# coding:iso-8859-9 Türkçe
# p_20201a.py: Dizgesel input'a karşılık tek karakterlik getch() girişi örneği.

from msvcrt import getch # Windows için tek karakter girişi...

a = input ("İstediğinizi girin [Ent:son]: ")
print (a)

print ("\nTek karakter girişi [q:son]==>")
while True:
    a = getch()
    print (chr (a[0]), "=", a[0])
    if a[0] == 113: break

"""Çıktı:
>python p_20201.py
İstediğinizi girin [Ent:son]: M.Nihat Yavaş, 1957, TR
M.Nihat Yavaş, 1957, TR

Tek karakter girişi [q:son]==>
M = 77
. = 46
N = 78
i = 105
h = 104
a = 97
t = 116
  = 32
Y = 89
a = 97
v = 118
a = 97
? = 159
, = 44
  = 32
1 = 49
9 = 57
5 = 53
7 = 55
, = 44
  = 32
T = 84
R = 82
q = 113
"""