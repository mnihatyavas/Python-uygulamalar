# coding:iso-8859-9 T�rk�e
# p_30601.py: random.random() ve random.SystemRandom().random() ile normal ve g�venli tesad�fi (0,1) say� �retme �rne�i.

import random

geli�ig�zelSay�1 = random.random()
geli�ig�zelSay�2 = random.SystemRandom().random()

print ("random.random() ile [0->1) aras� geli�ig�zel bir say�:", geli�ig�zelSay�1)
print ("random.SystemRandom().random() ile geli�ig�zel bir say�:", geli�ig�zelSay�2)
print ("-"*79)
#-------------------------------------------------------------------------------------------------------

def geli�ig�zelListe (adet, g�venliMi=True):
    liste = []
    for _ in range (adet):
        if g�venliMi: geli�ig�zel = random.SystemRandom().random()
        else: geli�ig�zel = random.random()
        liste.append (geli�ig�zel)
    liste.sort()
    return liste

try: n = abs (int (input ("\nKa� adet tesad�fi say� �reteceksin? ")))
except: n = 10

cevap = input ("G�venti kripto mu? [e/h]: ")
if cevap == "e": print ("�retilen ", n, " adet s�ral� g�venli geli�ig�zel kripto listesi:\n", geli�ig�zelListe (n), sep="")
else: print ("�retilen ", n, " adet s�ral� geli�ig�zel say� listesi:\n", geli�ig�zelListe (n, False), sep="")



"""��kt�:
>python p_30601.py
random.random() ile [0->1) aras� geli�ig�zel bir say�: 0.9321091708265229
random.SystemRandom().random() ile geli�ig�zel bir say�: 0.5448150262394439
--------------------------------------------------

Ka� adet tesad�fi say� �reteceksin? 12
G�venti kripto mu? [e/h]: e
�retilen 12 adet s�ral� g�venli geli�ig�zel kripto listesi:
[0.012700634439475555, 0.025565323407408136, 0.0422947841031881, 0.06918530563264158, 
0.1673051041695467, 0.3646126042950312, 0.4265063592314047, 0.5368366543456832, 
0.8070764605342521, 0.8464319660556548, 0.9125709611716839, 0.9954478872695051]

>python p_30601.py  ** TEKRAR **
random.random() ile [0->1) aras� geli�ig�zel bir say�: 0.3316792011416174
random.SystemRandom().random() ile geli�ig�zel bir say�: 0.28704436857555204
--------------------------------------------------

Ka� adet tesad�fi say� �reteceksin? 34
G�venti kripto mu? [e/h]: h
�retilen 34 adet s�ral� geli�ig�zel say� listesi:
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
random.random() ile [0->1) aras� geli�ig�zel bir say�: 0.706852168466992
random.SystemRandom().random() ile geli�ig�zel bir say�: 0.7209974511513185
-------------------------------------------------------------------------------

Ka� adet tesad�fi say� �reteceksin?
G�venti kripto mu? [e/h]:
�retilen 10 adet s�ral� geli�ig�zel say� listesi:
[0.027391592272264287, 0.042876442121731695, 0.05042880189680865, 0.09290853476916872, 
0.22470161081332785, 0.5414248918922047, 0.6225361343440073, 0.7195599776610597, 
0.875798271646376, 0.8945706250940068]
"""