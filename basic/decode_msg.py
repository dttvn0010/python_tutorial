"""
Chương trình giải mã bức điện
 - Đầu vào :
    + Khóa k (0 <= k <= 25) đã dùng để mã hóa
    + Bức điện đã được mã hóa
      trong đó mỗi kí tự đã được dịch đi k vị trí trong bảng chữ cái tiếng Anh
 - Đầu ra:
    + Nội dung bức điện gốc 
"""

encode_key = 10
key = 25 - encode_key
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
