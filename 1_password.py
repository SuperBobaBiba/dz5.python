import re


def passwd (str):
    #str = input('Введите пароль:')
    while True:
        #Должен быть не менее 6 символов
        if len (str)<6:
            print ('пароль должен быть не менее 6 символов!')
            return False
        #Должен содержать хотя бы одну цифру
        elif re.search('[0-9]',str) is None:
            print ('пароль должен содержать хотя бы одну цифру!')
            return False
        #Не должен состоять только из цифр
        elif  str.isdigit():
            print ('пароль не должен состоять только из цифр!')
            return False
        #Не должен содержать слово “password” в любом регистре
        elif re.search('password',str, re.IGNORECASE):
            print ('пароль не должен содержать слово “password”!')
            return False
        print(True)
        break
passwd(input('Введите пароль:'))
