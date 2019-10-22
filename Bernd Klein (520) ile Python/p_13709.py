# coding:iso-8859-9
# p_13709.py: Genel, korunakl� ve �zel tip de�i�kenlerinin eri�ilebilme ve de�i�tirilebilme farkl�l��� �rne�i.

from p_13709x import A

x = A()

x.genel = x.genel + " Yani beni istedi�iniz gibi de�i�tirebilirsiniz."
print (x.genel)

print()
x._korunakl� = x._korunakl� + " Ve beni de de�i�tirebilirsiniz."
print (x._korunakl�)

print()
try: print (x.__�zel)
except Exception as ist: print ("AttributeError/�zellikHatas�:", ist)

print()
print (x._A__�zel) # Gizli �zel de�i�kenin tavsiye edilmeyen ka�ak eri�imi...

"""��kt�:
>python p_13709.py
Ben herkese a��k genel bir tip de�i�keni �zelli�iyim. Yani beni istedi�iniz gibi
 de�i�tirebilirsiniz.

Ben sadece alts�flara a��k korunakl� bir tip de�i�keni �zelli�iyim. Ve beni de d
e�i�tirebilirsiniz.

AttributeError/�zellikHatas�: 'A' object has no attribute '__�zel'

Ben herkese kapal� s�n�fi�i �zel bir tip de�i�keni �zelli�iyim.
"""