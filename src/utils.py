#x = input('please enter the number of colleagues :')
import random
import string

def Generate_list(url,x=24):   #The default setup of the open space is 6 tables of 4 seats → 24 seats
    """
    Generate a list of random names and save them to a file

   Parameters
    ----------
    url : str
        The file path where the list of names will be saved
    x : int, optional
        The number of names to generate. Default is 24

    Returns
    -------
    list
        A list of generated names

    Example
    -------
    
    >>> Generate_list('names.txt', x=5)
    ['abcde', 'fghij', 'klmno', 'pqrst', 'uvwxy']
    """

    
    list_names=[]

    for i in range(int(x)):

        file_name = ''.join(random.choice(string.ascii_lowercase) for i in range(random.randint(5, 15)))
        list_names.append(file_name)

    with open(url, 'w') as file:
        file.write(" ".join(list_names))
    
    
    # opening the file in read mode 
    with open(url, "r") as my_file:
        data = my_file.read()
        data_into_list = data.split(" ")
    
    return data_into_list        

