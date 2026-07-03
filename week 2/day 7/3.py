# linear search using star and quargs 



def search (*numbers, **number_to_search):
    for number in numbers:
        if number == number_to_search['key']:
            print("The number", number_to_search['key'], "is found in the list.")
            break
    else:
        print("The number", number_to_search['key'], "is not found in the list.")


search(10, 20, 30, 40, 50, key=int(input("Enter the number to search: ")))


