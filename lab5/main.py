import math


def GetPoints(rangeValues, h):
    return [round(rangeValues[0] + h * i, 2) for i in range(int((rangeValues[1] - rangeValues[0]) / h) + 1)]


def Euler(rangeValues, h, y0, z0, zFunc, isKoshi):
    y = [y0]
    z = [z0]
    x = GetPoints(rangeValues, h)

    for i in range(len(x)):
        if isKoshi:
            if len(x) - 1 == i: break
            zBeta = z[-1] + (h * zFunc(x[-1], y[-1], z[-1]))
            yBeta = y[-1] + (h * z[-1])
            z.append(z[-1] + 0.5 * h * (zFunc(x[i - 1], y[i - 1], z[i - 1]) + zFunc(x[i], yBeta, zBeta)))
            y.append(y[-1] + 0.5 * h * (z[-1] + z[-2]))
        else:
            z.append(z[-1] + h * zFunc(x[i], y[i], z[i]))
            y.append(y[i] + h * z[-2])
    return y


def GetAccuracy(func, rangeValues, h, methodResults):
    result = []
    x = GetPoints(rangeValues, h)
    for i in range(len(x)):
        result.append(abs(methodResults[i] - func(x[i])))
    return result


def GetFuncResults(func, rangeValues, h):
    result = []
    x = GetPoints(rangeValues, h)
    for i in range(len(x)):
        result.append(func(x[i]))
    return result


def GetAccuracyInPercent(funcResults, methodResults):
    result = []
    for i in range(len(funcResults)):
        result.append(round(abs(100 - (methodResults[i] * 100 / funcResults[i])), 2))
    return result


def PrintResults(funcResults, methodResults, accuracy, accuracyInPercent):
    print("{0:20} | {1:20} | {2:20} | {3} |".format("FuncResults", "MethodResults", "Accuracy", "Accuracy (%)"))
    print("---------------------|----------------------|----------------------|--------------|")
    for i in range(len(funcResults)):
        print("{0:<20} | {1:<20} | {2:<20} |  \t{3}%\t  |".format(funcResults[i], methodResults[i], accuracy[i],
                                                                  accuracyInPercent[i]))


rangeValues = [1, 2]
h = 0.1
y0 = 1.5 * math.e + (1 / math.e)
z0 = 0.5 * math.e - (2 / math.e)


def func(x):
    return 0.5 * (math.e ** x) + (1 / x) * (math.e ** x - math.e ** (-x))


def zFunc(x, y, z):
    return (2 * z + x * y + math.e ** x) / x


funcResults = GetFuncResults(func, rangeValues, h)

eulerResults = Euler(rangeValues, h, y0, z0, zFunc, 0)
eulerKoshiResults = Euler(rangeValues, h, y0, z0, zFunc, 1)

eulerAccuracy = GetAccuracy(func, rangeValues, h, eulerResults)
eulerKoshiAccuracy = GetAccuracy(func, rangeValues, h, eulerKoshiResults)

eulerAccuracyInPercent = GetAccuracyInPercent(funcResults, eulerResults)
eulerKoshiAccuracyInPercent = GetAccuracyInPercent(funcResults, eulerKoshiResults)

print("Метод Ейлера")
PrintResults(funcResults, eulerResults, eulerAccuracy, eulerAccuracyInPercent)
print("\nМетод Ейлера-Коші")
PrintResults(funcResults, eulerKoshiResults, eulerKoshiAccuracy, eulerKoshiAccuracyInPercent)
