
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta
import calendar

def main():
    ## DATE OBJECTS
    # Get today's date from the simple today() method from the date class
    today = date.today()
    print ("Today's date is ", today)
    
    # print out the date's individual components
    print ("Date Components: ", today.day, today.month, today.year)
    
    # retrieve today's weekday (0=Monday, 6=Sunday)
    print ("Today's Weekday #: ", today.weekday())
    days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
    print ("Which is a " + days[today.weekday()])
    
    ## DATETIME OBJECTS
    # Get today's date from the datetime class
    today = datetime.now()
    print  ("The current date and time is ", today)
    
    # Get the current time
    t = datetime.time(datetime.now())
    print ("The current time is ", t)
    
    # Times and dates can be formatted using a set of predefined string
    # control codes 
    now = datetime.now() # get the current date and time
    
    #### Date Formatting ####
    
    # %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month
    print (now.strftime("The current year is: %Y")) # full year with century
    print (now.strftime("%a, %d %B, %y")) # abbreviated day, num, full month, abbreviated year
    
    # %c - locale's date and time, %x - locale's date, %X - locale's time
    print (now.strftime("Locale date and time: %c"))
    print (now.strftime("Locale date: %x"))
    print (now.strftime("Locale time: %X"))
    
    #### Time Formatting ####
    
    # %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
    print (now.strftime("Current time: %I:%M:%S %p")) # 12-Hour:Minute:Second:AM
    print (now.strftime("24-hour time: %H:%M")) # 24-Hour:Minute
    
    
        # construct a basic timedelta and print it
    print (timedelta(days=365, hours=5, minutes=1))

    # print today's date
    now = datetime.now()
    # print ("today is: " + str(now))

    # print today's date one year from now
    # print ("one year from now it will be: " + str(now + timedelta(days=365)))

    # create a timedelta that uses more than one argument
    # print ("in two weeks and 3 days it will be: " + str(now + timedelta(weeks=2, days=3)))

    # calculate the date 1 week ago, formatted as a string
    t = datetime.now() - timedelta(weeks=1)
    s = t.strftime("%A %B %d, %Y")
    print ("one week ago it was " + s)

    ### How many days until April Fools' Day?

    today = date.today()  # get today's date
    afd = date(today.year, 4, 1)  # get April Fool's for the same year
    # use date comparison to see if April Fool's has already gone for this year
    # if it has, use the replace() function to get the date for next year
    if afd < today:
        print ("April Fool's day already went by %d days ago" % ((today-afd).days))
        afd = afd.replace(year=today.year + 1)  # if so, get the date for next year

    # Now calculate the amount of time until April Fool's Day  
    time_to_afd = afd - today
    print ("It's just", time_to_afd.days, "days until next April Fools' Day!")

    c = calendar.TextCalendar(calendar.SUNDAY)
    str = c.formatmonth(2022, 1, 0, 0)
    print (str)

    # create an HTML formatted calendar
    hc = calendar.HTMLCalendar(calendar.SUNDAY)
    str = hc.formatmonth(2022, 1)
    print (str)

    # loop over the days of a month
    # zeroes mean that the day of the week is in an overlapping month
    for i in c.itermonthdays(2022, 8):
        print (i)
      
    # The Calendar module provides useful utilities for the given locale,
    # such as the names of days and months in both full and abbreviated forms
    for name in calendar.month_name:
        print (name)

    for day in calendar.day_name:
        print (day)

    # Calculate days based on a rule: For example, consider
    # a team meeting on the first Friday of every month.
    # To figure out what days that would be for each month,
    # we can use this script:
    print ("Team meetings will be on:")
    for m in range(1,13):
        # returns an array of weeks that represent the month
        cal = calendar.monthcalendar(2022, m)
        # The first Friday has to be within the first two weeks
        weekone = cal[0]
        weektwo = cal[1]
      
        if weekone[calendar.FRIDAY] != 0:
            meetday = weekone[calendar.FRIDAY]
        else:
          # if the first friday isn't in the first week, it must be in the second
            meetday = weektwo[calendar.FRIDAY]
          
        print ("%10s %2d" % (calendar.month_name[m], meetday))  

      
  
if __name__ == "__main__":
    main()
  