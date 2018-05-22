bang_so1 = {'một' : 1, 'hai' : 2, 'ba' : 3, 'bốn' : 4, 'năm' : 5, 'sáu' : 6, 'bảy' : 7, 'tám' : 8, 'chín' : 9, 'mười' : 10}
bang_so2 = {'một' : 1, 'hai' : 2, 'ba' : 3, 'bốn' : 4, 'lăm' : 5, 'sáu' : 6, 'bảy' : 7, 'tám' : 8, 'chín' : 9}
bang_so3 = {'mươi' : 0, 'mốt' : 1, 'hai' : 2, 'ba' : 3, 'bốn' : 4, 'lăm' : 5, 'sáu' : 6, 'bảy' : 7, 'tám' : 8, 'chín' : 9}


def convert1digit(words):
    return bang_so1.get(words[0], -1)

def convert2digit(words):
    N = len(words)

    if N == 1:
        return convert1digit(words)

    chuc, donvi = -1, -1

    if N == 2 and words[0] == 'mười':
        chuc = 1
        donvi = bang_so2.get(words[1], -1)

    if (N == 3 and words[1] == 'mươi') or N == 2:
        chuc = bang_so1.get(words[0], -1)
        donvi = bang_so3.get(words[-1], -1)

    if chuc >= 0 and donvi >= 0:
        return 10 * chuc + donvi
    
    return -1

def convert3digit(words):
    N = len(words)

    if N <= 1 or words[1] != 'trăm':
        return convert2digit(words)

    tram = bang_so1.get(words[0], -1)

    if N == 2 and tram >= 0:
        return 100*tram     
    
    if N == 4 and words[2] == 'lẻ':
        donvi = bang_so1.get(words[3], -1)

        if tram >= 0 and donvi >= 0:
            return 100*tram + donvi

    x = convert2digit(words[2:])

    if tram >= 0 and x >= 0:
        return 100*tram + x

    return -1
        

def text2num(text):    
    return convert3digit(text.lower().split())

print(text2num('tám trăm hai mươi bảy'))


