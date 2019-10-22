# coding:iso-8859-9 T�rk�e
# p_12802.py: Haz�r random, math ve builtins mod�llerinin incelenmesi �rne�i.

from math import pi, pow as �s, sin as sin�s, cos as kosin�s
print ("�s(2,3):", �s (2, 3) )
print ("�s(0.3562,-0.0125):", �s (0.3562, -0.0125) )

print ("sin�s(pi/4):", sin�s (pi / 4) )
print ("kosin�s(pi/4):", kosin�s (pi / 4) )
print ("-"*75, "\n")
#----------------------------------------------------------------------------------------------------

import sys
print ("Haz�r ar�iv python mod�l adlar� listesi:\n", sys.builtin_module_names)
print ("-"*75, "\n")
#----------------------------------------------------------------------------------------------------

import random, math, builtins
print ("random mod�l�n�n diskteki adresi:", random.__file__)
# print (sys mod�l�n�n adresi:", sys.__file__) Hata...

print ("\ndir(math):", dir (math) )
print ("\nBu programda kullan�lan de�i�ken adlar�, dir():", dir() )
print ("\nPython dir(builtins):", dir (builtins) )



"""��kt�:
>python p_12802.py
�s(2,3): 8.0
�s(0.3562,-0.0125): 1.012986892963937
sin�s(pi/4): 0.7071067811865475
kosin�s(pi/4): 0.7071067811865476
---------------------------------------------------------------------------

Haz�r ar�iv python mod�l adlar� listesi:
 ('_abc', '_ast', '_bisect', '_blake2', '_codecs', '_codecs_cn', '_codecs_hk',
 '_codecs_iso2022', '_codecs_jp', '_codecs_kr', '_codecs_tw', '_collections',
'_csv', '_datetime', '_functools', '_heapq', '_imp', '_io', '_json', '_locale',
'_lsprof', '_md5', '_multibytecodec', '_opcode', '_operator', '_pickle', '_random',
'_sha1', '_sha256', '_sha3', '_sha512', '_signal', '_sre', '_stat', '_string',
'_struct', '_symtable', '_thread', '_tracemalloc', '_warnings', '_weakref',
'_winapi', 'array', 'atexit', 'audioop', 'binascii', 'builtins', 'cmath', 'errno',
'faulthandler', 'gc', 'itertools', 'marshal', 'math', 'mmap', 'msvcrt', 'nt', 'parser',
'sys', 'time', 'winreg', 'xxsubtype', 'zipimport', 'zlib')
---------------------------------------------------------------------------

random mod�l�n�n diskteki adresi: C:/Users/pc/AppData/Local/Programs/Python/Python37-32/lib/random.py

dir(math): ['__doc__', '__loader__', '__name__', '__package__', '__spec__',
'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos',
'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor',
'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf',
'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'pi', 'pow',
'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan','tanh', 'tau', 'trunc']

Bu programda kullan�lan de�i�ken adlar�, dir(): ['__annotations__', '__builtins__',
'__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__',
'__spec__', 'builtins', 'kosin�s', 'math', 'pi', 'random', 'sin�s', 'sys', '�s']

Python dir(builtins): ['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException',
'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError',
'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError',
'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError',
'Exception', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError',
'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning',
'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError',
'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError',
'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError',
'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError',
'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning',
'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit',
'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError',
'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning',
'UserWarning', 'ValueError', 'Warning', 'WindowsError', 'ZeroDivisionError', '__build_class__',
'__debug__', '__doc__', '__import__', '__loader__','__name__', '__package__', '__spec__',
'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod',
'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval',
'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex',
'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max',
'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range',
'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super',
'tuple', 'type', 'vars', 'zip']
"""