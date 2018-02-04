from itertools import cycle


DAYS_OF_WEEK = [
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
    'Sunday',
]

MONTH_DAYS = [
    31,
    28,
    31,
    30,
    31,
    30,
    31,
    31,
    30,
    31,
    30,
    31
]

JAN_1_1900 = 'Monday'


def is_leap_year(year):
    """A leap year occurs on any year evenly divisible by 4,
    but not on a century unless it is divisible by 400.
    """
    return year % 4 == 0 and (not year % 100 == 0 or year % 400 == 0)


def days_in_month(month, year):
    if month == 2 and is_leap_year(year):
        return 29
    return MONTH_DAYS[month - 1]


def main():
    iter_days = cycle(DAYS_OF_WEEK)
    year = 1900
    month = 1
    day = 1
    day_name = next(iter_days)

    first_sundays = 0

    while year < 2001:
        if day == 1 and year >= 1901 and day_name == 'Sunday':
            first_sundays += 1

        day += 1
        day_name = next(iter_days)
        if day > days_in_month(month, year):
            day = 1
            if month == 12:
                month = 1
                year += 1
            else:
                month += 1

    return first_sundays


if __name__ == '__main__':
    print(main())
