# coding:iso-8859-9 Türkçe
# p_20403b.py: Asal sayı tespitini herbir ipi tamamlayarak gerçekleştirme örneği.

import threading
 
class AsalSayı (threading.Thread): # Miras yavrusu...
    asalSayılar = {}
    kilit = threading.Lock()

    def __init__ (self, sayı):
        threading.Thread.__init__ (self)
        self.Sayı = sayı
        AsalSayı.kilit.acquire()
        AsalSayı.asalSayılar[sayı] = "None"
        AsalSayı.kilit.release()

    def run (self):
        kontrol = 2
        kontrolaDevam = True
        while kontrol*kontrol < self.Sayı and kontrolaDevam:
            if self.Sayı % kontrol == 0:
                print ("%d bir asal sayı değildir, çünkü %d = %d * %d" % ( self.Sayı, self.Sayı, kontrol, self.Sayı / kontrol) )
                kontrolaDevam = False
            kontrol += 1
        if kontrolaDevam: print ("%d bir asal sayıdır" % self.Sayı)
        AsalSayı.kilit.acquire()
        AsalSayı.asalSayılar[self.Sayı] = kontrolaDevam
        AsalSayı.kilit.release()


ipler = []
while True:
    try: veri = abs (int (input ("\nSayı [q: son]: ")))
    except: break

    sicim = AsalSayı (veri) 
    ipler += [sicim]
    sicim.start() # run()'ı çalıştırır...

for x in ipler: x.join() # Bir ip tamamlanmadan diğerine geçmez...

"""Çıktı:
>python p_20403b.py

Sayı [q: son]: 23
23 bir asal sayıdır

Sayı [q: son]: 12
12 bir asal sayı değildir, çünkü 12 = 2 * 6

Sayı [q: son]: 56
56 bir asal sayı değildir, çünkü 56 = 2 * 28

Sayı [q: son]: 1
1 bir asal sayıdır

Sayı [q: son]: -13
13 bir asal sayıdır

Sayı [q: son]: q
"""