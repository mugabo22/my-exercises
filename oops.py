"""Below are some projects of how to write Object Oriented Programming 
and how to use many of these e.g using polymorphism,Data abstruction and 
inheritance using our python classes.."""
class Gadgets():
    def __init__(self,name,price,model):
        self.name=name
        self.price=price
        self.model=model
    def give_discount(self):
        discount=self.price * 0.2
        print(f"{self.name} has been given a discount of {discount}")
Class1=Gadgets("Samsung A+",2.45,"model M50")
Class1.give_discount()

class Man():
    def __init__(self,name):
        self.name=name
    def ear(self):
        print(f"{self.name} you over hear")
    def eat(self):
        print(f"{self.name} eats alot")
class Boy(Man):
    def __init__(self,name,age,status):
        super().__init__(name)
        self.age=age
        self.status=status
    def ear(self):
        print("We hear alot")
class Girl(Boy):
    def __init__(self, name, age, status,carrier,skills):
        super().__init__(name, age, status)
        self.carry=carrier
        self.scip=skills
    def ear(self):
        print("we hear alot")
    def cruise(self):
        print(f'if its all about {self.scip}, {self.name} does it more better than all')
beb20=Girl('Messi',24,'single','football','dribble')
beb20.cruise()


        
        

    