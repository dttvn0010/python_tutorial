## Biến số
Biến số là khái niệm cơ bản nhất trong các chương trình. Chúng được dùng để lưu giá trị trung gian trong quá trình tính toán.
Bạn hãy nhớ lại chương trình ở phần mở đầu :

```python
tuoiAn = 10
tuoiBinh = tuoiAn - 2
```

Ở chương trình này, ```tuoiAn```, ```tuoiBinh``` là các biến số. 
Để khai báo một biến số, chúng ta sử dụng cú pháp :

```
bienSo = <giá trị>
```

Trong đó ```bienSo``` là tên của biến số cần khai báo, còn ```<giá trị>``` là giá trị ban đầu chúng ta muốn đặt cho biến số đó. Giá trị này có thể là một hằng số, hoặc một biểu thức của các biến số đã khai báo trước.

Sau khi khai báo, biến số sẽ được lưu trong bộ nhớ máy tính và chúng ta có thể sử dụng để thực hiện các phép tính trên biến số đó.

Để in ra giá trị hiện tại của một biến số, chúng ta sử dụng lệnh ```print``` của Python:

```python
print(bienSo)
```

Giá trị của biến số có thể thay đổi sau khi khai báo. Để cập nhật giá trị mới cho biến số, chúng ta dùng cú pháp tương tự như cú pháp khai báo biến, biến số sẽ được cập nhật theo lần gán giá trị cuối cùng.
Ví dụ:

```python
x = 1
x = 2
```

Giá trị của x sẽ bằng 2 sau khi chạy chương trình trên.
Đặc biệt, chúng ta có thể dùng giá trị hiện tại của một biến để tính toán giá trị mới cho chính biến số đó. Ví dụ:

```python
x = 1
x = x + 1
```

Sau chương trình trên, giá trị của x cũng sẽ bằng 2.

Để xóa một biến số khỏi bộ nhớ, chúng ta dùng lệnh:

```
del bienSo
```

[Tiếp theo](Data_type.md)

