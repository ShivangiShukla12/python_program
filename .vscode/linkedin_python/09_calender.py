

import calendar

# create a plain text calendar

def main():
    c =calendar.TextCalendar(calendar.SUNDAY) # to start calendar from SUNDAY similarly MONDAY, TUESDAY..
    st = c.formatmonth(2021,2,0,0)
    print (st)

 #create an HTML formatted calendar
    hc = calendar.HTMLCalendar(calendar.SUNDAY)
    st = hc.formatmonth(2017,1)
    print (st)
# loop over the days of a month
# zeroes means that the day of the week belongs to previous or next month

    for i in c.itermonthdays(2071,8):
        print(i)
# calendar module provides utilities for the given locale
#such as the names of the days and months in both full and abbreviated forms
    for name in calendar.month_name:
        print(name)
    
    for days in calendar.day_name:
        print(days)
    
    for name in calendar.month_abbr:
        print(name)
    
    for days in calendar.day_abbr:
        print(days)

# calculate days based on rule for eg:-
# a tem meeting on the first Friday of every month
# to figure out what days that would be for each month
# we can use this script

    print("Team meeting  will be on: ")
    for m in range(1, 13):
        cal = calendar.monthcalendar(2018,m)
        #print(cal)
        weekone = cal[0]
        weektwo = cal[1]
        # print(weekone[calendar.FRIDAY])
        # print(calendar.FRIDAY)

        if weekone[calendar.FRIDAY] != 0:
            meetday = weekone[calendar.FRIDAY]
        else:
            meetday = weektwo[calendar.FRIDAY]
        
        print("%10s %2d" %(calendar.month_name[m], meetday))

        


if __name__ == "__main__":
    main()