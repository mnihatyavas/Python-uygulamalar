# coding:iso-8859-9 T�rk�e
# p_21102.py: Genelle�tirilen i�i�e 2 fonksiyonla a��rl�k-boy kriti�i �rne�i.

def i�i�eFonksiyon (g, f):
    def h (*arg�manlar, **kwarg�manlar): # *:liste veya t�ple arg�manlar, **:s�zl�k arg�manlar...
        return g (f (*arg�manlar, **kwarg�manlar))
    return h

def ABE (a��rl�k, boy): return a��rl�k / boy**2

def ABEde�erlemesi (abe):
    if abe < 15: return "�l�mc�l zay�f"
    elif abe < 16: return "Sa�l�ks�z zay�f"
    elif abe < 18.5: return "Zay�f"
    elif abe < 25: return "Sa�l�kl� ve formda"
    elif abe < 30: return "G�rb�z"
    elif abe < 35: return "1.derece Obez (�i�man)"
    elif abe < 40: return "2.derece Obez (sa�l�ks�z �i�man)"
    else: return "3.derece Obez (�l�mc�l �i�man)"

f = i�i�eFonksiyon (ABEde�erlemesi, ABE)

a��rl�k = 1
while a��rl�k != 0:
    try:
        a��rl�k = abs (float (input ("A��rl�k-kg [0=��k]: ")))
        boy = abs (float (input ("Boy-m [0=��k]: ")))
        if a��rl�k==0 or boy==0: break
    except: break

    print (ABE (a��rl�k, boy), ", De�erleme: ", f (a��rl�k, boy), "\n", sep="" )

"""��kt�:
>python p_21102.py
A��rl�k-kg [0=��k]: 55
Boy-m [0=��k]: 1.70
19.031141868512112, De�erleme: Sa�l�kl� ve formda

A��rl�k-kg [0=��k]: 50
Boy-m [0=��k]: 1.7
17.301038062283737, De�erleme: Zay�f

A��rl�k-kg [0=��k]: 40
Boy-m [0=��k]: 1.7
13.84083044982699, De�erleme: �l�mc�l zay�f

A��rl�k-kg [0=��k]: 70
Boy-m [0=��k]: 1.7
24.221453287197235, De�erleme: Sa�l�kl� ve formda

A��rl�k-kg [0=��k]: 80
Boy-m [0=��k]: 1.7
27.68166089965398, De�erleme: G�rb�z

A��rl�k-kg [0=��k]: 100
Boy-m [0=��k]: 1.7
34.602076124567475, De�erleme: 1.derece Obez (�i�man)

A��rl�k-kg [0=��k]: 120
Boy-m [0=��k]: 1.7
41.52249134948097, De�erleme: 3.derece Obez (�l�mc�l �i�man)

A��rl�k-kg [0=��k]: 110
Boy-m [0=��k]: 1.7
38.062283737024224, De�erleme: 2.derece Obez (sa�l�ks�z �i�man)

A��rl�k-kg [0=��k]:
"""