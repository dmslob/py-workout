import zlib
from timeit import Timer

s = b'witch which has which witches wrist watch'
print(len(s))

t = zlib.compress(s)
print(len(t))

print(zlib.decompress(t))

print(zlib.crc32(s))

# Performance Measurement
print(Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())
print(Timer('a,b = b,a', 'a=1; b=2').timeit())
# In contrast to timeit’s fine level of granularity,
# the profile and pstats modules provide tools for identifying time
# critical sections in larger blocks of code.

