class SampleClass():
    def __init__ (self, param2, param2):
        self.param1 = param1
        self.param2 = param2
    
    def some_method(self):
        print(self.param1)

class Dog():
    
    species = 'mammal'
    
    def __init__(self, breed, name, spots):
        self.breed = breed
        self.name = name
        self.spots = spots
        
    #methods 
    def bark(self,time):
        print('WOOF! My name is {}'.format((self.name +' ') * time))

my_dog = Dog(breed = 'tibert', name = 'Sam', spots = False)
my_dog.breed
my_dog.species

my_dog.bark(time = 3)




class Circle():
    #class object attribute
    pi = 3.14
    def __init__(self, radius = 1):
        self.radius = radius
        self.area = radius*radius*Circle.pi
    
    def calculate_circumference(self):
        return(2*self.radius*Circle.pi)
        
my_circle = Circle(15)
my_circle.calculate_circumference()
my_circle.area

class Animal():
    def __init__(self):
        print ('animal created')
    
    def who_am_i(self):
        print('I am an animal')
        
    def eat(self):
        print('I am eating')

some_animal = Animal()
some_animal.eat()

class Dog(Animal):
    
    def __init__(self):
        Animal.__init__(self)
        print('Dog created')
        
    #overwrite inherited method
    def who_am_i(self):
        print('I am a dog')
    
    def bark(self):
        print('WOLF')

my_dog = Dog()
my_dog.eat()
my_dog.who_am_i()


class Dog():
    def __init__(self,name):
        self.name = name
    
    def speak(self):
        return (self.name + ' says woof!')
        
class Cat():
    def __init__(self,name):
        self.name = name
    
    def speak(self):
        return (self.name + ' says meow!')
            
niko = Dog('niko')
felix = Cat('felix')
niko.speak()
felix.speak()
#though using same method name, these methods are defined independently
#and they can be called in function totaly the same

for pet in [niko,felix]:
    print(type(pet))
    print(pet.speak())

def pet_speak(pet):
    print(pet.speak())
    
pet_speak(niko)
pet_speak(felix)
