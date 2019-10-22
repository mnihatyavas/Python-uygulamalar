# coding:iso-8859-9 Türkçe
# p_30905.py: Boolean dizisi kullanarak asal sayıların bulunması örneği.

import numpy as np

n = 100
try: n = abs (int ( input ("Asal sayı kontrolu üst sınırını girin [100]? ")))
except: n = 100

asalMı = np.ones ((n,), dtype=bool)

asalMı[:2] = 0 # İlk 0 ve 1 asal değildir...

# Eratosthenes eleği gereği çarpım katları asal değildir...
kontrolUzunluğu = int (np.sqrt (len (asalMı)))
for i in range (2, kontrolUzunluğu): asalMı [2*i::i] = False

print ("\nİlk ", n, " asal sayılar tüplesi:\n", np.nonzero (asalMı),
    "\n\nAsal sayılar listesi:\n", np.nonzero (asalMı)[0], sep="")

print ("\n(", np.count_nonzero (asalMı), "/", n, ") adet asal sayılar listesi: \n", np.flatnonzero (asalMı), sep="")
print()
for i in range (np.count_nonzero (asalMı)):
    print ((i+1), ":", np.flatnonzero (asalMı)[i], sep="", end=" ")



"""Çıktı:
>python p_30905.py
Asal sayı kontrolu üst sınırını girin [100]?

İlk 100 asal sayılar tüplesi:
(array([ 2,  3,  5,  7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97], dtype=int32),)

Asal sayılar listesi:
[ 2  3  5  7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97]

>python p_30905.py  ** TEKRAR **
Asal sayı kontrolu üst sınırını girin [100]? 1000

İlk 1000 asal sayılar tüplesi:
(array([  2,   3,   5,   7,  11,  13,  17,  19,  23,  29,  31,  37,  41,
        43,  47,  53,  59,  61,  67,  71,  73,  79,  83,  89,  97, 101,
       103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167,
       173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239,
       241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313,
       317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397,
       401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467,
       479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569,
       571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643,
       647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733,
       739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823,
       827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911,
       919, 929, 937, 941, 947, 953, 961, 967, 971, 977, 983, 991, 997],
      dtype=int32),)

Asal sayılar listesi:
[  2   3   5   7  11  13  17  19  23  29  31  37  41  43  47  53  59  61
  67  71  73  79  83  89  97 101 103 107 109 113 127 131 137 139 149 151
 157 163 167 173 179 181 191 193 197 199 211 223 227 229 233 239 241 251
 257 263 269 271 277 281 283 293 307 311 313 317 331 337 347 349 353 359
 367 373 379 383 389 397 401 409 419 421 431 433 439 443 449 457 461 463
 467 479 487 491 499 503 509 521 523 541 547 557 563 569 571 577 587 593
 599 601 607 613 617 619 631 641 643 647 653 659 661 673 677 683 691 701
 709 719 727 733 739 743 751 757 761 769 773 787 797 809 811 821 823 827
 829 839 853 857 859 863 877 881 883 887 907 911 919 929 937 941 947 953
 961 967 971 977 983 991 997]

>python p_30905.py  ** TEKRAR **
Asal sayı kontrolu üst sınırını girin [100]? 10

İlk 10 asal sayılar tüplesi:
(array([2, 3, 5, 7, 9], dtype=int32),)

Asal sayılar listesi:
[2 3 5 7 9]

(5/10) adet asal sayılar listesi:
[2 3 5 7 9]

1:2 2:3 3:5 4:7 5:9
"""