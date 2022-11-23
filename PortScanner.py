# Garlic To Onion / Port Scanner


import nmap
from time import sleep
from colorama import Fore

from Banner import banner


ly,lr,lg,w = Fore.LIGHTYELLOW_EX,Fore.LIGHTRED_EX,Fore.LIGHTGREEN_EX,Fore.WHITE


def port_scanner() :
    
    banner()

    sleep (0.05)
    print (ly , "–•[PORT SCANNER]•–———————————————————————————————————————————————————————————")

    sleep (0.05)
    print (ly , "\n [!] ENTER A IP:")

    
    sleep (0.05)
    print (w)
    ip = input(" @G.O>>> ")

    if ip == "0" :
        exit()
        
    elif ip == "" :
        print (lr , "\n [!] ERROR")
        exit()

        
    sleep (0.05)
    print (ly,"\n [!] ENTER PORT RANGE:")

    
    sleep (0.05)
    print (w)
    port = input(" @G.O>>> ")

    if port == "0" :
        exit()
        
    elif port == "" :
        print (lr , "\n [!] ERROR")
        exit()


    try :
        
        scanner = nmap.PortScanner()
        scanner.scan(ip,port)
        tcp = scanner[ip]["tcp"].keys()

        for i in tcp:
            service = scanner[ip]["tcp"][i]["name"]
            print (lg , " [+] Port {} - {} is Open".format(i,service))

    except :
        print (lr,"\n ERROR")
        exit()

    print(ly,"\n Finish")
