# coding:iso-8859-9 T�rk�e
# p_30410.py: Bir �ehrin di�erlerine uzakl��� listesini her �ehrin di�er her �ehre uzakl��� matrisine �evirme �rne�i.

import numpy as np

�ehirler = ["Barselona", "Berlin", "Br�ksel", "Bu�arest", "Budape�te",
    "Kopenhag", "Dublin", "Hamburg", "�stanbul", "Kiyev", "Londra", "Madrid",
    "Milan", "Moskova", "M�nih", "Paris", "Prag", "Roma", "Sen Petersburg",
    "Stokholm", "Viyana", "Var�ova"] # Toplam 22 �ehir...

barselonayaMil = [0,  1498, 1063, 1968, 1498, 1758, 1469, 1472, 2230, 2391,
    1138, 505, 725, 3007, 1055, 833, 1354, 857, 2813, 2277, 1347, 1862]

barselonaya =  np.array (barselonayaMil)
#barselonaya = np.abs (barselonaya * 1.613) # Mil-->Km �evrimi...
herbirine = np.abs (barselonaya - barselonaya[:, np.newaxis])

print ("Barselona'dan di�er 21 �ehre olan mesafe/Km dizisi:\n", barselonaya, sep="")
print ("\nHerbir '0' �ehirden di�er 21'ine olan mesafe matrisi:\n", herbirine, sep="")

print ("\nHerbir �ehirden di�erine alt-alta d�k�m:")
for i in range (len (�ehirler)):
    for j in range (len (�ehirler)):
        print (�ehirler [i], "-->", �ehirler [j], ": ", herbirine [i] [j], " km", sep="")
    print() #input ("[Ent]:")



"""��kt�:
>python p_30410.py
Barselona'dan di�er 21 �ehre olan mesafe/Km dizisi:
[   0 1498 1063 1968 1498 1758 1469 1472 2230 2391 1138  505  725 3007
 1055  833 1354  857 2813 2277 1347 1862]

Herbir '0' �ehirden di�er 21'ine olan mesafe matrisi:
[[   0 1498 1063 1968 1498 1758 1469 1472 2230 2391 1138  505  725 3007 1055  833 1354  857 2813 2277 1347 1862]
 [1498    0  435  470    0  260   29   26  732  893  360  993  773 1509  443  665  144  641 1315  779  151  364]
 [1063  435    0  905  435  695  406  409 1167 1328   75  558  338 1944  8  230  291  206 1750 1214  284  799]
 [1968  470  905    0  470  210  499  496  262  423  830 1463 1243 1039  913 1135  614 1111  845  309  621  106]
 [1498    0  435  470    0  260   29   26  732  893  360  993  773 1509  443  665  144  641 1315  779  151  364]
 [1758  260  695  210  260    0  289  286  472  633  620 1253 1033 1249  703  925  404  901 1055  519  411  104]
 [1469   29  406  499   29  289    0    3  761  922  331  964  744 1538  414  636  115  612 1344  808  122  393]
 [1472   26  409  496   26  286    3    0  758  919  334  967  747 1535  417  639  118  615 1341  805  125  390]
 [2230  732 1167  262  732  472  761  758    0  161 1092 1725 1505  777 1175 1397  876 1373  583   47  883  368]
 [2391  893 1328  423  893  633  922  919  161    0 1253 1886 1666  616 1336 1558 1037 1534  422  114 1044  529]
 [1138  360   75  830  360  620  331  334 1092 1253    0  633  413 1869   83  305  216  281 1675 1139  209  724]
 [ 505  993  558 1463  993 1253  964  967 1725 1886  633    0  220 2502  550  328  849  352 2308 1772  842 1357]
 [ 725  773  338 1243  773 1033  744  747 1505 1666  413  220    0 2282  330  108  629  132 2088 1552  622 1137]
 [3007 1509 1944 1039 1509 1249 1538 1535  777  616 1869 2502 2282    0 1952 2174 1653 2150  194  730 1660 1145]
 [1055  443    8  913  443  703  414  417 1175 1336   83  550  330 1952   0  222  299  198 1758 1222  292  807]
 [ 833  665  230 1135  665  925  636  639 1397 1558  305  328  108 2174  222    0  521   24 1980 1444  514 1029]
 [1354  144  291  614  144  404  115  118  876 1037  216  849  629 1653  299  521    0  497 1459  923    7  508]
 [ 857  641  206 1111  641  901  612  615 1373 1534  281  352  132 2150  198   24  497    0 1956 1420  490 1005]
 [2813 1315 1750  845 1315 1055 1344 1341  583  422 1675 2308 2088  194 1758 1980 1459 1956    0  536 1466  951]
 [2277  779 1214  309  779  519  808  805   47  114 1139 1772 1552  730 1222 1444  923 1420  536    0  930  415]
 [1347  151  284  621  151  411  122  125  883 1044  209  842  622 1660  292  514    7  490 1466  930    0  515]
 [1862  364  799  106  364  104  393  390  368  529  724 1357 1137 1145  807 1029  508 1005  951  415  515    0]]

Herbir �ehirden di�erine alt-alta d�k�m:
Barselona-->Barselona: 0 km
Barselona-->Berlin: 1498 km
Barselona-->Br�ksel: 1063 km
Barselona-->Bu�arest: 1968 km
Barselona-->Budape�te: 1498 km
Barselona-->Kopenhag: 1758 km
Barselona-->Dublin: 1469 km
Barselona-->Hamburg: 1472 km
Barselona-->�stanbul: 2230 km
Barselona-->Kiyev: 2391 km
Barselona-->Londra: 1138 km
Barselona-->Madrid: 505 km
Barselona-->Milan: 725 km
Barselona-->Moskova: 3007 km
Barselona-->M�nih: 1055 km
Barselona-->Paris: 833 km
Barselona-->Prag: 1354 km
Barselona-->Roma: 857 km
Barselona-->Sen Petersburg: 2813 km
Barselona-->Stokholm: 2277 km
Barselona-->Viyana: 1347 km
Barselona-->Var�ova: 1862 km

Berlin-->Barselona: 1498 km
Berlin-->Berlin: 0 km
Berlin-->Br�ksel: 435 km
Berlin-->Bu�arest: 470 km
Berlin-->Budape�te: 0 km
Berlin-->Kopenhag: 260 km
Berlin-->Dublin: 29 km
Berlin-->Hamburg: 26 km
Berlin-->�stanbul: 732 km
Berlin-->Kiyev: 893 km
Berlin-->Londra: 360 km
Berlin-->Madrid: 993 km
Berlin-->Milan: 773 km
Berlin-->Moskova: 1509 km
Berlin-->M�nih: 443 km
Berlin-->Paris: 665 km
Berlin-->Prag: 144 km
Berlin-->Roma: 641 km
Berlin-->Sen Petersburg: 1315 km
Berlin-->Stokholm: 779 km
Berlin-->Viyana: 151 km
Berlin-->Var�ova: 364 km

Br�ksel-->Barselona: 1063 km
Br�ksel-->Berlin: 435 km
Br�ksel-->Br�ksel: 0 km
Br�ksel-->Bu�arest: 905 km
Br�ksel-->Budape�te: 435 km
Br�ksel-->Kopenhag: 695 km
Br�ksel-->Dublin: 406 km
Br�ksel-->Hamburg: 409 km
Br�ksel-->�stanbul: 1167 km
Br�ksel-->Kiyev: 1328 km
Br�ksel-->Londra: 75 km
Br�ksel-->Madrid: 558 km
Br�ksel-->Milan: 338 km
Br�ksel-->Moskova: 1944 km
Br�ksel-->M�nih: 8 km
Br�ksel-->Paris: 230 km
Br�ksel-->Prag: 291 km
Br�ksel-->Roma: 206 km
Br�ksel-->Sen Petersburg: 1750 km
Br�ksel-->Stokholm: 1214 km
Br�ksel-->Viyana: 284 km
Br�ksel-->Var�ova: 799 km

Bu�arest-->Barselona: 1968 km
Bu�arest-->Berlin: 470 km
Bu�arest-->Br�ksel: 905 km
Bu�arest-->Bu�arest: 0 km
Bu�arest-->Budape�te: 470 km
Bu�arest-->Kopenhag: 210 km
Bu�arest-->Dublin: 499 km
Bu�arest-->Hamburg: 496 km
Bu�arest-->�stanbul: 262 km
Bu�arest-->Kiyev: 423 km
Bu�arest-->Londra: 830 km
Bu�arest-->Madrid: 1463 km
Bu�arest-->Milan: 1243 km
Bu�arest-->Moskova: 1039 km
Bu�arest-->M�nih: 913 km
Bu�arest-->Paris: 1135 km
Bu�arest-->Prag: 614 km
Bu�arest-->Roma: 1111 km
Bu�arest-->Sen Petersburg: 845 km
Bu�arest-->Stokholm: 309 km
Bu�arest-->Viyana: 621 km
Bu�arest-->Var�ova: 106 km

Budape�te-->Barselona: 1498 km
Budape�te-->Berlin: 0 km
Budape�te-->Br�ksel: 435 km
Budape�te-->Bu�arest: 470 km
Budape�te-->Budape�te: 0 km
Budape�te-->Kopenhag: 260 km
Budape�te-->Dublin: 29 km
Budape�te-->Hamburg: 26 km
Budape�te-->�stanbul: 732 km
Budape�te-->Kiyev: 893 km
Budape�te-->Londra: 360 km
Budape�te-->Madrid: 993 km
Budape�te-->Milan: 773 km
Budape�te-->Moskova: 1509 km
Budape�te-->M�nih: 443 km
Budape�te-->Paris: 665 km
Budape�te-->Prag: 144 km
Budape�te-->Roma: 641 km
Budape�te-->Sen Petersburg: 1315 km
Budape�te-->Stokholm: 779 km
Budape�te-->Viyana: 151 km
Budape�te-->Var�ova: 364 km

Kopenhag-->Barselona: 1758 km
Kopenhag-->Berlin: 260 km
Kopenhag-->Br�ksel: 695 km
Kopenhag-->Bu�arest: 210 km
Kopenhag-->Budape�te: 260 km
Kopenhag-->Kopenhag: 0 km
Kopenhag-->Dublin: 289 km
Kopenhag-->Hamburg: 286 km
Kopenhag-->�stanbul: 472 km
Kopenhag-->Kiyev: 633 km
Kopenhag-->Londra: 620 km
Kopenhag-->Madrid: 1253 km
Kopenhag-->Milan: 1033 km
Kopenhag-->Moskova: 1249 km
Kopenhag-->M�nih: 703 km
Kopenhag-->Paris: 925 km
Kopenhag-->Prag: 404 km
Kopenhag-->Roma: 901 km
Kopenhag-->Sen Petersburg: 1055 km
Kopenhag-->Stokholm: 519 km
Kopenhag-->Viyana: 411 km
Kopenhag-->Var�ova: 104 km

Dublin-->Barselona: 1469 km
Dublin-->Berlin: 29 km
Dublin-->Br�ksel: 406 km
Dublin-->Bu�arest: 499 km
Dublin-->Budape�te: 29 km
Dublin-->Kopenhag: 289 km
Dublin-->Dublin: 0 km
Dublin-->Hamburg: 3 km
Dublin-->�stanbul: 761 km
Dublin-->Kiyev: 922 km
Dublin-->Londra: 331 km
Dublin-->Madrid: 964 km
Dublin-->Milan: 744 km
Dublin-->Moskova: 1538 km
Dublin-->M�nih: 414 km
Dublin-->Paris: 636 km
Dublin-->Prag: 115 km
Dublin-->Roma: 612 km
Dublin-->Sen Petersburg: 1344 km
Dublin-->Stokholm: 808 km
Dublin-->Viyana: 122 km
Dublin-->Var�ova: 393 km

Hamburg-->Barselona: 1472 km
Hamburg-->Berlin: 26 km
Hamburg-->Br�ksel: 409 km
Hamburg-->Bu�arest: 496 km
Hamburg-->Budape�te: 26 km
Hamburg-->Kopenhag: 286 km
Hamburg-->Dublin: 3 km
Hamburg-->Hamburg: 0 km
Hamburg-->�stanbul: 758 km
Hamburg-->Kiyev: 919 km
Hamburg-->Londra: 334 km
Hamburg-->Madrid: 967 km
Hamburg-->Milan: 747 km
Hamburg-->Moskova: 1535 km
Hamburg-->M�nih: 417 km
Hamburg-->Paris: 639 km
Hamburg-->Prag: 118 km
Hamburg-->Roma: 615 km
Hamburg-->Sen Petersburg: 1341 km
Hamburg-->Stokholm: 805 km
Hamburg-->Viyana: 125 km
Hamburg-->Var�ova: 390 km

�stanbul-->Barselona: 2230 km
�stanbul-->Berlin: 732 km
�stanbul-->Br�ksel: 1167 km
�stanbul-->Bu�arest: 262 km
�stanbul-->Budape�te: 732 km
�stanbul-->Kopenhag: 472 km
�stanbul-->Dublin: 761 km
�stanbul-->Hamburg: 758 km
�stanbul-->�stanbul: 0 km
�stanbul-->Kiyev: 161 km
�stanbul-->Londra: 1092 km
�stanbul-->Madrid: 1725 km
�stanbul-->Milan: 1505 km
�stanbul-->Moskova: 777 km
�stanbul-->M�nih: 1175 km
�stanbul-->Paris: 1397 km
�stanbul-->Prag: 876 km
�stanbul-->Roma: 1373 km
�stanbul-->Sen Petersburg: 583 km
�stanbul-->Stokholm: 47 km
�stanbul-->Viyana: 883 km
�stanbul-->Var�ova: 368 km

Kiyev-->Barselona: 2391 km
Kiyev-->Berlin: 893 km
Kiyev-->Br�ksel: 1328 km
Kiyev-->Bu�arest: 423 km
Kiyev-->Budape�te: 893 km
Kiyev-->Kopenhag: 633 km
Kiyev-->Dublin: 922 km
Kiyev-->Hamburg: 919 km
Kiyev-->�stanbul: 161 km
Kiyev-->Kiyev: 0 km
Kiyev-->Londra: 1253 km
Kiyev-->Madrid: 1886 km
Kiyev-->Milan: 1666 km
Kiyev-->Moskova: 616 km
Kiyev-->M�nih: 1336 km
Kiyev-->Paris: 1558 km
Kiyev-->Prag: 1037 km
Kiyev-->Roma: 1534 km
Kiyev-->Sen Petersburg: 422 km
Kiyev-->Stokholm: 114 km
Kiyev-->Viyana: 1044 km
Kiyev-->Var�ova: 529 km

Londra-->Barselona: 1138 km
Londra-->Berlin: 360 km
Londra-->Br�ksel: 75 km
Londra-->Bu�arest: 830 km
Londra-->Budape�te: 360 km
Londra-->Kopenhag: 620 km
Londra-->Dublin: 331 km
Londra-->Hamburg: 334 km
Londra-->�stanbul: 1092 km
Londra-->Kiyev: 1253 km
Londra-->Londra: 0 km
Londra-->Madrid: 633 km
Londra-->Milan: 413 km
Londra-->Moskova: 1869 km
Londra-->M�nih: 83 km
Londra-->Paris: 305 km
Londra-->Prag: 216 km
Londra-->Roma: 281 km
Londra-->Sen Petersburg: 1675 km
Londra-->Stokholm: 1139 km
Londra-->Viyana: 209 km
Londra-->Var�ova: 724 km

Madrid-->Barselona: 505 km
Madrid-->Berlin: 993 km
Madrid-->Br�ksel: 558 km
Madrid-->Bu�arest: 1463 km
Madrid-->Budape�te: 993 km
Madrid-->Kopenhag: 1253 km
Madrid-->Dublin: 964 km
Madrid-->Hamburg: 967 km
Madrid-->�stanbul: 1725 km
Madrid-->Kiyev: 1886 km
Madrid-->Londra: 633 km
Madrid-->Madrid: 0 km
Madrid-->Milan: 220 km
Madrid-->Moskova: 2502 km
Madrid-->M�nih: 550 km
Madrid-->Paris: 328 km
Madrid-->Prag: 849 km
Madrid-->Roma: 352 km
Madrid-->Sen Petersburg: 2308 km
Madrid-->Stokholm: 1772 km
Madrid-->Viyana: 842 km
Madrid-->Var�ova: 1357 km

Milan-->Barselona: 725 km
Milan-->Berlin: 773 km
Milan-->Br�ksel: 338 km
Milan-->Bu�arest: 1243 km
Milan-->Budape�te: 773 km
Milan-->Kopenhag: 1033 km
Milan-->Dublin: 744 km
Milan-->Hamburg: 747 km
Milan-->�stanbul: 1505 km
Milan-->Kiyev: 1666 km
Milan-->Londra: 413 km
Milan-->Madrid: 220 km
Milan-->Milan: 0 km
Milan-->Moskova: 2282 km
Milan-->M�nih: 330 km
Milan-->Paris: 108 km
Milan-->Prag: 629 km
Milan-->Roma: 132 km
Milan-->Sen Petersburg: 2088 km
Milan-->Stokholm: 1552 km
Milan-->Viyana: 622 km
Milan-->Var�ova: 1137 km

Moskova-->Barselona: 3007 km
Moskova-->Berlin: 1509 km
Moskova-->Br�ksel: 1944 km
Moskova-->Bu�arest: 1039 km
Moskova-->Budape�te: 1509 km
Moskova-->Kopenhag: 1249 km
Moskova-->Dublin: 1538 km
Moskova-->Hamburg: 1535 km
Moskova-->�stanbul: 777 km
Moskova-->Kiyev: 616 km
Moskova-->Londra: 1869 km
Moskova-->Madrid: 2502 km
Moskova-->Milan: 2282 km
Moskova-->Moskova: 0 km
Moskova-->M�nih: 1952 km
Moskova-->Paris: 2174 km
Moskova-->Prag: 1653 km
Moskova-->Roma: 2150 km
Moskova-->Sen Petersburg: 194 km
Moskova-->Stokholm: 730 km
Moskova-->Viyana: 1660 km
Moskova-->Var�ova: 1145 km

M�nih-->Barselona: 1055 km
M�nih-->Berlin: 443 km
M�nih-->Br�ksel: 8 km
M�nih-->Bu�arest: 913 km
M�nih-->Budape�te: 443 km
M�nih-->Kopenhag: 703 km
M�nih-->Dublin: 414 km
M�nih-->Hamburg: 417 km
M�nih-->�stanbul: 1175 km
M�nih-->Kiyev: 1336 km
M�nih-->Londra: 83 km
M�nih-->Madrid: 550 km
M�nih-->Milan: 330 km
M�nih-->Moskova: 1952 km
M�nih-->M�nih: 0 km
M�nih-->Paris: 222 km
M�nih-->Prag: 299 km
M�nih-->Roma: 198 km
M�nih-->Sen Petersburg: 1758 km
M�nih-->Stokholm: 1222 km
M�nih-->Viyana: 292 km
M�nih-->Var�ova: 807 km

Paris-->Barselona: 833 km
Paris-->Berlin: 665 km
Paris-->Br�ksel: 230 km
Paris-->Bu�arest: 1135 km
Paris-->Budape�te: 665 km
Paris-->Kopenhag: 925 km
Paris-->Dublin: 636 km
Paris-->Hamburg: 639 km
Paris-->�stanbul: 1397 km
Paris-->Kiyev: 1558 km
Paris-->Londra: 305 km
Paris-->Madrid: 328 km
Paris-->Milan: 108 km
Paris-->Moskova: 2174 km
Paris-->M�nih: 222 km
Paris-->Paris: 0 km
Paris-->Prag: 521 km
Paris-->Roma: 24 km
Paris-->Sen Petersburg: 1980 km
Paris-->Stokholm: 1444 km
Paris-->Viyana: 514 km
Paris-->Var�ova: 1029 km

Prag-->Barselona: 1354 km
Prag-->Berlin: 144 km
Prag-->Br�ksel: 291 km
Prag-->Bu�arest: 614 km
Prag-->Budape�te: 144 km
Prag-->Kopenhag: 404 km
Prag-->Dublin: 115 km
Prag-->Hamburg: 118 km
Prag-->�stanbul: 876 km
Prag-->Kiyev: 1037 km
Prag-->Londra: 216 km
Prag-->Madrid: 849 km
Prag-->Milan: 629 km
Prag-->Moskova: 1653 km
Prag-->M�nih: 299 km
Prag-->Paris: 521 km
Prag-->Prag: 0 km
Prag-->Roma: 497 km
Prag-->Sen Petersburg: 1459 km
Prag-->Stokholm: 923 km
Prag-->Viyana: 7 km
Prag-->Var�ova: 508 km

Roma-->Barselona: 857 km
Roma-->Berlin: 641 km
Roma-->Br�ksel: 206 km
Roma-->Bu�arest: 1111 km
Roma-->Budape�te: 641 km
Roma-->Kopenhag: 901 km
Roma-->Dublin: 612 km
Roma-->Hamburg: 615 km
Roma-->�stanbul: 1373 km
Roma-->Kiyev: 1534 km
Roma-->Londra: 281 km
Roma-->Madrid: 352 km
Roma-->Milan: 132 km
Roma-->Moskova: 2150 km
Roma-->M�nih: 198 km
Roma-->Paris: 24 km
Roma-->Prag: 497 km
Roma-->Roma: 0 km
Roma-->Sen Petersburg: 1956 km
Roma-->Stokholm: 1420 km
Roma-->Viyana: 490 km
Roma-->Var�ova: 1005 km

Sen Petersburg-->Barselona: 2813 km
Sen Petersburg-->Berlin: 1315 km
Sen Petersburg-->Br�ksel: 1750 km
Sen Petersburg-->Bu�arest: 845 km
Sen Petersburg-->Budape�te: 1315 km
Sen Petersburg-->Kopenhag: 1055 km
Sen Petersburg-->Dublin: 1344 km
Sen Petersburg-->Hamburg: 1341 km
Sen Petersburg-->�stanbul: 583 km
Sen Petersburg-->Kiyev: 422 km
Sen Petersburg-->Londra: 1675 km
Sen Petersburg-->Madrid: 2308 km
Sen Petersburg-->Milan: 2088 km
Sen Petersburg-->Moskova: 194 km
Sen Petersburg-->M�nih: 1758 km
Sen Petersburg-->Paris: 1980 km
Sen Petersburg-->Prag: 1459 km
Sen Petersburg-->Roma: 1956 km
Sen Petersburg-->Sen Petersburg: 0 km
Sen Petersburg-->Stokholm: 536 km
Sen Petersburg-->Viyana: 1466 km
Sen Petersburg-->Var�ova: 951 km

Stokholm-->Barselona: 2277 km
Stokholm-->Berlin: 779 km
Stokholm-->Br�ksel: 1214 km
Stokholm-->Bu�arest: 309 km
Stokholm-->Budape�te: 779 km
Stokholm-->Kopenhag: 519 km
Stokholm-->Dublin: 808 km
Stokholm-->Hamburg: 805 km
Stokholm-->�stanbul: 47 km
Stokholm-->Kiyev: 114 km
Stokholm-->Londra: 1139 km
Stokholm-->Madrid: 1772 km
Stokholm-->Milan: 1552 km
Stokholm-->Moskova: 730 km
Stokholm-->M�nih: 1222 km
Stokholm-->Paris: 1444 km
Stokholm-->Prag: 923 km
Stokholm-->Roma: 1420 km
Stokholm-->Sen Petersburg: 536 km
Stokholm-->Stokholm: 0 km
Stokholm-->Viyana: 930 km
Stokholm-->Var�ova: 415 km

Viyana-->Barselona: 1347 km
Viyana-->Berlin: 151 km
Viyana-->Br�ksel: 284 km
Viyana-->Bu�arest: 621 km
Viyana-->Budape�te: 151 km
Viyana-->Kopenhag: 411 km
Viyana-->Dublin: 122 km
Viyana-->Hamburg: 125 km
Viyana-->�stanbul: 883 km
Viyana-->Kiyev: 1044 km
Viyana-->Londra: 209 km
Viyana-->Madrid: 842 km
Viyana-->Milan: 622 km
Viyana-->Moskova: 1660 km
Viyana-->M�nih: 292 km
Viyana-->Paris: 514 km
Viyana-->Prag: 7 km
Viyana-->Roma: 490 km
Viyana-->Sen Petersburg: 1466 km
Viyana-->Stokholm: 930 km
Viyana-->Viyana: 0 km
Viyana-->Var�ova: 515 km

Var�ova-->Barselona: 1862 km
Var�ova-->Berlin: 364 km
Var�ova-->Br�ksel: 799 km
Var�ova-->Bu�arest: 106 km
Var�ova-->Budape�te: 364 km
Var�ova-->Kopenhag: 104 km
Var�ova-->Dublin: 393 km
Var�ova-->Hamburg: 390 km
Var�ova-->�stanbul: 368 km
Var�ova-->Kiyev: 529 km
Var�ova-->Londra: 724 km
Var�ova-->Madrid: 1357 km
Var�ova-->Milan: 1137 km
Var�ova-->Moskova: 1145 km
Var�ova-->M�nih: 807 km
Var�ova-->Paris: 1029 km
Var�ova-->Prag: 508 km
Var�ova-->Roma: 1005 km
Var�ova-->Sen Petersburg: 951 km
Var�ova-->Stokholm: 415 km
Var�ova-->Viyana: 515 km
Var�ova-->Var�ova: 0 km

"""