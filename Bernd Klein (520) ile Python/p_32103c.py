#coding:iso-8859-9 T�rk�e
# p_32103c.py Veri �er�eveleri sat�r ve s�tunlar�n�n na/mevcutlarla yeniden endekslenmesi �rne�i.

import pandas as pd
import numpy as np

kolonlar = ['a', 'b', 'c', 'd', 'e']
endeks = ['A', 'B', 'C', 'D', 'E']
v�1 = pd.DataFrame ( (np.random.rand (5, 5) * 201 - 100), columns=kolonlar, index=endeks)
print ("(5x5) ebatl� geli�ig�zel -/+100 say�l� veri �er�evesi:\n", v�1, sep="")
print ('\nSat�rlar� MEVCUTLARLA yeniden endeksli veri �er�evemiz:\n', v�1.reindex (['B', 'D', 'A', 'C', 'E']), sep="")

yeniEndeks = ['U', 'B', 'A', 'C', 'Z']
print ("\nSat�rlar� BAZI NaN NAMEVCUTLARLA yeniden endeksli veri �er�evemiz:\n", v�1.reindex (yeniEndeks), sep="")
print ("-"*70)
#---------------------------------------------------------------------------------------------------

yeniKolonlar = ['e', 'b', 'c', 'd', 'a']
print ("\nS�tunlar� MEVCUTLARLA yeniden endeksli veri �er�evemiz:\n", v�1.reindex (yeniKolonlar, axis='columns'), sep="")
  
yeniKolonlar =['b', 'a', 'c', 'g', 'h']
print ("\nS�tunlar� BAZI NaN NAMEVCUTLARLA yeniden endeksli veri �er�evemiz:\n", v�1.reindex (yeniKolonlar, axis ='columns'), sep="")
print ("\nS�tunlar� BAZI 1.5 NAMEVCUTLARLA yeniden endeksli veri �er�evemiz:\n", v�1.reindex (yeniKolonlar, axis ='columns', fill_value=1.5), sep="")
print ("\nS�tunlar� BAZI 'Eksik Veri' NAMEVCUTLARLA yeniden endeksli veri �er�evemiz:\n", v�1.reindex (yeniKolonlar, axis ='columns', fill_value="Eksik Veri"), sep="")



"""��kt�:
>python p_32103c.py
(5x5) ebatl� geli�ig�zel -/+100 say�l� veri �er�evesi:
           a          b          c          d          e
A  -6.636655 -79.320976 -11.207970 -69.949998 -65.854142
B  40.076864 -41.378856  70.065292  10.179271  94.160585
C -92.320858  27.596057  49.257260  34.214894 -96.424048
D -86.315057 -40.534008  -2.065819 -28.040501  -9.381370
E  65.715722 -62.564715  74.712089  72.536531 -47.630570

Sat�rlar� MEVCUTLARLA yeniden endeksli veri �er�evemiz:
           a          b          c          d          e
B  40.076864 -41.378856  70.065292  10.179271  94.160585
D -86.315057 -40.534008  -2.065819 -28.040501  -9.381370
A  -6.636655 -79.320976 -11.207970 -69.949998 -65.854142
C -92.320858  27.596057  49.257260  34.214894 -96.424048
E  65.715722 -62.564715  74.712089  72.536531 -47.630570

Sat�rlar� BAZI NaN NAMEVCUTLARLA yeniden endeksli veri �er�evemiz:
           a          b          c          d          e
U        NaN        NaN        NaN        NaN        NaN
B  40.076864 -41.378856  70.065292  10.179271  94.160585
A  -6.636655 -79.320976 -11.207970 -69.949998 -65.854142
C -92.320858  27.596057  49.257260  34.214894 -96.424048
Z        NaN        NaN        NaN        NaN        NaN
----------------------------------------------------------------------

S�tunlar� MEVCUTLARLA yeniden endeksli veri �er�evemiz:
           e          b          c          d          a
A -65.854142 -79.320976 -11.207970 -69.949998  -6.636655
B  94.160585 -41.378856  70.065292  10.179271  40.076864
C -96.424048  27.596057  49.257260  34.214894 -92.320858
D  -9.381370 -40.534008  -2.065819 -28.040501 -86.315057
E -47.630570 -62.564715  74.712089  72.536531  65.715722

S�tunlar� BAZI NaN NAMEVCUTLARLA yeniden endeksli veri �er�evemiz:
           b          a          c   g   h
A -79.320976  -6.636655 -11.207970 NaN NaN
B -41.378856  40.076864  70.065292 NaN NaN
C  27.596057 -92.320858  49.257260 NaN NaN
D -40.534008 -86.315057  -2.065819 NaN NaN
E -62.564715  65.715722  74.712089 NaN NaN

S�tunlar� BAZI 1.5 NAMEVCUTLARLA yeniden endeksli veri �er�evemiz:
           b          a          c    g    h
A -79.320976  -6.636655 -11.207970  1.5  1.5
B -41.378856  40.076864  70.065292  1.5  1.5
C  27.596057 -92.320858  49.257260  1.5  1.5
D -40.534008 -86.315057  -2.065819  1.5  1.5
E -62.564715  65.715722  74.712089  1.5  1.5

S�tunlar� BAZI 'Eksik Veri' NAMEVCUTLARLA yeniden endeksli veri �er�evemiz:
           b          a          c           g           h
A -79.320976  -6.636655 -11.207970  Eksik Veri  Eksik Veri
B -41.378856  40.076864  70.065292  Eksik Veri  Eksik Veri
C  27.596057 -92.320858  49.257260  Eksik Veri  Eksik Veri
D -40.534008 -86.315057  -2.065819  Eksik Veri  Eksik Veri
E -62.564715  65.715722  74.712089  Eksik Veri  Eksik Veri
"""