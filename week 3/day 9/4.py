
class User:

    '''def __init__(self, name=None, phone=None, email=None):
        self.name = name
        self.phone = phone
        self.email = email
        print('[User] [init] User Object Constructed', self)'''

#inputing user values with constructor:

    '''def __init__(self, name=input('enter name: '), 
                 phone=input('enter phone: '), 
                 email= input('enter email: ')):
        pass
'''


    def input_user_details(self):
        self.name = input('Enter Name: ')
        self.phone = input('Enter Phone: ')
        self.email = input('Enter Email: ')

    def show_user_details(self):
        print('~~~~~~~~~~~~~~~~~~~~~~~')
        print(self.name, self.phone, self.email)
        print('~~~~~~~~~~~~~~~~~~~~~~~')


user1 = User()
print(vars(user1))

print(vars(User))