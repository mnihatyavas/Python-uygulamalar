def fib1 (n):
    a, b = 0, 1
    if n == 0: return 0
    for i in range (n): a, b = b, a + b
    return b

bellek = {0:0, 1:1}
def fib2 (n):
    if not n in bellek: bellek [n] = fib2 (n-1) + fib2 (n-2)
    return bellek [n]