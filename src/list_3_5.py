#!/usr/bin/env python
# -*- coding: utf-8 -*-

def juggle(*nums):
    result = 0
    for num in nums:
        result += num
    return result

print apply(juggle, (1, 2, 3))
