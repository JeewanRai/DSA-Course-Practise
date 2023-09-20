# creating a model of general hotel room with associated parameters and attributes which is common to all hotel room
class Room:
    def __init__(self, room_number: int, capacity: int, price_per_night: int):
        self.room_number = room_number
        self.capacity = capacity 
        self.price_per_night = price_per_night
        self.is_book = False # wether the room is booked or not, initially mentioned not book

    def __str__(self):
        return f"Room {self.room_number}, Capacity: {self.capacity}, Price per night: Nu.{self.price_per_night}"

class Guest:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return f"Guest: {self.name}, Email: {self.email}"
    
class Reservation:
    def __init__(self, guest, room, check_in, check_out):
        self.guest = guest
        self.room = room
        self.check_in = check_in
        self.check_out = check_out
        self.services = []

    def add_service(self, service):
        self.services.append(service)

    def total_cost(self):
        nights = (self.check_out-self.check_in).day
        # self.room.price_per_night is indicate price associated with particular room 
        room_cost = nights * self.room.price_per_night
        # service_cost = 0
        # for service in self.services
        # service_cost += service_cost
        service_cost = sum(service_cost for service in self.services)
        return room_cost + service_cost
    

    def __str__(self):
        return f"Reservation for {self.guest_name} in {self.room}, Check in : {self.check_in}, Check out: {self.check_out}, Total cost: Nu.{self.total_cost()}"

# creating instance of the room
room1 = Room(101, 2, 100)
room1 = Room(102, 4, 140)

# creating instance of the guest class
guest1 = Guest("John", "john@gmail.com")





