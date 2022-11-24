import os #import the module or library os (to integrate the resources of operactional system)


print("-" * 60)#just printing a separator
ip_host = input("type the ip addres or hostname: ")#variable to receive the IP address or hostname of the user input
print("-" * 60)#just printing a separator

print(f'Running ping in: {ip_host} \n')#printing a message
os.system('ping -c 4 {}' .format(ip_host))#requesting system of library os to running command ping

