#coding:iso-8859-9 T�rk�e
# p_32601.py: Pandas serisinde �oklu endeks ve s�ralama �rne�i.

import pandas as pd

�ehirler = ["Viyana", "Hamburg", "Berlin", "Z�rih"]
�zellikleri = [("�lke", "y�z�l��m�", "n�fus", "yo�unluk")] * 4
endeks = [�ehirler, �zellikleri]
veriler = [
    ("Avusturya", 414.60, 1805681, int (1805681 / 414.6 * 100) / 100),
    ("Almanya", 755.00, 1760433, int (1760433 / 755 * 100) / 100),
    ("Almanya", 891.85, 3562166, int (3562166 / 891.85 * 100) / 100),
    ("�svi�re", 87.88, 378884, int (378884 / 87.88* 100) / 100) ]
�ehirlerSerisi = pd.Series (veriler, index=endeks)

print ("�ehirler ve �zellikleri'ne endeksli veriler serisi:\n", �ehirlerSerisi, sep="")
print ("-"*79)
#-------------------------------------------------------------------------------------------------------

�ehirler = [
    "Viyana", "Viyana", "Viyana", "Viyana",
    "Hamburg","Hamburg", "Hamburg", "Hamburg",
    "Berlin", "Berlin", "Berlin", "Berlin",
    "Z�rih", "Z�rih", "Z�rih", "Z�rih"]
�zellikleri = [
    "�lke", "y�z�l��m�", "n�fus", "yo�unluk",
    "�lke", "y�z�l��m�", "n�fus", "yo�unluk",
    "�lke", "y�z�l��m�", "n�fus", "yo�unluk",
    "�lke", "y�z�l��m�", "n�fus", "yo�unluk" ]
veriler = [
    "Avusturya", 414.60, 1805681, int (1805681 / 414.6 * 100) / 100,
    "Almanya", 755.00, 1760433, int (1760433 / 755 * 100) / 100,
    "Almanya", 891.85, 3562166, int (3562166 / 891.85 * 100) / 100,
    "�svi�re", 87.88, 378884, int (378884 / 87.88* 100) / 100 ]
endeks = [�ehirler, �zellikleri]
�ehirlerSerisi = pd.Series (veriler, index=endeks)

print ("\n4 fakl� �ehir ve �zellikleri'ne endeksli veriler serisi:\n", �ehirlerSerisi, sep="")
print ("-"*50)
#-------------------------------------------------------------------------------------------------------

�S= �ehirlerSerisi
print ("\nSadece Viyana'n�n �zellikli verileri:\n", �S ["Viyana"], sep="")

print ("\nViyana'n�n yo�unluk �zellikli verisi: ", �S ["Viyana"] ["yo�unluk"],
    "\nVeya: ", �S ["Viyana", "yo�unluk"], sep="")

print ("\nSadece Hamburg ve Z�rih'in �zellikli verileri:\n", �S [["Hamburg", "Z�rih"]], sep="")
print ("-"*50)
#-------------------------------------------------------------------------------------------------------

�S2 = �S.sort_index()
print ("\nT�m verileri artan s�ral� �ehirler serisi:\n", �S2, sep="")

print ("\n�ehirler aras�ndan dilim verileri:\n", �S2 ["Hamburg" : "Viyana"], sep="" )
print ("-"*40)
#-------------------------------------------------------------------------------------------------------

print ("\nT�m �ehirlerin sadece yo�unluk verileri:\n", �S [:, "yo�unluk"], sep="")
print ("-"*52)
#-------------------------------------------------------------------------------------------------------

�S3 = �S.swaplevel()
print ("\n�ehirler de�il �ZELL�KLER �ncelikli endeks verileri:\n", �S3, sep="")

�S3.sort_index (inplace=True)
print ("\n�zelliklere g�re artan s�ral� gruplanan veriler:\n", �S3, sep="")



"""��kt�:
>python p_32601.py
�ehirler ve �zellikleri'ne endeksli veriler serisi:
Viyana   (�lke, y�z�l��m�, n�fus, yo�unluk)    (Avusturya, 414.6, 1805681, 4355.23)
Hamburg  (�lke, y�z�l��m�, n�fus, yo�unluk)      (Almanya, 755.0, 1760433, 2331.69)
Berlin   (�lke, y�z�l��m�, n�fus, yo�unluk)     (Almanya, 891.85, 3562166, 3994.13)
Z�rih    (�lke, y�z�l��m�, n�fus, yo�unluk)       (�svi�re, 87.88, 378884, 4311.37)
dtype: object
-------------------------------------------------------------------------------

4 fakl� �ehir ve �zellikleri'ne endeksli veriler serisi:
Viyana   �lke         Avusturya
         y�z�l��m�        414.6
         n�fus          1805681
         yo�unluk       4355.23
Hamburg  �lke           Almanya
         y�z�l��m�          755
         n�fus          1760433
         yo�unluk       2331.69
Berlin   �lke           Almanya
         y�z�l��m�       891.85
         n�fus          3562166
         yo�unluk       3994.13
Z�rih    �lke           �svi�re
         y�z�l��m�        87.88
         n�fus           378884
         yo�unluk       4311.37
dtype: object
--------------------------------------------------

Sadece Viyana'n�n �zellikli verileri:
�lke         Avusturya
y�z�l��m�        414.6
n�fus          1805681
yo�unluk       4355.23
dtype: object

Viyana'n�n yo�unluk �zellikli verisi: 4355.23
Veya: 4355.23

Sadece Hamburg ve Z�rih'in �zellikli verileri:
Hamburg  �lke         Almanya
         y�z�l��m�        755
         n�fus        1760433
         yo�unluk     2331.69
Z�rih    �lke         �svi�re
         y�z�l��m�      87.88
         n�fus         378884
         yo�unluk     4311.37
dtype: object
--------------------------------------------------

T�m verileri artan s�ral� �ehirler serisi:
Berlin   n�fus          3562166
         yo�unluk       3994.13
         y�z�l��m�       891.85
         �lke           Almanya
Hamburg  n�fus          1760433
         yo�unluk       2331.69
         y�z�l��m�          755
         �lke           Almanya
Viyana   n�fus          1805681
         yo�unluk       4355.23
         y�z�l��m�        414.6
         �lke         Avusturya
Z�rih    n�fus           378884
         yo�unluk       4311.37
         y�z�l��m�        87.88
         �lke           �svi�re
dtype: object

�ehirler aras�ndan dilim verileri:
Hamburg  n�fus          1760433
         yo�unluk       2331.69
         y�z�l��m�          755
         �lke           Almanya
Viyana   n�fus          1805681
         yo�unluk       4355.23
         y�z�l��m�        414.6
         �lke         Avusturya
dtype: object
----------------------------------------

T�m �ehirlerin sadece yo�unluk verileri:
Viyana     4355.23
Hamburg    2331.69
Berlin     3994.13
Z�rih      4311.37
dtype: object
----------------------------------------------------

�ehirler de�il �ZELL�KLER �ncelikli endeks verileri:
�lke       Viyana     Avusturya
y�z�l��m�  Viyana         414.6
n�fus      Viyana       1805681
yo�unluk   Viyana       4355.23
�lke       Hamburg      Almanya
y�z�l��m�  Hamburg          755
n�fus      Hamburg      1760433
yo�unluk   Hamburg      2331.69
�lke       Berlin       Almanya
y�z�l��m�  Berlin        891.85
n�fus      Berlin       3562166
yo�unluk   Berlin       3994.13
�lke       Z�rih        �svi�re
y�z�l��m�  Z�rih          87.88
n�fus      Z�rih         378884
yo�unluk   Z�rih        4311.37
dtype: object

�zelliklere g�re artan s�ral� gruplanan veriler:
n�fus      Berlin       3562166
           Hamburg      1760433
           Viyana       1805681
           Z�rih         378884
yo�unluk   Berlin       3994.13
           Hamburg      2331.69
           Viyana       4355.23
           Z�rih        4311.37
y�z�l��m�  Berlin        891.85
           Hamburg          755
           Viyana         414.6
           Z�rih          87.88
�lke       Berlin       Almanya
           Hamburg      Almanya
           Viyana     Avusturya
           Z�rih        �svi�re
dtype: object
"""