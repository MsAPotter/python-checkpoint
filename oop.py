# 1: Define a Vehicle class with the following properties and methods:
# - `vehicle_type`
# - `wheel_count`
# - `name`
# - `mpg`, a 'dict', with the following properties:
#     - `city`
#     - `highway`
#     - `combined`
# - `get_vehicle_type` should return the `vehicle_type`
# - `get_vehicle_drive` if the `wheel_count` for that class is "no wheels!" then
#     it should return "no wheels send it back to the shop"
#     otherwise it should return "I have {self.wheel_count} wheel drive" as a formatted string
#
# Your Vehicle class should take one extra argument in the __init__ method (a `dict`) with the above
# attributes. Define the properties on the class from the dict that is passed in.
# 
# Here's an example of the dict that will be passed in to your class:
#
# vehicle_dict_vehicle = {
#     "vehicle_type": "Vehicle",
#     "wheel_count": 'no wheels!',
#     "mpg": {
#         "city": 19,
#         "highway": 30,
#         "combined": 27
#     },
#     "name": "Unidentified Flying Object",
# }

class Vehicle:
    def __init__(self, vehicle_type, wheel_count, name, mpg):
    # def __init__(self, d)
    #     self.__dict__ = d
        self.vehicle_type = vehicle_type
        self.wheel_count = wheel_count
        self.name = name
        self.mpg = {
            self.city: city,
            self.highway: highway,
            self.combined: combined
        }
    def get_vehicle_type(self):
        return vehicle_type

    def get_vehicle_drive(self):
        if wheel_count == "no wheels!":
          return "no wheels send it back to the shop"
        else:
            return f"I have {self.wheel_count} wheel drive"



# #2: Create a Motorcycle class that inherits from the Vehicle class and has the
# following properties and methods:
# - all the properties inherited from the Vehicle class
# - method: `pop_wheelie` if `wheel_count` is not equal to 2 then it should return False
#       otherwise return "popped a wheelie!"

class Motorcycle(Vehicle):
    def __init__(self, vehicle_type, wheel_count, name, mpg):
        super().__init__(vehicle_type, wheel_count, name, mpg)

    def pop_wheelie(self):
        if wheel_count != 2:
            return False
        else:
            return "popped a wheelie!"

# #3: Define a Car class that inherits from the Vehicle class with the following properties and methods:
# - all the properties inherited from the Vehicle class
# - property: `wheel_count` defaults to 4
# - method: `can_drive` that should return 'Vrrooooom Vroooom'

class Car(Vehicle):
    def __init__(self, vehicle_type, wheel_count = 4, name, mpg):
        super().__init__(vehicle_type, wheel_count = 4, name, mpg)
    
    def can_drive(self):
        return 'Vrrooooom Vroooom'


# #4: Define a Truck class that inherits from the Vehicle class with the following properties and methods:
# - all the properties inherited from the Vehicle class
# - method: `rev_engine` that should return a string 'rreevv!'

class Truck(Vehicle):
    def __init__(self, vehicle_type, wheel_count, name, mpg):
        super().__init__(vehicle_type, wheel_count, name, mpg)
    def rev_engine(self):
        return 'rreevv!'

# Commit when you finish working on these questions!
