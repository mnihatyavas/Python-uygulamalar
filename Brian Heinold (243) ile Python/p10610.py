# coding:iso-8859-9 T�rk�e

from math import pi

print ('\n'*5) # 5 sat�r bo� atlar...

c�mle = input ('Herhangibir c�mle girin: ')

print ("\nC�mlenizdeki 'a' harflerinin endeks konumlar�: ", end="")
for i in range (len (c�mle)):
    if c�mle[i]=='a': print (i, end=" ")

��l�_c�mle = ''
��l�_c�mle += c�mle*3
print ("\n\nC�mlenizin ��lemesi", ��l�_c�mle)

print ("\nC�mlenizin ard���k a��l�m�:")
for i in range (len (c�mle)): print (c�mle[:i+1])

c�mle2 = c�mle.lower()
for krk in ',.;:-?!()\'"': c�mle2 = c�mle2.replace (krk, '')
print ("\n\nK���k harfli ve noktalamalardan ar�nd�r�lan c�mleniz:", c�mle2)

p = str (pi)
print ("\nPi say�s�: [", pi, "]", sep="")
print ("Pi say�s�n�n tamsay� de�eri: [", p[:p.index('.')], "]", sep="")
print ("Pi say�s�n�n k�s�rat de�eri: [", p[p.index('.'):], "]", sep="")

alfabe = 'abc�defg�h�ijklmno�pqrs�tu�vwxyz'
anahtar= 'xzn�lweb��gjh�qdyvtkfuom�pcias�r'
mesaj = input ('\n�ifrelenecek mesaj�n�z� girin: ').lower()
�ifreli=de�ifreli=''
for k in mesaj:
    if k.isalpha(): �ifreli += anahtar[alfabe.index (k)]
    else: �ifreli += k
for k in �ifreli:
    if k.isalpha(): de�ifreli += alfabe[anahtar.index (k)]
    else: de�ifreli += k
print ("Girdi�iniz mesaj�n �ifreli sonucu: ", �ifreli)
print ("�ifrelenenin tekrar de�ifreli sonucu: ", de�ifreli)
