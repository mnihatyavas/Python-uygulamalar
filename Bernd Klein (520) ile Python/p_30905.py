# coding:iso-8859-9 T�rk�e
# p_30905.py: Boolean dizisi kullanarak asal say�lar�n bulunmas� �rne�i.

import numpy as np

n = 100
try: n = abs (int ( input ("Asal say� kontrolu �st s�n�r�n� girin [100]? ")))
except: n = 100

asalM� = np.ones ((n,), dtype=bool)

asalM�[:2] = 0 # �lk 0 ve 1 asal de�ildir...

# Eratosthenes ele�i gere�i �arp�m katlar� asal de�ildir...
kontrolUzunlu�u = int (np.sqrt (len (asalM�)))
for i in range (2, kontrolUzunlu�u): asalM� [2*i::i] = False

print ("\n�lk ", n, " asal say�lar t�plesi:\n", np.nonzero (asalM�),
    "\n\nAsal say�lar listesi:\n", np.nonzero (asalM�)[0], sep="")

print ("\n(", np.count_nonzero (asalM�), "/", n, ") adet asal say�lar listesi: \n", np.flatnonzero (asalM�), sep="")
print()
for i in range (np.count_nonzero (asalM�)):
    print ((i+1), ":", np.flatnonzero (asalM�)[i], sep="", end=" ")



"""��kt�:
>python p_30905.py
Asal say� kontrolu �st s�n�r�n� girin [100]?

�lk 100 asal say�lar t�plesi:
(array([ 2,  3,  5,  7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97], dtype=int32),)

Asal say�lar listesi:
[ 2  3  5  7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97]

>python p_30905.py  ** TEKRAR **
Asal say� kontrolu �st s�n�r�n� girin [100]? 1000

�lk 1000 asal say�lar t�plesi:
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

Asal say�lar listesi:
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
Asal say� kontrolu �st s�n�r�n� girin [100]? 10

�lk 10 asal say�lar t�plesi:
(array([2, 3, 5, 7, 9], dtype=int32),)

Asal say�lar listesi:
[2 3 5 7 9]

(5/10) adet asal say�lar listesi:
[2 3 5 7 9]

1:2 2:3 3:5 4:7 5:9
"""