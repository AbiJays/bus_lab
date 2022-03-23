class Bus:
    def __init__ (self, route_number, destination):
        self.route_number = route_number
        self.destination = destination
        self.passengers = []
    
    def drive(self):
        return "Brum brum"
    
    def passenger_count(self):
        return len(self.passengers)
        # changed the name so it was easier for me to know what was what and then breakpoint tested it and needed to return it.
    
    def pick_up(self, person):
        # add person to the passengers
        self.passengers.append(person) # same here, this wasn't working because either it was referencing the method and not the data or i was but regardless. different name made it clearer to me so wham. 
    
    def drop_off(self, person):
        self.passengers.remove(person)
    
    def empty(self):
        self.passengers = []
    
    def pick_up_from_stop(self, bus_stop):
        pass