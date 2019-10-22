# coding:iso-8859-9 T�rk�e
# p_32202b.py: Erkek, kad�n ve toplam n�fuslar�n ard���k ve birle�ik d�k�m� �rne�i.

import pandas as pd

kolonAdlar� = ["�lke"] + list (range (2002, 2013))
erkekN�fusu = pd.read_csv ("p_32202x1.txt", sep=",", index_col=0, names=kolonAdlar�)
kad�nN�fusu = pd.read_csv ("p_32202x3.txt", sep=",", index_col=0, names=kolonAdlar�)
toplamN�fus = erkekN�fusu + kad�nN�fusu

birle�ikN�fus1 = pd.concat ([toplamN�fus, erkekN�fusu, kad�nN�fusu],
    keys=["TOPLAM", "ERKEK", "KADIN"])
v�1 = birle�ikN�fus1.sort_index()

print ("�LKELERE G�RE erkek, kad�n ve toplam n�fuslar�n ARDI�IK d�k�m�:\n", v�1, sep="")
print ("-"*75)
#------------------------------------------------------------------------------------------------------

print ("\nYILLARA G�RE erkek, kad�n ve toplam n�fuslar�n ARDI�IK d�k�m�:\n", v�1.T, sep="")
print ("-"*75)
#------------------------------------------------------------------------------------------------------

birle�ikN�fus2 = pd.concat ([toplamN�fus.T, erkekN�fusu.T, kad�nN�fusu.T],
    keys=["TOPLAM:", "Erkek:", "Kad�n:"])
v�2 = birle�ikN�fus2.swaplevel()
v�2.sort_index (inplace=True)

print ("\n4 �lkenin YILLARA G�RE erkek, kad�n ve toplam n�fuslar�n B�RLE��K d�k�m�:\n",
    v�2 [["Turkey", "Australia", "Greece", "Luxembourg"]], sep="")



"""��kt�:
>python p_32202b.py
�LKELERE G�RE erkek, kad�n ve toplam n�fuslar�n ARDI�IK d�k�m�:
                               2002       2003  ...       2011       2012
       �lke                                     ...
ERKEK  Australia          9753133.0    9873447  ...   11260747   11280804
       Austria            3959567.0    3909120  ...    4095337    4118035
       Belgium            5042288.0    5066885  ...    5370234    5413801
       Canada                   NaN   15532438  ...   16826122   17113541
       Czech Republic     5005508.0    4966706  ...    5168799    5158210
       Denmark            2654146.0    2662423  ...    2756582    2766776
       Finland            2537597.0    2544916  ...    2638416    2652534
       France            28827658.0   28974588  ...   31531113   31670391
       Germany           40274676.0   40344879  ...   40112425   40206663
       Greece             5440113.0    5448582  ...    5600067    5590131
       Hungary            4836980.0    4818456  ...    4743901    4731724
       Iceland             143450.0     144287  ...     160006     160364
       Ireland            1928276.0    1969123  ...    2268429    2269831
       Italy             27587242.0   27766223  ...   29413274   29512404
       Japan             62244000.0   62250000  ...   62327000   62184000
       Korea             23983838.0   24126185  ...   24942339   25039557
       Luxembourg          218820.0     221009  ...     254619     261820
       Mexico            50683083.0   51274171  ...   53229849   56519797
       Netherlands        7971967.0    8015471  ...    8243482    8282871
       New Zealand        1934010.0    1971300  ...    2164590    2180100
       Norway             2241934.0    2256107  ...    2460849    2498871
       Poland            18760788.0   18506749  ...   18444373   18654577
       Portugal           4991590.0    5030247  ...    5146643    5030437
       Slovak Republic    2611921.0    2611306  ...    2642240    2631752
       Spain             19779378.0   20387085  ...   22724864   23099012
       Sweden             4408445.0    4427107  ...    4690244    4726834
       Switzerland        3549089.0    3575029  ...    3877426    3922253
       Turkey                   NaN   35418484  ...   37043182   37532954
       United Kingdom    28953126.0   28930648  ...   30772582   31140669
       United States    135301432.0  141957038  ...  152449134  153596908
...                             ...        ...  ...        ...        ...
TOPLAM Australia         19640979.0   19872646  ...   22620554   22683573
       Austria            8139310.0    8067289  ...    8404252    8443018
       Belgium           10309725.0   10355844  ...   10366843   11035958
       Canada                   NaN   31361611  ...   33927935   34492645
       Czech Republic    10269726.0   10203269  ...   10532770   10505445
       Denmark            5368354.0    5383507  ...    5560628    5580516
       Finland            5194901.0    5206295  ...    5375276    5401267
       France            59337731.0   59630121  ...   65129746   65394283
       Germany           82440309.0   82536680  ...   81751602   81843743
       Greece            10988000.0   11006377  ...   11309885   11290067
       Hungary           10174853.0   10142362  ...    9985722    9957731
       Iceland             286575.0     288471  ...     318452     319575
       Ireland            3882683.0    3963636  ...    4569864    4582769
       Italy             56993742.0   57321070  ...   60626442   60820696
       Japan            127291000.0  127435000  ...  128057000  127799000
       Korea             47639618.0   47925318  ...   49779440   50004441
       Luxembourg          444050.0     448300  ...     511840     524853
       Mexico           101826249.0  103039964  ...  108396211  115682867
       Netherlands       16105285.0   16192572  ...   16655799   16730348
       New Zealand        3939130.0    4009200  ...    4405150    4433100
       Norway             4524066.0    4552252  ...    4920305    4985870
       Poland            38632453.0   38218531  ...   38200037   38538447
       Portugal          10335559.0   10407465  ...   10636979   10542398
       Slovak Republic    5378951.0    5379161  ...    5435273    5404322
       Spain             40409330.0   41550584  ...   46152926   46818221
       Sweden             8909128.0    8940788  ...    9415570    9482855
       Switzerland        7261210.0    7313853  ...    7870134    7954662
       Turkey                   NaN   70171979  ...   73722988   74724269
       United Kingdom    58706905.0   59262057  ...   62498612   63256154
       United States    277244916.0  288774226  ...  309989078  312232049

[90 rows x 11 columns]
---------------------------------------------------------------------------

YILLARA G�RE erkek, kad�n ve toplam n�fuslar�n ARDI�IK d�k�m�:
           ERKEK                        ...      TOPLAM

�lke   Australia    Austria    Belgium  ...      Turkey United Kingdom United States
2002   9753133.0  3959567.0  5042288.0  ...         NaN     58706905.0   277244916.0
2003   9873447.0  3909120.0  5066885.0  ...  70171979.0     59262057.0   288774226.0
2004   9990513.0  3949825.0  5087176.0  ...  70689500.0     59699828.0   290810719.0
2005  10121438.0  3986296.0  5111325.0  ...  71607500.0     60059858.0   294442683.0
2006  10257418.0  4019354.0  5143821.0  ...  72519974.0     60412870.0   297308143.0
2007  10444622.0  4037171.0  5181408.0  ...  72519974.0     60781346.0   300184434.0
2008  10660917.0  4054214.0  5224309.0  ...  70586256.0     61179260.0   304846731.0
2009  10888385.0  4068047.0  5268651.0  ...  71517100.0     61595094.0   305127551.0
2010  11124254.0  4079093.0  5312221.0  ...  72561312.0     62026962.0   307756577.0
2011  11260747.0  4095337.0  5370234.0  ...  73722988.0     62498612.0   309989078.0
2012  11280804.0  4118035.0  5413801.0  ...  74724269.0     63256154.0   312232049.0

[11 rows x 90 columns]
---------------------------------------------------------------------------

4 �lkenin YILLARA G�RE erkek, kad�n ve toplam n�fuslar�n B�RLE��K d�k�m�:
�lke              Turkey   Australia      Greece  Luxembourg
2002 Erkek:          NaN   9753133.0   5440113.0    218820.0
     Kad�n:          NaN   9887846.0   5547887.0    225230.0
     TOPLAM:         NaN  19640979.0  10988000.0    444050.0
2003 Erkek:   35418484.0   9873447.0   5448582.0    221009.0
     Kad�n:   34753495.0   9999199.0   5557795.0    227291.0
     TOPLAM:  70171979.0  19872646.0  11006377.0    448300.0
2004 Erkek:   35666000.0   9990513.0   5464401.0    223020.0
     Kad�n:   35023500.0  10100991.0   5576249.0    228580.0
     TOPLAM:  70689500.0  20091504.0  11040650.0    451600.0
2005 Erkek:   36123000.0  10121438.0   5486632.0    224740.0
     Kad�n:   35484500.0  10218321.0   5596119.0    230260.0
     TOPLAM:  71607500.0  20339759.0  11082751.0    455000.0
2006 Erkek:   36574211.0  10257418.0   5508165.0    232100.0
     Kad�n:   35945763.0  10348070.0   5617014.0    236986.0
     TOPLAM:  72519974.0  20605488.0  11125179.0    469086.0
2007 Erkek:   36574211.0  10444622.0   5532047.0    235792.0
     Kad�n:   35945763.0  10570420.0   5639693.0    240395.0
     TOPLAM:  72519974.0  21015042.0  11171740.0    476187.0
2008 Erkek:   35376533.0  10660917.0   5553895.0    239607.0
     Kad�n:   35209723.0  10770864.0   5659890.0    244192.0
     TOPLAM:  70586256.0  21431781.0  11213785.0    483799.0
2009 Erkek:   35901154.0  10888385.0   5576740.0    244835.0
     Kad�n:   35615946.0  10986535.0   5683662.0    248665.0
     TOPLAM:  71517100.0  21874920.0  11260402.0    493500.0
2010 Erkek:   36462470.0  11124254.0   5597465.0    249406.0
     Kad�n:   36098842.0  11218144.0   5707653.0    252660.0
     TOPLAM:  72561312.0  22342398.0  11305118.0    502066.0
2011 Erkek:   37043182.0  11260747.0   5600067.0    254619.0
     Kad�n:   36679806.0  11359807.0   5709818.0    257221.0
     TOPLAM:  73722988.0  22620554.0  11309885.0    511840.0
2012 Erkek:   37532954.0  11280804.0   5590131.0    261820.0
     Kad�n:   37191315.0  11402769.0   5699936.0    263033.0
     TOPLAM:  74724269.0  22683573.0  11290067.0    524853.0
"""