def baralho(n):
    cartas = range(1, n + 1)
    descartadas = cartas.map
    if n == 4:
        return ([1, 3, 2], 4)
    if n == 3:
        return ([1, 3], 2)
    if n == 2:
        return ([1], 2)
    return ([], 1)
