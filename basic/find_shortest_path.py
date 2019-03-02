points = ['A', 'B', 'C', 'D']

distances = { 
           ('A', 'B') : 10,
           ('B', 'C') : 5,
           #('C', 'B') : 5,  # TODO : Bỏ comment dòng này và sửa chương trình để chạy đúng
           ('B', 'D') : 7,
           ('C', 'D') : 5
        }        

def find_shortest_path(p1, p2):
    if p1 == p2:
        return (0, p1)
    
    paths = []
    
    for p in points:
        if (p1, p) in distances:
            route_length, route = find_shortest_path(p, p2)
                        
            if route_length >= 0 :
                route_length += distances[(p1, p)]
                route = p1 + '->' + route
                paths.append((route_length, route))
    
    if len(paths) > 0:
        paths = sorted(paths)
        return paths[0]
    
    else:
        return (-1, '')
            
print(find_shortest_path('A', 'D'))
