# coding:iso-8859-9 Türkçe
# p_20202.py: Veri giriş input'la .exe programları işletme örneği.

import os

a = " "
while (a != "exit"):
    a = input ("Veri girişi [Çıkış: exit]: ")
    dosya = os.popen (a)
    print (dosya.read())

print ("Heyyaah, bu iş bu kadar!..")

"""Çıktı:
>python p_20202.py
Veri girişi: M.Nihat Yavaş
'M.Nihat' iç ya da dış komut, çalıştırılabilir
program ya da toplu iş dosyası olarak tanınmıyor.

Veri girişi: write # WordPad açılır...

Veri girişi: notepad # NotePad açılır...

Veri girişi: mspaint # MSPaint açılır...

Veri girişi: exit

Heyyaah, bu iş bu kadar!..
"""