# coding:iso-8859-9 T�rk�e

try: say� = abs (eval (input ("K�s�ratl� bir feet de�eri girin: ")))
except Exception: say� = 4.75
k�s�rat = say� - int (say�)
in� = k�s�rat * 30.48 / 2.54
print ("Girdi�iniz say�:", int (say�), "feet ve", in�, "in�'tir.")

L = []
b�y�kSay�1=b�y�kSay�2=0
k���kSay�1=k���kSay�2=999
while True:
    dizge = input ("\n(5'7\") bi�imli de�er girin [��k��: son]: ")
    if dizge.lower() == "son": break

    try: say�1 = int (dizge[:dizge.index ("'")])
    except Exception: say�1 = 5; print (say�1, "'")
    try: say�2 = int (dizge[dizge.index ("'")+1:dizge.index ("\"")])
    except Exception: say�2 = 7; print (say�2, "\"")

    if say�1 > b�y�kSay�1: b�y�kSay�1 = say�1
    if say�1 < k���kSay�1: k���kSay�1 = say�1
    if say�2 > b�y�kSay�2: b�y�kSay�2 = say�2
    if say�2 < k���kSay�2: k���kSay�2 = say�2

    say� = say�1 + (say�2 * 2.54 / 30.48)
    L = L + [say�]
print ("\nGirdi�iniz feet'in�\" de�erlerinin feet kar��l�klar� listesi==>")
for k in L: print ("{:.2f}" .format (k), end=" ")
print ("\n\nGirilen enb�y�k ve enk���k feet de�erleri:", b�y�kSay�1, k���kSay�1)
print ("Girilen enb�y�k ve enk���k in� de�erleri:", b�y�kSay�2, k���kSay�2)
