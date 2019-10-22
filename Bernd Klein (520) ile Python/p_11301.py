# coding:iso-8859-9 T�rk�e
# p_11301.py: input ile klavyeden girilen say�sal veya dizgesel verilerin de�erlendirilmesi �rne�i.

ad = input ("Ad�n�z� ��renebilir miyim?: ")
if ad == "": ad = "Nihat"
print ("Tan��t���m�za memnun oldum, " + ad + "!")

try: ya� = abs (int (eval (input ("\nPeki ya��n�z? "))))
except: ya� = 62
print ("O halde, halihaz�rda siz " + str (ya�) + " ya��ndas�n�z ve " + str (2019-ya�) + " do�umlusunuz, " + ad + "!")
#-----------------------------------------------------------------------------------------------------

�ehirler = input ('\nT�rkiyenin b�y�k birka� �ehrini girin: ')
if �ehirler == "": �ehirler = "Ankara, �stanbul, �zmir"
print ("Girilen �ehirler: " + �ehirler + "\nVeri tipi: " + str (type (�ehirler)) )

try: �ehirler = eval (input ('\nTekrar birka� �ehir girin ["..", "..",..]: '))
except: �ehirler = ["Ankara", "�stanbul", "�zmir"]
print ("Girilen �ehirler:", �ehirler, "\nVeri tipi: ", type (�ehirler) )

n�fus = input ('\nT�rkiyenin yakla��k n�fusunu girin: ')
if n�fus == "": n�fus = "80,000,000"
print ("T�rkiye'nin yakla��k n�fusu: " + n�fus + "\nVeri tipi: " + str (type (n�fus)) )

try: n�fus = eval (input ('\nSay�sal n�fusu tekrar girin: '))
except: n�fus = 80000000
print ("Yakla��k n�fus:", n�fus, "\nVeri tipi: ", type (n�fus) )

"""��kt�
>python p_11301.py
Ad�n�z� ��renebilir miyim?:
Tan��t���m�za memnun oldum, Nihat!

Peki ya��n�z?
O halde, halihaz�rda siz 62 ya��ndas�n�z ve 1957 do�umlusunuz, Nihat!

T�rkiyenin b�y�k birka� �ehrini girin:
Girilen �ehirler: Ankara, �stanbul, �zmir
Veri tipi: <class 'str'>

Tekrar birka� �ehir girin ["..", "..",..]:
Girilen �ehirler: ['Ankara', '�stanbul', '�zmir']
Veri tipi:  <class 'list'>

T�rkiyenin yakla��k n�fusunu girin:
T�rkiye'nin yakla��k n�fusu: 80,000,000
Veri tipi: <class 'str'>

Say�sal n�fusu tekrar girin:
Yakla��k n�fus: 80000000
Veri tipi:  <class 'int'>
"""