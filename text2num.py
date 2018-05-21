chuso = {'không' : 0, 'một' : 1, 'hai' : 2, 'ba' : 3, 'bốn' : 4, 'năm' : 5, 'sáu' : 6, 'bảy' : 7, 'tám' : 8, 'chín' : 9 }

def text2num(text):
    num = 0

    for word in text.split():
        if word in chuso:
            num = 10*num + chuso[word]

    return num

print(text2num("một một năm"))
