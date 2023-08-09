# **DSA Practical Learning**

These list of the code provided in the repository are soly for learning DSA course form Udemy. Not for any project


<span style="color: green; font-size: 25px; font-family: 'Times New Roman', serif;">This is practical python for understanding how to define function, creat function and call a function</span>
----

```python

def calculation():
    name = input("What is your name: ")
    age = int(input("What is your age: "))
    return name, age

def date(name, age):
    from datetime import datetime
    current_year = datetime.now().year
    at_100_years = current_year + (100 - age)
    message = f"Hello, {name}! You will turn 100 years in the year {at_100_years}"
    return message

if __name__ == "__main__":

    name, age = calculation()

    message = date(name, age)

    user_enter = int(input("Enter number to repeat: "))
    print(user_enter * (message + "\n"))

```