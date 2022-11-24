# Garlic To Onion / Port Scanner


import nmap
from time import sleep

from Banner import banner


white , green , yellow , red = "\033[0;37m" , "\033[92m" , "\033[93m" , "\033[91m"


def port_scanner() :

    while True :
   
 
    banner()

    sleep (0.05)
    print (yellow , "–•[PORT SCANNER]•–———————————————————————————————————————————————————————————")

    
    sleep (0.05)
    print (yellow , "\n [~] ENTER A IP:")

    sleep (0.05)
    print (white)
    ip = input (" @G.O>>> ")

    if ip == "0" :
        break
        
    elif ip == "" :
        print (red , "\n [!] ERROR")
        exit()

        
    sleep (0.05)
    print (yellow , "\n [~] ENTER PORT RANGE:")

    sleep (0.05)
    print (white)
    port = input (" @G.O>>> ")

    if port == "0" :
        break
        
    elif port == "" :
        print (red , "\n [!] ERROR")
        exit()


    try :
        
        scanner = nmap.PortScanner()
        scanner.scan (ip , port)
        tcp = scanner[ip]["tcp"].keys()

        for i in tcp :
            service = scanner[ip]["tcp"][i]["name"]
            print (green , " [+] Port {} - {} is Open" . format (i , service))

    except :
        print (red , "\n [!] ERROR")
        exit()

        
    print (yellow , "\n Finish")

    input()
