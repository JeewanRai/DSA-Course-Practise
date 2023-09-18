# creating global vairable that is outsid of the function, common to all the functions or program
discount_rate = 0.1 # 10% discount


# function to calculate total cost of the item which are aleady listed in the shopping cart, at the beginning
# will show like 10+5+20+15+8 = 58
def calculate_total_cost(cart):
    total_cost = sum(shopping_cart.values())

    # condition, applying discount above certain threshold
    if total_cost >= 100:
        total_cost = total_cost * discount_rate

    return total_cost

# function to display items in the shopping cart
def display_shopping_cart(shopping_cart):
    print("Shopping Cart")
    # its possible to declear variable within forloop wituout having to explicitely
    # defined at the beginning of the function considering the key pair value of the dictionary
    for item, price in shopping_cart.items():
        print(f"{item}: Nu.{price}")

if __name__ == "__main__":
    shopping_cart = {"Apples": 10, 
                     "Banana": 5,
                     "Chocolates": 20,
                     "Milk": 15,
                     "Eggs": 65} 
    
# display initial shopping cart
display_shopping_cart(shopping_cart)
total_cost = calculate_total_cost(shopping_cart)
print(f"Total Cost(after discount): Nu.{total_cost:.2f}")
