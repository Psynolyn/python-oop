class vehicle:
    def __init__(self, vehicle, speed):
        self.vehicle = vehicle
        self.speed = speed
    
    def drive(self):
        print(f'{self.vehicle} is movin at {self.speed} km/h')

lamb_truck = vehicle("Lamborghini Urus", 231)
s_class = vehicle("Mercedes-Benz S Class", 162)

lamb_truck.drive()
s_class.drive()



class plane(vehicle):
    def __init__(self, vehicle, speed, altitude):
        super().__init__(vehicle, speed)
        self.alt = altitude
    
    def drive(self):
        print(f'{self.vehicle} is cruising at {self.alt}ft, Speed {self.speed} Knots')


class truck(vehicle):
    def __init__(self, vehicle, speed, weight):
        super().__init__(vehicle, speed)
        self.weight = weight
    
    def drive(self):
        if(self.weight > 9):
            axle_status = "dropped"
        else:
            axle_status = "lifted"

        print(f'{self.vehicle} is movin at {self.speed} km/h, mid axle is {axle_status}')

A320 = plane("Airbus A320", 450, 13000)
S730 = truck("Scania S730", 90, 10)

print("\nInheritance:")

A320.drive()
S730.drive()