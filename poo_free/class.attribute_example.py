class Item:
    #class atribute it can be used by instances
    pay_rate = 0.2# The pay rate after 20% discount
    def __init__(self, name, price, quantity):

        #Run validations to hte received arguments
        assert price >= 0
        assert quantity >=0, f"quantity {quantity} is not greater or equal to zero!"

        
        # Assing to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def calculate_total_price(self):
        return self.price * self.quantity

    
    def apply_discount(self):
        self.price = self.price * self.pay_rate# pay_rate is a Class level and we call it Item.pay_rate but we can pass self.pay_rate to call it from INstance level



if __name__ == '__main__':
    item1 = Item("Phone", 100,5 )
    # item1.calculate_total_price()
    # print(item1.price)
    # print(item1.calculate_total_price())
    
    # item2 = Item("Laptop", 1000,3)
    # item2.pay_rate = 0.5# we can add it here because is Class level
    # item2.apply_discount()
    # print(item2.price)

    # # see the 20% discount of one phone
    item1.apply_discount()
    print(item1.price)

    print(item1.apply_discount())
