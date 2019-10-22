# coding:iso-8859-9 Türkçe
# p_12802.py: Hazır random, math ve builtins modüllerinin incelenmesi örneği.

from math import pi, pow as üs, sin as sinüs, cos as kosinüs
print ("üs(2,3):", üs (2, 3) )
print ("üs(0.3562,-0.0125):", üs (0.3562, -0.0125) )

print ("sinüs(pi/4):", sinüs (pi / 4) )
print ("kosinüs(pi/4):", kosinüs (pi / 4) )
print ("-"*75, "\n")
#----------------------------------------------------------------------------------------------------

import sys
print ("Hazır arşiv python modül adları listesi:\n", sys.builtin_module_names)
print ("-"*75, "\n")
#----------------------------------------------------------------------------------------------------

import random, math, builtins
print ("random modülünün diskteki adresi:", random.__file__)
# print (sys modülünün adresi:", sys.__file__) Hata...

print ("\ndir(math):", dir (math) )
print ("\nBu programda kullanılan değişken adları, dir():", dir() )
print ("\nPython dir(builtins):", dir (builtins) )



"""Çıktı:
>python p_12802.py
üs(2,3): 8.0
üs(0.3562,-0.0125): 1.012986892963937
sinüs(pi/4): 0.7071067811865475
kosinüs(pi/4): 0.7071067811865476
---------------------------------------------------------------------------

Hazır arşiv python modül adları listesi:
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

random modülünün diskteki adresi: C:/Users/pc/AppData/Local/Programs/Python/Python37-32/lib/random.py

dir(math): ['__doc__', '__loader__', '__name__', '__package__', '__spec__',
'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos',
'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor',
'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf',
'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'pi', 'pow',
'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan','tanh', 'tau', 'trunc']

Bu programda kullanılan değişken adları, dir(): ['__annotations__', '__builtins__',
'__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__',
'__spec__', 'builtins', 'kosinüs', 'math', 'pi', 'random', 'sinüs', 'sys', 'üs']

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