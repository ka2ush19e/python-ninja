#!/usr/bin/env python
# -*- coding: utf-8 -*-
from lib.utils import myassert

def is_prime(num):
    is_prime.answers = {}

    if num in is_prime.answers:
        return is_prime.answers[num]
    prime = num != 1
    for v in range(2, num):
        if num % v == 0:
            prime = False
            break
    is_prime.answers[num] = prime
    return prime

myassert(is_prime(5), '5 is prime')
myassert(is_prime.answers[5], 'answer is cached')
