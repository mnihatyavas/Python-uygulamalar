# coding:iso-8859-9 Türkçe

import re

def değiştir1 (uyan):
    harf = uyan.group()
    return harf.lower()
	
def değiştir2 (uyan):
    harf, sayı = uyan.groups()
    return harf.lower() + str (int (sayı)+10)

print ("İkincileri küçük ilk büyükharfleri küçült:",
    re.sub(r'([A-Z, ÇĞİÖŞÜ])[a-z, çğiöşü]', değiştir1, 'ŞEFTALİ Elma Kayısı İğde Üzüm Ğurma Öküzgözü ÇAMfıstığı') )
	
print ("\nHer büyükharften sonraki rakama 10 ekle:",
    re.sub (r'([A-Z, ÇĞİÖŞÜ])(\d)', değiştir2, 'A1 + B2 + C7 - Ü9 * İ8 / Ö3') )
