from datetime import datetime, timedelta
from collections import defaultdict, OrderedDict

Andrii_birthday = datetime(year=1991,month=5,day=3)
Kate_birthday = datetime(year=1992,month=6,day=15)
Vlada_birthday = datetime(year=2005,month=9,day=20)
Mark_birthday = datetime(year=1993,month=8,day=27)
Valeriya_birthday = datetime(year=1998,month=8,day=23)
test_birthday = datetime(year=2022,month=11,day=9)
test_birthday_s = datetime(year=2022,month=11,day=8)
test_birthday_2 = datetime(year=2022,month=11,day=6)
test_birthday_3 = datetime(year=2022,month=11,day=5)
test_birthday_4 = datetime(year=2022,month=11,day=7)
test_birthday_5 = datetime(year=2022,month=11,day=10)
curent_datetime = datetime.now()

delta = timedelta(days=7)
difference_week = curent_datetime + delta
# print(delta)

users = [{
    'Andrii': Andrii_birthday,
    'Kate': Kate_birthday,
    'Vlada' : Vlada_birthday,
    'Mark': Mark_birthday,
    'Valeriya': Valeriya_birthday,
    'test_birthday': test_birthday,
    'test_birthday_s': test_birthday_s,
    'test_birthday_2': test_birthday_2,
    'test_birthday_3': test_birthday_3,
    'test_birthday_4': test_birthday_4,
    'test_birthday_5': test_birthday_5,

}]

def b_d_function(lst):

    for item in users:
        grouped = defaultdict(list)
        d = OrderedDict(grouped)
        for key, val in item.items():

            if curent_datetime <= val <= difference_week:
                if val.weekday() == 5 or val.weekday() == 6:
                    char = 'Monday'
                    grouped[char].append(key)
                    # print(grouped)

                    # dic.append(key)
                    # string = ', '.join(dic)

                    # print(f'Monday: {string}')
                    # print(c)
                    # print(f'Monday: {string}')
                else:
                    char = val.strftime('%A')
                    grouped[char].append(key)
                    # print(grouped)

                    # dicto.append(key)
                    # stringo = ', '.join(dicto)
                    # week_day = val.strftime('%A')
                    # print(f'{week_day}: {stringo}')
            else:
                continue
        try:
            d = OrderedDict(grouped)
            d.move_to_end('Tuesday')
            d.move_to_end('Wednesday')
            d.move_to_end('Thursday')
            d.move_to_end('Friday')
            d.move_to_end('Saturday')
            d.move_to_end('Sunday')


        except KeyError as r:
            pass



        for k,v in d.items():
            val = ', '.join(v)
            print(f'{k}: {val}')

b_d_function(users)


