class vehicle:
    def move(self):
        print("used for move another place")

class bike(vehicle):
    def ride(self):
        print("enjoy the ride")

class electricbike(bike):
    def charge(self):
        print("charging is mandatory")

# b1= bike()
# b1.ride()

b1 = electricbike()
b1.charge()
b1.ride()
b1.move()
print(electricbike.__mro__)
