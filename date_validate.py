days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

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

day_in_month = days_in_month[month-1]

if month == 2 and year%4 == 0:
    day_in_month += 1

if date <= day_in_month:
    print('Tồn tại ngày này')
else:
    print('Không tồn tại ngày này')


