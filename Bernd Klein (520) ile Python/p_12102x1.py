def fib1 (n):
    a, b = 0, 1
    if n == 0: return 0
    for i in range (n): a, b = b, a + b
    return b

def fib2 (n):
    if n == 0: return 0
    elif n == 1: return 1
    else:  return fib2 (n-1) + fib2 (n-2)
