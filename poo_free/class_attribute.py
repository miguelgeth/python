class Item:
    #class atribute it can be used by instances
    pay_rate = 0.8# The pay rate after 20% discount
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



if __name__ == '__main__':
    item1 = Item("Phone", 100,-5 )
    item2 = Item("Laptop", 1000, -3)

    print(Item.pay_rate)# one way to access to class attribute
    print(item1.pay_rate)# one way to access to class attribute
    print(item2.pay_rate)# one way to access to class attribute

    print(Item.__dict__)# all the attributs of Class level
    print(item1.__dict__)# all the attributs of Instance level

    # print(item2.name)
    # print(item2.price)
    # print(item2.quantity)