cities = ['A', 'B', 'C', 'D']

distances = { 
           ('A', 'B') : 10,
           ('B', 'C') : 5,
           #('C', 'B') : 5,  # TODO : Bỏ comment dòng này và sửa chương trình để chạy đúng
           ('B', 'D') : 7,
           ('C', 'D') : 5
        }        

def find_shortest_path(c1, c2):
    if c1 == c2:
        return (0, c1)
    
    paths = []
    
    for c in cities:
        if (c1,c) in distances:
            distance, route = find_shortest_path(c, c2)
                        
            if distance >= 0 :
                distance += distances[(c1,c)]
                route = c1 + '->' + route
                paths.append((distance, route))
    
    if len(paths) > 0:
        paths = sorted(paths)
        return paths[0]
    
    else:
        return (-1, '')
            
print(find_shortest_path('A', 'D'))