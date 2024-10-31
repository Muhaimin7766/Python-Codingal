class BMW:
    def start(self):
        return "BMW engine starts with a tsssssss!"

    def stop(self):
        return "BMW engine stops with bang."

class Ferrari:
    def start(self):
        return "Ferrari engine starts with a V12 growling!"

    def stop(self):
        return "Ferrari engine stops with a ratattatatatat."

def vehicle_start(vehicle):
    print(vehicle.start())

def vehicle_stop(vehicle):
    print(vehicle.stop())

bmw_car = BMW()
ferrari_car = Ferrari()

vehicle_start(bmw_car)  
vehicle_stop(bmw_car)

vehicle_start(ferrari_car)  
vehicle_stop(ferrari_car)  