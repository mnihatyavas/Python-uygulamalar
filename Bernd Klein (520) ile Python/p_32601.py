#coding:iso-8859-9 Türkçe
# p_32601.py: Pandas serisinde çoklu endeks ve sıralama örneği.

import pandas as pd

şehirler = ["Viyana", "Hamburg", "Berlin", "Zürih"]
özellikleri = [("ülke", "yüzölçümü", "nüfus", "yoğunluk")] * 4
endeks = [şehirler, özellikleri]
veriler = [
    ("Avusturya", 414.60, 1805681, int (1805681 / 414.6 * 100) / 100),
    ("Almanya", 755.00, 1760433, int (1760433 / 755 * 100) / 100),
    ("Almanya", 891.85, 3562166, int (3562166 / 891.85 * 100) / 100),
    ("İsviçre", 87.88, 378884, int (378884 / 87.88* 100) / 100) ]
şehirlerSerisi = pd.Series (veriler, index=endeks)

print ("Şehirler ve özellikleri'ne endeksli veriler serisi:\n", şehirlerSerisi, sep="")
print ("-"*79)
#-------------------------------------------------------------------------------------------------------

şehirler = [
    "Viyana", "Viyana", "Viyana", "Viyana",
    "Hamburg","Hamburg", "Hamburg", "Hamburg",
    "Berlin", "Berlin", "Berlin", "Berlin",
    "Zürih", "Zürih", "Zürih", "Zürih"]
özellikleri = [
    "ülke", "yüzölçümü", "nüfus", "yoğunluk",
    "ülke", "yüzölçümü", "nüfus", "yoğunluk",
    "ülke", "yüzölçümü", "nüfus", "yoğunluk",
    "ülke", "yüzölçümü", "nüfus", "yoğunluk" ]
veriler = [
    "Avusturya", 414.60, 1805681, int (1805681 / 414.6 * 100) / 100,
    "Almanya", 755.00, 1760433, int (1760433 / 755 * 100) / 100,
    "Almanya", 891.85, 3562166, int (3562166 / 891.85 * 100) / 100,
    "İsviçre", 87.88, 378884, int (378884 / 87.88* 100) / 100 ]
endeks = [şehirler, özellikleri]
şehirlerSerisi = pd.Series (veriler, index=endeks)

print ("\n4 faklı şehir ve özellikleri'ne endeksli veriler serisi:\n", şehirlerSerisi, sep="")
print ("-"*50)
#-------------------------------------------------------------------------------------------------------

şS= şehirlerSerisi
print ("\nSadece Viyana'nın özellikli verileri:\n", şS ["Viyana"], sep="")

print ("\nViyana'nın yoğunluk özellikli verisi: ", şS ["Viyana"] ["yoğunluk"],
    "\nVeya: ", şS ["Viyana", "yoğunluk"], sep="")

print ("\nSadece Hamburg ve Zürih'in özellikli verileri:\n", şS [["Hamburg", "Zürih"]], sep="")
print ("-"*50)
#-------------------------------------------------------------------------------------------------------

şS2 = şS.sort_index()
print ("\nTüm verileri artan sıralı şehirler serisi:\n", şS2, sep="")

print ("\nŞehirler arasından dilim verileri:\n", şS2 ["Hamburg" : "Viyana"], sep="" )
print ("-"*40)
#-------------------------------------------------------------------------------------------------------

print ("\nTüm şehirlerin sadece yoğunluk verileri:\n", şS [:, "yoğunluk"], sep="")
print ("-"*52)
#-------------------------------------------------------------------------------------------------------

şS3 = şS.swaplevel()
print ("\nŞehirler değil ÖZELLİKLER öncelikli endeks verileri:\n", şS3, sep="")

şS3.sort_index (inplace=True)
print ("\nÖzelliklere göre artan sıralı gruplanan veriler:\n", şS3, sep="")



"""Çıktı:
>python p_32601.py
Şehirler ve özellikleri'ne endeksli veriler serisi:
Viyana   (ülke, yüzölçümü, nüfus, yoğunluk)    (Avusturya, 414.6, 1805681, 4355.23)
Hamburg  (ülke, yüzölçümü, nüfus, yoğunluk)      (Almanya, 755.0, 1760433, 2331.69)
Berlin   (ülke, yüzölçümü, nüfus, yoğunluk)     (Almanya, 891.85, 3562166, 3994.13)
Zürih    (ülke, yüzölçümü, nüfus, yoğunluk)       (İsviçre, 87.88, 378884, 4311.37)
dtype: object
-------------------------------------------------------------------------------

4 faklı şehir ve özellikleri'ne endeksli veriler serisi:
Viyana   ülke         Avusturya
         yüzölçümü        414.6
         nüfus          1805681
         yoğunluk       4355.23
Hamburg  ülke           Almanya
         yüzölçümü          755
         nüfus          1760433
         yoğunluk       2331.69
Berlin   ülke           Almanya
         yüzölçümü       891.85
         nüfus          3562166
         yoğunluk       3994.13
Zürih    ülke           İsviçre
         yüzölçümü        87.88
         nüfus           378884
         yoğunluk       4311.37
dtype: object
--------------------------------------------------

Sadece Viyana'nın özellikli verileri:
ülke         Avusturya
yüzölçümü        414.6
nüfus          1805681
yoğunluk       4355.23
dtype: object

Viyana'nın yoğunluk özellikli verisi: 4355.23
Veya: 4355.23

Sadece Hamburg ve Zürih'in özellikli verileri:
Hamburg  ülke         Almanya
         yüzölçümü        755
         nüfus        1760433
         yoğunluk     2331.69
Zürih    ülke         İsviçre
         yüzölçümü      87.88
         nüfus         378884
         yoğunluk     4311.37
dtype: object
--------------------------------------------------

Tüm verileri artan sıralı şehirler serisi:
Berlin   nüfus          3562166
         yoğunluk       3994.13
         yüzölçümü       891.85
         ülke           Almanya
Hamburg  nüfus          1760433
         yoğunluk       2331.69
         yüzölçümü          755
         ülke           Almanya
Viyana   nüfus          1805681
         yoğunluk       4355.23
         yüzölçümü        414.6
         ülke         Avusturya
Zürih    nüfus           378884
         yoğunluk       4311.37
         yüzölçümü        87.88
         ülke           İsviçre
dtype: object

Şehirler arasından dilim verileri:
Hamburg  nüfus          1760433
         yoğunluk       2331.69
         yüzölçümü          755
         ülke           Almanya
Viyana   nüfus          1805681
         yoğunluk       4355.23
         yüzölçümü        414.6
         ülke         Avusturya
dtype: object
----------------------------------------

Tüm şehirlerin sadece yoğunluk verileri:
Viyana     4355.23
Hamburg    2331.69
Berlin     3994.13
Zürih      4311.37
dtype: object
----------------------------------------------------

Şehirler değil ÖZELLİKLER öncelikli endeks verileri:
ülke       Viyana     Avusturya
yüzölçümü  Viyana         414.6
nüfus      Viyana       1805681
yoğunluk   Viyana       4355.23
ülke       Hamburg      Almanya
yüzölçümü  Hamburg          755
nüfus      Hamburg      1760433
yoğunluk   Hamburg      2331.69
ülke       Berlin       Almanya
yüzölçümü  Berlin        891.85
nüfus      Berlin       3562166
yoğunluk   Berlin       3994.13
ülke       Zürih        İsviçre
yüzölçümü  Zürih          87.88
nüfus      Zürih         378884
yoğunluk   Zürih        4311.37
dtype: object

Özelliklere göre artan sıralı gruplanan veriler:
nüfus      Berlin       3562166
           Hamburg      1760433
           Viyana       1805681
           Zürih         378884
yoğunluk   Berlin       3994.13
           Hamburg      2331.69
           Viyana       4355.23
           Zürih        4311.37
yüzölçümü  Berlin        891.85
           Hamburg          755
           Viyana         414.6
           Zürih          87.88
ülke       Berlin       Almanya
           Hamburg      Almanya
           Viyana     Avusturya
           Zürih        İsviçre
dtype: object
"""