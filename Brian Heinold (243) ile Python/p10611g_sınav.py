# coding:iso-8859-9 T�rk�e

form�l = input ("nx^y [5x^4] girin: ")
if not len(form�l): form�l = "5.6abc^5.65"
x = ''
for k in form�l:
    if k.isalpha(): x += k
n = eval (form�l[:form�l.index(x)])
�s = eval (form�l[form�l.index("^")+1:])
print ("Girilen [", form�l, "] e�itli�inin t�revi: [", n*�s, x, "^", �s-1, "]'dir.", sep="")
print()
form�l = input ("x25+65y-7(12z+5w) girin: ")
if not len(form�l): form�l = "x25+65y-7(12z+5w)"
i = 0
sonu� = ''
while i < len (form�l):
    if (form�l[i].isalpha() and form�l[i+1].isdigit()) or (form�l[i].isdigit() and form�l[i+1].isalpha()) or ((form�l[i].isdigit() or form�l[i].isalpha()) and form�l[i+1] == "("):
        sonu� += form�l[i] + "*" + form�l[i+1]
        i +=2
    else: sonu� += form�l[i]; i +=1
print ("Girilen [", form�l, "] e�itli�inin g�nceli: [", sonu�, "]'dir.", sep="")


��kt�="""
nx^y [5x^4] girin: 67.98vbg^43.65
Girilen [67.98vbg^43.65] e�itli�inin t�revi: [2967.327vbg^42.65]'dir.

x25+65y-7(12z+5w) girin: 78kj-98yt + 65(7y-98gf)
Girilen [78kj-98yt + 65(7y-98gf)] e�itli�inin g�nceli: [78*kj-98*yt + 65*(7*y-98*gf)]'dir.
"""