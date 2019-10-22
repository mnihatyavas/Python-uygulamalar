# coding:iso-8859-9 Türkçe

"""
>>>python # komutuyla etkileşimli shell/kabuk'a inilir...
>>>help() # ile yardım kipine girilir...
help> modules
pygame 1.9.4
Hello from the pygame community. https://www.pygame.org/contribute.html
PIL                 _tracemalloc        glob                reprlib
__future__          _warnings           gridfs              rlcompleter
_abc                _weakref            gzip                runpy
_ast                _weakrefset         hashlib             sched
_asyncio            _winapi             heapq               secrets
_bisect             abc                 hmac                select
_blake2             aifc                html                selectors
_bootlocale         antigravity         http                setuptools
_bz2                argparse            idlelib             shelve
_codecs             array               imaplib             shlex
_codecs_cn          ast                 imghdr              shutil
_codecs_hk          asynchat            imp                 signal
_codecs_iso2022     asyncio             importlib           site
_codecs_jp          asyncore            inspect             smtpd
_codecs_kr          atexit              io                  smtplib
_codecs_tw          audioop             ipaddress           sndhdr
_collections        base64              itertools           socket
_collections_abc    bdb                 json                socketserver
_compat_pickle      binascii            keyword             sqlite3
_compression        binhex              lib2to3             sre_compile
_contextvars        bisect              linecache           sre_constants
_csv                bson                locale              sre_parse
_ctypes             builtins            logging             ssl
_ctypes_test        bz2                 lzma                stat
_datetime           cProfile            macpath             statistics
_decimal            calendar            mailbox             string
_distutils_findvs   camelcase           mailcap             stringprep
_dummy_thread       cgi                 marshal             struct
_elementtree        cgitb               math                subprocess
_functools          chunk               mimetypes           sunau
_hashlib            cmath               mmap                symbol
_heapq              cmd                 modulefinder        symtable
_imp                code                msilib              sys
_io                 codecs              msvcrt              sysconfig
_json               codeop              multiprocessing     tabnanny
_locale             collections         mysql               tarfile
_lsprof             colorsys            netrc               telnetlib
_lzma               compileall          nntplib             tempfile
_markupbase         concurrent          nt                  test
_md5                configparser        ntpath              textwrap
_msi                contextlib          nturl2path          this
_multibytecodec     contextvars         numbers             threading
_multiprocessing    copy                opcode              time
_opcode             copyreg             operator            timeit
_operator           crypt               optparse            tkinter
_osx_support        csv                 os                  token
_overlapped         ctypes              p32209              tokenize
_pickle             curses              p32210              trace
_py_abc             dataclasses         parser              traceback
_pydecimal          datetime            pathlib             tracemalloc
_pyio               dbm                 pdb                 tty
_queue              decimal             pickle              turtle
_random             difflib             pickletools         turtledemo
_sha1               dis                 pip                 types
_sha256             distutils           pipes               typing
_sha3               doctest             pkg_resources       unicodedata
_sha512             dummy_threading     pkgutil             unittest
_signal             easy_install        platform            urllib
_sitebuiltins       email               plistlib            uu
_socket             encodings           poplib              uuid
_sqlite3            ensurepip           posixpath           venv
_sre                enum                pprint              warnings
_ssl                errno               profile             wave
_stat               faulthandler        pstats              weakref
_string             filecmp             pty                 webbrowser
_strptime           fileinput           py_compile          winreg
_struct             fnmatch             pyclbr              winsound
_symtable           formatter           pydoc               wsgiref
_testbuffer         fractions           pydoc_data          xdrlib
_testcapi           ftplib              pyexpat             xml
_testconsole        functools           pygame              xmlrpc
_testimportmultiple gc                  pymongo             xxsubtype
_testmultiphase     genericpath         queue               zipapp
_thread             getopt              quopri              zipfile
_threading_local    getpass             random              zipimport
_tkinter            gettext             re                  zlib

help> keywords # ile modules/modüller, keywords/anahtarkelimeler, symbols/semboller ve topics/konular yardımı alınır...
False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not

help> symbols
!=                  +                   <=                  __
"                   +=                  <>                  `
3çifttırnak                 ,                   ==                  b"
%                   -                   >                   b'
%=                  -=                  >=                  f"
&                   .                   >>                  f'
&=                  ...                 >>=                 j
'                   /                   @                   r"
3tektırnak              //                  J                   r'
(                   //=                 [                   u"
)                   /=                  \                   u'
*                   :                   ]                   |
**                  <                   ^                   |=
**=                 <<                  ^=                  ~
*=                  <<=                 _

help> topics
ASSERTION           DELETION            LOOPING             SHIFTING
ASSIGNMENT          DICTIONARIES        MAPPINGMETHODS      SLICINGS
ATTRIBUTEMETHODS    DICTIONARYLITERALS  MAPPINGS            SPECIALATTRIBUTES
ATTRIBUTES          DYNAMICFEATURES     METHODS             SPECIALIDENTIFIERS
AUGMENTEDASSIGNMENT ELLIPSIS            MODULES             SPECIALMETHODS
BASICMETHODS        EXCEPTIONS          NAMESPACES          STRINGMETHODS
BINARY              EXECUTION           NONE                STRINGS
BITWISE             EXPRESSIONS         NUMBERMETHODS       SUBSCRIPTS
BOOLEAN             FLOAT               NUMBERS             TRACEBACKS
CALLABLEMETHODS     FORMATTING          OBJECTS             TRUTHVALUE
CALLS               FRAMEOBJECTS        OPERATORS           TUPLELITERALS
CLASSES             FRAMES              PACKAGES            TUPLES
CODEOBJECTS         FUNCTIONS           POWER               TYPEOBJECTS
COMPARISON          IDENTIFIERS         PRECEDENCE          TYPES
COMPLEX             IMPORTING           PRIVATENAMES        UNARY
CONDITIONAL         INTEGER             RETURNING           UNICODE
CONTEXTMANAGERS     LISTLITERALS        SCOPING
CONVERSIONS         LISTS               SEQUENCEMETHODS
DEBUGGING           LITERALS            SEQUENCES

help> pass # Yukardakilerden herhangibiri girilirse detay gelir...
The "pass" statement
********************

   pass_stmt ::= "pass"

"pass" is a null operation ù when it is executed, nothing happens. It
is useful as a placeholder when a statement is required syntactically,
but no code needs to be executed, for example:

   def f(arg): pass    # a function that does nothing (yet)

   class C: pass       # a class with no methods (yet)

help> quit # Etkileşim kabuğuna çıkılır...
#---------------------------------------------------------------------------------------

>>> from math import *
>>> 2.3**3
12.166999999999998
>>> _ %10 # Burada _, birönceki sonucun varsayılı değişken adıdır...
2.166999999999998
>>> ln = log # Artık log için ln kullanılabilir...
>>> sum ([1 / (n**2-1) for n in range (2,100000)]) # Zn=1-->100000: 1 / (n2 - 1) için...
0.7499899999500057
>>> [round (sin (radians (i)), 4) for i in range (0,91,15)]
[0.0, 0.2588, 0.5, 0.7071, 0.866, 0.9659, 1.0]
# pip -m install'la yüklenebilen 3.parti modüllerle de ilginç işlemler yapılabilir: NumPy, SciPy, Mathplotlib, SymPy, PIL, pygame vb gibi...
>>> exit() veya quit() # DOS ileti satırına çıkılır...
c/:> _
"""