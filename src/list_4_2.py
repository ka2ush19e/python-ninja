#!/usr/bin/env python
# -*- coding: utf-8 -*-
from lib.utils import myassert

def chirp(n):
    return chirp(n - 1) + '-chirp' if  n > 1 else 'chirp'

myassert(chirp(3) == 'chirp-chirp-chirp', 'result is expected')
