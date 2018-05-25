## Kiểu dữ liệu
Mỗi biến số sau khi được khai báo sẽ chứa giá trị nhất định, chúng ta gọi là các dữ liệu. Mỗi giá trị dữ liệu này sẽ thuộc vào một trong các kiểu dữ liệu mà Python hỗ trợ.

Nếu giải các bài toán trong cuộc sống, chúng ta ít quan tâm đến kiểu dữ liệu, vì giá trị của các biến số luôn là các con số. Trên máy tính, ngoài dữ liệu kiểu số (vốn là kiểu dữ liệu thông dụng nhất), còn có dữ liệu kiểu văn bản. Một số loại biến số dùng kiểu dữ liệu này là tên, địa chỉ, số điện thoại ...

Ngoài ra trong Python còn có các kiểu dữ liệu khác mà chúng ta sẽ làm quen dần ở các phần sau, đó là :
  - Kiểu danh sách (List)
  - Kiểu nhóm (Tuple)
  - Kiểu tập hợp (Set)
  - Kiểu từ điển (Dictionary)

Chúng ta tạm quan tâm tới 2 kiểu dữ liệu chính là kiểu số và kiểu văn bản.

Dữ liệu kiểu số là loại dữ liệu phổ biến nhất, và cũng là kiểu dữ liệu chúng ta dùng trong các bài toán hàng ngày.

```python
x = 1
y = 2
z = x + y
```

Với Python (và với lập trình trên máy tính nói chung), dữ liệu kiểu số được chia thành 2 loại:
  - Kiểu số nguyên
  - Kiểu số thập phân

Lí do của việc chia này là việc tính toán trên số nguyên nhanh hơn tính toán với số thập phân, do đó trong các bài toán chỉ cần thao tác với các giá trị số nguyên thì ưu tiên dùng kiểu dữ liệu số nguyên để tăng tốc độ tính toán. Tuy nhiên ngày nay, tốc độ tính toán của máy tính với 2 kiểu dữ liệu trên đều rất nhanh, do đó bạn có thể không cần quan tâm đến sự khác biệt của 2 loại này, và sử dụng kiểu số thập phân chung cho tất cả các giá trị số.

Với kiểu số thập phân, cách khai báo trong Python như sau:

```python
x = 1.2
y = 0.0001
z = 1.7e6
```

Ngoài kiểu viết số thập phân thông dụng như chúng ta quen dùng (phần nguyên + dấu chấm + phần thập phân), thì chúng ta có thể dùng cách viết mà các nhà toán học hay sử dụng, đó giá trị đi kèm số mũ trong hệ số 10. Ở ví dụ trên, giá trị của ```z``` bằng 1.7e6, tức là bằng 1.7 nhân với 10 mũ 6, tức bằng 1700000

Kiểu dữ liệu phổ biến thứ 2 trong Python là kiểu văn bản, hay những người lập trình thường gọi là xâu (String). Cú pháp khai báo một biến kiểu văn bản trong Python như sau:

```python
hoten = 'Nguyễn Văn An'
diachi = "Hà Nội"
```

Giá trị của một biến kiểu văn bản được đặt trong 2 kí tự nháy đơn '', hoặc 2 kí tự nháy kép "".
Ngoài ra nếu văn bản gồm nhiều dòng, giá trị văn bản sẽ được mở đầu và kết thúc bằng 3 kí tự nháy kép """, ví dụ

```python
text = """ 
 Cộng hòa xã hội chủ nghĩa Việt Nam
    Độc lập - Tự do - Hạnh phúc
"""
```

Chúng ta sẽ tìm hiểu về các phép tính xử lý kiểu dữ liệu văn bản ở các phần sau.

[Tiếp theo](Input_Output.md)
