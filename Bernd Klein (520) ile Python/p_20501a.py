# coding:iso-8859-9 Türkçe
# p_20501a.py: Linus fork/çatallamayla bira şişeleri oyunu örneği.

import os

def yavru (dağıt):
  şişeler = 99
  while True:
    bira = "bira şişesi"
    duvarda = "duvarda dizilidir."
    biriniAl = "Birini al ve isteyene uzat."
    dükan = "Dükana git ve tekrar bir kutu bira satın al."

    if şişeler > 0:
      veriler =  (şişeler, bira, duvarda, biriniAl, şişeler - 1, bira, duvarda)
      koçak = "%2d %s %s\n%2d\n%2d %s %s" % veriler # İlk 99 mısra için koçak=117 byte (yeniden hesapla!)...
      os.write (dağıt, koçak)
      şişeler -= 1
    else:
      şişeler = 99
      veriler =  (bira, duvarda, dükan, şişeler, bira, duvarda)
      koçak = "Maalesef sıfır %s %s\n%s\n%s\n%2d %s %s" % veriler # Dükandan yenileme mısrası için koçak=128 byte (yeniden hesapla!)...
      os.write (dağıt, koçak)

def ebeveyn():
    yeniden, dağıt = os.pipe()
    if os.fork() == 0: yavru (dağıt) # os.fork() Linux içindir, Windows için exec/spawn kullanılabilir...
    else:
        sayaç = 1
        while True:
            if sayaç % 100: koçak = os.read (yeniden, 117)
            else: koçak = os.read (yeniden, 128)
            print ('Tekerleme no: %d\n%s\n' % (sayaç, koçak) )
            sayaç += 1


ebeveyn()