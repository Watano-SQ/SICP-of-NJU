def mystery():
    yield 1
    yield 1
    iter1 = mystery()
    iter2 = mystery()
    next(iter2)
    yield from map(lambda pair:pair[0] + pair[1],zip(iter1,iter2))
series1 = mystery()
series2 = filter(lambda n:n%2 != 0,series1)

[next(series1) for _ in range(2)]
[next(series1) for _ in range(2)]
[next(series2) for _ in range(2)]
next(series1)