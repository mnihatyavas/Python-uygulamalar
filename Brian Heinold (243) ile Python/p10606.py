# coding:iso-8859-9 Türkçe

s1 = "ABCDEFGHIJKLMNOPQRSTUVXWYZ"
print ("İngiliz alfabesi:", s1)
print ("Tersten:", s1[::-1])
print ("Harf sayısı:", len(s1))

# Dizge değiştirilemez, fakat yeniden/değişik yaratılır...
s2 = s1[:3] + "Ç" + s1[3:7] + "Ğ" + s1[7:9] + "İ" + s1[9:15] + "Ö"
s2 += s1[15] + s1[17:21] + "Ü" + s1[21] + s1[-2:]
print ("\nTürk alfabesi:", end="")
for k in s2: print (k,end="")
print ("\nTersten:", end="")
for k in range (len(s2)-1, -1, -1): print (s2[k], end="")
print ("\nHarf sayısı:", len(s2))

Çıktı="""
İngiliz alfabesi: ABCDEFGHIJKLMNOPQRSTUVXWYZ
Tersten: ZYWXVUTSRQPONMLKJIHGFEDCBA
Harf sayısı: 26

Türk alfabesi: ABCÇDEFGĞHIİJKLMNOÖPRSTUÜVYZ
Tersten: ZYVÜUTSRPÖONMLKJİIHĞGFEDÇCBA
Harf sayısı: 28
"""