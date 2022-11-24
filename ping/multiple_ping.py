#import the modules or librarys os and time (to integrate the resources of operactional system)
import os
import time


with open("hosts.txt") as file: #opening text.txt as file
    dump = file.read()#adding a variable to read the file
    dump = dump.splitlines()#using splitline to put in separated lines
    
    for ip in dump: #using (for) to go line by line of file
        print(f"Checking the Ip: {ip} \n")#printing a message
        print("-" * 60) #just printing a separator
        os.system("ping -c 1 {}" .format(ip))#requesting system of library os to running command ping
        print("-" * 60) #just printing a separator
        time.sleep(3) #setting the time 
        
    
    
    