class Item:
    pay_rate = 0.8 # The Pat rate after 20% discount
    all = [] # Empty list
    def __init__(self, name, price, quantity):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater than zero"
        
        # Assign to self objects
        self.__name = name  ## __ double underscore  make variable private
        self.price = price
        self.quantity = quantity
        
        # Action to execute
        Item.all.append(self)
     
    # It will make name attribute unchangable once it assigned as argument   
    @property
    def name(self):
        return self.__name
    
    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discout(self):
        self.price *= self.pay_rate
        
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"
    
        
class Phone(Item):
    def __init__(self, name, price, quantity, broke_phone = 0):
        super().__init__(name, price, quantity)
        self.broken_phone = broke_phone

item1 = Phone("Phone", 100, 1,1)
item2 = Phone("Laptop", 1000, 3,1)

print(item1.name)
