# coding:iso-8859-9 T�rk�e
# p_13409.py: Haz�r itertools.permutations ve �zel perm�tasyon fonksiyonu �rne�i.

def perm�tasyon (liste):
    n = len (liste)
    if n==0: yield []
    else:
        for i in range (len (liste)):
            for j in perm�tasyon (liste[:i]+liste[i+1:]): yield [liste[i]]+j

print ("[a,b,c] ��l� karakterlerin 3!=6 adet perm�tasyonu:")
for p in perm�tasyon (['a','b','c']): print (''.join (p))

print ("\n[o,y,u,n] d�rtl� karakterlerin 4!=24 adet perm�tasyonu:")
for p in perm�tasyon (list ("oyun")): print (''.join (p) + ", ", end="")

print ("\n\n[n,i,h,a,t] be�li karakterlerin 5!=120 adet perm�tasyonu:")
for p in perm�tasyon (list ("nihat")): print (''.join (p) + ", ", end="")
print ("\n", "-"*75, "\n", sep="")
#------------------------------------------------------------------------------------------------

# Ayn� i�lem yield �rete� fonksiyon yerine haz�r fonksiyonla da yap�labilir...
import itertools

��l� = itertools.permutations ([1,2,3])
d�rtl� = itertools.permutations ([1,2,3,4])
be�li = itertools.permutations ([1,2,3,4,5])

print ("��l� perm�tasyon listesi:", list (��l�) )
print ("\nD�rtl� perm�tasyon listesi:", list (d�rtl�) )
print ("\nBe�li perm�tasyon listesi:", list (be�li) )

"""��kt�:
>python p_13409.py
[a,b,c] ��l� karakterlerin 3!=6 adet perm�tasyonu:
abc
acb
bac
bca
cab
cba

[o,y,u,n] d�rtl� karakterlerin 4!=24 adet perm�tasyonu:
oyun, oynu, ouyn, ouny, onyu, onuy, youn, yonu, yuon, yuno, ynou, ynuo, 
uoyn, uony, uyon, uyno, unoy, unyo, noyu, nouy, nyou, nyuo, nuoy, nuyo,

[n,i,h,a,t] be�li karakterlerin 5!=120 adet perm�tasyonu:
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

��l� perm�tasyon listesi: [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

D�rtl� perm�tasyon listesi: [(1, 2, 3, 4), (1, 2, 4, 3), (1, 3, 2, 4), (1, 3, 4, 2), 
(1, 4, 2, 3), (1, 4, 3, 2), (2, 1, 3, 4), (2, 1, 4, 3), (2, 3, 1, 4), (2, 3, 4, 1), 
(2, 4, 1, 3), (2, 4, 3, 1), (3, 1, 2, 4), (3, 1, 4, 2), (3, 2, 1, 4), (3, 2, 4, 1),
 (3, 4, 1, 2), (3, 4, 2, 1), (4, 1, 2, 3), (4, 1, 3, 2), (4, 2, 1, 3), (4, 2, 3, 1),
 (4, 3, 1, 2), (4, 3, 2, 1)]

Be�li perm�tasyon listesi: [(1, 2, 3, 4, 5), (1, 2, 3, 5, 4), (1, 2, 4, 3, 5),
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