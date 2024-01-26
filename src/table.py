class Seat:
    """
    A class representing a seat in the open space

    Parameters
    ----------
    free : bool, optional
        The initial state of the seat (default is True)

    Attributes
    ----------
    free : bool
        The current state of the seat (True if free, False if occupied)
    occupant : str or None
        The name of the person occupying the seat (None if the seat is free)

    Methods
    -------
    set_occupant(name)
        Assign someone to the seat if it's free

    remove_occupant()
        Remove someone from the seat and return their name

    """
 
    def __init__ (self,free=True):
        """
        Initialize a seat with a default state of being free

        Parameters
        ----------
        free : bool, optional
        The initial state of the seat (default is True).
        """
        self.free=free #free is a boolean

        self.occupant=None #occupant is a name (string)
        
    #assign someone a seat if it's free
    def set_occupant(self,name): 
        
        """Assign someone to the seat if it's free
        
        Parameters
        ----------
        name : str
            The name of the person to be assigned

        Returns
        -------
        bool
            True if the assignment is successful, False otherwise
        """
        if self.free:
            self.occupant = name
            self.free = False
            return True
        else:
            return False 
    
    
    #removes someone from a seat and returns the name of the person occupying the seat before   
    def remove_occupant(self):
        """Remove someone from the seat and return their name
        Returns
        -------
        str or None
            The name of the person removed from the seat, or None if the seat was already free
        """
        if not self.free:
            pre_name = self.occupant
            self.occupant = None
            self.free = True
            print(f"{pre_name} has been removed from the seat")
            return pre_name
        else:
            return None
    
 

#The default setup of the open space is 6 tables of 4 seats → 24 seats
class Table:
    """A class representing a table in the open space
    Parameters
    ----------
    capacity : int, optional
        How many seats the table has (default is 4)

    Attributes
    ----------
    capacity : int
        The number of seats the table can has
    seats : list
        A list of Seat objects representing the seats at the table

    Methods
    -------
    has_free_spot()
        Check if the table has a free spot

    assign_seat(name)
        Assign someone to a free seat at the table

    capacity_left()
        Return the number of available seats at the table"""

    def __init__(self, capacity=4):   #capacity= How many seats has a table 
        """Initialize a table with a specified capacity.Defualt is 4
        
        Parameters
        ----------
        capacity : int, optional
            How many seats the table has (default is 4)"""

        self.capacity = capacity   #It is an integer
        self.seats = [Seat() for _ in range(capacity)]  #which is a list of Seat objects (size = capacity)
        

    def has_free_spot(self):
        """Check if the table has a free spot
        
        Returns
        -------
        bool
            True if a spot is available
     """

        return (seat.free for seat in self.seats)  #returns a boolean (True if a spot is available)

    #places someone at the table
    def assign_seat(self, name):
        """Assign someone to a free seat at the table
        
        Parameters
        ----------
        name : str
            The name of the person to be assigned


        Returns
        -------
        bool
            True if the assignment is successful, False otherwise.
     """

        for seat in self.seats:
            if seat.set_occupant(name):
                return True
        return False

    def capacity_left(self):
        """Return the number of available seats at the table
        Returns
        -------
        int
            The number of available seats"""

        return sum(seat.free for seat in self.seats)  #returns an integer
    
    
    
    