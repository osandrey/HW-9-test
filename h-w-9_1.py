
user_dict = {}
res = 1

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






def proceed():


    try:
        comand, comand_name, user_input = parser_comands()

        if comand_name == 'hello':

            hello_function()

        elif comand_name == 'add':
            result = comand(user_input, user_dict)
            return result
        elif comand_name == 'change':

            result = comand(user_input, user_dict)
            return result
        elif comand_name == 'phone':

            result = comand(user_input, user_dict)
            return result
        elif comand_name == 'showall':

            result = comand(user_dict)
            return result
        elif comand_name in ['goodbye', 'close', 'exit']:

            return good_bye_function()
    except TypeError:
        print('Command Not Found')
    except IndexError:
        print('Value Not Found, Please Use commands carrifuly.')



def hello_function():
    print('How can I help you?')



def add_func(user_input, user_dict):
    user_name = user_input[1]
    user_phone_numb = user_input[2]
    user_dict[user_name] = user_phone_numb
    print(f'Added to list: {user_name}, {user_phone_numb}')
    return user_name, user_phone_numb

def change_function(user_input, user_dict):
    user_name = user_input[1]
    user_phone_numb = user_input[2]
    user_dict[user_name] = user_phone_numb
    print(f'User: {user_name} number changed to: {user_phone_numb}')
    return user_name, user_phone_numb

def phone_function(user_input, user_dict):
    user_name = user_input[1]
    user_phone_number = user_dict[user_name]
    print(f'User:{user_name}, Phone number: {user_phone_number}')
    return user_phone_number

def show_all_function(user_dict):

    for k, v in user_dict.items():

        print(k.title(), v)



def good_bye_function():
    print('Good bye!')
    global res
    res = False
    return res





def main():
    global res
    while res:
        proceed()




print(main())
