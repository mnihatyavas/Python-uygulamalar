#coding:iso-8859-9 Türkçe
# p_11906.py: f"{}" formatıyla alışveriş fişi yazdırma örneği.

fiyat = 1957.83
print (f"Euro cinsinden fiyatı: {fiyat:,}" )
print (f"İsviçre Frank'ı cinsinden fiyatı: {fiyat * 1.086:,}" )
print (f"İsviçre Frank'ı cinsinden fiyatı: {fiyat * 1.086:,.2f}" )
print (f"ABD $'ı cinsinden fiyatı: {fiyat * 1.12:,.2f}" )
#------------------------------------------------------------------------------------------------------

print ("\nAlışveriş fişi:")
alışveriş = {"Ekmek":4, "Kola":12.75, "Çay":5.45, "Süt":8.65, "Sabun":4.5, "Şeker":19.65}
yekun = 0
for alınan in alışveriş.keys():
    yekun = yekun + alışveriş[alınan]
    print (f"{alınan:>10}: {alışveriş[alınan]:>5.2f}" )
print ("    -------------" )
print (f"    Toplam: {yekun:.2f}" )


"""Çıktı:
>python p_11906.py
Euro cinsinden fiyatı: 1,957.83
İsviçre Frank'ı cinsinden fiyatı: 2,126.20338
İsviçre Frank'ı cinsinden fiyatı: 2,126.20
ABD $'ı cinsinden fiyatı: 2,192.77

Alışveriş fişi:
     Ekmek:  4.00
      Kola: 12.75
       Çay:  5.45
       Süt:  8.65
     Sabun:  4.50
     Şeker: 19.65
    -------------
    Toplam: 55.00
"""