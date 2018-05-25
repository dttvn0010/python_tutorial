# Lập trình Python cơ bản

## Lập trình là gì?
Bạn có thể chưa cần quan tâm đến định nghĩa lập trình một cách chính xác, để đơn giản hãy tạm hiểu đó là cách giải các bài toán bằng cách viết các chương trình trên máy tính

Trước đây, khi chưa có máy tính, con người vẫn thực hiện giải các bài toán gặp phải trong cuộc sống, phương thức thực hiện là qua giấy và bút, giống như cách chúng ta vẫn làm bài tập toán khi đi học.

Bài toán đơn giản nhất mà chúng ta bắt đầu làm ở tiểu học là các bài toán có một phép tính. Chúng ta thử xem xét một ví dụ sau:
   
  - An và Bình là 2 anh em. Tuổi của An là 10, Bình kém An 2 tuổi. Hỏi Bình bao nhiêu tuổi.

Lời giải của bài toán này, giống như khi chúng ta làm ở lớp 1 như sau:
   - Tuổi của Bình là:
       10 - 2 = 8 (tuổi)

Với bài toán này chúng ta chỉ cần làm một phép tính. Trên thực tế, các bài toán sẽ gồm nhiều phép tính, hay nhiều bước, kết quả của bước này sẽ được dùng để tính toán cho bước tiếp theo. Chúng ta hãy xem xét bài toán sau:
  - Năm nay An 10 tuổi. Bình Kém An 2 tuổi. Tuấn hơn Bình 4 tuổi. Hỏi Tuấn bao nhiêu tuổi.

Với bài toán này, chúng ta phải thực hiện 2 phép tính (2 bước). Đầu tiên, phải tính tuổi của Bình, sau đó từ tuổi của Bình tính ra tuổi của Tuấn.
   - Tuổi của Bình là:
      10 - 2 = 8 (tuổi)
   - Tuổi của Tuấn là:
      8 + 4 = 12 (tuổi)

Đó là cách chúng ta vẫn giải toán trên giấy. Nếu sử dụng máy tính, cách thức giải cũng tương tự như vậy, tức là cũng gồm các bước nối tiếp nhau, kết quả bước trước được dùng làm đầu vào để tính kết quả cho bước tiếp theo.

Ví dụ trên, nếu dùng  ngôn ngữ lập trình Python trên máy để giải sẽ như sau:

```python
tuoiAn = 10
tuoiBinh = tuoiAn - 2
tuoiTuan = tuoiBinh + 4
print('Tuổi của Tuấn là : ', tuoiTuan)
```

Bạn hãy copy nội dung trên vào cửa sổ soạn thảo chương trình của Python, sau đó chạy chương trình để xem kết quả. Nếu chưa cài đặt hay chưa biết cách chạy chương trình Python, bạn có thể  chạy thử chương trình tại website : https://repl.it/site/languages/python

[Tiếp theo](Variable.md)
