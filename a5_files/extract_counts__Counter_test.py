"""
Light tests for correctness of _Counter

Author:  Lillian Lee (LJL2)
Version:  Apr 26, 2025
"""
# STUDENTS: compare the results of running this code with your extract_counts 
# code against what our code produced, stored as one of the files for A5 2025 SP.

from collections import Counter  # for testing update of a _Counter with a Counter
from extract_counts import _Counter

print('>>> c1 = _Counter()')
c1 = _Counter()
print('>>> print(c1)')
print(c1)

print('>>> c2 = _Counter(["hi", "there", "hi"]')
c2 = _Counter(["hi", "there", "hi"])
print('>>> print(c2)')
print(c2)

print('>>> c3 = _Counter(["hi", "again"])')
c3 = _Counter(["hi", "again"])

print('>>> c1.update(c2)')
c1.update(c2)

print('>>> print(c1)')
print(c1)

print('>>> c1.update(c3)')
c1.update(c3)

print('>>> print(c1)')
print(c1)

print('>>> print(repr(c1))')
print(repr(c1))

print('>>> new = Counter(["new"])')
new = Counter(["new"])

print('>>> print(new)')
print(new)

print('>>> c1.update(new)')
c1.update(new)
print('>>> print(c1)')
print(c1)

print('>>> print(repr(c1))')
print(repr(c1))
