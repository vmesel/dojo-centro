#!/usr/bin/env python
# -*- coding: utf-8 -*-

def paula_game(expression):
    first = int(expression[0])
    op = expression[1]
    second = int(expression[2])

    if first == second:
        return first * first
    if op.islower():
        return 3
    return 1