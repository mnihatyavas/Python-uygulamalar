# coding:iso-8859-9 T�rk�e
# p_21401.py: Anahtar-de�er �iftli s�zl�k verilerinde anahtar hatas� istisnas� �rne�i.

il�eler = {
    "Akdenizz": "Mersin",
    "Ku�adas": "Ayd�n",
    "�skendurun": "Hatay",
    "Ye�ilyurd": "Malatya",
    "Alenya": "Antalya",
    "Al�ancak": "�zmir",
    "Kizalay": "Ankara",
    "�sk�tar": "�stanbul",
    "�ekirke": "Bursa",
    "Band�rna": "Bal�kesir" }

try:
    print ("�l�elerin ba�l� olduklar� iller:")
    print (il�eler ["Akdeniz"] )
    print (il�eler ["Ku�adas�"] )
    print (il�eler ["�skenderun"] )
    print (il�eler ["Ye�ilyurt"] )
    print (il�eler ["Alanya"] )
    print (il�eler ["Alsancak"] )
    print (il�eler ["K�z�lay"] )
    print (il�eler ["�sk�dar"] )
    print (il�eler ["�ekirge"] )
    print (il�eler ["Band�rma"] )
except Exception as ist: print ("[KeyError/AnahtarHatas�]:", ist)



"""��kt�:
>python p_21401.py
�l�elerin ba�l� olduklar� iller:
[KeyError/AnahtarHatas�]: 'Akdeniz'
"""