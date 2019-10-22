# coding:iso-8859-9 Türkçe
# p_21102.py: Genelleştirilen içiçe 2 fonksiyonla ağırlık-boy kritiği örneği.

def içiçeFonksiyon (g, f):
    def h (*argümanlar, **kwargümanlar): # *:liste veya tüple argümanlar, **:sözlük argümanlar...
        return g (f (*argümanlar, **kwargümanlar))
    return h

def ABE (ağırlık, boy): return ağırlık / boy**2

def ABEdeğerlemesi (abe):
    if abe < 15: return "Ölümcül zayıf"
    elif abe < 16: return "Sağlıksız zayıf"
    elif abe < 18.5: return "Zayıf"
    elif abe < 25: return "Sağlıklı ve formda"
    elif abe < 30: return "Gürbüz"
    elif abe < 35: return "1.derece Obez (şişman)"
    elif abe < 40: return "2.derece Obez (sağlıksız şişman)"
    else: return "3.derece Obez (ölümcül şişman)"

f = içiçeFonksiyon (ABEdeğerlemesi, ABE)

ağırlık = 1
while ağırlık != 0:
    try:
        ağırlık = abs (float (input ("Ağırlık-kg [0=çık]: ")))
        boy = abs (float (input ("Boy-m [0=çık]: ")))
        if ağırlık==0 or boy==0: break
    except: break

    print (ABE (ağırlık, boy), ", Değerleme: ", f (ağırlık, boy), "\n", sep="" )

"""Çıktı:
>python p_21102.py
Ağırlık-kg [0=çık]: 55
Boy-m [0=çık]: 1.70
19.031141868512112, Değerleme: Sağlıklı ve formda

Ağırlık-kg [0=çık]: 50
Boy-m [0=çık]: 1.7
17.301038062283737, Değerleme: Zayıf

Ağırlık-kg [0=çık]: 40
Boy-m [0=çık]: 1.7
13.84083044982699, Değerleme: Ölümcül zayıf

Ağırlık-kg [0=çık]: 70
Boy-m [0=çık]: 1.7
24.221453287197235, Değerleme: Sağlıklı ve formda

Ağırlık-kg [0=çık]: 80
Boy-m [0=çık]: 1.7
27.68166089965398, Değerleme: Gürbüz

Ağırlık-kg [0=çık]: 100
Boy-m [0=çık]: 1.7
34.602076124567475, Değerleme: 1.derece Obez (şişman)

Ağırlık-kg [0=çık]: 120
Boy-m [0=çık]: 1.7
41.52249134948097, Değerleme: 3.derece Obez (ölümcül şişman)

Ağırlık-kg [0=çık]: 110
Boy-m [0=çık]: 1.7
38.062283737024224, Değerleme: 2.derece Obez (sağlıksız şişman)

Ağırlık-kg [0=çık]:
"""