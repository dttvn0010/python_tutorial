## Lệnh điều khiển

Khi giải các bài toán trên giấy, thứ tự thực hiện các phép tính là từ trên xuống dưới. Tuy nhiên, với các bài toán trên máy tính, có hiện tượng "rẽ nhánh", tức là tùy vào kết quả của phép tính trước mà một số phép tính sau có thể được thực hiện hay không.

Để thực hiện việc này, Python sử dụng lệnh ```if``` theo cấu trúc:

```python
if <điều kiện> :
    <Lệnh>
```
Cấu trúc trên có nghĩa : Nếu điều kiện đúng thì thực hiện lệnh, không thì không thực hiện lệnh.

```python
if <điều kiện> :
    <Lệnh 1>
else:
    <Lệnh 2>
```
Cấu trúc trên có nghĩa : Nếu điều kiện đúng thì thực hiện lệnh 1, không thì thực hiện lệnh 2.

```python
if <điều kiện 1> :
    <Lệnh 1>
elif <điều kiện 2>  :
    <Lệnh 2>
elif <điều kiện 3>  :
    <Lệnh 3>
else:
    <Lệnh 4>
```
Cấu trúc trên có nghĩa : Nếu điều kiện 1 đúng thì thực hiện lệnh 1, không thì kiểm tra điều kiện 2, nếu điều kiện 2 đúng thì thực hiện lệnh 2, nếu không tiếp tục kiểm tra các điều kiện tiếp theo.

Điều kiện trong câu lệnh ```if``` là điều kiện logic, chỉ có giá trị đúng (True) hoặc sai (False). Các phép tính sử dụng trong các biểu thức điều kiện này là:
 - Các phép so sánh : lớn hơn (>), nhỏ hơn (<), lớn hơn hoặc bằng (>=), nhỏ hơn hoặc bằng (<=), bằng nhau (==), khác nhau (!=)
 - Phép phủ định ```not``` : ```not dieukien``` có giá trị True nếu điều kiện sai và ngược lại
 - Phép "và" ```and``` : ```dieukien1 and dieukien2 ``` có giá trị True nếu cả 2 điều kiện thành phần đúng
 - Phép "hoặc" ```or``` : ```dieukien1 or dieukien2 ``` có giá trị True nếu ít nhất 1 trong 2 điều kiện thành phần đúng

Lưu ý:
 - Cuối các dòng của lệnh ```if``` hoặc ```else``` là dấu 2 chấm. Python sử dụng dấu 2 chấm để bắt đầu cho một khối lệnh con, bạn sẽ quen dần với điều này.
 - Các lệnh bên dưới ```if``` hoặc ```else``` cần được viết lùi vào bởi một số khoảng trắng (thường là 4), nếu có nhiều hơn một lệnh thì chúng phải được viết thẳng hàng.

### Ví dụ 1
So sánh 2 số sau:
 - A = 1999 * 2001
 - B = 2000 * 2000

Lời giải:

```python
A = 1999 * 2001
B = 2000 * 2000

if A > B:
   print('A > B)

if A < B:
   print('A < B')

if A == B:
   print('A = B')
```

### Ví dụ 2
- Nhập vào 2 số từ bàn phím và in ra giá trị nhỏ nhất của 2 số.

Lời giải:

```python
a = input('Số thứ nhất : ')
a = float(a)

b = input('Số thứ hai : ')
b = float(b)

if a < b:
   print(a)
else:
   print(b)
```

### Ví dụ 3
Tìm 2 số khi biết tổng và tích. Nhập vào từ bàn phím các giá trị S (tổng 2 số), P(tích 2 số). In ra màn hình giá trị 2 số nếu tồn tại, nếu không thì thông báo không tồn tại 2 số.

Lời giải:

Theo định lý Viét, 2 số cần tìm là nghiệm phương trình bậc 2:
  ```x*x - S*x + P = 0```

Dựa trên việc giải biện luận phương trình bậc 2 trên, chúng ta biết có tồn tại 2 số cần tìm không. 

Chương trình Python:

```python
import math

S = float(input('S = '))
P = float(input('P = '))

delta = S*S - 4*P

if delta < 0:
    print('Không tồn tại 2 số thỏa mãn yêu cầu')
    exit()

sqrt_delta = math.sqrt(delta)
a = (S - sqrt_delta)/2
b = (S + sqrt_delta)/2

print('a = ', a)
print('b = ', b)
```

### Ví dụ 4
Nhập vào từ bàn phím 3 giá trị ngày, tháng, năm (trong thế kỉ 21). Kiểm tra ngày đó có tồn tại không.

Ví dụ:
 - Ngày 29/2/2000 : có tồn tại
 - Ngày 29/2/2001 : không tồn tại
 - Ngày 31/7/2010 : có tồn tại
 - Ngày 31/6/2016 : không tồn tại

Lời giải:

Chúng ta có thể kiểm tra sự tồn tại của một bộ giá trị (ngày, tháng, năm) như sau:
 - Nếu ngày, tháng, năm nhỏ hơn hoặc bằng 0 -> ngày đó không tồn tại
 - Nếu tháng lớn hơn 12 -> ngày đó không tồn tại
 - Tính số ngày trong tháng
 - Nếu ngày lớn hơn số ngày trong tháng -> ngày đó không tồn tại, còn nếu không thì ngày đó tồn tại

Tháng 2 có 28 ngày vào năm thường, 29 ngày vào năm nhuận. Trong thế kỉ 21, các năm nhuận là các năm chia hết cho 4.

Chương trình Python:

```python
date = int(input('Ngày : '))
month = int(input('Tháng : '))
year = int(input('Năm : '))

if date <= 0 or month <= 0 or year <= 0:
    print('Không tồn tại ngày này')
    exit()

if month > 12:
    print('Không tồn tại ngày này')
    exit()

if month == 2:
    day_in_month = 29 if (year%4 == 0) else 28
else:
    x = month if (month < 8) else month-7
    day_in_month = 30 + x % 2
     
if date <= day_in_month:
    print('Tồn tại ngày này')
else:
    print('Không tồn tại ngày này')
```

### Ví dụ 4
Chỉ số BMI (Body mass index) dùng để đánh giá thân hình của một người. Chỉ số này được đo bằng tỉ số giữa cân nặng (tính theo kg) và bình phương của chiều cao (tính theo mét).
Dựa vào chỉ số BMI, người ta có thể đánh giá được thân hình của một người:
 - BMI nhỏ hơn 15 : thân hình quá gầy
 - BMI từ 15 đến 16 : thân hình gầy
 - BMI từ 16 đến 18.5 : thân hình hơi gầy
 - BMI từ 18.5 đến 25 : thân hình bình thường
 - BMI từ 25 đến 30 : thân hình hơi béo
 - BMI từ 30 đến 35: thân hình béo
 - BMI trên 35: thân hình quá béo

Nhập vào giá trị chiều cao và cân nặng của một người từ bàn phím và cho biết tình trạng thân hình của người đó.

Lời giải:

```python
height = input('Chiều cao (mét) : ')
height = float(height)

mass = input('Cân nặng (kg) : ')
mass = float(mass)

bmi = mass / (height * height)

if bmi < 15:
    print('Thân hình quá gầy')

elif bmi < 16:
    print('Thân hình gầy')

elif bmi < 18.5:
    print('Thân hình hơi gầy')

elif bmi < 25:
    print('Thân hình bình thường')

elif bmi < 30:
    print('Thân hình hơi béo')

elif bmi < 35:
    print('Thân hình béo')

else:
    print('Thân hình quá béo')
```

[Tiếp theo](Loop.md)


