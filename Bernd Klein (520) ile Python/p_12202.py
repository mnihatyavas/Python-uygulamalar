# coding:iso-8859-9 T�rk�e
# p_12202.py: Komut sat�r�ndan arg�man ge�irme �rne�i.

import sys                

print ("TUI/TextUserInterface/MetinKullan�c�Aray�z� arg�manlar�:")
for arg�man in sys.argv: print (arg�man)

""" ��kt�:
>python p_12202.py
TUI/TextUserInterface/MetinKullan�c�Aray�z� arg�manlar�:
p_12202.py

 >python p_12202.py Ankara �stanbul �zmir Mersin  **TEKRAR**
TUI/TextUserInterface/MetinKullan�c�Aray�z� arg�manlar�:
p_12202.py
Ankara
�stanbul
�zmir
Mersin

>python p_12202.py "M.Nihat Yava�" Ye�ilyurt-Malatya 17/04/1957  **TEKRAR**
TUI/TextUserInterface/MetinKullan�c�Aray�z� arg�manlar�:
p_12202.py
M.Nihat Yava�
Ye�ilyurt-Malatya
17/04/1957
"""