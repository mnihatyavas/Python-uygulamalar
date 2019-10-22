#coding:iso-8859-9 T�rk�e
# p_11905.py: center/ortala, ljust/solahizala, rjust/sa�ahizala ve zfill/s�f�rladoldur yazd�rma �rne�i.

dizge1 = "Python"
print ("center(..) ile ortalanan dizge:", dizge1.center (15) )
print ("center(..) ile ortalanan dizge:", dizge1.center (15, "-") )
print ("center(..) ile ortalanan dizge:", dizge1.center (15, "*") )

print ("\nljust(..) ile sola hizalanan dizge:", dizge1.ljust (15) )
print ("ljust(..) ile sola hizalanan dizge:", dizge1.ljust (15, ":") )
print ("ljust(..) ile sola hizalanan dizge:", dizge1.ljust (15, "<") )

print ("\nrjust(..) ile sa�a hizalanan dizge:", dizge1.rjust (15) )
print ("rjust(..) ile sa�a hizalanan dizge:", dizge1.rjust (15, "~") )
print ("rjust(..) ile sa�a hizalanan dizge:", dizge1.rjust (15, ">") )

dizge2 = "1234567890"
print ("\nzfill(..) ile 12 haneli su m��teri no'su:", dizge2.zfill (12) )
print ("rjust(..) ile 12 haneli su m��teri no'su:", dizge2.rjust (12, "0") )


"""��kt�:
>python p_11905.py
center(..) ile ortalanan dizge:      Python
center(..) ile ortalanan dizge: -----Python----
center(..) ile ortalanan dizge: *****Python****

ljust(..) ile sola hizalanan dizge: Python
ljust(..) ile sola hizalanan dizge: Python:::::::::
ljust(..) ile sola hizalanan dizge: Python<<<<<<<<<

rjust(..) ile sa�a hizalanan dizge:          Python
rjust(..) ile sa�a hizalanan dizge: ~~~~~~~~~Python
rjust(..) ile sa�a hizalanan dizge: >>>>>>>>>Python

zfill(..) ile 12 haneli su m��teri no'su: 001234567890
rjust(..) ile 12 haneli su m��teri no'su: 001234567890
"""