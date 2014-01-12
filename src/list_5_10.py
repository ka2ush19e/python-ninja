#!/usr/bin/env python
# -*- coding: utf-8 -*-
import functools

str.csv = functools.partial(str.split, ',')
print 'a,b,c'.csv()

