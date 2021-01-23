class Car:
    def __init__(self, name, age, model):
        self.name = name
        self.age = age
        self.model = model
        self.probeg = 0
    
    def get_probeg(self):
        print(self.probeg)
    
    def set_probeg(self, value):
        self.probeg = value

merc = Car("Merc", 1,"GLC")
merc.get_probeg()
merc.get_probeg()
merc.set_probeg(4000)
merc.get_probeg()





class Car:
    wigth = 2
    def __init__(self, name, age, model):
        self.name = name
        self.age = age
        self.model = model
        self.probeg = 0
    
    def get_probeg(self):
        print(self.probeg)
    
    def set_probeg(self, value):
        self.probeg = value

merc = Car("Merc", 1,"GLC")
merc.get_probeg()
Car.get_probeg(merc)

class Math1:
    @staticmethod
    def sqr(number):
        return number * number
    
    @staticmethod
    def cube(number):
        return number * number * number

print(Math1.sqr(2))

#В static-od не используем обьекты(экземпляры), обращение к классу

#class Parikm:
 #   @staticmethod
 #   def make_hairstyle(person):
  #      print("Bzzzh.... Hairstyle is ready!")
  #      print(person.get_name() + " must pay!")

#class Person:
  #  def __init__ (self, name):
   #     self.name = name
    
   # def get_name(self):
   #     return self.name

    #misha = Person("Misha") 
    #Parikm.make_hairstyle(misha)   НЕ РОБИТ!!

class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.type = cuisine_type
        self.number_serverd = 0
    
    def describe_restaurant(self):
        print(self.name)
        print(self.type)
    
    def open_rastaurant(self):
        print("Restaurant is open")

    def get_number_served(self):
        return self.number_serverd
    
    def set_number_served(self, value):
        self.number_serverd = value
    
    def increment_number_served(self):
        self.number_serverd += 1

rest = Restaurant("Recrent", "Cafe")
rest.set_number_served(10)
print(rest.get_number_served())
rest.increment_number_served()
rest.increment_number_served()
print(rest.get_number_served())