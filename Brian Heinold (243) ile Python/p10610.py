# coding:iso-8859-9 Türkçe

from math import pi

print ('\n'*5) # 5 satır boş atlar...

cümle = input ('Herhangibir cümle girin: ')

print ("\nCümlenizdeki 'a' harflerinin endeks konumları: ", end="")
for i in range (len (cümle)):
    if cümle[i]=='a': print (i, end=" ")

üçlü_cümle = ''
üçlü_cümle += cümle*3
print ("\n\nCümlenizin üçlemesi", üçlü_cümle)

print ("\nCümlenizin ardışık açılımı:")
for i in range (len (cümle)): print (cümle[:i+1])

cümle2 = cümle.lower()
for krk in ',.;:-?!()\'"': cümle2 = cümle2.replace (krk, '')
print ("\n\nKüçük harfli ve noktalamalardan arındırılan cümleniz:", cümle2)

p = str (pi)
print ("\nPi sayısı: [", pi, "]", sep="")
print ("Pi sayısının tamsayı değeri: [", p[:p.index('.')], "]", sep="")
print ("Pi sayısının küsürat değeri: [", p[p.index('.'):], "]", sep="")

alfabe = 'abcçdefgğhıijklmnoöpqrsştuüvwxyz'
anahtar= 'xznılweböügjhçqdyvtkfuomşpciasğr'
mesaj = input ('\nŞifrelenecek mesajınızı girin: ').lower()
şifreli=deşifreli=''
for k in mesaj:
    if k.isalpha(): şifreli += anahtar[alfabe.index (k)]
    else: şifreli += k
for k in şifreli:
    if k.isalpha(): deşifreli += alfabe[anahtar.index (k)]
    else: deşifreli += k
print ("Girdiğiniz mesajın şifreli sonucu: ", şifreli)
print ("Şifrelenenin tekrar deşifreli sonucu: ", deşifreli)
