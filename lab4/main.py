def rectangular(f, a, b, n):
    h = float(b - a) / n
    funcSum = f(a + 0.5 * h)
    for i in range(1, n):
        funcSum += f(a + (0.5 + i) * h)
    result = h * funcSum
    return result


def simpson(f, a, b, n):
    h = float(b - a) / n
    firstItem = 0
    secondItem = 0
    n = round((b - a) / (2 * h))
    for i in range(1, n + 1):
        firstItem += f(a + (2 * i - 1) * h)
    for i in range(1, n):
        secondItem += f(a + (2 * i) * h)

    result = (h / 3) * (f(a) + (4 * firstItem) + (2 * secondItem) + f(b))
    return result


def trapezoidal(f, a, b, n):
    h = float(b - a)/n
    func = 0
    for i in range(1, n):
        func += f(a + i*h)
    result = h*0.5*(f(a) + f(b) + 2*func)
    return result


def rungeRomberg(f, mF, a , b, n, k):
    h = mF(f, a, b, n)
    hHalf = mF(f, a, b, round(n / 2))
    result = hHalf - ((hHalf - h) / k)
    print('{0:10}  {1}\n'.format('Runge-Romberg method result:', result))

def f(x):
    return (x**2)/(x**4 + 256)

a = 0
b = 2
n1 = 4
n2 = 8

print("a:", a, "\tb:", b, "\tn:", n1)
print("------------------------------------")
print('{0:28} {1}'.format('Rectangular method result:', rectangular(f, a, b, n1)))
rungeRomberg(f, rectangular, a, b, n1, 1)
print('{0:28}  {1}'.format('Simpson method result:', simpson(f, a, b, n1)))
rungeRomberg(f, simpson, a, b, n1, 15)
print('{0:28}  {1}'.format('Trapezoidal method result:', trapezoidal(f, a, b, n1)))
rungeRomberg(f, trapezoidal, a, b, n1, 3)

print("a:", a, "\tb:", b, "\tn:", n2)
print("------------------------------------")
print('{0:28}  {1}'.format('Rectangular method result:', rectangular(f, a, b, n2)))
rungeRomberg(f, rectangular, a, b, n2, 1)
print('{0:28}  {1}'.format('Simpson method result:', simpson(f, a, b, n2)))
rungeRomberg(f, simpson, a, b, n2, 15)
print('{0:28}  {1}'.format('Trapezoidal method result:', trapezoidal(f, a, b, n2)))
rungeRomberg(f, trapezoidal, a, b, n2, 3)