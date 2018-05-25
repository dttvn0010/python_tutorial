## Các phép tính

Python hỗ trợ các phép tính toán học thông dụng. Để giải các bài toán thông dụng, chúng ta chỉ cần quan tâm đến các phép tính cơ bản sau:
  - Phép cộng (+)
  - Phép trừ (-)
  - Phép nhân (*)
  - Phép chia (/)
  - Phép chia số nguyên (//)
  - Phép lấy phần dư (%)
  - Phép lũy thừa (**)
  - Phép làm tròn số (round)
  - Phép lấy giá trị tuyệt đối (abs)

Các phép tính ```+ , - , *, /``` đều quen thuộc với chúng ta. Ví dụ :

```python
print(1+2)
print(3-2)
print(3*4)
print(1/2)
```

Ngoài ra, Python cho phép dùng các phép toán rút gọn ```+=, -=, *=, /=```. Ý nghĩa như sau:

```a += b``` tương đương với ```a = a + b```

```a -= b``` tương đương với ```a = a - b```

...

Bạn hãy chạy thử chạy chương trình trên và quan sát kết quả có như bạn ước tính hay không.

Ngoài ra trong Python còn phép chia số nguyên (//), và phép lấy phần dư (%). Hai phép tính này thực hiện trên các số nguyên. Ví dụ:

```python
print(10 // 3)
print(10 % 3)
```

Giá trị in ra màn hình là 3 và 1, tức 10 chia 3 được 3, dư 1.

Trong Python, 2 dấu * viết liền nhau được dùng để biểu thị phép lũy thừa :
```python
print(2 ** 10)
```
Kết quả trả về 2 mũ 10, tức 1024

Để làm tròn một số thập phân, bạn có thể dùng lệnh ```round``` :

```python
print(round(1.2))
```

Lệnh ```round``` còn có thể làm tròn theo một số lượng chữ số thập phân sau dấu phảy, ví dụ:

```python
print(round(1.66666, 2))
```
Kết quả in ra sẽ là 1.67

Lệnh ```abs``` được dùng để lấy giá trị tuyệt đối của một số:
```
print(abs(2))
print(abs(-2))
```

Ngoài ra, bạn có thể sử dụng các hàm toán học từ thư viện ```math``` của Python, ví dụ:

```python
import math
print(math.sin(math.pi/2))
```

Các hàm thông dụng trong thư viện toán học:
 - Các hàm lượng giác : ```sin, cos, tan, asin, acos, atan```
 - Hàm căn bậc 2 : ```sqrt```
 - Hàm phần nguyên ```floor```, hàm phần nguyên trên ```ceil```
 - Hàm logarith: ```log``` (cơ số e), ```log10``` (cơ số 10)

Để quen với các phép tính, chúng ta hãy xem xét một số ví dụ sau.

### Ví dụ 1
Bạn hãy viết chương trình in ra giá trị của các biểu thức:
 - 1999 * 2001
 - 2000 * 2000 - 1999*2001

Lời giải :

```python
print(1999 * 2001)
print(2000 * 2000 - 1999 * 2001)
```

### Ví dụ 2
Tìm 2 số biết tổng và hiệu của chúng. Nhập từ bàn phím các giá trị S (tổng 2 số), D(hiệu 2 số), in ra màn hình giá trị 2 số.

Lời giải:

Công thức tìm 2 số khi biết tổng và hiệu :
 - Số lớn = (Tổng + Hiệu)/2
 - Số bé = (Tổng - Hiệu)/2

Chương trình Python:

```python
S = input('S = ')
S = float(S)

D = input('D = ')
D = float(D)

a = (S - D)/2
b = (S + D)/2

print('a = ', a)
print('b = ', b)
```

### Ví dụ 3
Tìm 2 số biết tổng và tỉ số của chúng. Nhập từ bàn phím các giá trị S (tổng 2 số), R(tỉ số giữa 2 số), in ra màn hình giá trị 2 số.

Lời giải:

Bạn có thể xây dựng công thức tìm 2 số khi biết tổng (S), và tỉ số (R), kết quả như sau:
 - Số thứ nhất = ```S/(1+R)```
 - Số thứ hai = ```R*S/(1+R)```

Chương trình Python:

```python
S = input('S = ')
S = float(S)

R = input('R = ')
R = float(R)

a = S / (1+R)
b = a * R

print('a = ', a)
print('b = ', b)
```

### Ví dụ 4
Trên mặt phẳng cho 2 điểm có tọa độ (1, 1) và (4, 5). Tính khoảng cách giữa 2 điểm.

Lời giải:

```python
x1, y1 = 1 , 1
x2, y2 = 4, 5

dx = x2 - x1
dy = y2 - y1

d = math.sqrt(dx*dx + dy*dy)

print('Khoảng cách giữa 2 điểm : ', round(d, 6))
```

### Ví dụ 5
Trên mặt phẳng cho 3 điểm có tọa độ (0, 0), (1, 1), (2, 3). Tính diện tích tam giác tạo bởi 3 điểm trên.

Lời giải:
Để tích diện tích một tam giác tạo thành từ 3 điểm, ta sử dụng công thức diện tích tam giác do 2 vector tạo thành (X1, Y1) , (X2, Y2) là:
	```S = |X1*Y1 - X2*Y2|```

Như vậy, cần lấy một điểm trong 3 điểm làm mốc, tính tọa độ 2 vector xuất phát từ điểm đó đến 2 điểm còn lại, sau đó sử dụng công thức ở trên. 

Chương trình Python:

```python
x1, y1 = 1, 1
x2, y2 = 2, 3
x3, y3 = 0, 0

X1 = x1 - x3
Y1 = y1 - y3

X2 = x2 - x3
Y2 = y2 - y3

S0 = X1 * Y2
S1 = 0.5 * X1 * Y1
S2 = 0.5 * X2 * Y2
S3 = 0.5 * (X1-X2)*(Y2-Y1)
S = abs(S0 - S1 - S2 -S3)

print('Diện tích tam giác : ', round(S, 6))
```

### Ví dụ 6
Một máy bán hàng tự động cho phép người dùng đưa vào các tờ tiền có mệnh giá chia hết cho 5000. Trong trường hợp người mua hàng đưa vào nhiều tiền hơn giá trị mặt hàng mua (cũng có giá là bội số của 5000), máy sẽ trả lại tiền thừa cho người mua. Máy có 3 loại tiền để trả lại là 5 nghìn, 20 nghìn và 50 nghìn.

Bạn hãy viết chương trình nhập vào từ bàn phím số tiền cần trả lại (theo đơn vị nghìn đồng), sau đó tính số tiền trả lại mỗi loại (5k, 20k, 50k) sao cho tổng số tờ tiền trả lại là nhỏ nhất.

Lời giải:

Cách để trả lại tiền với tổng số tờ ít nhất:
 - Lấy số tiền trả lại chia cho 50k để được số tờ 50k
 - Lấy số dư của phép chia ở bước 1, chia cho 20k để được số tờ 20k
 - Lấy số dư của phép chia ở bước 2, chia cho 5k để được số tờ 5k

Chương trình Python:

```python
tientralai = input('Số tiền cần trả lại (nghìn đồng) :')
tientralai = int(tientralai)

soto50k = tientralai // 50
tientralai %= 50

soto20k = tientralai // 20
tientralai %= 20

soto5k = tientralai // 5

print('Số tờ tiền 50k : ', soto50k)
print('Số tờ tiền 20k : ', soto20k)
print('Số tờ tiền 5k : ', soto5k)
```

### Ví dụ 7
Để định vị một điểm trên mặt đất, người ta dùng tọa độ GPS gồm kinh độ, vĩ độ, (và độ cao).
Trên bản đồ Hà Nội, hồ Hoàn Kiếm có vĩ độ là 21.0259198, kinh độ 105.8444646 .
Lăng Bác có vĩ độ 21.0379367, kinh độ 105.8324912.
Bán kính trái đất là 6371 km.
Bạn hãy tính khoảng cách theo đường chim bay từ hồ Hoàn Kiếm đến lăng Bác.

Lời giải:
Trước hết chúng ta phải lập công thức tính khoảng cách giữa 2 điểm theo tọa độ GPS. 
Ở phạm vi nhỏ, chúng ta có thể coi tọa độ vĩ độ là tọa độ theo trục y, tọa độ kinh độ là tọa độ theo trục x.

Nếu 2 điểm có cùng kinh độ, còn vĩ độ là vd1 và vd2 thì khoảng cách giữa chúng là (bạn có thể tự chứng minh):
  ```dy = R * PI * (vd2-vd1)/180```

Nếu 2 điểm có cùng vĩ độ vd, còn kinh độ là kd1 và kd2 thì khoảng cách giữa chúng là (bạn có thể tự chứng minh):
  ```dx = R * cos(PI * vd/180) * (kd2-kd1)/180```

Từ đó chúng ta tính được khoảng cách giữa 2 điểm theo công thức:
  ```distance = sqrt(dx*dx + dy*dy)```

Chương trình Python:

```python
import math

R = 6371

vd1 = 21.0259198
kd1 = 105.8444646 

vd2 = 21.0379367
kd2 = 105.8324912

vd = (vd1+vd2)/2
phi = math.pi * vd/180
R1 = R * math.cos(phi)
dx = R1 * math.pi * abs(kd2-kd1)/180
dy = R * math.pi * abs(vd2-vd1)/180

d = math.sqrt(dx*dx + dy*dy)

print('Khoảng cách giữa 2 điểm : ', round(d, 6))
```

[Tiếp theo](Decision_making.md)
