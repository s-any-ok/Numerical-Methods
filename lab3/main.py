import matplotlib.pyplot as plt

xPoints = [0.1, 0.5, 0.9, 1.3, 1.7]
yPoints = [-2.2026, -0.19315, 0.79464, 1.5624, 2.2306]
h = 1
x = 8

def FindCoefs(xPoints, yPoints, h):
    n = len(xPoints)

    resultCoefs = [0 for i in range(n)]
    startCoefs = [[0, 0, 0, 0, 0, 0] for i in range(n)]  # a b c d A B (0, 1, 2, 3, 4, 5)
    startCoefs[1][0] = 0  # a1
    startCoefs[n - 2][2] = 0  # c(n-2)

    for i in range(2, n - 1):
        startCoefs[i][0] = h / 6  # a

    for i in range(1, n - 1):
        startCoefs[i][1] = (2 * h) / 3  # b

    for i in range(1, n - 2):
        startCoefs[i][2] = h / 6  # c

    for i in range(1, n - 1):
        startCoefs[i][3] = ((yPoints[i + 1] - yPoints[i]) / h) - ((yPoints[i] - yPoints[i - 1]) / h)  # d

    startCoefs[1][4] = startCoefs[1][2] / startCoefs[1][1]  # A =  c / b

    for i in range(2, n - 1):
        startCoefs[i][4] = startCoefs[i][2] / (startCoefs[i][1] + startCoefs[i][0] * startCoefs[i - 1][4])  # A

    startCoefs[1][5] = startCoefs[1][3] / startCoefs[i][1]  # B =  d / b

    for i in range(2, n - 1):
        startCoefs[i][5] = (startCoefs[i][3] - startCoefs[i][0] * startCoefs[i - 1][5])  # B =  d - a * B
        startCoefs[i][5] /= (startCoefs[i][1] + startCoefs[i][0] * startCoefs[i - 1][4])  # B /=  b + a * A

    for i in range(n - 2, 0, -1):
        resultCoefs[i] = startCoefs[i][4] * resultCoefs[i + 1] + startCoefs[i][5]  # q = A * q0 + B

    return resultCoefs

def SplineX(coefs, xPoints, yPoints, x, h):
    intervals = [(xPoints[i - 1], xPoints[i]) for i in range(1, len(xPoints))]
    intervalLen = len(intervals)
    if x < intervals[0][0]:
        return FinishFn(coefs, xPoints, yPoints, x,  0, h)
    if x > intervals[intervalLen - 1][1]:
        return FinishFn(coefs, xPoints, yPoints, x,  len(xPoints) - 2, h)
    for i in range(0, intervalLen):
        if x >= intervals[i][0] and x <= intervals[i][1]:
            return FinishFn(coefs, xPoints, yPoints, x,  i, h)


def FinishFn(coefs, xPoints, yPoints, x,  i, h):
    f = (((coefs[i] * (xPoints[i + 1] - x) ** 3) / 6 * h))
    f += ((coefs[i + 1] * (x - xPoints[i]) ** 3) / 6 * h)
    f += (((yPoints[i] / h) - coefs[i] * (h / 6)) * (xPoints[i + 1] - x))
    f += (((yPoints[i + 1] / h) - coefs[i + 1] * (h / 6)) * (x - xPoints[i]))
    f *= (-1)
    return f

coefs = FindCoefs(xPoints, yPoints, h)
s = SplineX(coefs, xPoints, yPoints, x, h)
print("Spline in x:", s)
valuesPlotX = [x * 0.1 for x in range(10, 50)]
valuesPlot = [SplineX(coefs, xPoints, yPoints, i, h) for i in valuesPlotX]
plt.plot(valuesPlotX, valuesPlot)
plt.show()


