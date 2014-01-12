#!/usr/bin/env python
# -*- coding: utf-8 -*-
from lib.utils import myassert

class Ninja:
    def chirp(self, n):
        return self.chirp(n - 1) + '-chirp' if  n > 1 else 'chirp'

class Samurai:
    pass

ninja = Ninja()
myassert(ninja.chirp(3) == 'chirp-chirp-chirp', 'ninja result is expected')

samurai = Samurai()
samurai.chirp = ninja.chirp

ninja = None
myassert(samurai.chirp(3) == 'chirp-chirp-chirp', 'samurai result is expected')
