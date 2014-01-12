#!/usr/bin/env python
# -*- coding: utf-8 -*-
from lib.utils import myassert

myassert(True, '---- before outer ----')
myassert('outer' in globals(), 'outer is in global scope')
myassert('outer' in locals(), 'outer is in local scope')
myassert('inner' in globals(), 'inner is in global scope')
myassert('inner' in locals(), 'inner is in local scope')
myassert('a' in locals(), 'a is in scope')
myassert('b' in locals(), 'b is in scope')
myassert('c' in locals(), 'c is in scope')

def outer():
    myassert(True, '---- in outer ----')
    myassert('outer' in globals(), 'outer is in global scope')
    myassert('outer' in locals(), 'outer is in local scope')
    myassert('inner' in globals(), 'inner is in global scope')
    myassert('inner' in locals(), 'inner is in local scope')
    myassert('a' in locals(), 'a is in scope')
    myassert('b' in locals(), 'b is in scope')
    myassert('c' in locals(), 'c is in scope')

    a = 1

    myassert(True, '---- in outer after a ----')
    myassert('outer' in globals(), 'outer is in global scope')
    myassert('outer' in locals(), 'outer is in local scope')
    myassert('inner' in globals(), 'inner is in global scope')
    myassert('inner' in locals(), 'inner is in local scope')
    myassert('a' in locals(), 'a is in scope')
    myassert('b' in locals(), 'b is in scope')
    myassert('c' in locals(), 'c is in scope')

    def inner():
        pass
    b = 2

    myassert(True, '---- in outer after b ----')
    myassert('outer' in globals(), 'outer is in global scope')
    myassert('outer' in locals(), 'outer is in local scope')
    myassert('inner' in globals(), 'inner is in global scope')
    myassert('inner' in locals(), 'inner is in local scope')
    myassert('a' in locals(), 'a is in scope')
    myassert('b' in locals(), 'b is in scope')
    myassert('c' in locals(), 'c is in scope')

    if a == 1:
        c = 3
        myassert(True, '---- in outer in if ----')
        myassert('outer' in globals(), 'outer is in global scope')
        myassert('outer' in locals(), 'outer is in local scope')
        myassert('inner' in globals(), 'inner is in global scope')
        myassert('inner' in locals(), 'inner is in local scope')
        myassert('a' in locals(), 'a is in scope')
        myassert('b' in locals(), 'b is in scope')
        myassert('c' in locals(), 'c is in scope')

    myassert(True, '---- in outer after c ----')
    myassert('outer' in globals(), 'outer is in global scope')
    myassert('outer' in locals(), 'outer is in local scope')
    myassert('inner' in globals(), 'inner is in global scope')
    myassert('inner' in locals(), 'inner is in local scope')
    myassert('a' in locals(), 'a is in scope')
    myassert('b' in locals(), 'b is in scope')
    myassert('c' in locals(), 'c is in scope')

outer()

myassert(True, '---- after outer ----')
myassert('outer' in globals(), 'outer is in global scope')
myassert('outer' in locals(), 'outer is in local scope')
myassert('inner' in globals(), 'inner is in global scope')
myassert('inner' in locals(), 'inner is in local scope')
myassert('a' in locals(), 'a is in scope')
myassert('b' in locals(), 'b is in scope')
myassert('c' in locals(), 'c is in scope')
