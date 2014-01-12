#!/usr/bin/env python
# -*- coding: utf-8 -*-
from lib.utils import myassert

weapons = ['shuriken', 'katana', 'nunchucks']
map((lambda (i, x): myassert(x == weapons[i], weapons[i] + ' is expected')), enumerate(weapons))
