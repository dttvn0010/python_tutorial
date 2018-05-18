key = 10
msg = 'TOI NAY CO DI CHOI KHONG'

enc_msg = ''
for c in msg:
    if c == ' ':
        enc_msg += c
    else:
        x = ord(c) - ord('A') + key
        x = x % 25
        x = x + ord('A')
        enc_msg += chr(x)

print(enc_msg)
