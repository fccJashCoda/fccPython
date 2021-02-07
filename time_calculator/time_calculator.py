def add_time(start, duration, day=None):

    start_time, period = start.split(" ")
    start_hour, start_minutes = start_time.split(":")
    added_hours, added_minutes = duration.split(":")

    current_day = None
    new_hour = None
    new_minutes = None
    days_passed = None
    new_time = None

    start_hour = int(start_hour)
    start_minutes = int(start_minutes)
    added_hours = int(added_hours)
    added_minutes = int(added_minutes)

    # convert start hour to military time by adding 12 hours if period is "PM"
    if period == 'PM':
        start_hour += 12

    # add minutes and check if tehy add up to an hour ( > 59)
    new_minutes = start_minutes + added_minutes
    if new_minutes > 59:
        new_minutes = new_minutes % 60
        added_hours += 1

    # add hours and check if a day has passed
    new_hour = start_hour + added_hours
    if new_hour > 23:
        days_passed = new_hour // 24
        new_hour = new_hour % 24

    # check if time is AM or PM and convert back to a 12 hour cycle
    if new_hour > 11:
        period = "PM"
        new_hour = new_hour % 12
    else:
        period = "AM"

    # format the hour to display the correct time
    if new_hour == 0:
        new_hour = 12

    # get the current day if necessary
    if day:
        current_day = get_current_day(day, days_passed)
    # format the way days are displayed if necessary
    if days_passed:
        days_passed = format_days_passed(days_passed)

    # build the new time string
    new_time = f"{str(new_hour)}:{str(new_minutes).rjust(2, '0')} {period}{', ' + current_day if current_day else ''}{' ' + days_passed if days_passed else ''}"

    return new_time


def format_days_passed(days_passed):
    tag = None
    if days_passed > 1:
        tag = f"({days_passed} days later)"
    elif days_passed == 1:
        tag = '(next day)'

    return tag


def get_current_day(day, num_days_passed=None):
    current_day = None
    added_days = num_days_passed if num_days_passed else 0
    index_of_day = None

    days_of_the_week = ['monday', 'tuesday', 'wednesday',
                        'thursday', 'friday', 'saturday', 'sunday']

    index_of_day = (days_of_the_week.index(day.lower()) + added_days) % 7
    current_day = days_of_the_week[index_of_day].capitalize()

    return current_day
