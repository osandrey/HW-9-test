

user_dict = {}

#'''def user input'''
while True:
    user_input = input('Enter the comand:')
    user_input.strip('\n')
    user_input = user_input.split(' ')
    comand = user_input[0].lower()

# '''handler_comands'''

    if comand == 'hello':
        print('How can I help you?')
    elif comand == 'add':
        user_name = user_input[1].lower()
        user_phone_number = user_input[2].lower()
        user_dict[user_name] = user_phone_number

        print(f'Command: {comand}, Username: {user_name}, Phone: {user_phone_number}')

    elif comand == 'change':
        user_name = user_input[1].lower()
        new_user_phone_number = user_input[2].lower()
        user_dict[user_name] = new_user_phone_number
        print('Changed to', new_user_phone_number)

    elif comand == 'phone':
        user_name = user_input[1].lower()
        user_phone_number = user_dict[user_name]

        print(f'{user_name.title()} number is {user_phone_number}')

    elif comand == 'show':
        for k,v in user_dict.items():

            print(k.title(),v)

    elif comand in ['good', 'close', 'exit']:
        print('Good bye!')
        break


# '''Main (Цикл запит-відповідь
# отримання від користувача даних та
# повернення користувачеві відповіді
# від функції-handlerа.)'''