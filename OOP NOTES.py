# This is notes of Object oriented program in python

# Object is the instance of class
# Class is the blueprint 

""" Class have 2 important things 
1) Attributes = data is/has, ex. name, age, height
2) Methods = action, functions, ex. eat, walk, sleep """

# __init__ function
# Its also called constructor 
""" It take one parameter self, self parameter is a reference to the current instance of the class
 and is used to access variables that belongs to the class""" 
# This function contain attributes 

# ATTRIBUTES
""" Class.attr : If something is common in all objects than we create class attribute, its declare outside the 
constructor but inside class, ex. we have 3 students object and in all objects college name is same so we declare 
attribute in class outside the constructor which is same for all objects
    Obj.attr : Object attribute is declared inside constructed with self. , And while creating object u can assigned
values to it differntly for different object"""
    
# METHODS
""" Its the functions or action inside the class which will be called by the object """

# There are four pillars of oop
""" ABSTRACTION : Hiding the implementation details of a class and only showing the essential features to the user
    ENCAPSULATION : Wrapping and functions into single unit(object)
    INHERITANCE : When one class(child/derived) derives the properties & methods of another class(Parent/base)
    There are 3 types of inheritance:
        1) Single inheritance : Its simple inheritance one child class and one parent class
        2) Multi-level inheritance : When child class inherits another child class.
        3) Multiple inheritance: When a child class is derived from more than one parent class
    POLYMORPHISM : When the same operator is allowed to have different meaning acccording to the context"""
    
""" We can make an method or attribute private by writing __(double underscore) with variable name inside 
constructor with self.
    class Name:
        def __init__(self, name):
            self.__name = name 
            
and for method we can make it private by __(double underscore) while declaring function name
 def __hello(self):
    ....
    ....
    
we can access this only inside class , if we access outside class it will get us error"""

# super() method is used to access methods of the parent class 
# super().__init__()
# It inherit attributes from parent class and than we can add more attributes in child class constructor

# Assert is a keyword in python that allows you to verify that a certain condition is true,
# If the condition is false it will raise an error 
# Its write inside def __init__() method
# You can write a statment with in same line by seprating with comma, the statment will be written in error terminal

""" @staticmethod, @classmethod, @property are decorators

1) staticmethod : This should do something that has relationship with class, but not something that must be unique
                   per instance.
                   It dont take self as parameter 
2) classmethod : This should also do something that has a relationship with the class, but usually those are used
                  to manipulate different structure of data to instantiate objects
                  There shall must be cls parameter in paranthesis
3) property : It makes an variable read only, when parameter value is assigned once after that you cant change it just can read it"""
