# givens
day_of_week = 1
day = 1
month = 1
year = 1900
day_names = ['Sun', 'Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat']

count = 1

def check(dow, day, year):
    start_year = 1901
    end_year = 2000
    if year in range(start_year, end_year):
        if dow == 0 and day == 1:
            return True
    return False

def dow(current_dow):
    if current_dow == 6:
        return 0
    else:
        current_dow+=1
        return current_dow

def days_in_month(month, year):
    
    if month in [4,6,9,11]:
        day_lim = 30
    elif month in [2]:
        if year % 100 == 0:
            if year % 400 == 0:
                day_lim = 29
            else:
                day_lim = 28
        elif year % 4 == 0:
            day_lim = 29
        else:
            day_lim = 28
    else:  
        day_lim = 31
    
    return day_lim

while not year > 2000:
    month = 1
    
    while not month > 12:
        day = 1
        days = days_in_month(month, year)
        
        while not day > days:
            if check(day_of_week, day, year):
                count += 1
                #print '%d/%d/%d' % (month, day, year)
            #print day_names[day_of_week], '%d/%d/%d' % (month, day, year)
            day_of_week = dow(day_of_week)
            day+=1
        
        month+=1
    
    year+=1    
    

print '# of sundays that fall on first of the month = ', count