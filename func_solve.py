def f(x):
    return x*x*x + x - 1

a = 0
b = 1
eps = 1e-6
fa = f(a)
fb = f(b)

while True:
    x = (a+b)/2
    fx = f(x)

    if abs(fx) < eps:
        break
    elif fx * fa > 0:
        a = x
    else:
        b = x

print('x=', x)
    
