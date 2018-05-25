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

### Ví dụ 1:
So sánh 2 số sau:
 - A = 1999 * 2001
 - B = 2000 * 2000

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

### Ví dụ 2:
- Nhập vào 2 số từ bàn phím và in ra giá trị nhỏ nhất của 2 số.

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

### Ví dụ 3:
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


