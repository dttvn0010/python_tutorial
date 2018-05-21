import math

S = float(input('S = '))
P = float(input('P = '))

delta = S*S - 4*P

if delta < 0:
    print('Không tồn tại 2 số thỏa mãn yêu cầu')
    exit()

sqrt_delta = math.sqrt(delta)
a = (S - sqrt_delta)/2
b = (S + sqrt_delta)/2

print('a = ', a)
print('b = ', b)
