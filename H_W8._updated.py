from datetime import datetime, timedelta



test_users = [
    {"name": "Tanya", "birthday": datetime(year=1992, month=9, day=23)},
    {"name": "Kostya", "birthday": datetime(year=1992, month=3, day=8)},
    {"name": "Serhiy", "birthday": datetime(year=1992, month=11, day=9)},
    {"name": "Sasha", "birthday": datetime(year=1994, month=11, day=10)},
    {"name": "Nastya", "birthday": datetime(year=1989, month=12, day=29)},
    {"name": "Vasya", "birthday": datetime(year=1986, month=11, day=14)},
    {"name": "Pasha", "birthday": datetime(year=1986, month=11, day=13)},
    {"name": "Pasha Padlo", "birthday": datetime(year=1986, month=11, day=12)},
    {"name": "I Ego Brat", "birthday": datetime(year=1986, month=11, day=13)},
    {"name": "Nezhdanchik", "birthday": datetime(year=1986, month=12, day=1)},
    {"name": "Olia", "birthday": datetime(year=1995, month=11, day=15)}
]




def get_birthdays_per_week(users):

    current_day = datetime.now()

    days_interval = define_days_interval(current_day)

    new_time_line = current_day + days_interval

    user_list = {
        "Monday": [],
        "Tuesday": [],
        "Wednesday": [],
        "Thursday": [],
        "Friday": []
    }

    for user in users:

        new_date_for_user = datetime(
            year=current_day.year,
            month=user.get('birthday').month,
            day=user.get('birthday').day
        )
        print(new_date_for_user)
        print('AAAA', current_day)
        print('BBBBBB',new_time_line)
        if current_day < new_date_for_user <= new_time_line:
            weekday_string = new_date_for_user.strftime("%A")
            print(user)
            if weekday_string in ['Saturday', 'Sunday']:
                weekday_string = 'Monday'
            user_list.get(weekday_string).append(user.get('name'))

    print_users_list(user_list)


def define_days_interval(current_day: datetime) -> timedelta:
    """
    Тут ми отримуємо інтервал наступних днів, враховуючи можливість запуску програми у вихідні дні.
    Тобто запустивши в сб- ми отримаємо нд лише поточного тижня.
    :param current_day: отримує об'єкт - поточну дату.
    :return: повертає об'єкт timedelta - интервал днів для котрих нам потрібні дати народження.
    """
    if current_day.weekday() == 5:
        days_interval = timedelta(days=6)
    elif current_day.weekday() == 6:
        days_interval = timedelta(days=5)
    else:
        days_interval = timedelta(days=7)

    return days_interval


def print_users_list(user_list):
    for key, value in user_list.items():
        if value != False:
            print(f"{key}: {', '.join(value)}")





get_birthdays_per_week(test_users)