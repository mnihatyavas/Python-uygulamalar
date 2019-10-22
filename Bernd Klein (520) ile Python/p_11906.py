#coding:iso-8859-9 T�rk�e
# p_11906.py: f"{}" format�yla al��veri� fi�i yazd�rma �rne�i.

fiyat = 1957.83
print (f"Euro cinsinden fiyat�: {fiyat:,}" )
print (f"�svi�re Frank'� cinsinden fiyat�: {fiyat * 1.086:,}" )
print (f"�svi�re Frank'� cinsinden fiyat�: {fiyat * 1.086:,.2f}" )
print (f"ABD $'� cinsinden fiyat�: {fiyat * 1.12:,.2f}" )
#------------------------------------------------------------------------------------------------------

print ("\nAl��veri� fi�i:")
al��veri� = {"Ekmek":4, "Kola":12.75, "�ay":5.45, "S�t":8.65, "Sabun":4.5, "�eker":19.65}
yekun = 0
for al�nan in al��veri�.keys():
    yekun = yekun + al��veri�[al�nan]
    print (f"{al�nan:>10}: {al��veri�[al�nan]:>5.2f}" )
print ("    -------------" )
print (f"    Toplam: {yekun:.2f}" )


"""��kt�:
>python p_11906.py
Euro cinsinden fiyat�: 1,957.83
�svi�re Frank'� cinsinden fiyat�: 2,126.20338
�svi�re Frank'� cinsinden fiyat�: 2,126.20
ABD $'� cinsinden fiyat�: 2,192.77

Al��veri� fi�i:
     Ekmek:  4.00
      Kola: 12.75
       �ay:  5.45
       S�t:  8.65
     Sabun:  4.50
     �eker: 19.65
    -------------
    Toplam: 55.00
"""