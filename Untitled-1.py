class Parent:
    def __init__(self, name, f_name):
        self.name = name
        self.f_name = f_name
        
    

class Child(Parent):
    def __init__(self, name, f_name, age):
        super().__init__(name, f_name)
        self.age = age
        
    
c1 = Child("M", "K", "s")
c1.age.print()