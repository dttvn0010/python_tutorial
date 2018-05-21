day_of_week = ['Thứ hai', 'Thứ ba', 'Thứ tư', 'Thứ năm', 'Thứ sáu', 'Thứ bảy', 'Chủ nhật']
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def get_day_of_week(date, month, year):
    year -= 2000    
    days_since_2000 = (year//4) * (365*4+1) + 5
    days_since_2000 += (year%4) * 365
   
    for x in range(month-1):
        days_since_2000 += days_in_month[x]

    days_since_2000 += date-1
    
    if year%4 != 0 or month > 2:
        days_since_2000 += 1

    return day_of_week[days_since_2000%7]

print(get_day_of_week(21, 5, 2018))
    
