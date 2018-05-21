date = input('Ngày : ')
date = int(date)

month = input('Tháng : ')
month = int(month)

year = input('Năm : ')
year = int(year)

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


