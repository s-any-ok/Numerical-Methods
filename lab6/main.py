import numpy.linalg
from math import sqrt
import numpy as np

np.set_printoptions(suppress=True)

Array1 = [
    [-5., -1., -3., -1., 18.],
    [-2., 0., 8., -4., -12.],
    [-7., -2., 2., -2., 0.],
    [2., -4., -4., 4., -12.]]

Array2 = np.array([
    [18, -9, 0, 0, 0],
    [2, -9, -4, 0, 0],
    [0, -9, 21, -8, 0],
    [0, 0, -4, -10, 5],
    [0, 0, 0, 7, 12]])
result2 = np.array([-81, 71, -39, 64, 3])

a = np.array([2, -9, -4, 7])
b = np.array([18, -9, 21, -10, 12])
c = np.array([-9, -4, -8, 5])
d = np.array([-81, 71, -39, 64, 3])

Array3 = np.array([
    [21, -6, -9, -4],
    [-6, 20, -4, 2],
    [-2, -7, -20, 3],
    [4, 9, 6, 24]])
result3 = np.array([127, -144, 236, -5])
target = 0.01

def MaxRow(m, col):
    max_element = m[col][col]
    max_row = col
    for i in range(col + 1, len(m)):
        print(m[i][col], max_element)
        if abs(m[i][col]) > abs(max_element):
            max_element = m[i][col]
            max_row = i
    if max_row != col:
        m[col], m[max_row] = m[max_row], m[col]


def Gauss(m):
    n = len(m)

    for k in range(n - 1):
        MaxRow(m, k)
        for i in range(k + 1, n):
            div = m[i][k] / m[k][k]
            m[i][-1] -= div * m[k][-1]
            for j in range(k, n):
                m[i][j] -= div * m[k][j]

    if IsSingular(m):
        print("Визначник дорівнює нулю => система має безліч розв'язків")
        return

    x = [0 for i in range(n)]
    for k in range(n - 1, -1, -1):
        x[k] = (m[k][-1] - sum([m[k][j] * x[j] for j in range(k + 1, n)])) / m[k][k]

    return x


def IsSingular(m):
    for i in range(len(m)):
        if not m[i][i]:
            return True
    return False

def Progon(a, b, c, d):
    nf = len(d)
    ac, bc, cc, dc = map(np.array, (a, b, c, d))
    for it in range(1, nf):
        mc = ac[it - 1] / bc[it - 1]
        bc[it] = bc[it] - mc * cc[it - 1]
        dc[it] = dc[it] - mc * dc[it - 1]

    xc = bc
    xc[-1] = dc[-1] / bc[-1]

    for il in range(nf - 2, -1, -1):
        xc[il] = (dc[il] - cc[il] * xc[il + 1]) / bc[il]

    return xc


def Seidel(A, b, eps):
    n = len(A)
    x = [.0 for i in range(n)]
    converge = False
    while not converge:
        x_new = np.copy(x)
        for i in range(n):
            s1 = sum(A[i][j] * x_new[j] for j in range(i))
            s2 = sum(A[i][j] * x[j] for j in range(i + 1, n))
            x_new[i] = (b[i] - s1 - s2) / A[i][i]
        converge = sqrt(sum((x_new[i] - x[i]) ** 2 for i in range(n))) <= eps
        x = x_new
    return x


def Iteration(Array,result,N=50,x=0):
    if x == 0:
        x = np.zeros(len(Array[0]))
    D = np.diag(Array)
    R = Array - np.diagflat(D)
    x_new = np.zeros_like(D)
    x = np.ones_like(D)

    while np.any(np.abs(x-x_new) > 1e-5*np.abs(x+x_new)):
        x = x_new
        x_new = (result - np.dot(R, x)) / D
    return x

print("Гаус: ")
print(Gauss(Array1))
print("Прогон: ")
print(Progon(a, b, c, d))
print(np.linalg.solve(Array2, result2))
print("Зейдель: ")
print(Seidel(Array3, result3, target))
print ("Итераций: ")
print(Iteration(Array3, result3, N=33))