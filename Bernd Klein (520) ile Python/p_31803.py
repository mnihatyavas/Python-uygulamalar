# coding:iso-8859-9 Türkçe
# p_31803.py: Herhangi bir jpg png gif resmini görüntüleme örneği.

import matplotlib.pyplot as mp
from p_315 import Renk

mp.style.use ("dark_background")
resim = mp.imread ('resim/nehirliDağlar.jpg')
mp.imshow (resim)

mp.title ("'.jpg, .png ve .gif' Resimleri", color="r", fontsize=20) # color=Renk.renk()
mp.axis ("off")
mp.tight_layout()
mp.show()
#-----------------------------------------------------------------------------------------------------

mp.figure().set_facecolor (Renk.renk())
resim2 = mp.imread ('resim/frankfurt.png') [:, :, 1]
mp.imshow (resim2)

mp.title ("'.jpg, .png ve .gif' Resimleri", color=Renk.renk(), fontsize=20)
mp.axis ("off")
mp.tight_layout()
mp.show()
#-----------------------------------------------------------------------------------------------------

print ("Resim1'den veriler:\n", resim, sep="")
resim2 =resim [:, :, 1]
print ("\nResim2'den veriler:\n", resim2, sep="")



"""Çıktı:
>python p_31803.py
Resim1'den veriler:
[[[187 182 186]
  [189 184 188]
  [190 185 189]
  ...
  [212 207 203]
  [211 206 202]
  [211 206 202]]

 [[188 183 187]
  [189 184 188]
  [191 186 190]
  ...
  [211 206 202]
  [210 205 201]
  [210 205 201]]

 [[188 183 187]
  [190 185 189]
  [192 187 191]
  ...
  [211 206 202]
  [211 206 202]
  [211 206 202]]

 ...

 [[ 84  57  36]
  [ 94  67  46]
  [ 98  71  52]
  ...
  [ 38  36  39]
  [ 40  35  39]
  [ 38  36  39]]

 [[ 93  67  44]
  [114  88  65]
  [141 114  93]
  ...
  [ 45  40  44]
  [ 46  40  44]
  [ 44  39  43]]

 [[153 127 104]
  [120  94  71]
  [105  78  57]
  ...
  [ 42  36  40]
  [ 42  36  40]
  [ 42  36  40]]]

Resim2'den veriler:
[[182 184 185 ... 207 206 206]
 [183 184 186 ... 206 205 205]
 [183 185 187 ... 206 206 206]
 ...
 [ 57  67  71 ...  36  35  36]
 [ 67  88 114 ...  40  40  39]
 [127  94  78 ...  36  36  36]]
"""
