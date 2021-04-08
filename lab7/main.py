from sympy import *
import math

def getDet(x, y, fns):
    mainDiag = 1
    diag = 1
    for i in range(len(fns)):
        fn = fns[i]
        fnResult = fn(x, y)
        if i <= 1:
            mainDiag *= fnResult
        else:
            diag *= fnResult
    result = mainDiag - diag
    return result

def newton(x, y, fns, diffFns, e):
    x1, y1 = x, y
    while true:
        J = getDet(x1, y1, diffFns)
        A1 = getDet(x1, y1, [fns[0], diffFns[1], diffFns[2], fns[1]])
        A2 = getDet(x1, y1, [diffFns[0], fns[1], fns[0], diffFns[3]])
        x1 = x - (A1 / J)
        y1 = y - (A2 / J)
        if abs(x - x1) <= e: break
        x, y = x1, y1
    return [x1, y1]

def iteration(x, y, fns, e):
    x1, y1 = x, y
    while true:
        x1 = fns[0](x1, y1)
        y1 = fns[1](x1, y1)
        if abs(x - x1) <= e: break
        x, y = x1, y1
    return [x1, y1]

# def f1(x, y):
#     return 0.1 * (x ** 2) + x + 0.2 * (y ** 2) - 0.3
#
# def f2(x, y):
#     return 0.2 * (x ** 2) + y - (0.1 * x * y) - 0.7
#
# def deffFunc1X1(x, y):
#     return 0.2*x + 1
#
# def deffFunc1X2(x, y):
#     return 0.4*y
#
# def deffFunc2X1(x, y):
#     return 0.4*x - 0.1*y
#
# def deffFunc2X2(x, y):
#     return 1 - 0.1*x
#
# def f1Iter(x, y):
#     return - (0.1 * (x ** 2) + 0.2 * (y ** 2) - 0.3)
#
# def f2Iter(x, y):
#     return - (0.2 * (x ** 2) - (0.1 * x * y) - 0.7)
#
#
# def deffFuncIter1X1(x, y):
#     return -0.2*x
#
# def deffFuncIter1X2(x, y):
#     return -0.4*y
#
# def deffFuncIter2X1(x, y):
#     return -0.4*x -0.1*y
#
# def deffFuncIter2X2(x, y):
#     return 0.1*x

# x = 0.25
# y = 0.75

def f1(x, y):
    return 2*x - math.cos(y)

def f2(x, y):
    return 2*y - math.e**x

def deffFunc1X1(x, y):
    return 2

def deffFunc1X2(x, y):
    return math.sin(y)

def deffFunc2X1(x, y):
    return -math.e**x

def deffFunc2X2(x, y):
    return 2

def f1Iter(x, y):
    return math.cos(y) / 2

def f2Iter(x, y):
    return math.e**x / 2


def deffFuncIter1X1(x, y):
    return 0

def deffFuncIter1X2(x, y):
    return -(math.sin(y) / 2)

def deffFuncIter2X1(x, y):
    return math.e**x / 2

def deffFuncIter2X2(x, y):
    return 0

x = 0.5
y = 0.5
e = 0.0001
diffFns = [deffFunc1X1, deffFunc2X2, deffFunc1X2, deffFunc2X1]
fns = [f1, f2]
iterFns = [f1Iter, f2Iter]

x1 = newton(x, y, fns, diffFns, e)[0]
y1 = newton(x, y, fns, diffFns, e)[1]
x2 = iteration(x, y, iterFns, e)[0]
y2 = iteration(x, y, iterFns, e)[1]

print("Метод Ньютона")
print("x: ", x1)
print("y: ", y1)
print("\nМетод простої Ітерації")
print("x: ", x2)
print("y: ", y2)
