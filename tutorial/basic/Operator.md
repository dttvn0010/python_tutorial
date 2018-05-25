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

Các phép tính + , - , *, / đều quen thuộc với chúng ta. Ví dụ :

```python
print(1+2)
print(3-2)
print(3*4)
print(1/2)
```

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

[Tiếp theo](Decision_making.md)
