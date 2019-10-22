# coding:iso-8859-9 Türkçe

teklif1 = "Sayın "
teklif2 = "\n\nSize yeni Platin Artı İkramiyeli kartımızı %47.99 gibi\nçok özel bir tanıtım indirimiyle sunmaktan gurur duyuyorum.\n"
teklif3 = ", böyle bir teklif kimseye her gün pek sık yapılmaz;\nbu yüzden +90-800-314-1592 ücretsiz numaramızı hemen\naramanızı şiddetle tavsiye ediyorum.\nBöylesi indirimli tanıtım kampanya indirimini çok uzun süre devam\nettiremeyiz, "
teklif4 = ", bu yüzden hiç vakit yitirmeden\nhemen bizi aramalısınız!.."

giriş = input ("Açık ad soyadınızı giriniz: ")
if len(giriş) > 0:
    try: ad = giriş[:giriş.index(' ')]
    except ValueError: ad = giriş
    print (teklif1, giriş, teklif2, ad, teklif3, ad, teklif4, sep="")
