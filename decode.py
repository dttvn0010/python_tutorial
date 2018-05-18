key = 15
msg = 'EYS XKJ MY NS MRYS URYXQ'

dec_msg = ''
for c in msg:
    if c == ' ':
        dec_msg += c
    else:
        x = ord(c) - ord('A') + key
        x = x % 25
        x = x + ord('A')
        dec_msg += chr(x)

print(dec_msg)
