class InvalidDateException(Exception):
    pass

class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
        self.validate_date()

    def validate_date(self):
        if self.month < 1 or self.month > 12:
            raise InvalidDateException("Month must be between 1 and 12.")
        if self.day < 1 or self.day > 31:
            raise InvalidDateException("Day must be between 1 and 31.")
        if self.month in [4, 6, 9, 11] and self.day == 31:
            raise InvalidDateException("This month has only 30 days.")
        if self.month == 2:
            if self.is_leap_year(self.year):
                if self.day > 29:
                    raise InvalidDateException("February has only 29 days in a leap year.")
            else:
                if self.day > 28:
                    raise InvalidDateException("February has only 28 days.")

    def is_leap_year(self, year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    def display_date(self):
        print(f"Date: {self.day:02d}/{self.month:02d}/{self.year}")

# Accept date from user
try:
    day = int(input("Enter day: "))
    month = int(input("Enter month: "))
    year = int(input("Enter year: "))
    date = Date(day, month, year)
    date.display_date()
except InvalidDateException as e:
    print(e)
except ValueError:
    print("Please enter valid integers for day, month, and year.")
