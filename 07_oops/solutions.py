class Car():
    total_cars = 0
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_cars += 1

    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def get_brand(self):
        return self.__brand
    
    def set_brand(self, new_brand):
        self.__brand = new_brand

    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_description():
        return "A very nice car"
    
    @property
    def model(self):
        return self.__model
    

class Electric_car(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Battery" 
    
class Battery():
    def battery_info(self):
        return "super cool battery"

class Engine():
    def engine_info(self):
        return "super hot engine"

class ElectCarTwo(Battery, Engine, Car):
    pass

my_new_tesla = ElectCarTwo("Ford", "Mustang")
print(my_new_tesla.get_brand())
print(my_new_tesla.battery_info())
print(my_new_tesla.engine_info())