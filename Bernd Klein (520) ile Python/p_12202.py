# coding:iso-8859-9 Türkçe
# p_12202.py: Komut satırından argüman geçirme örneği.

import sys                

print ("TUI/TextUserInterface/MetinKullanıcıArayüzü argümanları:")
for argüman in sys.argv: print (argüman)

""" Çıktı:
>python p_12202.py
TUI/TextUserInterface/MetinKullanıcıArayüzü argümanları:
p_12202.py

 >python p_12202.py Ankara İstanbul İzmir Mersin  **TEKRAR**
TUI/TextUserInterface/MetinKullanıcıArayüzü argümanları:
p_12202.py
Ankara
İstanbul
İzmir
Mersin

>python p_12202.py "M.Nihat Yavaş" Yeşilyurt-Malatya 17/04/1957  **TEKRAR**
TUI/TextUserInterface/MetinKullanıcıArayüzü argümanları:
p_12202.py
M.Nihat Yavaş
Yeşilyurt-Malatya
17/04/1957
"""