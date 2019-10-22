# coding:iso-8859-9 Türkçe

s = ''
for i in range (10000):
    k = input ('Bir karakter gir [Çık:q/Q]: ')
    if  k=='q' or k=='Q': break
    s = s + k
print ("-"*50, "\nGirdiğiniz cümle: ", s, "\n", "-"*50, sep="")

if "ş" in s: print ("Girdiğiniz cümlede 'ş' harfi mevcuttur.")
if "Yavaş" in s: print ("Girdiğiniz cümlede 'Yavaş' kelimesi mevcuttur.")
if ("ş" or "Ş" or "ç" or "Ç" or "ğ" or "Ğ" or "ı" or "İ" or "ö" or "Ö" or "ü" or "Ü") in s:
    print ("Girdiğiniz cümle Türkçe karakter içermektedir.")
if ("." or "," or ":" or ";" or ".." or "...") in s:
    print ("Girdiğiniz cümle noktalama karakteri içermektedir.")
