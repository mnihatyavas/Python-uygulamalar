# coding:iso-8859-9 T�rk�e
# p_30302.py: numpy.dtype'�n tamsay� ve kayannoktal� �e�itleri �rne�i.

import numpy as np

dt = np.dtype ([('yo�unluk', np.int16)]) # np.int32 = "i4", np.int16 = "i2", np.int8 = "i1" (hatal� g�sterim)
x = np.array ([(393,), (337,), (256,)], dtype=dt)

print ("np.array ile tek tip dizi/matris yarat�l�r;\ndtype ile ise her kolon i�in farkl� tip yarat�labilir.\nB�ylece np.dtype bize veritaban� tablosu olu�turmam�za imkan sa�lar.")
print ("\ndt: ", dt, "\ntype(dt): ", type (dt), "\nstr(x) veya x: ", x, "\ntype(x): ", type (x), "\nrepr(x): ", repr (x), sep="")
print ("\nx('yo�unluk'):", x ["yo�unluk"] )
print ("-"*50)
#----------------------------------------------------------------------------------------------------

dt = np.dtype ([('yo�unluk', "i2")]) # Yukardakiyle ayn� sonucu verir...
print ("dt=:", dt)
dt = np.dtype ([('yo�unluk', ">i2")])
print ("dt>:", dt)
dt = np.dtype ([('yo�unluk', "<i2")])
print ("dt<:", dt)

dt = np.dtype ([('yo�unluk', "i")]) # int64
print ("\ndt=:", dt)
dt = np.dtype ([('yo�unluk', ">i")])
print ("dt>:", dt)
dt = np.dtype ([('yo�unluk', "<i")])
print ("dt<:", dt)

dt = np.dtype ([('yo�unluk', "d")]) # d:double = float64 = f8
print ("\ndt=:", dt)
dt = np.dtype ([('yo�unluk', ">d")])
print ("dt>:", dt)
dt = np.dtype ([('yo�unluk', "<d")])
print ("dt<:", dt)

print()
dt = np.dtype ("=d"); print (dt.name, dt.byteorder, dt.itemsize)
dt = np.dtype (">d"); print (dt.name, dt.byteorder, dt.itemsize)
dt = np.dtype ("<d"); print (dt.name, dt.byteorder, dt.itemsize)



"""��kt�:
>python p_30302.py
np.array ile tek tip dizi/matris yarat�l�r;
dtype ile ise her kolon i�in farkl� tip yarat�labilir.
B�ylece np.dtype bize veritaban� tablosu olu�turmam�za imkan sa�lar.

dt: [('yo�unluk', '<i2')]
type(dt): <class 'numpy.dtype'>
str(x) veya x: [(393,) (337,) (256,)]
type(x): <class 'numpy.ndarray'>
repr(x): array([(393,), (337,), (256,)], dtype=[('yo�unluk', '<i2')])

x('yo�unluk'): [393 337 256]
--------------------------------------------------
dt=: [('yo�unluk', '<i2')]
dt>: [('yo�unluk', '>i2')]
dt<: [('yo�unluk', '<i2')]

dt=: [('yo�unluk', '<i4')]
dt>: [('yo�unluk', '>i4')]
dt<: [('yo�unluk', '<i4')]

dt=: [('yo�unluk', '<f8')]
dt>: [('yo�unluk', '>f8')]
dt<: [('yo�unluk', '<f8')]

float64 = 8
float64 > 8
float64 = 8
"""