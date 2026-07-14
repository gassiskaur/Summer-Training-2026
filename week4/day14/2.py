from DBHELPER1 import *
print('code execution started.')


#CRUD operation in mongoDB


def main():


    print('inside main: ')
    db = DBHelper()
    db.select_collection()

    #RETIEVE LOGIC 
    condition = {
        'name': 'blair willows',
        'email' : 'blair@pcschool.com'
    }
    db.retrieve(condition)


    #UPDATE LOGIC 
    condition2= {'email': 'annaliese@pcschool.com'}
    doc_to_update = {
        'name' : 'rapunzel',
        'phone ': '+39 291931'
    }
    db.update(condition=condition2, document_to_update=doc_to_update)


    #DELETE LOGIC 
    db.delete(condition=condition)

    #id is the hascode of the documents
    #cursor behaves like a list 



if __name__ == '__main__':
    print('main called:')
    main() 




