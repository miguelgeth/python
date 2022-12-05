class Item:
    #class atribute it can be used by instances
    pay_rate = 0.8# The pay rate after 20% discount
    def __init__(self, name, price, quantity):#si no se cuantos tengo quantity=0, price_float pra pasarlo a float/str/int, etc, puedo con los demas

        #Run validations to hte received arguments
        assert price >= 0 # if a change the arguments below to a negative it'wll give us an error(AssertionError), and we can add and str or f"" to explain
        assert quantity >=0, f"quantity {quantity} is not greater or equal to zero!"

        
        # Assing to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def calculate_total_price(self):
        return self.price * self.quantity# hacemos la operacion



if __name__ == '__main__':
    item1 = Item("Phone", 100,5 )# it gives me -result but in math it doesn't make sense so to avoid negative numbers we use assert(afirmation)
    item2 = Item("Laptop", 1000, 3)

    print(item1.calculate_total_price())
    print(item2.calculate_total_price())


    # print(item2.name)
    # print(item2.price)
    # print(item2.quantity)