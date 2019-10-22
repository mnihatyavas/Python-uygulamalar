# coding:iso-8859-9 "Türkçe"

import calendar

yıl = int (input ("4 rakamlı yılı girin: "))  
ay = int (input ("1-12 ay rakamını girin: "))  

print ("AYLIK TAKVİM\n=====================\n", calendar.month (yıl, ay))
