class User:
    
    def __init__(self, kuchbhi, phone, email, age, gender, address):
        
        self.name = kuchbhi
        self.phone = phone
        self.email = email
        self.age = age
        self.gender = gender
        self.address = address


user1 = User(kuchbhi='John', 
             phone='+91 99990 11110', 
             email='john@example.com',
             age=20,
             gender='male',
             address='redwood shores')

user2 = User(kuchbhi='Fionna', 
             phone='+91 99991 11111', 
             email='fionna@example.com',
             age=21,
             gender='female',
             address='country homes')


user3 = user1
print('user1:', user1, vars(user1))
print('user2:', user2, vars(user2))
print('user3:', user3, vars(user3))