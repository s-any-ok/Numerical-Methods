def f(x):
    return (x**2)/(x**4 + 256)


def simpson(f, a, b, h):
    firstItem = 0
    secondItem = 0
    n = round((b - a) / (2 * h))
    for i in range(1, n + 1):
        firstItem += f(a + (2 * i - 1) * h)
    for i in range(1, n):
        secondItem += f(a + (2 * i) * h)

    result = (h / 3) * (f(a) + (4 * firstItem) + (2 * secondItem) + f(b))
    print('Simpson method result: ', result)

simpson(f, 0, 2, 0.5)
simpson(f, 0, 2, 0.25)