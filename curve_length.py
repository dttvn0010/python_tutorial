import math

points = [(0,0), (1,1), (2,3), (3,6)]

N = len(points)
total_length = 0

for i in range(N-1):
	x1, y1 = points[i]
	x2, y2 = points[i+1]
	dx = x2 - x1
	dy = y2 - y1 
	d = math.sqrt(dx*dx + dy*dy)
	total_length += d
	
print('Curve length = ', round(total_length,6))
