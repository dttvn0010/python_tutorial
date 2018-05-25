## Hàm giá trị

Nếu một đoạn chương trình được gọi nhiều lần, chúng ta có thể viết đoạn đó thành một hàm để gọi tới.

Cách khai báo một hàm như sau:

```python
def tenham(<danh_sach_bien>):
    <noi_dung_ham>
    return <ket_qua>
```

Các thành phần của hàm:
 - Khai báo hàm : bắt đầu bằng từ khóa ```def``` của Python, tiếp theo là tên hàm, tiếp theo là danh sách các biến nằm trong 2 dấu ```()```, các biến ngăn cách nhau bởi dấu phảy.
 - Nội dung hàm : bao gồm các lệnh thực hiện của hàm. Các dòng lệnh này phải được viết lùi vào so với dòng khai báo hàm một số (thường là 4) khoảng trắng.
 - Kết quả trả về của hàm : kết quả được trả về với từ khóa ```return``` đi kèm các giá trị trả về, cũng được ngăn cách bởi dấu phảy.

Trong chương trình, việc gọi hàm tuân theo cú pháp sau:

```python
<danh_sach_bien_ketqua> = tenham(<danh_sach_bien_dau_vao>)
```

Trong trường hợp không quan tâm đến kết quả trả về của hàm, chúng ta dùng cú pháp:

```python
tenham(<danh_sach_bien_dau_vao>)
```

## Ví dụ

### Ví dụ 1
Viết hàm tính bình phương của một số

Lời giải:

```python
def square(x):
   return x*x

for i in range(1,11):
   print(square(x))
```

### Ví dụ 2
Viết hàm tính diện tích và chu vi của một hình chữ nhật khi biết độ dài 2 cạnh

Lời giải:

```python
def calcAreaAndPerimeter(width, height):
    S = width * height
    P = 2*(width + height)
    return S, P

S, P = calcAreaAndPerimeter(5, 4)
print('S = ', S)
print('P = ', P)
```

### Ví dụ 3
Tìm giá trị nhỏ nhất của hàm số ```2*x*x - x + 1``` trên đoạn [0,1]

Lời giải:

Chúng ta chia nhỏ đoạn [0,1] thành N vị trí, tính giá trị của hàm số tại các vị trí đó, sau đó tìm ra giá trị nhỏ nhất trong các vị trí này.

```python
def f(x):
    return 2*x*x - x + 1

a = 0
b = 1
xmin = a
fmin = f(a)
N = 1000

for i in range(N):
    x = a + (b-a) * (i/N)
    fx = f(x)
    if fx < fmin:
        fmin = fx
        xmin = x

print('fmin=', fmin, ' , xmin=', xmin)
```

Bạn hãy kiểm tra xem giá trị nhỏ nhất của hàm có phải đạt tại ```x=1/4``` không.

### Ví dụ 4:
Tìm nghiệm gần đúng của phương trình ```x*x*x + x - 1 = 0 ```

Lời giải:

Chúng ta nhận thấy hàm số ```f(x) = x*x*x + x - 1``` thỏa mãn điều kiện ```f(0) < 0``` và ```f(1) > 0```, do đó chúng ta có thể dùng thuật toán tìm kiếm nhị phân giống như ở bài toán đoán số nguyên trong chương trước, để tìm nghiệm gần đúng của phương trình trên đoạn [0,1].

Cách thức thực hiện như sau:
 - Đặt 2 giá trị đầu mút của đoạn chứa nghiệm là 0 và 1
 - Với mỗi bước, tính giá trị hàm số tại điểm chính giữa của đoạn chứa nghiệm. Thu hẹp đoạn chứa nghiệm sao cho giá trị của hàm số tại 2 đầu của đoạn này luôn trái dấu nhau.
 - Khi độ dài đoạn chứa nghiệm đủ nhỏ thì dừng lại.

Chương trình Python:

```
def f(x):
    return x*x*x + x - 1

a = 0
b = 1
eps = 1e-6
fa = f(a)
fb = f(b)

while True:
    x = (a+b)/2
    fx = f(x)

    if abs(fx) < eps:
        break
    elif fx * fa > 0:
        a = x
    else:
        b = x

print('x=', x)
```

[Tiếp theo](String.md)
