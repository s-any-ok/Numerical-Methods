def f(x):
    return (x**2)/(x**4 + 256)

def romberg(f,a,b,n):
    result=[]
    h = (b - a)
    result.append([(h/2.0)*(f(a)+f(b))])
    for i in range(1, n+1):
        h = h/2.
        amount = 0
        for k in range(1,2**i ,2):
            amount = amount + f(a+k*h)

        rowi = [0.5*result[i-1][0] + amount*h]

        for j in range(1, i+1):
            rij = rowi[j-1] + (rowi[j-1]-result[i-1][j-1])/(4.**j-1.)
            rowi.append(rij)

        result.append(rowi)
    return result

a = 0
b = 2
n1 = 4
n2 = 8
for i in romberg(f, a, b, n1):
    print(i)
for i in romberg(f, a, b, n2):
    print(i)