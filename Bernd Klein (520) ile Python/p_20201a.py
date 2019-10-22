# coding:iso-8859-9 T�rk�e
# p_20201a.py: Dizgesel input'a kar��l�k tek karakterlik getch() giri�i �rne�i.

from msvcrt import getch # Windows i�in tek karakter giri�i...

a = input ("�stedi�inizi girin [Ent:son]: ")
print (a)

print ("\nTek karakter giri�i [q:son]==>")
while True:
    a = getch()
    print (chr (a[0]), "=", a[0])
    if a[0] == 113: break

"""��kt�:
>python p_20201.py
�stedi�inizi girin [Ent:son]: M.Nihat Yava�, 1957, TR
M.Nihat Yava�, 1957, TR

Tek karakter giri�i [q:son]==>
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