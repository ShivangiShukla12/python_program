from datetime import date
from datetime import time
from datetime import datetime

def main():

# Get today's date from today() method
    today = date.today()
    print("Today's date is:",today)

# print out the date's individual componennt
    print("Date component", today.day, today.month, today.year)

# retrive today's weekday
    print("Today's weekday # is:", today.weekday())
    days = ["Mon", "Tues", "Wed", "Thrus", "Fri", "Sat", "Sun"]
    print("Which is a:", days[today.weekday()])

# get today's date from dateTime class
    today_date = datetime.now()
    print("Current date and time:", today_date)

# Get current time
    today_time = datetime.time(datetime.now())
    print("Current time:", today_time)

# Time and date can be formatted using a set of predefined string control codes
    now = datetime.now()

# %y/%Y - year, %a/%A - weekday, %b/%B - month, %d - day of month(date)
    print(now.strftime("The current year is: %Y"))
    print(now.strftime("%a, %d, %B, %Y"))

# %c - locale's date and time, %x - locale's date, %X - locale's time
    print(now.strftime("Locale date and time: %c"))
    print(now.strftime("Locale date: %x"))
    print(now.strftime("Locale time: %X"))


# %I/%H -12/24 Hour, %M - minutes, %S - second, %p - locale's AM/PM
    print(now.strftime("Current time: %I:%M:%S %p"))
    print(now.strftime("24-Hour time: %H:%M"))

if __name__ == "__main__":
    main()