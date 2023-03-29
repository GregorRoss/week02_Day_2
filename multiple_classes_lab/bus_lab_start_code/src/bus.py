class Bus:
    def __init__ (self, route, destination):
        self.route_number = route
        self.destination = destination
        self.passengers = []

    def drive(self):
        return "Brum brum"
    
    def passenger_count(self):
        return len(self.passengers)
    
    def pick_up_from_stop(self, bus_stop):
        for people in bus_stop.queue:
            self.pick_up(people)
        bus_stop.queue.clear()
    
    def pick_up(self, passenger):
        self.passengers.append(passenger)

    def drop_off(self, passenger):
        self.passengers.remove(passenger)

    def empty_bus(self):
        self.passengers.clear()




    
