# Classes & Object Oriented programming

class Person:
    # __ means "private" like in php
    __name = ''
    __email = ''
    
    #python uses the keyword "self" instead of "this" for
    #something to refer to an instance of its self
    def __init__(self, name, email):
        self.__name = name
        self.__email = email
    
    #a setter function so we can set the private variables
    def set_name(self, name):
        self.__name = name
        
    #a getter function
    def get_name(self):
        return self.__name
    
    def set_email(self, email):
        self.__email = email
        
    def get_email(self):
        return self.__email
    
    def toString(self):
        return '{} can be contacted at {}'.format(self.__name, self.__email)
    
#brad = Person('Brad Traversy', 'brad@gmail.com')
#brad.set_name('Brad Traversy')
#brad.set_email('brad@gmail.com')
#print(brad.toString())

#Customer is inheriting from the Person class (stealing it's cool stuff)
class Customer(Person):
    __balance = 0
    
    #  def __init__ is python's answer to a constructor
    # so the constructor runs whenever you create an object from a class
    def __init__(self, name, email, balance):
        self.__name = name
        self.__email = email
        self.__balance = balance
        #summon the constructor from the inherited class "Person"
        super(Customer, self).__init__(name, email)
        
    def set_balance(self, balance):
        self.__balance = balance
        
    def get_balance(self):
        return self.__balance
    
    def toString(self):
        return '{} has a balance of {} and can be contacted at {}'.format(self.__name, self.__balance, self.__email)


john = Customer('John Doe', 'jdoe@gmail.com', 100)

john.set_balance(400)

print(john.toString())

kate = Customer('Kate Smith', 'ksmith@yahoo.com', 5000)
print(kate.toString())