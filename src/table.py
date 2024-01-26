class Seat:
    
    def __init__ (self,free=True):
        self.free=free #free is a boolean

        self.occupant=None #occupant is a name (string)
        
    #assign someone a seat if it's free
    def set_occupant(self,name):    
        if self.free:
            self.occupant = name
            self.free = False
            return True
        else:
            return False 
    
    
    #removes someone from a seat and returns the name of the person occupying the seat before   
    def remove_occupant(self):
        if not self.free:
            pre_name = self.occupant
            self.occupant = None
            self.free = True
            print(f"{pre_name} has been removed from the seat.")
            return pre_name
        else:
            return None
    
 

#The default setup of the open space is 6 tables of 4 seats → 24 seats
class Table:
    def __init__(self, capacity=4):   #capacity= How many seats has a table 
        self.capacity = capacity   #It is an integer
        self.seats = [Seat() for _ in range(capacity)]  #which is a list of Seat objects (size = capacity)
        

    def has_free_spot(self):
        return (seat.free for seat in self.seats)  #returns a boolean (True if a spot is available)

    #places someone at the table
    def assign_seat(self, name):
        for seat in self.seats:
            if seat.set_occupant(name):
                return True
        return False

    def capacity_left(self):
        return sum(seat.free for seat in self.seats)  #returns an integer
    
    
    
    