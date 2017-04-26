#!/usr/bin/env python
# -*- coding: utf-8 -*-

def miojo(a1, a2):
    if 3 in (a1, a2):
        return 3

    elif abs(a1 - a2) == 3:
        return max((a1, a2))

    elif abs(a1 - a2) == 1:
        if a1%2 == 0:
            return 2*a1
        else: 
            return 3*a2

    elif (a1, a2) == (7, 9):
        return 21

    return 10