def f(x):
    return 2*x*x - x + 1

a = 0
b = 1
xmin = a
fmin = f(a)
N = 1000

for i in range(N):
    x = a + (b-a) * (i/N)
    fx = f(x)
    if fx < fmin:
        fmin = fx
        xmin = x

print('fmin=', fmin, ' , xmin=', xmin)
