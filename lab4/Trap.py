def f(x):
    return (x**2)/(x**4 + 256)

def trapezoidal(f, a, b, n):
    h = float(b - a)/n
    func = 0
    for i in range(1, n):
        func += f(a + i*h)
    result = h*0.5*(f(a) + f(b) + 2*func)
    print('Rectangular method result: ', result)

a = 0
b = 2
n1 = 4
n2 = 8
trapezoidal(f, a, b, n1)
trapezoidal(f, a, b, n2)