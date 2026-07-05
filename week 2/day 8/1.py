#oops 
#understanding classes and objects 


class Restaurant:
    pass

class Menu:
    pass

class Dish:
    def __init__(self):
        pass


restaurant = Restaurant()

menu = Menu()

dish1 = Dish()
dish2 = Dish()
dish3 = Dish()

print('restaurant:', restaurant)
print('menu:', menu)

print('dish1:', dish1)
print('dish2:', dish2)
print('dish3:', dish3)

print('data in restaurant:', vars(restaurant))
print('data in menu:', vars(menu))
print('data in dish1:', vars(dish1))
print('data in dish2:', vars(dish2))
print('data in dish3:', vars(dish3))