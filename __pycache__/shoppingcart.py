
# creating class is like creating blue print of an object where multiple objects has common features. like vehical class has speed as one of the 
# feature/property and use for transportation is another method/feature which will be common to car, bus, bike, cycle
class Product:
    # while using sepcial init function we are assigning or giving some features to object that we will create at the end, example product1 =
    # Product("iPhone 15 Pro Max", 1999), with this method we are creating object with reference to features defined in Product class. While
    # calling this Product class using above method it will store in product1, we have to pass value to which will The name attribute of the product1 object will 
    # be set to "iPhone 13 Pro" and the price attribute will be set to 999.
    def __init__(self, name, price): # giving features and attributes to object or name and price attribute to object
        self.name = name
        self.price = price

    def get_info(self):
        return f"{self.name}: Nu.{self.price:.2f}"


class DiscountProduct(Product):
    def __init__(self, name, price, discount):
        super().__init__(name, price)
        self.discount = discount 

    def get_info(self):
        original_price = self.price *(1-self.discount)/100
        return f"The discount price of the {self.name} is Nu.{self.discount:.2f}"

        
class ShoppingCart:
    def __init__(self):
        self.shoppingcart = {}
    
    def add_item(self, product, quantity):
        if product in self.shoppingcart:
            self.shoppingcart[product] += quantity
        else:
            self.shoppingcart[product] = quantity

    def remove_purchase(self, product, quantity):
        if product in self.shoppingcart:
            if self.shoppingcart[product] >= quantity:
                self.shoppingcart[product] -= quantity
            elif self.shoppingcart[product] == 0:
                return f"The {product} is empty in the {self.shoppingcart}"
        else:
            return f"The {product} is not in the {self.shoppingcart}"
        
    def view_cart(self):
        total_cost = 0
        for product, quantity in self.shoppingcart.items():
            cost = product.price * quantity
            total_cost += cost
            print(f"{product.get_info()}: {quantity} items - ${cost:.2f} (total)")
        print(f"Total cost: ${total_cost:.2f}")

if __name__ == "__main__":
    apple = Product("Apple", 0.5)
    banana = Product("Banana", 0.3)
    orange = Product("Orange", 0.6)

    discounted_apple = DiscountProduct("Discounted Apple", 0.5, 10)  # 10% discount

    cart = ShoppingCart()
    cart.add_item(apple, 3)
    cart.add_item(banana, 2)
    cart.add_item(orange, 4)
    cart.add_item(discounted_apple, 5)

    cart.view_cart()


   


