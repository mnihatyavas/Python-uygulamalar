# coding:iso-8859-9 Türkçe

import re

# Örnekteki Düzenliİfade=RegularExpression=re modül metodu tüm rakamlı ÖSÜA kelimeleri yerine "***" koyar...
# sub-stitute (r-aw"kalıp", "değiştir", "dizge") #raw'da esc=\ etkisizdir

print (re.sub (r"([ÖSÜA])(\d+)", "***", "Önce Ö1957yılı04ayı17günü, Sonra S2018, Üst Ü1512bugün ve Alt A1704") )
