from datetime import date



class Room:
    def __init__(self, room_number, capacity, price_per_night):
        self.room_number = room_number
        self.capacity = capacity
        self.price_per_night = price_per_night
        self.is_booked = False

    def __str__(self):
        return f"Room {self.room_number}, Capacity: {self.capacity}, Price per Night: ${self.price_per_night}"

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
        nights = (self.check_out - self.check_in).days
        room_cost = nights * self.room.price_per_night
        service_cost = sum(service.cost for service in self.services)
        return room_cost + service_cost

    def __str__(self):
        return f"Reservation for {self.guest.name} in {self.room}, Check-in: {self.check_in}, Check-out: {self.check_out}, Total Cost: ${self.total_cost()}"

# Decorator for adding room service
def add_room_service(cost):
    def decorator(func):
        def wrapper(*args, **kwargs):
            reservation = func(*args, **kwargs)
            reservation.add_service(Service("Room Service", cost))
            return reservation
        return wrapper
    return decorator

# Decorator for adding Wi-Fi
def add_wifi(cost):
    def decorator(func):
        def wrapper(*args, **kwargs):
            reservation = func(*args, **kwargs)
            reservation.add_service(Service("Wi-Fi", cost))
            return reservation
        return wrapper
    return decorator

class Service:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

# Usage example:
if __name__ == "__main__":
    # Create rooms
    room1 = Room(101, 2, 100)
    room2 = Room(102, 4, 150)
    room3 = Room(103, 1, 80)

    # Create a guest
    guest1 = Guest("John Doe", "john@example.com")

    # Reserve room with room service and Wi-Fi using decorators
    @add_room_service(20)
    @add_wifi(10)
    def reserve_room(guest, room, check_in, check_out):
        return Reservation(guest, room, check_in, check_out)

    reservation1 = reserve_room(guest1, room1, check_in=date(2023, 9, 20), check_out=date(2023, 9, 25))
    print(reservation1)
