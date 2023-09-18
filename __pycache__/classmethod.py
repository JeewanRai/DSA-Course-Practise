class Resturent:
    def __init__(self, resturent_name, cusine_type):
        self.resturent_name = resturent_name
        self.cusine_type = cusine_type
    
    def describe_resturent(self):
        print("The resturent is open every day")
        print("Welcome")

    def open_resturent(self):
        print("The resturent is open")

resturent = Resturent("OplaZa", "Emadatshi")

print(resturent.resturent_name)
print(resturent.cusine_type)

resturent.describe_resturent()
resturent.open_resturent()


