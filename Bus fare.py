class Vehicle:
    def __init__(self, fare_per_person):
        self.fare_per_person = fare_per_person

    def calculate_fare(self, passengers):
        return self.fare_per_person * passengers

class Bus(Vehicle):
    def __init__(self, fare_per_person):
        super().__init__(fare_per_person)

    def calculate_total_fare(self, passengers):
        base_fare = super().calculate_fare(passengers)
        return base_fare * 2.5

bus = Bus(fare_per_person=50)
total_fare = bus.calculate_total_fare(passengers=10)
print("Total Bus Fare:", total_fare)
