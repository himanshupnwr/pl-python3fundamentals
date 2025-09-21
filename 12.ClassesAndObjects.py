class Robot:
    #the init method lets us initialize our class properties
    #self is required, it refers to the instance we are creating like this in c#
    #others are the properies we want to initialize as parameters
    def __init__(self,name):
        self.name = name
        self.position = [0,0]
        print('My name is', self.name)

    def walk(self, x):
        self.position[0] = self.position[0] + x
        print('New Position:', self.position)

    def bark(self):
        print('Woof Woof!')

#using inheritence 
class Robot_Dog(Robot):
    #if we leave the init for child class it will call the parent init method by default
    #the init method lets us initialize our class properties
    #self is required, it refers to the instance we are creating like this in c#
    #others are the properies we want to initialize as parameters
    def __init__(self,name_val,breed_val):
        self.name = name
        self.breed = breed

    #method overriding
    def bark(self):
        #calling the parent bark also using super
        super().bark()
        print('not Woof Woof!')

my_dog = Robot_Dog('Spot','Chihuaha')
my_dog.walk(10)
my_dog.bark()
print(my_dog.name)
print(my_dog.breed)
