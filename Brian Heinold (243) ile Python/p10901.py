#coding:iso-8859-9 T�rk�e

from random import randint
�s�=tip=0
while tip != 9:
    try: tip = eval (input ('[1:F; 2:C; 3:K] Derece tipi girin {9:��k}: '))
    except Exception: tip = randint (1,3)
    if tip == 9: print ("Ho��akal�n, program� sonland�r�yorum!")
    if not (tip == 1 or tip == 2 or tip == 3 or tip == 9): tip = randint (1,3)
    if tip != 9:
        try: �s� = eval (input (str(tip)+' i�in �s� de�eri girin: '))
        except Exception:
            if tip == 1: �s� = randint (-459, 5000)
            elif tip == 2: �s� = randint (-273, 5000)
            else: �s� = randint (0, 5000)
    if tip == 1 and �s� >= - 459.66999: print ("Girdi�iniz", �s�, "F=",  5/9*(�s�-32), "C ve", 5/9*(�s�-32)+273.15, "K derecedir.")
    elif tip == 2 and �s� >= -273.15: print ("Girdi�iniz", �s�, "C=",  1.8*�s�+32, "F ve", 273.15+�s�, "K derecedir.")
    elif tip == 3 and �s� >= 0: print ("Girdi�iniz", �s�, "K=",  �s�-273.15, "C ve", (�s�-273.15)*1.8+32, "F derecedir.")

