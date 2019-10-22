# coding:iso-8859-9 Türkçe
# p_30302.py: numpy.dtype'ın tamsayı ve kayannoktalı çeşitleri örneği.

import numpy as np

dt = np.dtype ([('yoğunluk', np.int16)]) # np.int32 = "i4", np.int16 = "i2", np.int8 = "i1" (hatalı gösterim)
x = np.array ([(393,), (337,), (256,)], dtype=dt)

print ("np.array ile tek tip dizi/matris yaratılır;\ndtype ile ise her kolon için farklı tip yaratılabilir.\nBöylece np.dtype bize veritabanı tablosu oluşturmamıza imkan sağlar.")
print ("\ndt: ", dt, "\ntype(dt): ", type (dt), "\nstr(x) veya x: ", x, "\ntype(x): ", type (x), "\nrepr(x): ", repr (x), sep="")
print ("\nx('yoğunluk'):", x ["yoğunluk"] )
print ("-"*50)
#----------------------------------------------------------------------------------------------------

dt = np.dtype ([('yoğunluk', "i2")]) # Yukardakiyle aynı sonucu verir...
print ("dt=:", dt)
dt = np.dtype ([('yoğunluk', ">i2")])
print ("dt>:", dt)
dt = np.dtype ([('yoğunluk', "<i2")])
print ("dt<:", dt)

dt = np.dtype ([('yoğunluk', "i")]) # int64
print ("\ndt=:", dt)
dt = np.dtype ([('yoğunluk', ">i")])
print ("dt>:", dt)
dt = np.dtype ([('yoğunluk', "<i")])
print ("dt<:", dt)

dt = np.dtype ([('yoğunluk', "d")]) # d:double = float64 = f8
print ("\ndt=:", dt)
dt = np.dtype ([('yoğunluk', ">d")])
print ("dt>:", dt)
dt = np.dtype ([('yoğunluk', "<d")])
print ("dt<:", dt)

print()
dt = np.dtype ("=d"); print (dt.name, dt.byteorder, dt.itemsize)
dt = np.dtype (">d"); print (dt.name, dt.byteorder, dt.itemsize)
dt = np.dtype ("<d"); print (dt.name, dt.byteorder, dt.itemsize)



"""Çıktı:
>python p_30302.py
np.array ile tek tip dizi/matris yaratılır;
dtype ile ise her kolon için farklı tip yaratılabilir.
Böylece np.dtype bize veritabanı tablosu oluşturmamıza imkan sağlar.

dt: [('yoğunluk', '<i2')]
type(dt): <class 'numpy.dtype'>
str(x) veya x: [(393,) (337,) (256,)]
type(x): <class 'numpy.ndarray'>
repr(x): array([(393,), (337,), (256,)], dtype=[('yoğunluk', '<i2')])

x('yoğunluk'): [393 337 256]
--------------------------------------------------
dt=: [('yoğunluk', '<i2')]
dt>: [('yoğunluk', '>i2')]
dt<: [('yoğunluk', '<i2')]

dt=: [('yoğunluk', '<i4')]
dt>: [('yoğunluk', '>i4')]
dt<: [('yoğunluk', '<i4')]

dt=: [('yoğunluk', '<f8')]
dt>: [('yoğunluk', '>f8')]
dt<: [('yoğunluk', '<f8')]

float64 = 8
float64 > 8
float64 = 8
"""