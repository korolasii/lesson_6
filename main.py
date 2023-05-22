import string

def check_pasword(password):
    password_characters = {
        'lowwer': [],
        'upper': [],
        'number': [],
        'simbol': [],
        'invalid_sibol': []
    }
    error_dict = {
        'errors': []
    }
    if len(password) >= 8 and len(password) <= 12: 
        for i in password:
            if i in string.ascii_lowercase:
                password_characters['lowwer'].append(i)
            elif i in string.ascii_uppercase:
                password_characters['upper'].append(i)
            elif i in string.digits:
                password_characters['number'].append(i)
            elif i in '«*-#»;':
                password_characters['simbol'].append(i)
            else:
                password_characters['invalid_sibol'].append(i)
                error_dict['errors'].append(f'In password invalid character "{i}"')
        if len(password_characters['simbol']) > 0 and len(password_characters['upper']) > 0 and len(password_characters['lowwer']) > 0 and len(password_characters['number']) > 0 and len(password_characters['invalid_sibol']) == 0:
            return 'Password is good'
        if len(password_characters['simbol']) == 0:
            error_dict['errors'].append('In password no simbol')
        if len(password_characters['upper']) == 0:
            error_dict['errors'].append('In password no upper letter')
        if len(password_characters['lowwer']) == 0:
            error_dict['errors'].append('In password no lowwer letter')
        if len(password_characters['number']) == 0:
            error_dict['errors'].append('In password no number')
        return error_dict
    elif len(password) < 8:
        return 'Few characters'
    else:
        return 'Many characters'
        
    

if __name__ == '__main__':
    password = input('Write your password: ')
    return_check = check_pasword(password)
    if return_check == 'Password is good' or return_check == 'Few characters' or return_check == 'Many characters':
        print(return_check)
    else:
        print(return_check)
