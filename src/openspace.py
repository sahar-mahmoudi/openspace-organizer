from src.table import Table
import random
from src.utils import get_user



#The default setup of the open space is 6 tables of 4 seats → 24 seats
class OpenSpace:
    """A class representing an open space with multiple tables
    Parameters
    ----------
    capacity_table : int, optional
        The number of seats per table (default is 4)
    n_tables : int, optional
        The number of tables in the open space (default is 6)

    Attributes
    ----------
    capacity_table : int
        The number of seats per table
    n_tables : int
        The number of tables
    tables : list
        A list of Table objects representing the tables in the open space

    Methods
    -------
    organize(names)
        Randomly assign people to the seats in the different tables

    display()
        Display the occupants of the different tables and seats

    store(filename)
        Store the seating arrangement in a text file"""

    def __init__(self,capacity_table=None ,n_tables=None ):  

        """Initialize the OpenSpace with the specified table capacity and number of tables

        Parameters
        ----------
        capacity_table : int, optional
            The number of seats per table (default is 4)
        n_tables : int, optional
            The number of tables in the open space (default is 6)"""
        if n_tables is None:
            n_tables=get_user(default=6,prompt="Please enter the number of table: ")
            
        if capacity_table is None:
            capacity_table=get_user(default=4,prompt="Please enter the number of seats for each table:")

        self.capacity_table=capacity_table  #capacity_table=4 . Number of the seats per table
        self.n_tables = n_tables  
        self.tables=[Table(self.capacity_table) for _ in range (n_tables)] #which is a list of Table 


    def organize(self, names):   # names is the list of colleagues
        """Randomly assign people to the seats in the different tables
        
        Parameters
        ----------
        names : list
            A list of colleague names

        Returns
        -------
        list
            A list of names successfully assigned to seats"""
                    
        random.shuffle(names)   #randomize the list of the colleagues 
        
        
        for name in names:
            table_notfull = False  # at first the tables is not full
            for current_table in range(self.n_tables) :
                if self.tables[current_table].assign_seat(name):   # 
                    table_notfull = True
                    break  
                 
            if not table_notfull:   # if there is no more seats availble
                print(f"No more free seats available for {name}")  
       
    def display(self):
        """Display the occupants of the different tables and seats"""
        for i, table in enumerate(self.tables):
            print(f"\nTable {i+1})")
            for j, seat in enumerate(table.seats):
                print(f" Seat {j+1}: {seat.occupant}")
    
    def store(self, filename):
        """Store the seating arrangement in a text file"""
        with open(filename, 'w') as txtfile:
            # Write data as a list to the text file
            
            for i, table in enumerate(self.tables, start=1):
                txtfile.write(f"Table {i}:\n")
                for j, seat in enumerate(table.seats, start=1):
                    occupant_info = seat.occupant if not seat.free else 'Empty'
                    txtfile.write(f"  Seat {j}: {occupant_info}\n")

    def add_colleague(self, name):
        """Add a person to the open space by assigning them to an available seat"""

        for table in self.tables:
            if table.assign_seat(name):
                print(f"{name} has been assigned to a seat")
                return True

        print(f"No available seats to assign {name}.")
        return False 