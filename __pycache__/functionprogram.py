# definig global variable outside of any function or top of the function, any function can access it anytime 
# from anywhere in the code.
TAXT_RATE = 0.08

""" Initilizing empty list of dictionary, the list will have numbers of dictionry or key value pairs. The list will
store dictionary with numbers of parameters such as name, id, class, year etc and each dictionary will represent
one item in the list like item1 = {name, id, class, year}; easier to organize, figure out particular item from the 
list otherwise storing all these parametes in the dictionary will get messy and difficult to find particular item
when required. List of dictionary is used in the case where there are multiple paramets of particular item."""

shopping_cart = [] # creating list to store dictionary item

# defining parameterized function or function with parameter to give input value to perform specific task in the code
def add_item(item_name, item_price, item_quentity):
    item = {"Item Name": item_name,
            "Item Price": item_price,
            "Item Quantity": item_quentity}
    
    # adding item into shopping_cart list
    shopping_cart.append(item)

# creating funtion to calculate the money for all the available items inthe shopping_cart
def calculate_total_cost():
    total_cost = 0
    for item in shopping_cart:
        # calculating total cost by accessing specific attribute like (item quantity or item price) to calculate total cost
        # from dictionary called item.
        total_cost += item['Item Price'] * item['Item Quantity']
    return total_cost

# function to apply taxt rate
def apply_tax(total_cost):
    return total_cost + (total_cost * TAXT_RATE)

if __name__ == "__main__":
     while True:
        print("1. Add item to cart")
        print("2. Calculate total cost")
        print("3. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            item_name = input("Enter item name: ")
            item_price = float(input("Enter item price: "))
            item_quantity = int(input("Enter item quantity: "))
            add_item(item_name, item_price, item_quantity)
            print(f"{item_quantity} {item_name}(s) added to the cart.")

        elif choice == "2":
            total_cost = calculate_total_cost()
            total_cost_with_tax = apply_tax(total_cost)
            print(f"Total cost (before tax): ${total_cost:.2f}")
            print(f"Total cost (with tax): ${total_cost_with_tax:.2f}")

        elif choice == "3":
            print("Thank you for shopping with us!")
            break

        else:
            print("Invalid choice. Please select a valid option.")