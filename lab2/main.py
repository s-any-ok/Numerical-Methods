import numpy as np
import math
import matplotlib.pyplot as plt

def yValues(xValues, func):
    return [func(xVal) for xVal in xValues]

def lagranz(x, f, xVal):
    y = yValues(x, f)
    result = 0
    for j in range(len(y)):
        p = 1
        for i in range(len(x)):
            if i != j:
                p *= (xVal - x[i])
                p /= (x[j] - x[i])
        result = result + y[j] * p
    return result

def nevton(x, f, xVal):
    y = yValues(x, f)
    delta = y.copy()
    n = len(y)
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            delta[i] = (delta[i] - delta[i - 1]) / (x[i] - x[i - j])
    result = 0
    for i in range(0, n):
        count = delta[i]
        for j in range(0, i):
            count *= (xVal - x[j])
        result += count
    return result

def mistake(xVal, deffRes, f, polinom, x):
    polMistake = (deffRes / math.factorial(len(x)))
    for xV in x:
        polMistake *= xVal - xV
    polMistake = abs(polMistake)
    absPolError = abs(f(xVal) - polinom(x, f, xVal))
    print("Верхня оцінка похибки", polMistake)
    print("Абсолютна похибка", absPolError)
    return polMistake / absPolError


xVal = 0.8
x1 = [0.1, 0.5, 0.9, 1.3]
x2 = [0.1, 0.5, 1.1, 1.3]

def f(x):
    return np.log(x) + x

#1
print("№1")
print("Ньютон", nevton(x1, f, xVal))
print("Лагранж", lagranz(x1, f, xVal))
print("Співвідношення", mistake(xVal, 60000, f, nevton, x1))

plotX = [x * 0.08 for x in range(1, 20)]
plotNevton = [nevton(x1, f, x) for x in plotX]
plotLagranz = [lagranz(x1, f, x) for x in plotX]
plotStart = [f(x) for x in plotX]

plt.plot(plotX, plotNevton, 'g', label='Ньютон')
plt.plot(plotX, plotLagranz, 'r', label='Лагранж')
plt.plot(plotX, plotStart, 'y', label='Старт')
plt.legend(loc='upper left')
plt.show()

#2
print("№2")
print("Ньютон", nevton(x2, f, xVal))
print("Лагранж", lagranz(x2, f, xVal))
print("Співвідношення", mistake(xVal, 60000, f, nevton, x2))

plotX = [x * 0.08 for x in range(1, 20)]
plotNevton = [nevton(x2, f, x) for x in plotX]
plotLagranz = [lagranz(x2, f, x) for x in plotX]
plotStart = [f(x) for x in plotX]

plt.plot(plotX, plotNevton, 'g', label='Ньютон')
plt.plot(plotX, plotLagranz, 'r', label='Лагранж')
plt.plot(plotX, plotStart, 'y', label='Старт')
plt.legend(loc='upper left')
plt.show()