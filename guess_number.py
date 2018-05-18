low = 0
high = 1000

print('Bạn hãy nghĩ trong đầu một số trong phạm vi từ 0 đến 1000, sau đó trả lời các câu hỏi sau.')

for i in range(10):
    mid = (low + high) // 2
    a = input('Số đó lớn hơn ' + str(mid)  + ' ? (Y/N) : ')
    
    if a == 'Y':
        low = mid
    else:
        high = mid

print('Số bạn nghĩ là ', high)

