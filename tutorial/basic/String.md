## Dữ liệu kiểu văn bản

Dữ liệu kiểu văn bản dùng để chứa các giá trị chứa thông tìn về ngôn ngữ như tên, địa chỉ, số điện thoại ...

Ở phần đầu, chúng ta đã biết qua về kiểu dữ liệu văn bản, mỗi giá trị văn bản được đặt trong 2 dấu nháy đơn, hoặc 2 dấu nháy kép

```python
hoten = 'Nguyễn Văn An'
diachi = "Hà Nội"
```

Phần này chúng ta sẽ tìm hiểu các phép tính thông dụng trên kiểu dữ liệu văn bản.

Các phép tính thông dụng về dữ liệu văn bản trong Python:
 - Hàm ```str``` : chuyển đổi số (và các kiểu dữ liệu khác) sang dữ liệu văn bản
 - Phép ```+``` 2 chuỗi : ghép 2 xâu văn bản thành một
 - Hàm ```lower``` chuyển văn bản sang chữ thường, hàm ```upper``` chuyển văn bản sang chữ hoa
 - Hàm ```replace``` : thay nội dung một xâu con trong xâu văn bản
 - Hàm ```split``` : tách một xâu thành các xâu con

Ví dụ:
 - str(1000) -> '1000'
 - 'Chào ' + 'bạn' -> 'Chào bạn'
 - 'Chào bạn'.lower() -> 'chào bạn'
 - 'Chào bạn'.upper() -> 'CHÀO BẠN'
 - 'Tôi sống ở Hà Nội'.replace('Hà Nội', 'Huế') -> 'Tôi sống ở Huế'
 - 'Hà Nội'.split() -> ['Hà', 'Nội']
 - 'Hà Nội, Việt Nam'.split(',') -> ['Hà Nội', 'Việt Nam']

Ngoài ra, mỗi xâu văn bản có thể coi là một tập các kí tự, chúng ta có thể dùng vòng lặp ```for``` trên tập này:

```python
text = 'Chào bạn'
for c in text:
    print(c)
```

Để lấy một đoạn con trong một xâu văn bản, chúng ta sử dụng cú pháp:

```python
text[start:end]
```
Trong đó ```start```, ```end``` là vị trí bắt đầu và kết thúc của xâu con chúng ta muốn lấy ra. Lưu ý :
 - Kí tự đầu tiên trong xâu có vị trí là 0
 - Kí tự ở vị trị ```end``` không bao gồm trong xâu con lấy ra, tức xâu con gồm các kí tự từ vị trí 0 đến ```end-1```

Ví dụ:
```python
text = 'Chào bạn'
text1 = text[0:4]
print(text1)
```

Nếu giá trị ```end``` được bỏ qua thì xâu con trả về sẽ chứa các kí tự từ vị trí ```start``` đến hết cuối xâu.
```python
text = 'Chào bạn'
print(text[5:])
```

Trong Python, có thể dùng chỉ số âm, khi đó vị trí phần tử đang xét sẽ được tính từ cuối xâu trở về.

```python
text = 'Chào bạn'
print(text[-1])
print(text[-3:])
```

## Ví dụ

Để hiểu hơn về dữ liệu kiểu văn bản, chúng ta hãy xem xét một số ví dụ sau.

### Ví dụ 1
Nhập vào từ bàn phím một số tự nhiên và in ra biểu diễn nhị phân của số đó.

Lời giải:

Để chuyển một số từ hệ thập phân sang nhị phân, chúng ta chia số đó cho 2 liên tiếp cho đến khi thương bằng 1. Số dư các lần chia được viết từ phải qua trái.

Chương trình Python:

```python
x = input("Nhập số tự nhiên : ")
x = int(x)

s = ''
while x > 0:
    i = x % 2
    s = str(i) + s
    x = x // 2

print(s)
```


### Ví dụ 2
Mã hóa một bức điện

An và Bình trao đổi qua email. Để tránh việc bị lộ nội dung trao đổi ra ngoài, An dùng chương trình để mã hóa nội dung gửi đi. Giả sử nội dung bức điện chỉ chứa các chữ cái hoa trong bảng chữ cái tiếng Anh (từ 'A' đến 'Z') và kí tự trắng (phân cách các từ). Chương trình mã hóa được thực hiện như sau:
 - An chọn một số tự nhiên ```k``` trong khoảng từ 1 đến 25, dùng làm khóa hay mật mã
 - Với mỗi kí tự trong xâu nội dung, nếu kí tự đó là kí tự trắng (phân cách các từ) thì giữ nguyên, nếu là kí tự là chữ cái thì dịch đi ```k``` vị trí trong bảng chữ cái tiếng Anh, khi dịch qua 'Z' thì quay về 'A' trong bảng chữ cái.

Bạn hãy giúp An viết chương trình mã hóa trên. Để đơn giản, An chọn trước khóa ```k = 10```.

Lời giải:

Để thực hiện chương trình trên, chúng ta cần biết một số hàm:
 - Hàm ```ord(c)``` : lấy mã thứ tự của một kí tự trong bảng mã kí tự. Ví dụ ```ord('A') -> 65, ord('Z') -> 90```
 - Hàm ```chr(x)``` : chuyển ngược từ thứ tự của một kí tự trong bảng kí tự thành kí tự đó. Ví dụ ```chr(65) -> 'A'```

Với 2 hàm trên, việc dịch một kí ```c``` tự đi ```k``` vị trí trong bảng chữ cái được thực hiện như sau:

```python
x = ord(c) - ord('A')
x += k
x = x % 26
x = x + ord('A')
c = chr(x)
```

Ở đoạn chương trình trên, dòng đầu tiên tính vị trị của kí tự ```c``` trong bảng chữ cái tiếng Anh, dòng thứ 2 dịch đi k vị trị, dòng thứ 3 đảm bảo nếu vị trí dịch qua 'Z' sẽ quay về 'A', dòng thứ 4 chuyển vị trị được dịch tới về kí tự tương ứng trong bảng chữ cái.

Chương trình mã hóa bức điện đầy đủ như sau:

```python
k = 10
msg = 'TOI NAY CO DI CHOI KHONG'

enc_msg = ''
for c in msg:
    if c == ' ':
        enc_msg += c
    else:
        x = ord(c) - ord('A')
        x += k
        x = x % 26
        x = x + ord('A')
        enc_msg += chr(x)

print(enc_msg)
```

Nội dung bức điện được mã hóa là 'DYS XKI MY NS MRYS URYXQ'


### Ví dụ 3
Giải mã bức điện.

Tiếp tục với ví dụ 2. Sau khi Bình nhận được bức điện của An, cần giải mã lại nội dung bức điện. Giả sử An cho Bình biết khóa đã mã hóa là ```k = 10```. Bạn hãy giúp Bình giải mã bức điện.

Lời giải:

Về cơ bản, chương trình giải mã giống với chương trình mã hóa, chỉ khác là khóa giải mã khác với khóa mã hóa. Chúng ta biết nếu dịch một kí tự đi 26 vị trí trong bảng chữ cái thì sẽ trở về chính nó, do đó ta chọn khóa giải mã sao cho tổng khóa mã hóa và khóa giải mã bằng 26.

Chương trình giải mã của Bình như sau:

```python
k = 10
k = 26 - k
msg = 'DYS XKI MY NS MRYS URYXQ'

dec_msg = ''
for c in msg:
    if c == ' ':
        dec_msg += c
    else:
        x = ord(c) - ord('A')
        x += k
        x = x % 26
        x = x + ord('A')
        dec_msg += chr(x)

print(dec_msg)
```

Bạn hãy kiểm tra xem bức điện Bình nhận được có giống bức điện gốc trước khi mã hóa của An không.


[Tiếp theo](List.md)
