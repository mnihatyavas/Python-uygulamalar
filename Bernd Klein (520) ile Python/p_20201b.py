# coding:iso-8859-9 T�rk�e
# p_20201b.py: Platforman ba��ms�z tek karakterlik veri giri�i �rne�i.

import os, platform
if platform.system() == "Windows": import msvcrt
    
print ("Herhangibir tu�a bas�n [q:son]")
while True:
    # Platformdan ba��ms�z karakter giri�i...
    if platform.system() == "Linux": krk = os.system ("bash -c \"read -n 1\"")
    else: krk = msvcrt.getch()

    if krk[0] == 113: break
    print (chr (krk[0]), "=", krk[0])

print ("\n'q' ile veri giri�i sonland�r�ld�.")

"""��kt�:
>python p_20201b.py
Herhangibir tu�a bas�n [q:son]
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

'q' ile veri giri�i sonland�r�ld�.
"""