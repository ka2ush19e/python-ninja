#!/usr/bin/env python
# -*- coding: utf-8 -*-
from lib.utils import myassert

outer_value = 'ninja'
later = None

def outer_funtion():
    inner_value = 'samurai'
    def inner_function():
        myassert(outer_value == 'ninja', 'can see ninja')
        myassert(inner_value == 'samurai', 'can see samurai')
    global later
    later = inner_function

outer_funtion()
later()

