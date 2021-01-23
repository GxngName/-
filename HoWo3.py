class Restaurant():
    def __init__(self, name, type): 
        self.restaurant_name=name
        self.cuisine_type=type
    def describe_restaurant(self):
        print("Vkusno - " + 
    self.restaurant_name)
    def open_restaurant(self):
        print("Ресторан открыт с 9:00\n")

restaurant = Restaurant("Домашняя кухня")
restaurant.describe_restaurant()
restaurant.open_restaurant()