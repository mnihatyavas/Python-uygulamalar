# coding:iso-8859-9 T�rk�e
# p_20403b.py: Asal say� tespitini herbir ipi tamamlayarak ger�ekle�tirme �rne�i.

import threading
 
class AsalSay� (threading.Thread): # Miras yavrusu...
    asalSay�lar = {}
    kilit = threading.Lock()

    def __init__ (self, say�):
        threading.Thread.__init__ (self)
        self.Say� = say�
        AsalSay�.kilit.acquire()
        AsalSay�.asalSay�lar[say�] = "None"
        AsalSay�.kilit.release()

    def run (self):
        kontrol = 2
        kontrolaDevam = True
        while kontrol*kontrol < self.Say� and kontrolaDevam:
            if self.Say� % kontrol == 0:
                print ("%d bir asal say� de�ildir, ��nk� %d = %d * %d" % ( self.Say�, self.Say�, kontrol, self.Say� / kontrol) )
                kontrolaDevam = False
            kontrol += 1
        if kontrolaDevam: print ("%d bir asal say�d�r" % self.Say�)
        AsalSay�.kilit.acquire()
        AsalSay�.asalSay�lar[self.Say�] = kontrolaDevam
        AsalSay�.kilit.release()


ipler = []
while True:
    try: veri = abs (int (input ("\nSay� [q: son]: ")))
    except: break

    sicim = AsalSay� (veri) 
    ipler += [sicim]
    sicim.start() # run()'� �al��t�r�r...

for x in ipler: x.join() # Bir ip tamamlanmadan di�erine ge�mez...

"""��kt�:
>python p_20403b.py

Say� [q: son]: 23
23 bir asal say�d�r

Say� [q: son]: 12
12 bir asal say� de�ildir, ��nk� 12 = 2 * 6

Say� [q: son]: 56
56 bir asal say� de�ildir, ��nk� 56 = 2 * 28

Say� [q: son]: 1
1 bir asal say�d�r

Say� [q: son]: -13
13 bir asal say�d�r

Say� [q: son]: q
"""