# coding:iso-8859-9 T�rk�e
# p_12506.py: �zyinelelemeli ve de�i�ken arg�manl� dekorat�r fonksiyonlar�nda saya� �rne�i.

def tamsay�l�_arg�man_kontrol� (f):
    def yard�mc� (x):
        if type (x) == int and x >= 0: return f (x)
        else:
            print ("HATA: Arg�man ge�erli bir tamsay� de�ildir!..")
            return "***"
    return yard�mc�

@tamsay�l�_arg�man_kontrol�
def ard�l�arp (n):
    if n == 1 or n == 0: return 1
    else: return n * ard�l�arp (n-1)

t�ple = (10, 1, 10, 20, 3.8, -15, 9, 0)
for (i, j) in enumerate (t�ple): print (i+1, j, ard�l�arp (j) )
print ("-"*75, "\n")
#------------------------------------------------------------------------------------------------------

def sayal�m (fonk):
    def yard�mc� (x):
        yard�mc�.saya� += 1
        return fonk (x)
    yard�mc�.saya� = 0
    return yard�mc�

@sayal�m
def birsonraki (x): return x+1

print ("sayal�m(..) dekorat�r� ka� kez �a�r�ld�:", birsonraki.saya�)
for i in range (10): birsonraki (i)
print ("sayal�m(..) dekorat�r� ka� kez �a�r�ld�:", birsonraki.saya�)
for i in range (15): birsonraki (i)
print ("sayal�m(..) dekorat�r� toplamda ka� kez �a�r�ld�:", birsonraki.saya�)
print ("-"*75, "\n")
#------------------------------------------------------------------------------------------------------

def sayal�m2 (fonk):
    def yard�mc� (*a, **b):
        yard�mc�.saya� += 1
        return fonk (*a, **b)
    yard�mc�.saya� = 0
    return yard�mc�

@sayal�m2
def birsonraki (x): return x+1

@sayal�m2
def �arp (x, y=1):
    if y==1: return x*y + 1 # birsonraki(x)'yle ayn�...
    else: return x*y # �ki say�n�n �arp�m�...

print ("birsonraki(..) ka� kez �a�r�ld�:", birsonraki.saya�)

for i in range (10): birsonraki (i)
�arp (3, 4)
�arp (4)
�arp (y=3, x=2)

print ("birsonraki(..) ka� kez �a�r�ld�:", birsonraki.saya�)
print ("�arp(..) ka� kez �a�r�ld�:", �arp.saya�)

for i in range (15): birsonraki (i)
�arp (5, 5)
�arp (10)
�arp (y=5, x=7.9)
�arp (x=-3.5, y=0.59)

print ("birsonraki(..) toplamda ka� kez �a�r�ld�:", birsonraki.saya�)
print ("�arp(..) toplamda ka� kez �a�r�ld�:", �arp.saya�)



"""��kt�:
>python p_12506.py
1 10 3628800
2 1 1
3 10 3628800
4 20 2432902008176640000
HATA: Arg�man ge�erli bir tamsay� de�ildir!..
5 3.8 ***
HATA: Arg�man ge�erli bir tamsay� de�ildir!..
6 -15 ***
7 9 362880
8 0 1
---------------------------------------------------------------------------

sayal�m(..) dekorat�r� ka� kez �a�r�ld�: 0
sayal�m(..) dekorat�r� ka� kez �a�r�ld�: 10
sayal�m(..) dekorat�r� toplamda ka� kez �a�r�ld�: 25
---------------------------------------------------------------------------

birsonraki(..) ka� kez �a�r�ld�: 0
birsonraki(..) ka� kez �a�r�ld�: 10
�arp(..) ka� kez �a�r�ld�: 3
birsonraki(..) toplamda ka� kez �a�r�ld�: 25
�arp(..) toplamda ka� kez �a�r�ld�: 7
"""