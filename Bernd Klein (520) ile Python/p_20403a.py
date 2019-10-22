# coding:iso-8859-9 Türkçe
# p_20403a.py: Girilen sayının asal sayılığının ip kontrolüyle testi örneği.

import threading
 
class AsalSayı (threading.Thread):
    def __init__ (self, sayı):
        threading.Thread.__init__ (self)
        self.Sayı = sayı
 
    def run (self):
        sayaç = 2
        while sayaç*sayaç < self.Sayı:
            if self.Sayı % sayaç == 0:
                print ("%d bir asal sayı değildir, çünkü %d = %d * %d" % ( self.Sayı, self.Sayı, sayaç, self.Sayı / sayaç) )
                return
            sayaç += 1
        print ("%d bir asal sayıdır" % self.Sayı)

ipler = []
while True:
    try: veri = abs (int (input ("\nSayı [q: son]: ") ))
    except: break

    sicim = AsalSayı (veri)
    ipler += [sicim]
    sicim.start() # run()'ı çalıştırır...

for x in ipler: x.join()


"""Çıktı:
>python p_20403.py

Sayı [q: son]: 128
128 bir asal sayı değildir, çünkü 128 = 2 * 64

Sayı [q: son]: 7
7 bir asal sayıdır

Sayı [q: son]: 125
125 bir asal sayı değildir, çünkü 125 = 5 * 25

Sayı [q: son]: -65
65 bir asal sayı değildir, çünkü 65 = 5 * 13

Sayı [q: son]: 0
0 bir asal sayıdır

Sayı [q: son]: q
"""