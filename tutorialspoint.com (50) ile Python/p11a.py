# coding:iso-8859-9 T�rk�e
# Python3 - Date & Time

import time;

saniye = time.time()
print ("12:00am, January 1, 1970'den beri ge�en saniye:", saniye)

print (time.localtime() )
print (time.localtime (saniye) )
print (time.asctime (time.localtime (saniye)) )

print (time.asctime (time.localtime (time.time())))
time.sleep (3) # 3 saniye bekler...
print (time.asctime (time.localtime() ))
print (time.timezone)
print ("Saat dilimi:", - time.timezone / 3600)
print ("Saat dilimi ad�: ", time.tzname)