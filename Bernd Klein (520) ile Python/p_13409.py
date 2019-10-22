# coding:iso-8859-9 Türkçe
# p_13409.py: Hazır itertools.permutations ve özel permütasyon fonksiyonu örneği.

def permütasyon (liste):
    n = len (liste)
    if n==0: yield []
    else:
        for i in range (len (liste)):
            for j in permütasyon (liste[:i]+liste[i+1:]): yield [liste[i]]+j

print ("[a,b,c] üçlü karakterlerin 3!=6 adet permütasyonu:")
for p in permütasyon (['a','b','c']): print (''.join (p))

print ("\n[o,y,u,n] dörtlü karakterlerin 4!=24 adet permütasyonu:")
for p in permütasyon (list ("oyun")): print (''.join (p) + ", ", end="")

print ("\n\n[n,i,h,a,t] beşli karakterlerin 5!=120 adet permütasyonu:")
for p in permütasyon (list ("nihat")): print (''.join (p) + ", ", end="")
print ("\n", "-"*75, "\n", sep="")
#------------------------------------------------------------------------------------------------

# Aynı işlem yield üreteç fonksiyon yerine hazır fonksiyonla da yapılabilir...
import itertools

üçlü = itertools.permutations ([1,2,3])
dörtlü = itertools.permutations ([1,2,3,4])
beşli = itertools.permutations ([1,2,3,4,5])

print ("Üçlü permütasyon listesi:", list (üçlü) )
print ("\nDörtlü permütasyon listesi:", list (dörtlü) )
print ("\nBeşli permütasyon listesi:", list (beşli) )

"""Çıktı:
>python p_13409.py
[a,b,c] üçlü karakterlerin 3!=6 adet permütasyonu:
abc
acb
bac
bca
cab
cba

[o,y,u,n] dörtlü karakterlerin 4!=24 adet permütasyonu:
oyun, oynu, ouyn, ouny, onyu, onuy, youn, yonu, yuon, yuno, ynou, ynuo, 
uoyn, uony, uyon, uyno, unoy, unyo, noyu, nouy, nyou, nyuo, nuoy, nuyo,

[n,i,h,a,t] beşli karakterlerin 5!=120 adet permütasyonu:
nihat, nihta, niaht, niath, nitha, nitah, nhiat, nhita, nhait, nhati, nhtia, nhtai,
 naiht, naith, nahit, nahti, natih, nathi, ntiha, ntiah, nthia, nthai, ntaih,
 ntahi, inhat, inhta, inaht, inath, intha, intah, ihnat, ihnta, ihant, ihatn, ihtna, 
ihtan, ianht, ianth, iahnt, iahtn, iatnh, iathn, itnha, itnah, ithna, ithan,
 itanh, itahn, hniat, hnita, hnait, hnati, hntia, hntai, hinat, hinta, hiant, hiatn,
 hitna, hitan, hanit, hanti, haint, haitn, hatni, hatin, htnia, htnai, htina, htian,
 htani, htain, aniht, anith, anhit, anhti, antih, anthi, ainht, ainth,aihnt, aihtn, aitnh, aithn, ahnit, ahnti, ahint, ahitn, ahtni, ahtin, atnih, atn
hi, atinh, atihn, athni, athin, tniha, tniah, tnhia, tnhai, tnaih, tnahi, tinha,
 tinah, tihna, tihan, tianh, tiahn, thnia, thnai, thina, thian, thani, thain, tanih,
 tanhi, tainh, taihn, tahni, tahin,
---------------------------------------------------------------------------

Üçlü permütasyon listesi: [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

Dörtlü permütasyon listesi: [(1, 2, 3, 4), (1, 2, 4, 3), (1, 3, 2, 4), (1, 3, 4, 2), 
(1, 4, 2, 3), (1, 4, 3, 2), (2, 1, 3, 4), (2, 1, 4, 3), (2, 3, 1, 4), (2, 3, 4, 1), 
(2, 4, 1, 3), (2, 4, 3, 1), (3, 1, 2, 4), (3, 1, 4, 2), (3, 2, 1, 4), (3, 2, 4, 1),
 (3, 4, 1, 2), (3, 4, 2, 1), (4, 1, 2, 3), (4, 1, 3, 2), (4, 2, 1, 3), (4, 2, 3, 1),
 (4, 3, 1, 2), (4, 3, 2, 1)]

Beşli permütasyon listesi: [(1, 2, 3, 4, 5), (1, 2, 3, 5, 4), (1, 2, 4, 3, 5),
 (1, 2, 4, 5, 3), (1, 2, 5, 3, 4), (1, 2, 5, 4, 3), (1, 3, 2, 4, 5), (1, 3, 2, 5,4),
 (1, 3, 4, 2, 5), (1, 3, 4, 5, 2), (1, 3, 5, 2, 4), (1, 3, 5, 4, 2), (1, 4, 2, 3, 5), 
(1, 4, 2, 5, 3), (1, 4, 3, 2, 5), (1, 4, 3, 5, 2), (1, 4, 5, 2, 3), (1, 4, 5, 3, 2), 
(1, 5, 2, 3, 4), (1, 5, 2, 4, 3), (1, 5, 3, 2, 4), (1, 5, 3, 4, 2), (1, 5, 4, 2, 3),
 (1, 5, 4, 3, 2), (2, 1, 3, 4, 5), (2, 1, 3, 5, 4), (2, 1, 4,3, 5), (2, 1, 4, 5, 3),
 (2, 1, 5, 3, 4), (2, 1, 5, 4, 3), (2, 3, 1, 4, 5), (2, 3, 1, 5, 4), (2, 3, 4, 1, 5),
 (2, 3, 4, 5, 1), (2, 3, 5, 1, 4), (2, 3, 5, 4, 1),(2, 4, 1, 3, 5), (2, 4, 1, 5, 3),
 (2, 4, 3, 1, 5), (2, 4, 3, 5, 1), (2, 4, 5, 1, 3), (2, 4, 5, 3, 1), (2, 5, 1, 3, 4),
 (2, 5, 1, 4, 3), (2, 5, 3, 1, 4), (2, 5,3, 4, 1), (2, 5, 4, 1, 3), (2, 5, 4, 3, 1),
 (3, 1, 2, 4, 5), (3, 1, 2, 5, 4), (3, 1, 4, 2, 5), (3, 1, 4, 5, 2), (3, 1, 5, 2, 4),
 (3, 1, 5, 4, 2), (3, 2, 1, 4, 5), (3, 2, 1, 5, 4), (3, 2, 4, 1, 5), (3, 2, 4, 5, 1), 
(3, 2, 5, 1, 4), (3, 2, 5, 4, 1), (3, 4, 1, 2, 5), (3, 4, 1, 5, 2), (3, 4, 2, 1, 5),
 (3, 4, 2, 5, 1), (3,4, 5, 1, 2), (3, 4, 5, 2, 1), (3, 5, 1, 2, 4), (3, 5, 1, 4, 2), 
(3, 5, 2, 1, 4), (3, 5, 2, 4, 1), (3, 5, 4, 1, 2), (3, 5, 4, 2, 1), (4, 1, 2, 3, 5), 
(4, 1, 2, 5, 3), (4, 1, 3, 2, 5), (4, 1, 3, 5, 2), (4, 1, 5, 2, 3), (4, 1, 5, 3, 2), 
(4, 2, 1, 3, 5), (4, 2, 1, 5, 3), (4, 2, 3, 1, 5), (4, 2, 3, 5, 1), (4, 2, 5, 1, 3), 
(4, 2, 5, 3, 1), (4, 3, 1, 2, 5), (4, 3, 1, 5, 2), (4, 3, 2, 1, 5), (4, 3, 2, 5,1), 
(4, 3, 5, 1, 2), (4, 3, 5, 2, 1), (4, 5, 1, 2, 3), (4, 5, 1, 3, 2), (4, 5, 2, 1, 3), 
(4, 5, 2, 3, 1), (4, 5, 3, 1, 2), (4, 5, 3, 2, 1), (5, 1, 2, 3, 4), (5, 1, 2, 4, 3), 
(5, 1, 3, 2, 4), (5, 1, 3, 4, 2), (5, 1, 4, 2, 3), (5, 1, 4, 3, 2), (5, 2, 1, 3, 4), 
(5, 2, 1, 4, 3), (5, 2, 3, 1, 4), (5, 2, 3, 4, 1), (5, 2, 4,1, 3), (5, 2, 4, 3, 1), 
(5, 3, 1, 2, 4), (5, 3, 1, 4, 2), (5, 3, 2, 1, 4), (5, 3, 2, 4, 1), (5, 3, 4, 1, 2), 
(5, 3, 4, 2, 1), (5, 4, 1, 2, 3), (5, 4, 1, 3, 2),(5, 4, 2, 1, 3), (5, 4, 2, 3, 1), 
(5, 4, 3, 1, 2), (5, 4, 3, 2, 1)]
"""