import hashlib 



class User:
    def __init__(self,name=None,phone=None,email=None,password=None):
        self.name=name,
        self.phone=phone,
        self.email=email,
        self.password=password

    def input_details(self):
        self.name= input('Enter your name: ')
        self.phone= input('Enter your phone: ')
        self.email= input('Enter your email: ')
        self.password= input('Enter your password: ')
        self.password = self.encrypt(self.password)

    def show(self):
        print('~'*20)
        print('USER DETAILS:')
        print('Name: ',self.name)   
        print('Phone: ',self.phone)   
        print('E-mail: ',self.email)
        print('~'*20)


    def to_csv(self):
        return f'{self.name},{self.phone},{self.email},{self.password}\n'
    
    def to_dictionary(self):
        return vars(self)      


    def encrypt(self, data):
        #sha256 is one way decryption, passwords cannot be decrypted
        hash_data = hashlib.sha256(data.encode()).hexdigest()
        return hash_data


