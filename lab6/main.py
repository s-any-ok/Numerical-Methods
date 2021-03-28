import numpy.linalg
from math import sqrt
import numpy as np

np.set_printoptions(suppress=True)

Array1 = [
    [-5., -1., -3., -1., 18.],
    [-2., 0., 8., -4., -12.],
    [-7., -2., 2., -2., 0.],
    [2., -4., -4., 4., -12.]]

Array1_2 = [
    [-5., -1., -3., -1.],
    [-2., 0., 8., -4.],
    [-7., -2., 2., -2.],
    [2., -4., -4., 4.]]

Array2 = np.array([
    [18, -9, 0, 0, 0],
    [2, -9, -4, 0, 0],
    [0, -9, 21, -8, 0],
    [0, 0, -4, -10, 5],
    [0, 0, 0, 7, 12]])
result2 = np.array([-81, 71, -39, 64, 3])

Array2_2 = np.array([
    [8, -2, 0, 0],
    [-1, 6, -2, 0],
    [0, 2, 10, -4],
    [0, 0, -1, 6]])

# a = [-1, 2, -1, 0]
# b = [8, 6, 10, 6]
# c = [-2, -2, -4, 0]
# d = [6, 3, 8, 5]

a = [2, -9, -4, 7, 0]
b = [18, -9, 21, -10, 12]
c = [-9, -4, -8, 5, 0]
d = [-81, 71, -39, 64, 3]

Array3 = [
    [10, 1, 1],
    [2, 10, 1],
    [2, 2, 10]]
result3 = [12, 13, 14]

# Array3 = [
#     [21, -6, -9, -4],
#     [-6, 20, -4, 2],
#     [-2, -7, -20, 3],
#     [4, 9, 6, 24]]
# result3 = [127, -144, 236, -5]
e = 0.01

def Gauss(m):
    n = len(m)
    # прямий хід (результат - верхня трикутна матриця)
    for k in range(n - 1):  # обираємо провідний рядок
        m = MaxRowChange(m, k)  # рядок з найбільшим по модулю елементом на верх
        for i in range(k + 1, n):
            div = m[i][k] / m[k][k]    # An1/A11
            for j in range(k, n + 1):
                m[i][j] -= div * m[k][j]  # m[k][j] - елемент провідного рядка

    if IsSingular(m):
        print("Визначник дорівнює нулю => система має безліч розв'язків")
        return

    # зворотній хід
    x = [0 for i in range(n)]  # [0, 0, 0, 0]
    for k in range(n - 1, -1, -1):
        b = m[k][-1]
        sumOfRowOnX = sum([m[k][j] * x[j] for j in range(k + 1, n)])
        x[k] = (b - sumOfRowOnX) / m[k][k]
        if abs(x[k] == 0.0): x[k] = 0.0
    return x

def MaxRowChange(m, col):
    max_element = m[col][col]
    max_row = col
    for i in range(col + 1, len(m)):
        if abs(m[i][col]) > abs(max_element):
            max_element = m[i][col]
            max_row = i
    if max_row != col:
        m[col], m[max_row] = m[max_row], m[col]
    return m

def IsSingular(m):
    for i in range(len(m)):
        if not m[i][i]:
            return True
    return False

def Determinant(m):
    d = 0
    for i in range(0, len(m)):
        for j in range(0, len(m)):
            if (i == j):
                d += m[i][j]
    return d

def GaussInverse(M):
    n = len(M)
    I = [] # створити одиничну матрицю
    for i in range(n): # заповнити одиничну матрицю
        L = []
        for j in range(n):
            if i == j: L.append(1)
            else: L.append(0)
        I.append(L)

    for i in range(n):
        j = i
        while M[j][i] == 0: # шукаємо перший рядок із ненульовим значенням
            j += 1
        # поміняти місцями рядок i та рядок j
        M[i], M[j] = M[j], M[i]
        I[i], I[j] = I[j], I[i]
        const = M[i][i]
        for j in range(n): # ділимо на const, щоб мати 1 по діагоналі
            I[i][j] = I[i][j] / const
            M[i][j] = M[i][j] / const

        for j in range(i+1,n): # операція, щоб мати 0 в i-му стовпці всіх рядків нижче i-го
            const = M[j][i]
            for k in range(n):
                I[j][k] -= const * I[i][k]
                M[j][k] -= const * M[i][k]

    # маємо матрицю верхнього трикутника в M з одиницями по діагоналі
    for i in range(n):
        for j in range(i):
            const = M[j][i]
            for k in range(n):
                I[j][k] -= const * I[i][k]
                M[j][k] -= const * M[i][k]
    return I

def Progonka(a,b,c,d):
    M = len(d)
    p = []
    q = []
    x = []
    for i in range(M):
        x.append(0)

    p.append((-1)*c[0]/b[0])
    q.append(d[0]/b[0])

    for i in range(1, M):
        p.append(((-1)*c[i]) / (b[i]+a[i-1]*p[i-1]))
        q.append((d[i]-a[i-1]*q[i-1]) / (b[i]+a[i-1]*p[i-1]))

    x[M-1] = q[M-1]
    for i in reversed(range(M-1)):
        x[i] = p[i]*x[i+1]+q[i]
    print("P:", p)
    print("Q:", q)
    return x


def Zeidel(M, b, e):
    n = len(M)
    x = [.0 for i in range(n)]
    converge = False
    while not converge:
        xNew = np.copy(x)
        for i in range(n):
            sum1 = sum(M[i][j] * xNew[j] for j in range(i))
            sum2 = sum(M[i][j] * x[j] for j in range(i + 1, n))
            xNew[i] = (b[i] - sum1 - sum2) / M[i][i]
        converge = abs(sum(xNew[i] - x[i] for i in range(n))) <= e
        x = xNew
    return x


def Iteration(M, results, tolerance):
    diag = np.diag(M)
    div = M - np.diagflat(diag)  # по діагоналі нулі
    xNew = np.zeros_like(diag)
    x = np.ones_like(diag)

    while np.any(np.abs(x-xNew) > tolerance*np.abs(x+xNew)):
        x = xNew
        xNew = (results - np.dot(div, x)) / diag
    return x



print("Гаус: ")
print(Gauss(Array1))
print("Визначник матриці: ")
print(Determinant(Array1))
print("Обернена матриця: ")
print(np.array(GaussInverse(Array1_2)))
print("Метод Прогону: ")
print(Progonka(a, b, c, d))
print(np.linalg.solve(Array2, result2))
print("Зейдель: ")
print(Zeidel(Array3, result3, e))
print ("Ітерацій: ")
print(Iteration(Array3, result3, e))