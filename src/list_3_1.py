#!/usr/bin/env python
# -*- coding: utf-8 -*-
from lib.utils import myassert

def is_nimble():
    return True

myassert('is_nimble' in locals(), 'is_nimble is defined')
myassert(is_nimble.__name__ == 'is_nimble', 'is_nimble has name')

can_fly = lambda s: True

myassert('can_fly' in locals(), 'can_fly is defined')
myassert(can_fly.__name__ == 'canfly', 'canfly has name')

def outer():
    myassert('inner' in locals(), 'inner is defined before innner')
    def inner():
        pass
    myassert('inner' in locals(), 'inner is defined after innner')

outer()
myassert('inner' in globals(), 'inner is in global scope')
