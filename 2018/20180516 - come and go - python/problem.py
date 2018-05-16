#!/usr/bin/env python
# -*- coding: utf-8 -*-

def is_connected(streets):
    if len(streets) == 1:
        return streets[0][2] == 2

    if len(streets) == 2:
        return False

    return ((streets[0][2] == 2 and streets[1][2] == 2) or
            (len(streets) == 3 and streets[1][2] == 2))