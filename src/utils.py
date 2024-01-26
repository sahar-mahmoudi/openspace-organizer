#x = input('please enter the number of colleagues :')
import random
import string

def Generate_list(url,x=24):   #The default setup of the open space is 6 tables of 4 seats → 24 seats

    
    list_names=[]

    for i in range(int(x)):

        file_name = ''.join(random.choice(string.ascii_lowercase) for i in range(random.randint(5, 15)))
        list_names.append(file_name)

    file = open(url,'w')
    file.write(" ".join(list_names))  
    file.close()
    
    
    # opening the file in read mode 
    my_file = open(url, "r") 
  
    # reading the file 
    data = my_file.read() 
    data_into_list = data.split(" ") 
    
    return data_into_list        

