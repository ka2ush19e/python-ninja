#!/usr/bin/env python
# -*- coding: utf-8 -*-
from lib.utils import myassert

class Store:
    def __init__(self):
        self.next_id = 1
        self.cache = {}

    def add(self, fn):
        try:
            fn.id
            return False
        except:
            self.next_id = self.next_id + 1
            fn.id = self.next_id
            self.cache[fn.id] = fn
            return True

def ninja():
    pass

store = Store()

myassert(store.add(ninja), 'function is added')
myassert(store.add(ninja), 'function is added')

