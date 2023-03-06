passwords = {
    'acebook' : {'password' : 'password123', 'added on' : '22/03/22'},
    'makersbnb' : {'password' : 'qwerty789', 'added on' : '22/03/22'}
}

print(passwords['acebook'])

def are_all_passwords_long_enough(passwords):
    for i in passwords:
        if len(i['password']) > 7:
            return True
        return False
    

print(are_all_passwords_long_enough(passwords))