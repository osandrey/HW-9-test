
user_dict = {}


def parser_comands():
    user_input = input('Enter the comand:')
    user_input = user_input.split(' ')
    check_key = ''.join(user_input)
    check_key =check_key.lower()
    print(check_key)
    COMAND_LIST = {
        'hello': hello_function,
        'add': add_func,
        'change': change_function,
        'phone': phone_function,
        'showall': show_all_function,
        "goodbye": good_bye_function,
        "close": good_bye_function,
        "exit": good_bye_function
    }
    for key, val in COMAND_LIST.items():
        if check_key.startswith(key):
            comand = val
            comand_name = key
            print(comand)
            return comand, comand_name, user_input




def main():
    res = 1
    while res:
        parser_comands()
        def proceed(comand,comand_name, *args, **kwargs):

            if comand_name == 'hello':
                print('AAAAAAAAA')
                hello_function()

            elif comand_name == 'add':
                result = comand(*args, **kwargs)
                return result
            elif comand_name == 'change':

                result = comand(user_dict)
                return result
            elif comand_name == 'phone':

                result = comand(user_dict)
                return result
            elif comand_name == 'showall':

                result = comand(user_dict)
                return result
            elif comand_name in ['goodbye', 'close', 'exit']:
                nonlocal res
                res = 0
                return good_bye_function
        return proceed


def hello_function():
    print('How can I help you?')


def add_func(user_input, user_dict):
    user_name = user_input[1]
    user_phone_numb = user_input[2]
    user_dict[user_name] = user_phone_numb
    return user_name, user_phone_numb

def change_function(user_input, user_dict):
    user_name = user_input[1]
    user_phone_numb = user_input[2]
    user_dict[user_name] = user_phone_numb
    return user_name, user_phone_numb

def phone_function(user_input, user_dict):
    user_name = user_input[1]
    user_phone_number = user_dict[user_name]
    return user_phone_number

def show_all_function(user_dict):

    for k, v in user_dict.items():
        return k.title(), v


def good_bye_function():
    res = False
    return res




print(main())
