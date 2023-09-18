# creating a generic product where all the product will have name, id, price and quentity so we can make lots of other real objects
class Product:
    def __init__(self, product_ID, name, price, quantity):
        self.product_id = product_ID
        self.name = name
        self.price = price
        self.quantity = quantity 

    def product_d3isplay(self): # function that will display products with features pointing to Product class
        print(f"Product ID: {self.product_id}")
        print(f"Product Nmae: {self.name}")
        print(f"Product Price: {self.price:.2f}")
        print(f"Product Quantity: {self.quantity}\n")

""" creating inventory to store all products in empty container called products/dictionary,  in this class 3 functions
are defined for adding new product, removing product and displaying product inside of  container"""
class Inventory():
    def __init__(self):
        self.products = {} # container to store all products added into products container

    """ creating function that initially check whether the product is already there in the container(products) with product_id
    if its there it will add with product_id as reference of the product to container by adding up to previous quantity or if the
    container is empty it will keep the qiven quantity as it is. In this function one new argument is passed to indicate the
    product that need to be added to products container. In the if statement product.product_id tells the id of the product
    passed as an argument of add_product function that is going to be stored in self.products container """

    def add_product(self, product):
        if product.product_id not in self.products:
            # telling computer to store particular product name book to be store in container called Library wtih 
            # unique book barcode: Library[Books.Barcode] = Books

            self.products[product.product_id] = product
        else:
            self.products[product.product_id] += product


    def remove_product(self, product_id, quantity):
        if product_id in self.products:
            # in this code in the context of book and library the nasted if will check in the Library container is there
            # a particular book with unique ISBN number with how manay copy. The computere is able to figuer out how manay 
            # copies are there in library as quentity variable is defined in diffrent scope which is associated with 
            # self.products[product_id].quantity and on the other hand quentity is alone which means request quentity
            # for the particular book to be borrowed
            if self.products[product_id].quantity >= quantity:
                self.products[product_id].quantity -= quantity
            else:
                return f"Not sufficient quentity available of {self.product_id}"
        else:
            return "Product not found"
    
    def display_inventory(self):
        print('Inventory')
        # its like student looking into the book in a shelf(dictionary/products), look details of each book one by one such as 
        # book name, quentity, id etc. going from one end to other end so that it display all the information
        for product in self.products.values():
            product.display_products()


def main():
    inventory = Inventory()

    while True:
        print("Inventory Management System")
        print("1. Add Product")
        print("2. Remove Product")
        print("3. Display Inventory")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            product_id = input("Enter Product ID: ")
            name = input("Enter Product Name: ")
            price = float(input("Enter Product Price: "))
            quantity = int(input("Enter Product Quantity: "))
            product = Product(product_id, name, price, quantity)
            inventory.add_product(product)
            print("Product added to inventory.\n")

        elif choice == "2":
            product_id = input("Enter Product ID to remove: ")
            quantity = int(input("Enter Quantity to remove: "))
            inventory.remove_product(product_id, quantity)
            print("Product removed from inventory.\n")

        elif choice == "3":
            inventory.display_inventory()

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
