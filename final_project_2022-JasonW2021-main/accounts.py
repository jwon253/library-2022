import os

class Accounts:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def create_account_check(self, check):
        '''Checks if input contains certain characters'''
        username_input = self.username
        password_input = self.password

        check1 = 1
        check2 = 2
        hasSpecial = False
        hasAlpha = False
        hasNumber = False
        special_characters = "!@#$%^&*()-=_+,./<>?"
        if any(x in special_characters for x in password_input):
            hasSpecial = True

        for x in password_input:
            if x.isupper():
                hasAlpha = True
            if x.isnumeric():
                hasNumber = True

        if (username_input.isalpha() or (username_input.isalpha() or username_input.isdigit)) and len(username_input) > 2: 
            check1 = 0

            if (hasAlpha and hasNumber and hasSpecial):
                check2 = 0

            else:
                check = 2
        else:
            check = 2
            return check

        if check1 == 0 and check2 == 0:
            acc_file = open(username_input, 'w')
            acc_file.write(username_input + '\n')
            acc_file.write(password_input + '\n')
            acc_file.close()
            check = 0
            return check

        else:
            check = 3
            return check 

    def admin_ui_info(self):
        '''Check if input matches admin'''
        username_admin = 'Admin'
        password_admin = 'Admin1!'
        username_input = self.username
        password_input = self.password
        if (str(username_input) == username_admin and str(password_input) == password_admin):
            check = 3
            return check
        else:
            check = 0
            return check

    def login_check(self, check):
            '''Checks if the inputs matchs a existing user'''
            username_input = self.username
            password_input = self.password

            user_files = os.listdir()
            if username_input in user_files:
                acc_file = open(username_input, 'r')
                validate = acc_file.read().splitlines()
                check = 8

                if password_input == '':
                    check = 1
                    return check
                
                if password_input in validate:
                    check = 2
                    admin_check = self.admin_ui_info()
                    return check + admin_check

                else:
                    check = 6
                    return check
            else:
                check = 7
                return check