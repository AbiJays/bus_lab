class BusStop:

    def __init__(self, name):
        self.name = name
        self.queue = 0
    
    def queue_length(self):
        return (self.queue)
    
    def add_to_queue(self, person):
        self.queue += 1

    def clear(self):
        self.queue = 0