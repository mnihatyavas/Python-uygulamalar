# coding:iso-8859-9 Türkçe
# p_30601.py: random.random() ve random.SystemRandom().random() ile normal ve güvenli tesadüfi (0,1) sayı üretme örneği.

import random

gelişigüzelSayı1 = random.random()
gelişigüzelSayı2 = random.SystemRandom().random()

print ("random.random() ile [0->1) arası gelişigüzel bir sayı:", gelişigüzelSayı1)
print ("random.SystemRandom().random() ile gelişigüzel bir sayı:", gelişigüzelSayı2)
print ("-"*79)
#-------------------------------------------------------------------------------------------------------

def gelişigüzelListe (adet, güvenliMi=True):
    liste = []
    for _ in range (adet):
        if güvenliMi: gelişigüzel = random.SystemRandom().random()
        else: gelişigüzel = random.random()
        liste.append (gelişigüzel)
    liste.sort()
    return liste

try: n = abs (int (input ("\nKaç adet tesadüfi sayı üreteceksin? ")))
except: n = 10

cevap = input ("Güventi kripto mu? [e/h]: ")
if cevap == "e": print ("Üretilen ", n, " adet sıralı güvenli gelişigüzel kripto listesi:\n", gelişigüzelListe (n), sep="")
else: print ("Üretilen ", n, " adet sıralı gelişigüzel sayı listesi:\n", gelişigüzelListe (n, False), sep="")



"""Çıktı:
>python p_30601.py
random.random() ile [0->1) arası gelişigüzel bir sayı: 0.9321091708265229
random.SystemRandom().random() ile gelişigüzel bir sayı: 0.5448150262394439
--------------------------------------------------

Kaç adet tesadüfi sayı üreteceksin? 12
Güventi kripto mu? [e/h]: e
Üretilen 12 adet sıralı güvenli gelişigüzel kripto listesi:
[0.012700634439475555, 0.025565323407408136, 0.0422947841031881, 0.06918530563264158, 
0.1673051041695467, 0.3646126042950312, 0.4265063592314047, 0.5368366543456832, 
0.8070764605342521, 0.8464319660556548, 0.9125709611716839, 0.9954478872695051]

>python p_30601.py  ** TEKRAR **
random.random() ile [0->1) arası gelişigüzel bir sayı: 0.3316792011416174
random.SystemRandom().random() ile gelişigüzel bir sayı: 0.28704436857555204
--------------------------------------------------

Kaç adet tesadüfi sayı üreteceksin? 34
Güventi kripto mu? [e/h]: h
Üretilen 34 adet sıralı gelişigüzel sayı listesi:
[0.017932925603532213, 0.046916617919822934, 0.04858795859581999, 0.07180710633065635, 
0.07927795320947162, 0.09694586888048806, 0.0975886308325078, 0.10387791514621114, 
0.14996753020893772, 0.15172415483866053, 0.17854134092789464, 0.17861739473501925, 
0.2819909143673798, 0.3027621672979989, 0.33652307663209713, 0.36347165066156595, 
0.37786022229330385, 0.4111888651028158, 0.4273635144096437, 0.4340134612928517, 
0.4826845830367468, 0.683959848913884, 0.7003913856246609, 0.7224660839293968, 
0.7427089046216556, 0.7930349517111259, 0.806179385672255, 0.8253947591496235, 
0.8267970541889049, 0.8903337572594882, 0.8950322790916979, 0.913877817563439, 
0.919036931058476, 0.9537532205859741]

>python p_30601.py  ** TEKRAR **
random.random() ile [0->1) arası gelişigüzel bir sayı: 0.706852168466992
random.SystemRandom().random() ile gelişigüzel bir sayı: 0.7209974511513185
-------------------------------------------------------------------------------

Kaç adet tesadüfi sayı üreteceksin?
Güventi kripto mu? [e/h]:
Üretilen 10 adet sıralı gelişigüzel sayı listesi:
[0.027391592272264287, 0.042876442121731695, 0.05042880189680865, 0.09290853476916872, 
0.22470161081332785, 0.5414248918922047, 0.6225361343440073, 0.7195599776610597, 
0.875798271646376, 0.8945706250940068]
"""