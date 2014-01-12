#!/usr/bin/env python
# -*- coding: utf-8 -*-
from lib.utils import myassert

outer_values = 'ninja'

def outer_function():
    myassert(outer_values == 'ninja', 'can see ninja')

outer_function()
