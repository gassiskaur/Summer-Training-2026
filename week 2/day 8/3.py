class User:
    def __init__(self):
        print('self:' ,self, type(self))

user1 = User()
user2 = User()

print('user1: ', user1, id(user1))
print('user2: ',user2, id(user2))
print('variables in user1: ', vars(user1))
print('variables in user2 : ', vars(user2))


user3= user1
print('user3: ',user3, id(user3))



user1.name = 'John'
user2.full_name = 'Fionna Flynn'
user3.age = 20
user2.age = 25
user3.email = 'john@example.com'


