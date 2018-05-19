import math

S = input('S = ')
S = float(S)

P = input('P = ')
P = float(P)

delta = S*S - 4*P

if delta < 0:
    print('Khong ton tai 2 so thoa man yeu cau')
    exit()

sqrt_delta = math.sqrt(delta)
a = (S - sqrt_delta)/2
b = (S + sqrt_delta)/2

print('a = ', a)
print('b = ', b)
