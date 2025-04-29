"""
var_m1_a = 30
var_m1_b = 40

print("Hello form Module 1")

def m1_first():
    print("-----Hello from M1_first function in side Module 1 -----")


def word_vol(a):
    v_str = a
    vol_set = {"a","e","i","o","u"}
    print(v_str,":")
    for i in sorted(vol_set):
        p = v_str.count(i)
        print(i,p)

vol_str = "This is a vowel string with aeiour as many time repaet "
sp = vol_str.split()
print(len(sp))
for k in range(len(sp)):
    word_vol(sp[k])

"""

import pytest


def test_first1():
    print("-------Hello from first1 function in side Module 1")

