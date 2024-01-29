from src.utils import Generate_list
from src.utils import read_list
from src.openspace import OpenSpace





if __name__ == "__main__":
    #takes a filepath as an argument to load the list of colleagues
    #Generate_list(url,x=24):  x is the number of colleagues

    colleagues=read_list(Generate_list("colleagues.txt"))
    

    # Create an OpenSpace with the default value:
    # 4 tables, each has 6 chairs
    #OpenSpace(capacity_table=4,n_tables=6):  
    open_space = OpenSpace()

    # Organize colleagues randomly into the OpenSpace
    open_space.organize(colleagues)
    
    # Display the results
    open_space.display()

    # Store the seating arrangement in a text file
    open_space.store('organize_room.txt')
    
    new_colleague_name = "John Doe"
    open_space.add_colleague(new_colleague_name)


