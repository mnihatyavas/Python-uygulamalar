# coding:iso-8859-9 T�rk�e
# p_31005.py: Numpy 3 boyutlu cross/�apraz vekt�rel �arp�m �rne�i.

import numpy as np

x = np.array ([0, 0, 1])
y = np.array ([0, 1, 0])

print ("[0,0,1] ile [0,1,0] cross/�apraz �arp�m�:", np.cross (x, y) )
print ("[0,1,0] ile [0,0,1] �apraz �arp�m�:", np.cross (y, x) )

print ("\n[0,0,2] ile (0,3,0) cross/�apraz �arp�m�:", np.cross ([0,0,2], (0,3,0)) )
print ("(0,3,0) ile [0,0,2] �apraz �arp�m�:", np.cross ((0,3,0), [0,0,2]) )

print ("\n(0,1,2) ile (1,3,0) cross/�apraz �arp�m�:", np.cross ((0,1,2), (1,3,0)) )
print ("(1,3,0) ile (0,1,2) �apraz �arp�m�:", np.cross ((1,3,0), (0,1,2)) )



"""��kt�:
>python p_31005.py
[0,0,1] ile [0,1,0] cross/�apraz �arp�m�: [-1  0  0]
[0,1,0] ile [0,0,1] �apraz �arp�m�: [1 0 0]

[0,0,2] ile (0,3,0) cross/�apraz �arp�m�: [-6  0  0]
(0,3,0) ile [0,0,2] �apraz �arp�m�: [6 0 0]

(0,1,2) ile (1,3,0) cross/�apraz �arp�m�: [-6  2 -1]
(1,3,0) ile (0,1,2) �apraz �arp�m�: [ 6 -2  1]
"""