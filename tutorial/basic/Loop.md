## Lệnh lặp

Trong lập trình, nhiều lúc chúng ta muốn thực hiện một công việc nào đó lặp lại nhiều lần. Các lệnh lặp sẽ giúp chúng ta thực hiện điều đó.

### Lệnh lặp for:
Lệnh ```for``` được dùng để thực hiện một vòng lặp với số lần lặp biết trước. Cấu trúc lệnh này như sau:

```python
for bienLap in tapGiaTri:
    <khoi_lenh>
```
Các thành phần của vòng lặp ```for```:
 - Tập giá trị : chứa tập giá trị cần duyệt qua
 - Biến lặp : biến được gán giá trị từ mỗi phần tử trong tập giá trị lặp
 - Khối lênh lặp : khối lệnh cần thực hiện lặp lại

Như vậy cấu trúc ```for``` ở trên có nghĩa : với mỗi giá trị ```bienLap``` của ```tapGiaTri```, thực hiện khối lệnh ```<khoi_lenh>```

Các cách biểu diễn tập giá trị lặp thông dụng:
 - Liệt kê các thành phần. Ví dụ [1, 2, 3, 4, 5]. Đây thực chất là dữ liệu kiểu danh sách mà chúng ta sẽ biết ở các phần sau.
 - Khoảng ```range(end)``` : bao gồm các số tự nhiên từ 0 đến trước ```end```. Lưu ý, với Python (và nhiều ngôn ngữ lập trình), khoảng này không chứa giá trị ```end```, tức giá trị cuối của khoảng là ```end-1```
 - Khoảng ```range(start, end)``` bao gồm các số nguyên bắt đầu từ ```start``` đến trước ```end```. 
 - Khoảng ```range(start, end, increment)```  bao gồm các số nguyên từ ```start``` đến trước ```end``` và tăng đều theo khoảng cách ```increment```

Ví dụ:
 - range(5) gồm : 0, 1, 2, 3, 4
 - range(1, 5) gồm : 1, 2, 3, 4
 - range(0, 10, 2)  gồm : 0, 2, 4, 6, 8

Chúng ta sẽ xem xét một số chương trình ví dụ sau.

### Ví dụ

#### Ví dụ 1
Tính tổng các số nguyên từ 1 đến 100

Lời giải:

```python
S = 0
for i in range(1, 101):
    S += i

print('S = ', S)
```

Như chúng ta biết ở trên, khoảng ```range(start, end)``` bao gồm các số từ ```start``` đến ```end-1```, do đó để thể hiện các số từ 1 đến 100 chúng ta phải dùng ```range(1, 100)```

#### Ví dụ 2
Tính tổng:

```S = 1/(1*2) + 1/(2*3) + 1/(3*4) + ... + 1/(999*1000)```

Lời giải:

```python
S = 0
for i in range(1, 1000):
    S += 1/(i*(i+1))

print('S = ', round(S,6))
```
Bạn hãy kiểm tra xem kết quả có phải bằng ```1-1/1000``` không.

#### Ví dụ 3
Viết chương trình in ra bảng cửu chương.

Lời giải:
```python
for i in range(2, 10):
    for j in range(2, 10):
        print(i, '*', j, '=', i*j)

    print()
```

### Lệnh lặp while:
Lệnh lặp ```while``` dùng để thực hiện một vòng lặp với số lần lặp không biết trước. Cấu trúc lệnh này như sau:

```python
while dieukien:
    <khoi_lenh>
```

Cấu trúc trên có nghĩa : Chừng nào điều kiện ```dieukien``` còn đúng thì thực hiện khối lệnh ```khoi_lenh```.

### Ví dụ

#### Ví dụ 1
Kiểm tra số 8477216359 có phải số nguyên tố không.

Lời giải:

Để kiểm tra một số có phải số nguyên tố hay không, chúng ta cần kiểm tra số đó có chia hết cho số nguyên tố nào trong phạm vi từ 2 đến căn bậc 2 của số đó hay không. Tuy nhiên do chúng ta không có danh sách các số nguyên tố, chúng ta có thể dùng cách kiểm tra số đó có chia hết cho số tự nhiên nào từ 2 đến căn bậc 2 của số đó không.

Chương trình Python:

```python
x = 8477216359

i = 2
while i * i <= x:
    if x % i == 0:
        j = x // i
        print(x, '=', i , '*', j)
        exit()
    i += 1

print(x, ' là số nguyên tố')
```

#### Ví dụ 2
Chương trình đoán số tự nhiên.

Bạn hãy nghĩ trong đầu một số trong phạm vi từ 0 đến 1000. Máy tính sẽ đưa ra các câu hỏi, với mỗi câu bạn chỉ cần trả lời câu đó là đúng hay sai. 
Sau không quá 10 câu hỏi máy tính sẽ đưa ra số bạn đang nghĩ là gì.

```python
low = 0
high = 1000

print('Bạn hãy nghĩ một số trong phạm vi từ 0 đến 1000, sau đó trả lời các câu hỏi sau.')

while low + 1 != high:
    mid = (low + high) // 2
    a = input('Số đó lớn hơn ' + str(mid)  + ' ? (Y/N) : ')
    
    if a == 'Y':
        low = mid
    else:
        high = mid

print('Số bạn nghĩ là ', high)
```
   
Giải thích:
- Chương trình trên dựa trên thuật toán tìm kiếm nhị phân. Máy tính đã biết số bạn đang nghĩ nằm trong khoảng từ 0 đến 1000, do đó đặt ra 2 giá trị ```low = 0``` và ```high = 1000``` để giới hạn khoảng giá trị của số bạn nghĩ. 
 - Ở mỗi bước, máy tính tính giá trị chính giữa của khoảng giá trị ```mid = (low+high)//2```, sau đó hỏi bạn số bạn nghĩ có lớn hơn điểm giữa đó không. Dựa vào câu trả lời của bạn, máy tính sẽ thu hẹp khoảng giá trị chứa số bạn nghĩ.
 - Sau mỗi câu hỏi, khoảng giá trị chứa số bạn nghĩ sẽ bị thu hẹp đi một nửa. Vì ban đầu khoảng này có độ rộng là 1000, nhỏ hơn 2 mũ 10 (1024), nên sau không quá 10 câu hỏi, độ rộng khoảng này sẽ thu về 1 và máy tính sẽ xác định được số bạn đang nghĩ là bao nhiêu. Điều kiện ```low + 1 != high``` là điều kiện giúp máy tính kiểm tra khoảng giá trị đã thu về 1 điểm hay chưa.

[Tiếp theo](String.md)
