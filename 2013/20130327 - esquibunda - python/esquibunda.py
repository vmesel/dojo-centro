#-*- coding: utf-8 -*-

def esquibunda(montanha):
    if not montanha:
        return 0

    pista = montanha[0]

    max_index = pista.index(max(pista))
    return max(max_index + 1, len(pista) - max_index)
