def is_leap(year:int):
    """Checks if a given year is a leap year"""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                # return "Leap year"
                return True
            else:
                # return "Not leap year"
                return False
        else:
            # return "Leap year"
            return True
    else:
        # return "Not leap year"
        return False

# Add more code here 👇
def days_in_month(y:int, m:int):
    """Returns the number of days in a month for a given year. References isLeap()"""

    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(y):
        month_days[1] += 1
    list_month = m-1
    return month_days[list_month]


# 🚨 Do NOT change any of the code below
# year = int(input())  # Enter a year
# month = int(input())  # Enter a month
year = 2020
month = 2
days = days_in_month(year, month)
print(days)