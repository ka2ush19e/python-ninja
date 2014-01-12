#!/usr/bin/env python
# -*- coding: utf-8 -*-
from lib.utils import myassert

outer_value = 'ninja'
later = None

def outer_funtion():
    inner_value = 'samurai'
    def inner_function(param_value):
        myassert(outer_value, 'can see ninja from inside')
        myassert(inner_value, 'can see samurai from inside')
        myassert(param_value, 'can see wakizashi from inside')
        myassert(too_late,    'can see ronin from inside')
    global later
    later = inner_function

myassert('too_late' in locals(), 'can see ronin from outside')
too_late = 'ronin'
outer_funtion()
later('wakizashi')
