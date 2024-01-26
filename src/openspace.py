from src.table import Table
import random



#The default setup of the open space is 6 tables of 4 seats → 24 seats
class OpenSpace:
    def __init__(self,capacity_table=4,n_tables=6):  #n_tables=6 . Number of the tabels in the openspace
        self.capacity_table=capacity_table  #capacity_table=4 . Number of the seats per table
        self.n_tables = n_tables  
        self.tables=[Table(self.capacity_table) for _ in range (n_tables)] #which is a list of Table 


    def organize(self, names):   # names is the list of colleagues
        random.shuffle(names)   #randomize the list of the colleagues 
        
        
        for name in names:
            table_notfull = False  # at first the tables is not full
            for current_table in range(self.n_tables) :
                if self.tables[current_table].assign_seat(name):   # 
                    table_notfull = True
                    break  
                 
            if not table_notfull:   # if there is no more seats availble
                print(f"No more free seats available for {name}. Some colleagues may not have a seat.")  
       
    #display the different tables and their occupants
    def display(self):
        for i, table in enumerate(self.tables):
            print(f"\nTable {i+1})")
            for j, seat in enumerate(table.seats):
                print(f" Seat {j+1}: {seat.occupant}")
    
    def store(self, filename):
        ''' store the repartition in an text file'''
        with open(filename, 'w') as txtfile:
            # Write data as a list to the text file
            
            for i, table in enumerate(self.tables, start=1):
                txtfile.write(f"Table {i}:\n")
                for j, seat in enumerate(table.seats, start=1):
                    occupant_info = seat.occupant if not seat.free else 'Empty'
                    txtfile.write(f"  Seat {j}: {occupant_info}\n")

