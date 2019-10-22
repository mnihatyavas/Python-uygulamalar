# coding:iso-8859-9 T�rk�e

import re

def de�i�tir1 (uyan):
    harf = uyan.group()
    return harf.lower()
	
def de�i�tir2 (uyan):
    harf, say� = uyan.groups()
    return harf.lower() + str (int (say�)+10)

print ("�kincileri k���k ilk b�y�kharfleri k���lt:",
    re.sub(r'([A-Z, ������])[a-z, ��i���]', de�i�tir1, '�EFTAL� Elma Kay�s� ��de �z�m �urma �k�zg�z� �AMf�st���') )
	
print ("\nHer b�y�kharften sonraki rakama 10 ekle:",
    re.sub (r'([A-Z, ������])(\d)', de�i�tir2, 'A1 + B2 + C7 - �9 * �8 / �3') )
