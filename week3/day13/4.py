from USERCLASS import *
from FILEHELPERCLASS import *
from DBHELPER import DBHelper 


def main():
    user = User()
    user.input_details()
    user.show()

    csv_data = user.to_csv()                    # Write this in File
    user_document = user.to_dictionary()      # Write this in MongoDB

    print(csv_data)
    print(user_document)


    '''#anyone can access this local file system and also passwords can be read easily
    file_helper = FileHelper()
    file_helper.write_in_file(csv_data)
    file_helper.close_file()
    '''

    
    db_helper = DBHelper()
    db_helper.select_collection()
    # db_helper.select_collection(collection_name='users')
    db_helper.save(user_document)



if (__name__ == '__main__') :
    main()


