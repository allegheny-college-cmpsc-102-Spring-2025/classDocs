#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Finding the Most Common Elements
'''

from collections import Counter


simplelist = [4, 2, 1, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4] # four is most common int in the list
c = Counter(simplelist)
c.most_common()
print(f"counter : {c}")
print(f"c.most_common() : {c.most_common()}") 

# [(4, 10), (2, 1), (1, 1), (3, 1)]
print(f"c.most_common(1) : {c.most_common(1)}")
# c.most_common(1) : [(4, 10)], four with ten counts

print(f"Mode is the following : {c.most_common(1)}")
print(f"Mode is the following : {c.most_common(1)[0][0]}")



