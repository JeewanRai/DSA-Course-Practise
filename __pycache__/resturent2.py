class Resturent:
    def __init__(self, food_type, number_items):
        self.food_type = food_type
        self.number_items = number_items
        self.customer_served = 0

    def printing_value(self):
        return f"Number of customer served {self.customer_served}"

    def setnumber_served(self, served_number):
        self.customer_served = served_number

    def increment_customer_served(self, increment_served):
        self.customer_served += increment_served

resturent = Resturent("Bhutanese Disc", 12)
print(resturent.printing_value())

# Method 1: Directly updating the customer served 
resturent.customer_served = 10
print(resturent.printing_value())

#Method 3: Updating the customer served through method
resturent.setnumber_served(233)
print(resturent.printing_value())

resturent.increment_customer_served(9000)
print(resturent.printing_value())



