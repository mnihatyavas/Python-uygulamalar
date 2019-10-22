# coding:iso-8859-9 Türkçe

sayı=saat=dakika=dilim=0; dizge=çıktı=am_pm=''
try:
    dizge = input ("Büyük noktalamasız bir tamsayı girin: ")
    eval (dizge)
except Exception: dizge = "19570417"
çıktı=''
if len (dizge) > 3:
    for i in range (len (dizge), 3, -3): çıktı = "," + dizge[i-3:i] + çıktı
    if len(dizge)+1 % 3 != 0: çıktı = dizge[:i-3] + çıktı
    print (çıktı)
else: print (dizge)
print()
dizge = input ("Saatı girin [11:59am]: ")
if  not (len(dizge)==7 and dizge.count(":") and (dizge.lower().count("am") or dizge.lower().count("pm"))):
    saat=11; dakika=59; am_pm="am"
else: saat = int (dizge[:dizge.index(":")]) % 12; dakika = int (dizge[dizge.index(":")+1:dizge.index(":")+3]) % 60; am_pm = dizge[len(dizge)-2:].lower()
print ("Türkiye saatı: [", saat, ":", dakika, am_pm, "]", sep="")
dilim = int (input ("Zaman bölgesi [1.Londra, 2.Tokyo, 3.NewYork]: "))
if dilim == 1: saat = saat - 3
elif dilim == 2: saat = saat + 4
else: saat = saat + 12
if saat > 12:
    saat = saat -12
    if am_pm == "am": am_pm = "pm"
    else: am_pm = "am"
elif saat < 0:
    saat = 12 + saat
    if am_pm == "am": am_pm = "pm"
    else: am_pm = "am"
print (dilim, ".'inci zaman bölgesinde şu anda saat: [", saat, ":", dakika, am_pm, "]'dir.", sep="")
