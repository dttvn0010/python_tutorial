chuso = ['không', 'một', 'hai', 'ba', 'bốn', 'năm', 'sáu', 'bảy', 'tám', 'chín', 'mười']

def convert2digit(x):
    chuc = x // 10
    donvi = x % 10
    
    text = ''
    
    if chuc == 1:
        text = chuso[10]
    else:
        text = chuso[chuc] + ' mươi'

    if donvi > 0:
        text += ' '

        if donvi == 5:
            text += 'lăm'
        elif donvi == 1 and chuc > 1:
            text += 'mốt'
        else:
            text += chuso[donvi]

    return text

def convert(x):
    if x <= 10:
        return chuso[x]

    tram = x // 100
    chuc = (x//10) % 10
    donvi = x % 10
 
    if tram == 0:
        return convert2digit(x)
  
    text = chuso[tram] + ' trăm'

    if chuc > 0:
        text += ' ' + convert2digit(x%100)
    elif donvi > 0:
        text += ' lẻ ' + chuso[donvi]

    return text

print(convert3digit(105))
    

    
