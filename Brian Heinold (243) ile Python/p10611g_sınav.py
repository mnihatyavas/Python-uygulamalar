# coding:iso-8859-9 Türkçe

formül = input ("nx^y [5x^4] girin: ")
if not len(formül): formül = "5.6abc^5.65"
x = ''
for k in formül:
    if k.isalpha(): x += k
n = eval (formül[:formül.index(x)])
üs = eval (formül[formül.index("^")+1:])
print ("Girilen [", formül, "] eşitliğinin türevi: [", n*üs, x, "^", üs-1, "]'dir.", sep="")
print()
formül = input ("x25+65y-7(12z+5w) girin: ")
if not len(formül): formül = "x25+65y-7(12z+5w)"
i = 0
sonuç = ''
while i < len (formül):
    if (formül[i].isalpha() and formül[i+1].isdigit()) or (formül[i].isdigit() and formül[i+1].isalpha()) or ((formül[i].isdigit() or formül[i].isalpha()) and formül[i+1] == "("):
        sonuç += formül[i] + "*" + formül[i+1]
        i +=2
    else: sonuç += formül[i]; i +=1
print ("Girilen [", formül, "] eşitliğinin günceli: [", sonuç, "]'dir.", sep="")


çıktı="""
nx^y [5x^4] girin: 67.98vbg^43.65
Girilen [67.98vbg^43.65] eşitliğinin türevi: [2967.327vbg^42.65]'dir.

x25+65y-7(12z+5w) girin: 78kj-98yt + 65(7y-98gf)
Girilen [78kj-98yt + 65(7y-98gf)] eşitliğinin günceli: [78*kj-98*yt + 65*(7*y-98*gf)]'dir.
"""