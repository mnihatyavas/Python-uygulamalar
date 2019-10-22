# coding:iso-8859-9 T�rk�e
# p_20403a.py: Girilen say�n�n asal say�l���n�n ip kontrol�yle testi �rne�i.

import threading
 
class AsalSay� (threading.Thread):
    def __init__ (self, say�):
        threading.Thread.__init__ (self)
        self.Say� = say�
 
    def run (self):
        saya� = 2
        while saya�*saya� < self.Say�:
            if self.Say� % saya� == 0:
                print ("%d bir asal say� de�ildir, ��nk� %d = %d * %d" % ( self.Say�, self.Say�, saya�, self.Say� / saya�) )
                return
            saya� += 1
        print ("%d bir asal say�d�r" % self.Say�)

ipler = []
while True:
    try: veri = abs (int (input ("\nSay� [q: son]: ") ))
    except: break

    sicim = AsalSay� (veri)
    ipler += [sicim]
    sicim.start() # run()'� �al��t�r�r...

for x in ipler: x.join()


"""��kt�:
>python p_20403.py

Say� [q: son]: 128
128 bir asal say� de�ildir, ��nk� 128 = 2 * 64

Say� [q: son]: 7
7 bir asal say�d�r

Say� [q: son]: 125
125 bir asal say� de�ildir, ��nk� 125 = 5 * 25

Say� [q: son]: -65
65 bir asal say� de�ildir, ��nk� 65 = 5 * 13

Say� [q: son]: 0
0 bir asal say�d�r

Say� [q: son]: q
"""