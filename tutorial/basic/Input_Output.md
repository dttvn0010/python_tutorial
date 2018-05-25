## Nhập dữ liệu từ bàn phím và in dữ liệu ra màn hình

### Nhập dữ liệu từ bàn phím
Giá trị của các biến số có thể được khai báo trực tiếp trong chương trình, như chúng ta đã biết ở phần trước.

Tuy nhiên, trong nhiều trường hợp, chúng ta muốn sử dụng lại chương trình đã viết với các bộ dữ liệu vào khác nhau. Trong trường hợp đó, chúng ta cần cho phép người sử dụng nhập dữ liệu vào cho các biến. Cách đơn giản nhất để nhập giá trị vào là từ bàn phím.

Trong Python, lệnh ```input``` cho phép lưu giá trị mà người dùng nhập vào từ bàn phím :

```python
line = input('Thông tin cần nhập : ')
```

Lệnh ```input``` sẽ đọc các kí tự người dùng nhập từ bán phím, cho đến khi người dùng nhấn Enter. Như vậy giá trị trả về sẽ là một dòng văn bản.

Chương trình sau yêu cầu bạn giới thiệu tên, sau đó sẽ đưa ra lời chào dựa vào tên bạn:

```python
ten = input('Mời bạn cho biết tên của bạn : ')
print('Xin chào ', ten)
```

Lệnh ```input``` của Python luôn trả về dữ liệu ở dạng văn bản. Trong trường hợp chúng ta muốn nhập giá trị vào cho một biến ở kiểu số, chúng ta phải dùng lệnh chuyển đổi từ văn bản sang số :
  - Lệnh ```int(text)``` chuyển giá trị văn bản ```text``` thành số nguyên
  - Lệnh ```float(text)``` chuyển giá trị văn bản ```text``` sang số thập phân

Ví dụ:

```python
tuoi = input('Mời bạn cho biết tuổi của bạn : ')
tuoi = int(tuoi)
print('Cảm ởn, tôi đã biết tuổi của bạn là : ', tuoi)
```

Ở chương trình trên, dòng thứ 2 ```tuoi = int(tuoi)``` đổi giá trị nhập vào ở dòng đầu tiên (có kiểu dữ liệu là văn bản) thành một biến có kiểu dữ liệu là số nguyên (int)

Bạn có thể thử nghiệm tương tự với kiểu số thập phân.

### In dữ liệu ra màn hình
Sau khi đã giải xong bài toán, chúng ta phải in kết quả ra màn hình cho người sử dụng biết. Để in giá trị ra màn hình, Python sử dụng lệnh ```print```:

```python
print(<danh sách biến ngăn cách nhau bởi dấu phảy>)
```

Bên trong lệnh ```print```, bạn có thể đặt nhiều biến số muốn in ra, các biến số cách nhau bởi dấu phảy. Khi được in ra, các giá trị biến số sẽ được ngăn cách nhau bởi một kí tự trống.
Ví dụ:

```python
x = 1
y = 2
z = x + y
print(x, '+', y , '=', z)
```

Chương trình trên sẽ in ra : 1 + 2 = 3

Với các bạn đã biết về lập trình thì lệnh ```print``` ở trên khá đơn giản. Tuy nhiên, nếu bạn hoàn toàn mới với lập trình và cảm thấy lệnh ```print``` ở dòng cuối chương trình trên hơi khó hiểu. 

```python
print(x, '+', y , '=', z)
```

Danh sách các biến in ra trong lệnh ```print``` ở trên có lẫn cả biến đã khai báo (x, y, z) và cả các hằng số ('+', '='), cách viết này sẽ khiến người mới biết về lập trình hơi khó hiểu, nhưng đó là cách được sử dụng rất phổ biến trong tất cả các ngôn ngữ lập trình.

Thực chất, chương trình ở trên tương đương với:

```python
x = 1
y = 2
x = 3
plus_sign = '+'
equal_sign = '='
print(x, plus_sign, y, equal_sign, z)
```

Như vậy, lệnh ```print``` sẽ in ra các biến theo thứ tự : x, plus_sign, y, equal_sign, z.
Do vậy bạn sẽ nhìn thấy trên màn hình kết quả :
	1 + 2 = 3

Dần dần bạn sẽ quen với cách viết ```print``` ở trên để đưa kết quả ra màn hình.

