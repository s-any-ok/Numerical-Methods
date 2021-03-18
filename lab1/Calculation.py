from sympy import *
x = symbols('x')
init_printing(use_unicode=True)

# const
e = 2.718281828459045

def halfDivisionMethodFn(func, seg):
    arr = seg.copy()
    result = 1
    i = 0;
    while round(result, 4) != 0.0:
        # arr.append([arr[0], arr[1]])
        d = (arr[0] + arr[1]) / 2
        result = func(d)
        print('k', i)
        print('a', round(arr[0], 4), 'b', round(arr[1], 4))
        print('f(a)', round(func(arr[0]), 4), 'f(b)', round(func(arr[1]), 4))
        print('(a+b)/2', round(d, 4))
        print('f((a+b)/2)', round(result, 4))
        print()
        if func(arr[0]) * result >= 0:
            arr[0] = d
        else:
            arr[1] = d
        i = i + 1
    print('result', round(d, 4))
    print()


def newtonMethodFn(fnSign, func, seg):
    f1 = diff(fnSign)
    f2 = diff(f1)
    fx1 = lambdify(x, f1, 'numpy')
    fx2 = lambdify(x, f2, 'numpy')
    if func(seg[1]) * fx2(seg[1]) > 0:
        x0 = seg[1]
    else:
        x0 = seg[0]
    print('f``(x1)', round(fx2(x0), 4))
    print('f(x1)*f``(x1)', round(func(x0) * fx2(x0), 4))
    print('f1', f1)
    print('f2', f2)
    print()
    i = 0;
    while abs(round(func(x0)/fx1(x0), 4)) != 0.0:
        print('k', i)
        print('x1', round(x0, 4))
        print('f(x1)', round(func(x0), 4))
        print('f`(x1)', round(fx1(x0), 4))
        print('-f(x1)/f`(x1)', round(-(func(x0)/fx1(x0)), 4))
        print()
        x0 = x0 - (func(x0)/fx1(x0))
        i = i + 1
    print('result', round(x0 - (func(x0) / fx1(x0)), 4))
    print()


def simpleIterationMethodFn(fn, seg):
    x0 = (seg[0]+seg[1])/2
    i = 0
    while round(x0, 4) != round(fn(x0), 4):
        print('k', i)
        print('x0', round(x0, 4))
        print('f(x0)', round(fn(x0), 4))
        print()
        x0 = fn(x0)
        i = i + 1
    print('result', round(fn(x0), 4))
    print()


# def funcTest(x):
#     return e**(2*x) + 3*x - 4
#
# def funcTest2(x):
#     return np.log(4-3*x)/2
#
# seg3 = [0.4, 0.6]

funcSign = x*exp(x) + x**2 - 1
funcSign1 = 1 - x**2
funcSign2 = x*exp(x)

def startFunc(x):
    return x*e**x + x**2 - 1

def startFuncFirstPart(x):
    return (1/2)*(x + 1/(e**x + x))


# segment1
seg1 = [0, 1]
seg2 = [-1.5, -1]

print('Методом повторного ділення \n')
halfDivisionMethodFn(startFunc, seg2)
print('==================================================== \n')
print('Методом Ньютона \n')
newtonMethodFn(funcSign, startFunc, seg2)
print('==================================================== \n')
print('Методом простої ітерації \n')
simpleIterationMethodFn(startFuncFirstPart, seg2)

print()
print('#=================================================# \n')
print()

print('Методом повторного ділення \n')
halfDivisionMethodFn(startFunc, seg1)
print('==================================================== \n')
print('Методом Ньютона \n')
newtonMethodFn(funcSign, startFunc, seg1)
print('==================================================== \n')
print('Методом простої ітерації \n')
simpleIterationMethodFn(startFuncFirstPart, seg1)