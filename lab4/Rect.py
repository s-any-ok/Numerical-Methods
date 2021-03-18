def f(x):
    return (x**2)/(x**4 + 256)

def rectangular(f, a, b, n):
    h = float(b - a) / n
    funcSum = f(a + 0.5 * h)
    for i in range(1, n):
        funcSum += f(a + (0.5 + i) * h)
    result = h * funcSum
    return print('Rectangular method result: ', result)

a = 0
b = 2
n1 = 4
n2 = 8
rectangular(f, a, b, n1)
rectangular(f, a, b, n2)